import math


def smoothstep01(t):
    """Smoothstep of t, assuming t is already in [0, 1]."""
    return t * t * (3 - 2 * t)
