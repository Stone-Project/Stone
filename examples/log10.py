import math


def log10(x):
    """Log base 10. Refuses non-positive input by returning None."""
    if x <= 0:
        return None
    return math.log10(x)
