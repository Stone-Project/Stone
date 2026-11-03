import math


def atan2_deg(y, x):
    """atan2 of y and x in degrees, in (-180, 180]."""
    r = math.degrees(math.atan2(y, x))
    if r <= -180:
        r += 360
    return r
