import math


def smootherstep_unclamped(edge0, edge1, x):
    """Smootherstep from edge0 to edge1 without clamping. Refuses equal edges by returning None."""
    if edge0 == edge1:
        return None
    t = (x - edge0) / (edge1 - edge0)
    return t * t * t * (t * (t * 6 - 15) + 10)
