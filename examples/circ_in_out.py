def circ_in_out(t):
    """Circular ease-in-out on t."""
    return 0.5 * (1 - (1 - 2 * t) ** 0.5) if t < 0.5 else 0.5 * ((2 * t - 1) ** 0.5 + 1)
