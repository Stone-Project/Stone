def ceil_to(x, step):
    """Round x up to a multiple of step."""
    return ((x + step - 1) // step) * step
