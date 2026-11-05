import math


def inverse_lerp_unclamped(a, b, x):
    """Where x falls between a and b as a fraction, without clamping. Refuses a == b by returning None."""
    if a == b:
        return None
    return (x - a) / (b - a)
