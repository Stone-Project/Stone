import math


def wrap_degrees(d):
    """Wrap degrees to [-180, 180)."""
    return (d + 180) % 360 - 180
