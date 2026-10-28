def approach(current, target, step):
    """Move current toward target by at most step."""
    if step < 0:
        step = -step
    if current < target:
        next_value = current + step
        if next_value > target:
            return target
        return next_value
    next_value = current - step
    if next_value < target:
        return target
    return next_value
