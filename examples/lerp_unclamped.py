def lerp_unclamped(a, b, t):
    """Linear blend from a to b by t, without clamping t."""
    return a + (b - a) * t
