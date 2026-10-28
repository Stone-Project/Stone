def wrap_value(value, low, high):
    """Wrap value into the half-open range low..high."""
    span = high - low
    if span == 0:
        return low
    offset = value - low
    return low + (offset % span)
