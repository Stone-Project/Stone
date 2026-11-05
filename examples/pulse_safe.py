import math


def pulse_safe(x, duty):
    """Pulse wave with period 1: 1 while the phase is below duty, else 0. Refuses non-finite input or duty outside (0, 1) by returning None."""
    if not (math.isfinite(x) and math.isfinite(duty)):
        return None
    if duty <= 0 or duty >= 1:
        return None
    return 1 if (x % 1) < duty else 0
