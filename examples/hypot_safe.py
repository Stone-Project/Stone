import math


def hypot_safe(a, b):
    """Hypotenuse of a and b. Refuses None or non-finite input by returning None."""
    if a is None or b is None:
        return None
    if not (math.isfinite(a) and math.isfinite(b)):
        return None
    return math.hypot(a, b)
