def clamp(value, minimum, maximum):
    """Keep value inside an inclusive range."""
    if value < minimum:
        return minimum
    if value > maximum:
        return maximum
    return value
