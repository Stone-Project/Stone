import math


def asin_deg(x):
    """Arcsine returning degrees. Refuses input outside [-1, 1] by returning None."""
    if x < -1 or x > 1:
        return None
    return math.degrees(math.asin(x))
