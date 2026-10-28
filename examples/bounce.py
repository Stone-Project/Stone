def bounce(x):
    """Bounce x between 0 and 1 with period 2."""
    return 1 - abs((x % 2) - 1)
