def apply_damage(health, amount):
    """Subtract damage from health. Does not go below zero."""
    health = health - amount
    if health < 0:
        return 0
    return health
