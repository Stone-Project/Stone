import math


def mix_safe(a, b, t):
    """Blend from a to b by t. Refuses non-finite input by returning None."""
    if not (math.isfinite(a) and math.isfinite(b) and math.isfinite(t)):
        return None
    return a + (b - a) * t
