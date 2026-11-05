import math


def damp_safe(current, target, rate, dt):
    """Critically damped approach of current toward target. Refuses non-finite input or dt <= 0 by returning None."""
    if not (math.isfinite(current) and math.isfinite(target) and math.isfinite(rate) and math.isfinite(dt)):
        return None
    if dt <= 0:
        return None
    return current + (target - current) * (1 - math.exp(-rate * dt))
