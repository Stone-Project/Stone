import math


def lerp_safe(start, end, t):
    """Linear interpolate from start to end by t. Refuses non-finite input by returning None."""
    if not (math.isfinite(start) and math.isfinite(end) and math.isfinite(t)):
        return None
    return start + (end - start) * t
