import math


def exp_decay(value, rate, t):
    """Exponential decay: value * exp(-rate * t)."""
    return value * math.exp(-rate * t)
