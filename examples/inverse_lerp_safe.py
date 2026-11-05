import math


def inverse_lerp_safe(a, b, x):
    """Where x falls between a and b as a fraction. Refuses non-finite input or a == b by returning None."""
    if not (math.isfinite(a) and math.isfinite(b) and math.isfinite(x)):
        return None
    if a == b:
        return None
    return (x - a) / (b - a)
