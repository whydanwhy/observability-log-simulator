import time

from engine.state import SystemState
from engine.traffic import TrafficModel

from services.frame_processor import process
from services.condition_engine import evaluate

from observability.logger import log_state


class Simulation:
    def __init__(self, failures=None, tick_duration=0.0):
        """
        failures: list of Failure objects
        tick_duration: real-time delay per tick (seconds)
        """
        self.state = SystemState()
        self.traffic = TrafficModel()
        self.failures = failures if failures else []

        self.tick = 0
        self.tick_duration = tick_duration  # 0 = run as fast as possible

    def step(self):
        """
        Execute one simulation tick.
        Order matters.
        """

        # --- 1. Traffic (defines demand) ---
        traffic_level, expected = self.traffic.get_profile(self.tick)
        self.state.traffic_level = traffic_level
        self.state.expected_waiting = expected

        # --- 2. Reset per-tick values ---
        self.state.frames_in = 120
        self.state.frames_out = 120
        self.state.alerts_triggered = 0
        self.state.customers_seated = 0
        self.state.customers_left = 0

        # --- 3. Apply failures (affect system capacity) ---
        for failure in self.failures:
            failure.apply(self.state, self.tick)

        # --- 4. Process pipeline ---
        process(self.state)

        # --- 5. Business logic ---
        evaluate(self.state)

        # --- 6. Log state ---
        log_state(self.state, self.tick)

        # --- 7. Increment time ---
        self.tick += 1

        # --- 8. Optional delay ---
        if self.tick_duration > 0:
            time.sleep(self.tick_duration)

    def run(self, max_ticks=None):
        """
        Run simulation.

        max_ticks: stop after N ticks (None = infinite)
        """
        while True:
            if max_ticks and self.tick >= max_ticks:
                break

            self.step()