import re

def normalize(code: str) -> str:
    """
    Basic but improved normalizer.
    Goal: make functionally similar code produce the same hash
    while staying simple and predictable.
    """
    if not code:
        return ""

    # 1. Normalize line endings
    code = code.replace("\r\n", "\n").replace("\r", "\n")

    # 2. Remove full-line comments (simple version)
    lines = []
    for line in code.split("\n"):
        stripped = line.strip()
        if stripped.startswith("#"):
            continue
        lines.append(line)
    code = "\n".join(lines)

    # 3. Collapse multiple blank lines into one
    code = re.sub(r"\n\s*\n+", "\n\n", code)

    # 4. Strip leading/trailing whitespace on each line
    lines = [line.rstrip() for line in code.split("\n")]
    code = "\n".join(lines)

    # 5. Final strip
    code = code.strip()

    print("🔧 Normalization complete")
    return code
