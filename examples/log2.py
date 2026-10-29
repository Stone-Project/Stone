import math


def log2(x):
    """Log base 2. Refuses non-positive input by returning None."""
    if x <= 0:
        return None
    return math.log2(x)
