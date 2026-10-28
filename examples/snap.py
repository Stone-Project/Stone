def snap(x, step):
    """Snap x to the nearest multiple of step."""
    return ((x + step / 2) // step) * step
