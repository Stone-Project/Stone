import math


def dist(x1, y1, x2, y2):
    """Euclidean distance between (x1, y1) and (x2, y2)."""
    return math.hypot(x2 - x1, y2 - y1)
