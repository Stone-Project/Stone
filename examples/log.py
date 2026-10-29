import math


def log(x):
    """Natural log. Refuses non-positive input by returning None."""
    if x <= 0:
        return None
    return math.log(x)
