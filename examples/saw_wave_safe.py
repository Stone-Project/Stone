import math


def saw_wave_safe(x):
    """Sawtooth wave with period 1, in [0, 1), using x minus floor(x). Refuses non-finite input by returning None."""
    if not math.isfinite(x):
        return None
    return x - math.floor(x)
