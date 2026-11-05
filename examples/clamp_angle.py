import math


def clamp_angle(a, lo, hi):
    """Clamp an angle in degrees to the arc from lo counterclockwise to hi, handling wrap. Result in [0, 360). Outside the arc it returns the nearer end, hi on a tie."""
    span = (hi - lo) % 360
    off = (a - lo) % 360
    if off <= span:
        return (lo + off) % 360
    if off - span <= 360 - off:
        return hi % 360
    return lo % 360
