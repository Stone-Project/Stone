def expo_out(t):
    """Exponential ease-out on t."""
    return 1 if t == 1 else 1 - 2 ** (-10 * t)
