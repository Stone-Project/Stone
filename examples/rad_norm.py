import math


def rad_norm(r):
    """Normalize radians to [0, 2*pi)."""
    return r % (2 * math.pi)
