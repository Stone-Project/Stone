def bounce_in(t):
    """Bounce ease-in on t."""
    return 1 - bounce_out(1 - t)


def bounce_out(t):
    """Bounce ease-out on t."""
    return 7.5625 * t * t if t < 1/2.75 else 7.5625 * (t - 1.5/2.75) ** 2 + 0.75 if t < 2/2.75 else 7.5625 * (t - 2.25/2.75) ** 2 + 0.9375 if t < 2.5/2.75 else 7.5625 * (t - 2.625/2.75) ** 2 + 0.984375
