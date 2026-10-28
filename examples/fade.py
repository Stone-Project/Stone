def fade(t):
    """Quintic fade curve on t."""
    return t * t * t * (t * (t * 6 - 15) + 10)
