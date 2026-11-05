import math


def smootherstep_safe(edge0, edge1, x):
    """Smoother S-curve from edge0 to edge1. Refuses non-finite input or equal edges by returning None."""
    if not (math.isfinite(edge0) and math.isfinite(edge1) and math.isfinite(x)):
        return None
    if edge0 == edge1:
        return None
    t = (x - edge0) / (edge1 - edge0)
    if t < 0:
        return 0.0
    if t > 1:
        return 1.0
    return t * t * t * (t * (t * 6 - 15) + 10)
