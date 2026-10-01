def apply_gravity(velocity_y, gravity, dt):
    """Add gravity to a vertical velocity for one time step."""
    return velocity_y + gravity * dt
