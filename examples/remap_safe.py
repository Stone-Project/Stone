import math


def remap_safe(x, in_min, in_max, out_min, out_max):
    """Map x from one range onto another. Refuses non-finite input or an empty input range by returning None."""
    if not (math.isfinite(x) and math.isfinite(in_min) and math.isfinite(in_max) and math.isfinite(out_min) and math.isfinite(out_max)):
        return None
    if in_min == in_max:
        return None
    return out_min + (out_max - out_min) * (x - in_min) / (in_max - in_min)
