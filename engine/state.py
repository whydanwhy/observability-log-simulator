class SystemState:
    def __init__(self):
        # system metrics
        self.memory_mb = 500
        self.cpu_pct = 40
        self.latency_ms = 50

        # throughput
        self.frames_in = 120
        self.frames_out = 120

        # traffic
        self.traffic_level = "quiet"
        self.expected_waiting = 1

        # business metrics
        self.detections_waiting = 0
        self.alerts_triggered = 0
        self.customers_seated = 0
        self.customers_left = 0

        # failure signal
        self.error_rate = 0.0