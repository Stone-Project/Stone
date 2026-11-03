import math


def hypot_deg(a, b):
    """Angle in degrees opposite leg a, from a over the hypotenuse of a and b. Refuses a zero hypotenuse by returning None."""
    h = math.hypot(a, b)
    if h == 0:
        return None
    return math.degrees(math.asin(a / h))
