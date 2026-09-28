def map_range(value, in_min, in_max, out_min, out_max):
    """Map value from one range into another using linear interpolation."""
    if in_max == in_min:
        return out_min
    t = (value - in_min) / (in_max - in_min)
    return out_min + (out_max - out_min) * t
