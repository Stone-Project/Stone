import math


def chebyshev(x1, y1, x2, y2):
    """Chebyshev distance between (x1, y1) and (x2, y2)."""
    return max(abs(x2 - x1), abs(y2 - y1))
