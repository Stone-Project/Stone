import math


def wrap_angle_safe(a):
    """Wrap an angle in radians to [-pi, pi). Refuses non-finite input by returning None."""
    if not math.isfinite(a):
        return None
    return (a + math.pi) % (2 * math.pi) - math.pi
