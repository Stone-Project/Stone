import math


def clamp11(x):
    """Clamp x to the range -1 to 1."""
    return -1 if x < -1 else 1 if x > 1 else x
