import math


def pow_safe(base, exponent):
    """Power that stays real. Negative base with a non-integer exponent returns 0."""
    if base < 0 and not float(exponent).is_integer():
        return 0.0
    return base ** exponent
