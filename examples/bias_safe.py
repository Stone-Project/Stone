import math


def bias_safe(x, bias):
    """Bias curve on x in 0 to 1. Refuses non-finite input by returning None."""
    if not (math.isfinite(x) and math.isfinite(bias)):
        return None
    return x ** (math.log(bias) / math.log(0.5))
