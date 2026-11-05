import math


def saw_wave(x):
    """Sawtooth wave with period 1, in [0, 1), using x minus floor(x)."""
    return x - math.floor(x)
