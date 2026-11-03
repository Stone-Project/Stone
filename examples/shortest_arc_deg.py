import math


def shortest_arc_deg(a, b):
    """Shortest signed arc from a to b in degrees, in (-180, 180]."""
    d = (b - a) % 360
    if d > 180:
        d -= 360
    return d
