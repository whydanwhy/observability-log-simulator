from failures.base import Failure


class MemoryLeak(Failure):
    def __init__(self, leak_rate=2):
        """
        leak_rate: MB increase per tick
        """
        self.leak_rate = leak_rate

    def apply(self, state, tick):
        # --- 1. Increase memory gradually ---
        state.memory_mb += self.leak_rate

        # --- 2. Increase latency based on memory pressure ---
        # Non-linear growth gives more realistic degradation
        state.latency_ms = 50 + (state.memory_mb * 0.03)

        # --- 3. Reduce throughput as memory increases ---
        # Higher memory → worse processing capacity
        degradation = min(0.8, (state.memory_mb - 500) / 2000)

        state.frames_out = int(state.frames_in * (1 - degradation))

        # --- 4. Optional: CPU pressure (secondary signal) ---
        state.cpu_pct = min(95, 40 + (state.memory_mb * 0.01))