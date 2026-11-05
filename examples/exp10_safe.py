import math


def exp10_safe(x):
    """10 raised to x. Refuses non-finite input or an overflowing result by returning None."""
    if not math.isfinite(x):
        return None
    try:
        return math.pow(10.0, x)
    except OverflowError:
        return None
