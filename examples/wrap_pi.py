import math


def wrap_pi(a):
    """Wrap radians to (-pi, pi]."""
    r = a % (2 * math.pi)
    if r > math.pi:
        r -= 2 * math.pi
    return r
