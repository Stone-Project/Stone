import math


def log2_safe(x):
    """Log base 2. Refuses non-positive or non-finite input by returning None."""
    if not math.isfinite(x) or x <= 0:
        return None
    return math.log2(x)
