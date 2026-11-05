import math


def smoothstep_unclamped(edge0, edge1, x):
    """Smoothstep from edge0 to edge1 without clamping. Refuses equal edges by returning None."""
    if edge0 == edge1:
        return None
    t = (x - edge0) / (edge1 - edge0)
    return t * t * (3 - 2 * t)
