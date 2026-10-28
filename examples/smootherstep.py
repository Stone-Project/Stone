def smootherstep(edge0, edge1, x):
    """Smoother S-curve from edge0 to edge1."""
    t = (x - edge0) / (edge1 - edge0)
    return t * t * t * (t * (t * 6 - 15) + 10) if 0 <= t <= 1 else 0 if t < 0 else 1
