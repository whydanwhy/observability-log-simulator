import json
from datetime import datetime, timedelta


def log_state(state, tick):
    base_time = datetime(2026, 5, 8, 11, 0, 0) #Simulation start
    
    simulated_time = base_time + timedelta(minutes=tick)
    
    
    log = {
        "timestamp": simulated_time.isoformat(),
        "tick": tick,

        # --- Traffic / business context ---
        "traffic_level": state.traffic_level,
        "expected_waiting": state.expected_waiting,

        # --- Throughput ---
        "frames_in": state.frames_in,
        "frames_out": state.frames_out,

        # --- Business metrics ---
        "detections_waiting": state.detections_waiting,
        "alerts_triggered": state.alerts_triggered,
        "customers_seated": state.customers_seated,
        "customers_left": state.customers_left,

        # --- System metrics ---
        "memory_mb": state.memory_mb,
        "latency_ms": state.latency_ms,
        "cpu_pct": state.cpu_pct
    }

    with open("logs.json", "a") as f:
        f.write(json.dumps(log) + "\n")