def hash01(x):
    """Cheap hash of x in 0 to 1."""
    return abs((x * 0.1031) % 1)
