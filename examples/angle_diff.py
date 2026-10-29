import math


def angle_diff(a, b):
    """Shortest signed difference from angle a to angle b in radians, range [-pi, pi)."""
    return (b - a + math.pi) % (2 * math.pi) - math.pi
