def pingpong(x, length):
    """Ping-pong x between 0 and length."""
    return abs((x % (2 * length)) - length)
