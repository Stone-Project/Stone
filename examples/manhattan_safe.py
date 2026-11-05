import math


def manhattan_safe(x1, y1, x2, y2):
    """Manhattan distance between (x1, y1) and (x2, y2). Refuses None or non-finite input by returning None."""
    if x1 is None or y1 is None or x2 is None or y2 is None:
        return None
    if not (math.isfinite(x1) and math.isfinite(y1) and math.isfinite(x2) and math.isfinite(y2)):
        return None
    return abs(x2 - x1) + abs(y2 - y1)
