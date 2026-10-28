def back_out(t):
    """Back ease-out on t, with overshoot."""
    return 1 + (t - 1) ** 2 * (2.70158 * (t - 1) + 1.70158)
