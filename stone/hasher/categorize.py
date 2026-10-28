def guess_category(function_name: str, filepath: str = "", code: str = "") -> str:
    """Very early category guess. Replace later with review + hierarchical names."""
    text = f"{function_name} {filepath} {code}".lower()

    rules = [
        ("health", ["heal", "damage", "health", "armor"]),
        ("physics", ["gravity", "velocity", "collision", "impulse", "rigid", "explode", "aabb", "overlap", "force", "drag"]),
        ("math", ["sqrt", "sin", "cos", "tan", "pow", "log", "inv", "vector", "matrix", "lerp", "saturate", "map_range", "sign", "abs", "square", "approach", "min", "max", "wrap", "deadzone", "map", "range", "inverse"]),
        ("util", ["clamp", "minmax", "hash", "copy", "parse", "normalize", "overlap", "aabb"]),
        ("render", ["draw", "render", "pixel", "texture", "light", "column", "span", "shader"]),
        ("audio", ["sound", "audio", "mix", "sample", "wav"]),
        ("input", ["key", "mouse", "gamepad", "input"]),
    ]

    for category, keywords in rules:
        if any(word in text for word in keywords):
            return category

    return "unknown"
