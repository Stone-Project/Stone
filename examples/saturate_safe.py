import math


def saturate_safe(value):
    """Clamp a number into the 0..1 range. Refuses non-finite input by returning None."""
    if not math.isfinite(value):
        return None
    if value < 0:
        return 0
    if value > 1:
        return 1
    return value
