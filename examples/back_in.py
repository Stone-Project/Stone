def back_in(t):
    """Back ease-in on t, with overshoot."""
    return t * t * (2.70158 * t - 1.70158)
