import math


def acos_deg(x):
    """Arccosine returning degrees. Refuses input outside [-1, 1] by returning None."""
    if x < -1 or x > 1:
        return None
    return math.degrees(math.acos(x))
