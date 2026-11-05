import math


def log10_safe(x):
    """Log base 10. Refuses non-positive or non-finite input by returning None."""
    if not math.isfinite(x) or x <= 0:
        return None
    return math.log10(x)
