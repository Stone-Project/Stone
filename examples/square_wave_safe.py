import math


def square_wave_safe(x):
    """Square wave on x with period 2. Refuses non-finite input by returning None."""
    if not math.isfinite(x):
        return None
    return 1 if (x % 2) < 1 else 0
