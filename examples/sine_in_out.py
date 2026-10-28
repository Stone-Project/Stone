import math


def sine_in_out(t):
    """Sine ease-in-out on t."""
    return 0.5 * (1 - math.cos(math.pi * t))
