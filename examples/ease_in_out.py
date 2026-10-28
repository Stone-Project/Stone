def ease_in_out(t):
    """Quadratic ease-in-out on t."""
    return 2 * t * t if t < 0.5 else -1 + (4 - 2 * t) * t
