def cubic_in_out(t):
    """Cubic ease-in-out on t."""
    return 4 * t * t * t if t < 0.5 else 1 - 4 * (1 - t) ** 3
