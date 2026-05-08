def evaluate(state):
    """
    Converts system performance into business outcomes.
    """

    # --- 1. Detection Efficiency ---
    # How well the system is keeping up with workload
    if state.frames_in == 0:
        detection_efficiency = 0
    else:
        detection_efficiency = state.frames_out / state.frames_in

    # --- 2. Generate detections ---
    state.detections_waiting = int(state.expected_waiting * detection_efficiency)

    # --- 3. Alert logic ---
    # Only alert if meaningful number of people waiting
    if state.detections_waiting >= 5:
        state.alerts_triggered = 1
    else:
        state.alerts_triggered = 0

    # --- 4. Business outcomes ---
    if state.alerts_triggered:
        # Staff respond → most customers seated
        state.customers_seated = int(state.detections_waiting * 0.7)
        state.customers_left = int(state.detections_waiting * 0.3)
    else:
        # No alert → customers leave
        state.customers_seated = 0
        state.customers_left = state.expected_waiting