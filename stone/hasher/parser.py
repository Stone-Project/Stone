def parse_file(filepath: str):
    """
    Read a source file and do light validation.
    Still simple — real AST parsing can come later.
    """
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()

        if not content.strip():
            print("❌ File is empty")
            return None

        print(f"📄 Parsed {filepath} ({len(content)} characters)")
        return content

    except FileNotFoundError:
        print(f"❌ File not found: {filepath}")
        return None
    except Exception as e:
        print(f"❌ Failed to read file: {e}")
        return None
