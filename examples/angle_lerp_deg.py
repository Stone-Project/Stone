import math


def angle_lerp_deg(a, b, t):
    """Lerp from a to b in degrees along the shortest path, result in [0, 360)."""
    diff = (b - a + 180) % 360 - 180
    return (a + diff * t) % 360
