import math


def exp2_safe(x):
    """2 raised to x. Refuses non-finite input or an overflowing result by returning None."""
    if not math.isfinite(x):
        return None
    try:
        return math.pow(2.0, x)
    except OverflowError:
        return None
