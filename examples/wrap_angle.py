import math


def wrap_angle(a):
    """Wrap an angle in radians to [-pi, pi)."""
    return (a + math.pi) % (2 * math.pi) - math.pi
