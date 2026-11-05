import math


def deg_lerp_safe(a, b, t):
    """Lerp from a to b in degrees along the shortest path, result not wrapped. An exact 180 tie goes the negative way. Refuses non-finite input by returning None."""
    if not (math.isfinite(a) and math.isfinite(b) and math.isfinite(t)):
        return None
    d = (b - a + 180) % 360 - 180
    return a + d * t
