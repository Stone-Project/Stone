def aabb_overlap(ax, ay, aw, ah, bx, by, bw, bh):
    """Return True if two axis-aligned boxes overlap."""
    return ax < bx + bw and ax + aw > bx and ay < by + bh and ay + ah > by
