import math


def cbrt_safe(x):
    """Real cube root, negative input gives a negative root. Refuses non-finite input by returning None."""
    if not math.isfinite(x):
        return None
    return math.copysign(abs(x) ** (1 / 3), x)
