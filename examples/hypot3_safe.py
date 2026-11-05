import math


def hypot3_safe(a, b, c):
    """Hypotenuse of a, b and c. Refuses None or non-finite input by returning None."""
    if a is None or b is None or c is None:
        return None
    if not (math.isfinite(a) and math.isfinite(b) and math.isfinite(c)):
        return None
    return math.sqrt(a * a + b * b + c * c)
