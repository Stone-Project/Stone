def parse_file(filepath: str):
    """Basic file reader for now. Will be replaced with real AST parser later."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        print(f"📄 Parsed {filepath} ({len(content)} characters)")
        return content
    except Exception as e:
        print(f"❌ Failed to read file: {e}")
        return None
