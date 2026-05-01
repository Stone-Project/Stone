#!/usr/bin/env python3
"""Stone CLI"""

import sys
from .hasher.parser import parse_file
from .hasher.normalizer import normalize

def main():
    if len(sys.argv) < 2:
        print("Usage: stone hash-function <file>   or   stone intent \"description\"")
        return

    cmd = sys.argv[1]

    if cmd == "hash-function" and len(sys.argv) > 2:
        filepath = sys.argv[2]
        print(f"🔨 Hashing function: {filepath}")
        try:
            code = parse_file(filepath)
            if code:
                normalized = normalize(code)
                print("✅ Successfully parsed and normalized")
        except Exception as e:
            print(f"❌ Error: {e}")

    elif cmd == "intent" and len(sys.argv) > 2:
        description = " ".join(sys.argv[2:])
        print(f"💡 Intent: {description}")
        print("🔍 (Search not implemented yet)")

    else:
        print("Unknown command")

if __name__ == "__main__":
    main()
