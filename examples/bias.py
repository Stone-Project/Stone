import math


def bias(x, bias):
    """Bias curve on x in 0 to 1."""
    return x ** (math.log(bias) / math.log(0.5))
