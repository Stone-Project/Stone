#!/usr/bin/env python3
"""Stone CLI"""

import sys
import os
import json
import time
import hashlib
import importlib.util
import traceback
from .hasher.parser import parse_file
from .hasher.normalizer import normalize
from .hasher.tester import run_basic_tests, is_safe_for_hashing
from .hasher.library import save_hash, list_hashes, get_by_short_id, delete_hash, search_by_intent, decide_status, find_by_name, find_backends
from .hasher.categorize import guess_category

def generate_content_hash(normalized_code: str) -> str:
    return hashlib.sha256(normalized_code.encode("utf-8")).hexdigest()

def extract_flag_args(argv, flag):
    if flag not in argv:
        return []
    idx = argv.index(flag)
    values = []
    for item in argv[idx + 1:]:
        if item.startswith("--"):
            break
        values.append(item)
    return values

def extract_intent(argv):
    return " ".join(extract_flag_args(argv, "--intent")).strip()

def extract_depends(argv):
    return extract_flag_args(argv, "--depends")

def extract_job(argv):
    values = extract_flag_args(argv, "--job")
    return values[0] if values else ""

def print_help():
    print("""
Stone - Semantic Function Hashing CLI
=====================================

Usage:
  python -m stone.cli <command> [arguments]

Commands:
  hash-function <file> [--intent "what it does"] [--depends name ...] [--job name]
  list [category]
  show <short-id>
  delete <short-id>
  intent "description"     Search hashes by intent/name/category
  call <name> [args...]    Run a verified local hash
  backends <job>           List local backends for one job
  run <file.json>          Run a sequence of verified calls
  publish <short-id>       Not enabled yet (local library only)
  packs                    List local pack files
  verify [pack-file]       Check pack jobs against the local library
  help

Examples:
  python -m stone.cli hash-function examples/inverse_sqrt_quake.py --intent "fast inverse square root" --job stone:math.inverse_sqrt
  python -m stone.cli backends stone:math.inverse_sqrt
  python -m stone.cli call stone:math.inverse_sqrt 4 --backend inverse_sqrt_quake
  python -m stone.cli run examples/health_turn.json
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
        if entry.get("job"):
            print(f"     Job     : {entry.get('job')}")
        if entry.get("timing_us") is not None:
            print(f"     Time    : {entry.get('timing_us')} us")
        if entry.get("intent"):
            print(f"     Intent  : {entry.get('intent')}")
        print(f"     Source  : {entry.get('source_file')}")
        print(f"     Status  : {entry.get('status')}  |  Tests: {entry.get('tests_passed')}/{entry.get('tests_total')}")
        print()

def parse_call_arg(raw: str):
    try:
        return json.loads(raw)
    except Exception:
        return raw

def load_entry_function(entry):
    source = entry.get("source_file") or ""
    function_name = entry.get("function_name") or ""
    if not source or not os.path.isfile(source):
        raise FileNotFoundError(f"Source file not found: {source}")
    spec = importlib.util.spec_from_file_location("stone_call_mod", source)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Could not load {source}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    fn = getattr(module, function_name, None)
    if not callable(fn):
        raise RuntimeError(f"{function_name} is not callable in {source}")
    return fn

def time_cases(filepath: str, function_name: str):
    """Time the same local cases the tester already accepted. Not part of the hash."""
    if not filepath.endswith(".py"):
        return None
    case_path = filepath[:-3] + ".cases.json"
    if not os.path.isfile(case_path):
        return None
    fn = load_entry_function({"source_file": filepath, "function_name": function_name})
    with open(case_path, "r", encoding="utf-8") as f:
        cases = json.load(f)
    calls = [(case.get("args") or []) for case in cases]
    for args in calls:
        fn(*args)
    loops = 300
    start = time.perf_counter()
    for _ in range(loops):
        for args in calls:
            fn(*args)
    elapsed = time.perf_counter() - start
    return round((elapsed / (loops * max(len(calls), 1))) * 1_000_000, 3)

def call_hash(name: str, raw_args: list, quiet: bool = False, backend: str = ""):
    backends = find_backends(name)
    if backend:
        needle = backend.lower()
        backends = [
            item for item in backends
            if needle in str(item.get("function_name", "")).lower()
            or needle in str(item.get("hierarchical_name", "")).lower()
            or needle in str(item.get("source_file", "")).lower()
        ]
    entry = next((item for item in backends if item.get("status") == "verified_basic"), None)
    if not entry:
        print(f"No verified local hash for: {name}")
        if backend:
            print(f"Backend filter: {backend}")
        print("Hash the function first. This caller does not download code.")
        sys.exit(1)
    fn = load_entry_function(entry)
    args = [parse_call_arg(item) for item in raw_args]
    result = fn(*args)
    if not quiet:
        print(f"Job:    {entry.get('job', entry.get('hierarchical_name'))}")
        print(f"Name:   {entry.get('hierarchical_name')}")
        print(f"Source: {entry.get('source_file')}")
        print(f"Result: {result}")
    return result

def resolve_step_arg(item, previous):
    if item == "$prev":
        if previous is None:
            raise RuntimeError("$prev used before any result")
        return previous
    return item

def run_steps(path: str):
    with open(path, "r", encoding="utf-8") as f:
        spec = json.load(f)
    steps = spec.get("steps") or []
    if not steps:
        print(f"No steps in {path}")
        sys.exit(1)
    previous = None
    print(spec.get("name") or path)
    for index, step in enumerate(steps, start=1):
        name = step.get("name")
        raw_args = [resolve_step_arg(item, previous) for item in step.get("args") or []]
        previous = call_hash(name, raw_args, quiet=True)
        print(f"{index}. {name} {raw_args} -> {previous}")
    print(f"Final: {previous}")

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
        depends_on = extract_depends(sys.argv)
        job = extract_job(sys.argv)
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
            timing_us = time_cases(filepath, function_name)
            saved_path, short_id, already_existed, hierarchical_name = save_hash(
                content_hash, filepath, normalized, test_results, function_name, category, intent, depends_on, job, timing_us
            )

            if already_existed:
                print("This function already exists in the library (same content hash)")
            else:
                print("New function added to the library")

            print(f"Function:     {function_name}")
            print(f"Category:     {category}")
            print(f"Name:         {hierarchical_name}")
            print(f"Status:       {decide_status(category, test_results, intent)}")
            if job:
                print(f"Job:          {job}")
            if timing_us is not None:
                print(f"Time:         {timing_us} us")
            if intent:
                print(f"Intent:       {intent}")
            if depends_on:
                print(f"Depends on:   {', '.join(depends_on)}")
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

    elif cmd == "call" and len(sys.argv) > 2:
        try:
            backend_values = extract_flag_args(sys.argv, "--backend")
            backend = backend_values[0] if backend_values else ""
            raw_args = [item for item in sys.argv[3:] if item != "--backend" and item != backend]
            call_hash(sys.argv[2], raw_args, backend=backend)
        except Exception as e:
            print(f"Call failed: {e}")
            sys.exit(1)

    elif cmd == "backends" and len(sys.argv) > 2:
        matches = find_backends(sys.argv[2])
        print(f"Backends for {sys.argv[2]}")
        print_entries(matches)

    elif cmd == "run" and len(sys.argv) > 2:
        try:
            run_steps(sys.argv[2])
        except Exception as e:
            print(f"Run failed: {e}")
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
            for dep in entry.get("depends_on") or []:
                dep_entry = find_by_name(dep)
                if dep_entry:
                    print(f"      depends OK   {dep}")
                else:
                    print(f"      depends MISS {dep}")
                    missing += 1
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
