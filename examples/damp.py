import math


def damp(current, target, rate, dt):
    """Critically damped approach of current toward target."""
    return current + (target - current) * (1 - math.exp(-rate * dt))
