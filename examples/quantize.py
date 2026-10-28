def quantize(x, step):
    """Quantize x down to a multiple of step."""
    return ((x / step) // 1) * step
