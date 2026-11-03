import math


def smootherstep01(t):
    """Smootherstep of t, assuming t is already in [0, 1]."""
    return t * t * t * (t * (t * 6 - 15) + 10)
