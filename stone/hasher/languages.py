import os
import shutil

# One row per language. A loader is code in this repo. A tool is a compiler on PATH.
# Unknown extensions are not added here automatically.
LANGUAGES = [
    {"language": "python", "extensions": [".py"], "tools": ["python"], "loader": True},
    {"language": "c", "extensions": [".c", ".h"], "tools": ["gcc", "clang"], "loader": True},
    {"language": "rust", "extensions": [".rs"], "tools": ["rustc"], "loader": False},
    {"language": "go", "extensions": [".go"], "tools": ["go"], "loader": False},
]


def tool_on_path(names):
    for name in names:
        if shutil.which(name):
            return name
    return ""


def language_for_path(path: str):
    lower = (path or "").lower()
    for row in LANGUAGES:
        if any(lower.endswith(ext) for ext in row["extensions"]):
            return row
    return None


def describe_languages():
    lines = []
    for row in LANGUAGES:
        tool = tool_on_path(row["tools"])
        if row["loader"] and tool:
            state = f"callable via {tool}"
        elif row["loader"]:
            state = "loader exists, tool missing"
        elif tool:
            state = f"{tool} found, no loader yet"
        else:
            state = "no loader, tool missing"
        exts = ", ".join(row["extensions"])
        lines.append(f"{row['language']:8} {exts:12} {state}")
    return lines


def admit_source(path: str):
    """Say what Stone can do with a file. Does not download a compiler or invent a loader."""
    row = language_for_path(path)
    if row is None:
        return {"ok": False, "reason": "unknown language, no loader"}
    tool = tool_on_path(row["tools"])
    if not row["loader"]:
        return {"ok": False, "language": row["language"], "reason": "known language, no loader yet"}
    if not tool:
        return {"ok": False, "language": row["language"], "reason": "loader exists, tool missing"}
    return {"ok": True, "language": row["language"], "tool": tool}
