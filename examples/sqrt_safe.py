import math


def sqrt_safe(x):
    """Square root. Refuses negative input by returning None."""
    if x < 0:
        return None
    return math.sqrt(x)
