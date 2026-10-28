def apply_drag(velocity, drag, dt):
    """Reduce velocity by drag over one time step. Drag is a rate, not a clamp."""
    return velocity * (1 - drag * dt)
