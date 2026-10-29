import math


def manhattan(x1, y1, x2, y2):
    """Manhattan distance between (x1, y1) and (x2, y2)."""
    return abs(x2 - x1) + abs(y2 - y1)
