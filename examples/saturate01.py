import math


def saturate01(x):
    """Saturate x to the range 0 to 1 using min and max."""
    return min(1, max(0, x))
