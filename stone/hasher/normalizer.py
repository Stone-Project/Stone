import re

def normalize(code: str) -> str:
    """
    Basic but improved normalizer.
    Goal: make functionally similar code produce the same hash
    while staying simple and predictable.
    """
    if not code:
        return ""

    code = code.replace("\r\n", "\n").replace("\r", "\n")

    lines = []
    for line in code.split("\n"):
        stripped = line.strip()
        if stripped.startswith("#"):
            continue
        lines.append(line)
    code = "\n".join(lines)

    code = re.sub(r"\n\s*\n+", "\n\n", code)

    lines = [line.rstrip() for line in code.split("\n")]
    code = "\n".join(lines).strip()

    print("Normalization complete")
    return code
   