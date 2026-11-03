import math


def wrap_180(d):
    """Wrap degrees to (-180, 180]."""
    r = d % 360
    if r > 180:
        r -= 360
    return r
