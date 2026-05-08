from engine.simulation import Simulation
from failures.memory_leak import MemoryLeak

if __name__ == "__main__":
    failures = [
        MemoryLeak(leak_rate=5)
    ]

    sim = Simulation(failures=failures, tick_duration=0.0)

    sim.run(max_ticks=500)