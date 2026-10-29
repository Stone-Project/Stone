import math


def cbrt(x):
    """Real cube root, negative input gives a negative root."""
    return math.copysign(abs(x) ** (1 / 3), x)
