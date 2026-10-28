def expo_in_out(t):
    """Exponential ease-in-out on t."""
    return 0 if t == 0 else 1 if t == 1 else 0.5 * 2 ** (20 * t - 10) if t < 0.5 else 1 - 0.5 * 2 ** (-20 * t + 10)
