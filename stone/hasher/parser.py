import os
import re

def parse_file(filepath: str):
    """
    Read a source file and extract a basic function name if possible.
    Still simple — real AST parsing can come later.
    Returns: {"code": str, "function_name": str} or None
    """
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()

        if not content.strip():
            print("❌ File is empty")
            return None

        function_name = extract_function_name(content, filepath)

        print(f"📄 Parsed {filepath} ({len(content)} characters)")
        print(f"📦 Function name: {function_name}")
        return {
            "code": content,
            "function_name": function_name
        }

    except FileNotFoundError:
        print(f"❌ File not found: {filepath}")
        return None
    except Exception as e:
        print(f"❌ Failed to read file: {e}")
        return None

def extract_function_name(code: str, filepath: str) -> str:
    """Best-effort function name from Python/C-like code."""
    patterns = [
        r"^\s*def\s+([A-Za-z_][A-Za-z0-9_]*)\s*\(",
        r"^\s*(?:static\s+)?(?:inline\s+)?[A-Za-z_][\w\s\*]*\s+([A-Za-z_][A-Za-z0-9_]*)\s*\(",
        r"^\s*function\s+([A-Za-z_][A-Za-z0-9_]*)\s*\(",
        r"^\s*fn\s+([A-Za-z_][A-Za-z0-9_]*)\s*\(",
    ]

    for pattern in patterns:
        match = re.search(pattern, code, re.MULTILINE)
        if match:
            return match.group(1)

    base = os.path.splitext(os.path.basename(filepath))[0]
    return base or "unknown"