def process(state):
    """
    Simulates frame processing.

    The actual throughput (frames_out) is already influenced
    by failures (e.g., memory leak).

    This function exists to represent the processing stage
    in the pipeline.
    """

    # In this simple version:
    # failures have already adjusted frames_out
    # so we just ensure it never exceeds input

    state.frames_out = min(state.frames_out, state.frames_in)