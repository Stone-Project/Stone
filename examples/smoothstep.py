def smoothstep(edge0, edge1, x):
    """Smooth Hermite step from 0 to 1 as x moves from edge0 to edge1."""
    t = (x - edge0) / (edge1 - edge0)
    if t < 0:
        t = 0
    if t > 1:
        t = 1
    return t * t * (3 - 2 * t)
