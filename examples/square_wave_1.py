import math


def square_wave_1(x):
    """Square wave with period 1: 1 for the first half of each period, 0 for the second."""
    return 1 if (x % 1) < 0.5 else 0
