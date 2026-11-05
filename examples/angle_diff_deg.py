import math


def angle_diff_deg(a, b):
    """Shortest signed difference from a to b in degrees, in (-180, 180]."""
    d = (b - a + 180) % 360 - 180
    if d == -180:
        d = 180
    return d
