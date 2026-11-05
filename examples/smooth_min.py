import math


def smooth_min(a, b, k):
    """Polynomial smooth minimum of a and b with blend width k. k <= 0 gives the plain minimum."""
    if k <= 0:
        return min(a, b)
    h = max(k - abs(a - b), 0) / k
    return min(a, b) - h * h * k * 0.25
