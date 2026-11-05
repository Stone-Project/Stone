import math


def wrap_degrees_safe(d):
    """Wrap degrees to [-180, 180). Refuses non-finite input by returning None."""
    if not math.isfinite(d):
        return None
    return (d + 180) % 360 - 180
