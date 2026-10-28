def expo_in(t):
    """Exponential ease-in on t."""
    return 0 if t == 0 else 2 ** (10 * (t - 1))
