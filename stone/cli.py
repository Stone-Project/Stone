#!/usr/bin/env python3
"""Stone CLI"""

import sys
import os
import json
import hashlib
import traceback
from .hasher.parser import parse_file
from .hasher.normalizer import normalize
from .hasher.tester import run_basic_tests, is_safe_for_hashing
from .hasher.library import save_hash, list_hashes, get_by_short_id, delete_hash, search_by_intent, decide_status, find_by_name
from .hasher.categorize import guess_category

def generate_content_hash(normalized_code: str) -> str:
    return hashlib.sha256(normalized_code.encode("utf-8")).hexdigest()

def extract_intent(argv):
    if "--intent" not in argv:
        return ""
    idx = argv.index("--intent")
    return " ".join(argv[idx + 1:]).strip()

def print_help():
    print("""
Stone - Semantic Function Hashing CLI
=====================================

Usage:
  python -m stone.cli <command> [arguments]

Commands:
  hash-function <file> [--intent "what it does"]
  list [category]
  show <short-id>
  delete <short-id>
  intent "description"     Search hashes by intent/name/category
  publish <short-id>       Not enabled yet (local library only)
  packs                    List local pack files
  verify [pack-file]       Check pack jobs against the local library
  help

Examples:
  python -m stone.cli hash-function examples/test_func.py
  python -m stone.cli hash-function examples/test_func.py --intent "fast inverse square root"
  python -m stone.cli list math
  python -m stone.cli show stone-v1:9b04fb6195afe000
""")

def print_entries(entries):
    if not entries:
        print("No matching hashes.")
        return

    print(f"Stone Library ({len(entries)} entries)\n")
    for entry in entries:
        print(f"  {entry.get('short_id')}")
        print(f"     Name    : {entry.get('hierarchical_name', 'n/a')}")
        print(f"     Function: {entry.get('function_name', 'unknown')}")
        print(f"     Category: {entry.get('category', 'unknown')}")
        if entry.get("intent"):
            print(f"     Intent  : {entry.get('intent')}")
        print(f"     Source  : {entry.get('source_file')}")
        print(f"     Status  : {entry.get('status')}  |  Tests: {entry.get('tests_passed')}/{entry.get('tests_total')}")
        print()

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
        intent = extract_intent(sys.argv)
        print(f"Hashing function: {filepath}")

        try:
            parsed = parse_file(filepath)
            if not parsed:
                sys.exit(1)

            code = parsed["code"]
            function_name = parsed["function_name"]
            category = guess_category(function_name, filepath, code)

            normalized = normalize(code)
            test_results = run_basic_tests(code, function_name, filepath)

            if not is_safe_for_hashing(test_results):
                print("Function failed enough tests — not hashing yet.")
                for detail in test_results.get("details", []):
                    print(f"   {detail}")
                sys.exit(1)

            content_hash = generate_content_hash(normalized)
            saved_path, short_id, already_existed, hierarchical_name = save_hash(
                content_hash, filepath, normalized, test_results, function_name, category, intent
            )

            if already_existed:
                print("This function already exists in the library (same content hash)")
            else:
                print("New function added to the library")

            print(f"Function:     {function_name}")
            print(f"Category:     {category}")
            print(f"Name:         {hierarchical_name}")
            print(f"Status:       {decide_status(category, test_results, intent)}")
            if intent:
                print(f"Intent:       {intent}")
            print(f"Content hash: {content_hash}")
            print(f"Short ID:     {short_id}")
            print(f"Saved to:     {saved_path}")

        except Exception as e:
            print(f"Error: {e}")
            print("\n--- Debug traceback ---")
            traceback.print_exc()
            sys.exit(1)

    elif cmd == "list":
        entries = list_hashes()
        if len(sys.argv) > 2:
            category = sys.argv[2].lower()
            entries = [e for e in entries if e.get("category", "").lower() == category]
            print(f"Filter: {category}")
        print_entries(entries)

    elif cmd == "show" and len(sys.argv) > 2:
        short_id = sys.argv[2]
        entry = get_by_short_id(short_id)

        if not entry:
            print(f"No entry found for: {short_id}")
            sys.exit(1)

        print(f"{entry.get('short_id')}")
        print(f"Name         : {entry.get('hierarchical_name', 'n/a')}")
        print(f"Function     : {entry.get('function_name', 'unknown')}")
        print(f"Category     : {entry.get('category', 'unknown')}")
        print(f"Intent       : {entry.get('intent', '')}")
        print(f"Content hash : {entry.get('content_hash')}")
        print(f"Source       : {entry.get('source_file')}")
        print(f"Status       : {entry.get('status')}")
        print(f"Tests        : {entry.get('tests_passed')}/{entry.get('tests_total')}")
        print(f"Created      : {entry.get('created_at')}")
        print(f"Updated      : {entry.get('updated_at')}")
        if entry.get("seen_sources"):
            print(f"Seen in      : {', '.join(entry.get('seen_sources'))}")

    elif cmd == "delete" and len(sys.argv) > 2:
        short_id = sys.argv[2]
        success = delete_hash(short_id)
        if success:
            print(f"Deleted: {short_id}")
        else:
            print(f"Could not find or delete: {short_id}")
            sys.exit(1)

    elif cmd == "packs":
        pack_dir = os.path.join(os.getcwd(), "packs")
        if not os.path.isdir(pack_dir):
            print("No packs directory found.")
            return
        files = [f for f in os.listdir(pack_dir) if f.endswith(".json")]
        if not files:
            print("No pack files found.")
            return
        print(f"Stone Packs ({len(files)})\n")
        for name in sorted(files):
            path = os.path.join(pack_dir, name)
            try:
                with open(path, "r", encoding="utf-8") as f:
                    pack = json.load(f)
                print(f"  {pack.get('pack', name)}")
                print(f"     File   : {name}")
                print(f"     About  : {pack.get('description', '')}")
                for item in pack.get("order", []):
                    print(f"     - {item}")
                print()
            except Exception as e:
                print(f"  {name}: could not read ({e})")

    elif cmd == "verify":
        pack_dir = os.path.join(os.getcwd(), "packs")
        target = sys.argv[2] if len(sys.argv) > 2 else "math_util.json"
        path = target if os.path.isfile(target) else os.path.join(pack_dir, target)
        if not os.path.isfile(path):
            print(f"Pack not found: {target}")
            sys.exit(1)
        try:
            with open(path, "r", encoding="utf-8") as f:
                pack = json.load(f)
        except Exception as e:
            print(f"Could not read pack: {e}")
            sys.exit(1)

        jobs = pack.get("order", [])
        print(f"Verify {pack.get('pack', target)}")
        missing = 0
        untested = 0
        for job in jobs:
            entry = find_by_name(job)
            if not entry:
                print(f"MISS  {job}")
                print("      No local hash. Add the function or pick another backend.")
                missing += 1
                continue
            status = entry.get("status", "unknown")
            mark = "OK  " if status == "verified_basic" else "WARN"
            if status != "verified_basic":
                untested += 1
            print(f"{mark}  {job}")
            print(f"      {entry.get('short_id')}  status={status}")
        print(f"\nMissing: {missing}  Untested: {untested}  Checked: {len(jobs)}")
        if missing:
            print("Verify failed. Offer missing code; do not auto-download.")
            sys.exit(1)

    elif cmd == "publish":
        target = sys.argv[2] if len(sys.argv) > 2 else ""
        print("Publish is not enabled.")
        print("Failed or unreviewed code will not be uploaded.")
        if target:
            print(f"Requested: {target}")
        print("Use local save only until review and license checks exist.")

    elif cmd == "intent" and len(sys.argv) > 2:
        description = " ".join(sys.argv[2:])
        print(f"Intent search: {description}")
        matches = search_by_intent(description)
        print_entries(matches)

    else:
        print("Unknown command.\n")
        print_help()
        sys.exit(1)

if __name__ == "__main__":
    main()
