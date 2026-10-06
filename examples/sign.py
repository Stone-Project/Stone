def sign(value):
    """Return -1, 0, or 1 for the sign of a number."""
    if value < 0:
        return -1
    if value > 0:
        return 1
    return 0
