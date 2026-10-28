import math


def sine_in(t):
    """Sine ease-in on t."""
    return 1 - math.cos(t * math.pi / 2)
