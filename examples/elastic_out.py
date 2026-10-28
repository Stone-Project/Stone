def elastic_out(t):
    """Elastic ease-out on t."""
    return 0 if t == 0 else 1 if t == 1 else 2 ** (-10 * t) * (t * 10 - 0.75) ** 0.5 + 1
