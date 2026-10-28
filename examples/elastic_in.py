def elastic_in(t):
    """Elastic ease-in on t."""
    return 0 if t == 0 else 1 if t == 1 else -(2 ** (10 * t - 10)) * (t * 10 - 10.75) ** 0.5
