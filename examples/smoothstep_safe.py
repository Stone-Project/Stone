import math


def smoothstep_safe(edge0, edge1, x):
    """Smooth Hermite step from 0 to 1 as x moves from edge0 to edge1. Refuses non-finite input or equal edges by returning None."""
    if not (math.isfinite(edge0) and math.isfinite(edge1) and math.isfinite(x)):
        return None
    if edge0 == edge1:
        return None
    t = (x - edge0) / (edge1 - edge0)
    if t < 0:
        t = 0
    if t > 1:
        t = 1
    return t * t * (3 - 2 * t)
