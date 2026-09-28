def lerp(start, end, t):
    """Linear interpolate from start to end by t in 0..1."""
    return start + (end - start) * t
