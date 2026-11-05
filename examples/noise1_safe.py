import math


def noise1_safe(x):
    """Deterministic 1D value noise in [0, 1]: hashes the integer lattice and blends neighbors smoothly. Refuses non-finite input by returning None."""
    if not math.isfinite(x):
        return None
    i = math.floor(x)
    f = x - i
    a = ((i * 1103515245 + 12345) & 0x7FFFFFFF) / 0x7FFFFFFF
    b = (((i + 1) * 1103515245 + 12345) & 0x7FFFFFFF) / 0x7FFFFFFF
    u = f * f * (3 - 2 * f)
    return a + (b - a) * u
