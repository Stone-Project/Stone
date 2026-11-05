import math


def deg_lerp(a, b, t):
    """Lerp from a to b in degrees along the shortest path, result not wrapped. An exact 180 tie goes the negative way."""
    d = (b - a + 180) % 360 - 180
    return a + d * t
