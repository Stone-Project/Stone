def deadzone(value, threshold):
    """Return 0 when value is within threshold of 0. Otherwise return value."""
    if threshold < 0:
        threshold = -threshold
    if value < 0:
        if -value <= threshold:
            return 0
        return value
    if value <= threshold:
        return 0
    return value
