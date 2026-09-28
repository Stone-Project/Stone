def saturate(value):
    """Clamp a number into the 0..1 range."""
    if value < 0:
        return 0
    if value > 1:
        return 1
    return value
