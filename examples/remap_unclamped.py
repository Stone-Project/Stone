import math


def remap_unclamped(x, in_min, in_max, out_min, out_max):
    """Map x from one range onto another, without clamping. Refuses an empty input range by returning None."""
    if in_min == in_max:
        return None
    return out_min + (out_max - out_min) * (x - in_min) / (in_max - in_min)
