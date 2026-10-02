def clamp_minmax(value, minimum, maximum):
    """Keep value inside an inclusive range using min and max."""
    return min(maximum, max(minimum, value))
