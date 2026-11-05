import math


def smooth_max(a, b, k):
    """Polynomial smooth maximum of a and b with blend width k. k <= 0 gives the plain maximum."""
    if k <= 0:
        return max(a, b)
    h = max(k - abs(a - b), 0) / k
    return max(a, b) + h * h * k * 0.25
