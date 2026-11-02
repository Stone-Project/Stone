import math


def tan_deg(d):
    """Tangent of an angle given in degrees. Refuses odd multiples of 90 by returning None."""
    if d % 180 == 90:
        return None
    return math.tan(math.radians(d))
