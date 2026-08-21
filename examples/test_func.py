def fast_inverse_sqrt(x):
    """Classic Quake-style fast inverse square root."""
    i = int(x * 0x5f3759df) >> 1
    y = x * (1.5 - (x * 0.5 * i * i))
    return y
