def noise01(x):
    """Cheap pseudo-noise of x in 0 to 1."""
    return abs((x * 12.9898) % 1)
