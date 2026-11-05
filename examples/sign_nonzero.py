import math


def sign_nonzero(x):
    """Sign of x as -1, 0 or 1, returning 0 only for exact zero."""
    return (x > 0) - (x < 0)
