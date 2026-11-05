import math


def log_safe(x):
    """Natural log. Refuses non-positive or non-finite input by returning None."""
    if not math.isfinite(x) or x <= 0:
        return None
    return math.log(x)
