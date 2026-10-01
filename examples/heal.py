def heal(health, amount, max_health):
    """Add health up to a maximum. The maximum is a parameter, not part of the hash."""
    health = health + amount
    if health > max_health:
        return max_health
    return health
