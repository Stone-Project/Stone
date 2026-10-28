def clamp01(x):
    """Clamp x to the range 0 to 1."""
    return 0 if x < 0 else 1 if x > 1 else x
