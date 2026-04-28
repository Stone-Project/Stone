#!/usr/bin/env python3
"""Stone CLI - Main entry point."""

import sys
from .hasher.parser import parse_file
from .hasher.normalizer import normalize

def main():
    if len(sys.argv) < 2:
        print("Usage: stone hash-function <file>  or  stone intent \"description\"")
        sys.exit(1)

    command = sys.argv[1]

    if command == "hash-function" and len(sys.argv) > 2:
        filepath = sys.argv[2]
        print(f"🔨 Hashing function: {filepath}")
        # Placeholder for now
        try:
            ast = parse_file(filepath)
            normalized = normalize(ast)
            print("✅ Parsed and normalized successfully")
            print(f"Normalized form: {normalized[:200]}..." if len(str(normalized)) > 200 else normalized)
        except Exception as e:
            print(f"❌ Error: {e}")

    elif command == "intent" and len(sys.argv) > 2:
        description = " ".join(sys.argv[2:])
        print(f"💡 Intent received: {description}")
        print("🔍 Searching for best matching hash... (not implemented yet)")

    else:
        print("Unknown command. Use 'hash-function' or 'intent'")

if __name__ == "__main__":
    main()
