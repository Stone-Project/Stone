#!/usr/bin/env python3
"""Stone CLI"""

import sys
import hashlib
import traceback
from .hasher.parser import parse_file
from .hasher.normalizer import normalize
from .hasher.tester import run_basic_tests, is_safe_for_hashing
from .hasher.library import save_hash, list_hashes, get_by_short_id, delete_hash

def generate_content_hash(normalized_code: str) -> str:
    """Create a stable SHA-256 hash of the normalized code."""
    return hashlib.sha256(normalized_code.encode("utf-8")).hexdigest()

def print_help():
    print("""
Stone - Semantic Function Hashing CLI
=====================================

Usage:
  python -m stone.cli <command> [arguments]

Commands:
  hash-function <file>     Parse, normalize, test, and hash a function
  list                     Show all hashes currently in the library
  show <short-id>          Show details for a specific hash
  delete <short-id>        Remove a hash from the library
  intent "description"     (Coming soon) Search by natural language intent
  help                     Show this help message

Examples:
  python -m stone.cli hash-function examples/test_func.py
  python -m stone.cli list
  python -m stone.cli show stone-v1:9b04fb6195afe000
  python -m stone.cli delete stone-v1:9b04fb6195afe000
  python -m stone.cli help
""")

def main():
    if len(sys.argv) < 2:
        print_help()
        sys.exit(1)

    cmd = sys.argv[1]

    if cmd in ("help", "--help", "-h"):
        print_help()
        return

    if cmd == "hash-function" and len(sys.argv) > 2:
        filepath = sys.argv[2]
        print(f"🔨 Hashing function: {filepath}")

        try:
            code = parse_file(filepath)
            if not code:
                sys.exit(1)

            normalized = normalize(code)
            test_results = run_basic_tests(code, filepath)

            if not is_safe_for_hashing(test_results):
                print("⚠️  Function failed enough tests — not hashing yet.")
                for detail in test_results.get("details", []):
                    print(f"   {detail}")
                sys.exit(1)

            content_hash = generate_content_hash(normalized)
            saved_path, short_id, already_existed = save_hash(
                content_hash, filepath, normalized, test_results
            )

            if already_existed:
                print("♻️  This function already exists in the library (same content hash)")
            else:
                print("✅ New function added to the library")

            print(f"🔑 Content hash: {content_hash}")
            print(f"📌 Short ID:     {short_id}")
            print(f"💾 Saved to:     {saved_path}")

        except Exception as e:
            print(f"❌ Error: {e}")
            print("\n--- Debug traceback ---")
            traceback.print_exc()
            sys.exit(1)

    elif cmd == "list":
        entries = list_hashes()
        if not entries:
            print("📭 Library is empty.")
            return

        print(f"📚 Stone Library ({len(entries)} entries)\n")
        for entry in entries:
            print(f"  {entry.get('short_id')}")
            print(f"     Source  : {entry.get('source_file')}")
            print(f"     Status  : {entry.get('status')}  |  Tests: {entry.get('tests_passed')}/{entry.get('tests_total')}")
            print(f"     Version : {entry.get('version', 'unknown')}")
            print(f"     Updated : {entry.get('updated_at', entry.get('created_at'))}")
            print()

    elif cmd == "show" and len(sys.argv) > 2:
        short_id = sys.argv[2]
        entry = get_by_short_id(short_id)

        if not entry:
            print(f"❌ No entry found for: {short_id}")
            sys.exit(1)

        print(f"📌 {entry.get('short_id')}")
        print(f"🔑 Content hash : {entry.get('content_hash')}")
        print(f"📁 Source       : {entry.get('source_file')}")
        print(f"✅ Status       : {entry.get('status')}")
        print(f"🧪 Tests        : {entry.get('tests_passed')}/{entry.get('tests_total')}")
        print(f"📅 Created      : {entry.get('created_at')}")
        print(f"🔄 Updated      : {entry.get('updated_at')}")
        if entry.get("seen_sources"):
            print(f"👀 Seen in      : {', '.join(entry.get('seen_sources'))}")

    elif cmd == "delete" and len(sys.argv) > 2:
        short_id = sys.argv[2]
        success = delete_hash(short_id)

        if success:
            print(f"🗑️  Deleted: {short_id}")
        else:
            print(f"❌ Could not find or delete: {short_id}")
            sys.exit(1)

    elif cmd == "intent" and len(sys.argv) > 2:
        description = " ".join(sys.argv[2:])
        print(f"💡 Intent: {description}")
        print("🔍 (Search not implemented yet)")

    else:
        print("Unknown command.\n")
        print_help()
        sys.exit(1)

if __name__ == "__main__":
    main()