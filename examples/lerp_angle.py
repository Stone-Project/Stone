import math


def lerp_angle(a, b, t):
    """Lerp from angle a to angle b along the shortest path."""
    d = (b - a + math.pi) % (2 * math.pi) - math.pi
    return a + d * t
