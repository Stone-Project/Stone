import math


def exp_decay_safe(value, rate, t):
    """Exponential decay value * exp(-rate * t). Refuses non-finite input or negative t by returning None."""
    if not (math.isfinite(value) and math.isfinite(rate) and math.isfinite(t)):
        return None
    if t < 0:
        return None
    return value * math.exp(-rate * t)
