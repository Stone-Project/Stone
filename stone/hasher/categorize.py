def guess_category(function_name: str, filepath: str = "", code: str = "") -> str:
    """Very early category guess. Replace later with review + hierarchical names."""
    text = f"{function_name} {filepath} {code}".lower()

    rules = [
        ("health", ["heal", "damage", "health", "armor"]),
        ("util", ["clamp", "minmax", "hash", "copy", "parse", "normalize"]),
        ("math", ["sqrt", "sin", "cos", "tan", "pow", "log", "inv", "vector", "matrix", "lerp", "saturate", "map_range"]),
        ("render", ["draw", "render", "pixel", "texture", "light", "column", "span", "shader"]),
        ("physics", ["gravity", "velocity", "collision", "impulse", "rigid", "explode", "aabb", "overlap"]),
        ("audio", ["sound", "audio", "mix", "sample", "wav"]),
        ("input", ["key", "mouse", "gamepad", "input"]),
    ]

    for category, keywords in rules:
        if any(word in text for word in keywords):
            return category

    return "unknown"
