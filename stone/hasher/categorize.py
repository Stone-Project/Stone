import re


def purpose_marker(code: str) -> str:
    """First docstring or first comment that starts a line, cut to 200 characters."""
    if not code:
        return ""
    match = re.search(r'("""|\'\'\')(.*?)\1|^[ \t]*#(.*)$', code, re.S | re.M)
    if not match:
        return ""
    text = match.group(2) if match.group(2) is not None else match.group(3)
    return (text or "").strip()[:200]


def guess_category(function_name: str, filepath: str = "", code: str = "") -> str:
    """Very early category guess. Replace later with review + hierarchical names."""
    marker = purpose_marker(code).lower()

    rules = [
        ("health", ["heal", "damage", "health", "armor"]),
        ("physics", ["gravity", "velocity", "collision", "impulse", "rigid", "explode", "aabb", "overlap", "force", "drag"]),
        ("math", ["sqrt", "sin", "cos", "tan", "pow", "log", "inv", "vector", "matrix", "lerp", "saturate", "map_range", "sign", "abs", "square", "approach", "min", "max", "wrap", "deadzone", "map", "range", "inverse"]),
        ("util", ["clamp", "minmax", "hash", "copy", "parse", "normalize", "overlap", "aabb"]),
        ("render", ["draw", "render", "pixel", "texture", "light", "column", "span", "shader"]),
        ("audio", ["sound", "audio", "mix", "sample", "wav"]),
        ("input", ["key", "mouse", "gamepad", "input"]),
    ]

    if marker:
        for category, keywords in rules:
            if any(word in marker for word in keywords):
                return category

    text = f"{function_name} {filepath} {code}".lower()
    for category, keywords in rules:
        if any(word in text for word in keywords):
            return category

    return "unknown"
