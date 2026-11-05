import math


def step_unclamped(edge, x, width):
    """Linear step through edge with the given width, centered so x == edge gives 0.5, without clamping. Refuses width <= 0 by returning None."""
    if width <= 0:
        return None
    return (x - edge) / width + 0.5
