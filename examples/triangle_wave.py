import math


def triangle_wave(x):
    """Triangle wave with period 1, rising from 0 at x=0 to 1 at x=0.5 and back to 0."""
    return 1 - abs(2 * (x % 1) - 1)
