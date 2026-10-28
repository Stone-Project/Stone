def round_to(x, step):
    """Round x to the nearest multiple of step."""
    return ((x + step / 2) // step) * step
