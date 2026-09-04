def guess_category(function_name: str, filepath: str = "", code: str = "") -> str:
    """Very early category guess. Replace later with review + hierarchical names."""
    text = f"{function_name} {filepath} {code}".lower()

    rules = [
        ("math", ["sqrt", "sin", "cos", "tan", "pow", "log", "inv", "vector", "matrix", "lerp"]),
        ("render", ["draw", "render", "pixel", "texture", "light", "column", "span", "shader"]),
        ("physics", ["gravity", "velocity", "collision", "impulse", "rigid", "explode"]),
        ("audio", ["sound", "audio", "mix", "sample", "wav"]),
        ("input", ["key", "mouse", "gamepad", "input"]),
        ("util", ["hash", "copy", "clamp", "parse", "normalize"]),
    ]

    for category, keywords in rules:
        if any(word in text for word in keywords):
            return category

    return "unknown"