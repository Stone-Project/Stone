def gain(x):
    """Gain curve on x in 0 to 1."""
    return 0.5 * (2 * x) ** 0.5 if x < 0.5 else 1 - 0.5 * (2 * (1 - x)) ** 0.5
