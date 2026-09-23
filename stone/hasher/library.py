# Stone library module - versioned hashing + storage
import json
import os
from datetime import datetime, timezone

LIBRARY_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "library")
HASH_VERSION = "v1"

def ensure_library_dir():
    os.makedirs(LIBRARY_DIR, exist_ok=True)
    return LIBRARY_DIR

def make_hierarchical_name(category: str, function_name: str) -> str:
    cat = (category or "unknown").strip().lower().replace(" ", "_")
    name = (function_name or "unknown").strip().lower().replace(" ", "_")
    return f"stone:{cat}.{name}"

def get_hash_path(content_hash: str) -> str:
    short_id = content_hash[:16]
    return os.path.join(LIBRARY_DIR, f"{short_id}.json")

def load_hash(content_hash: str):
    filepath = get_hash_path(content_hash)
    if not os.path.exists(filepath):
        return None
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return None

def save_hash(
    content_hash: str,
    source_file: str,
    normalized_code: str,
    test_results: dict,
    function_name: str = "unknown",
    category: str = "unknown",
    intent: str = "",
):
    ensure_library_dir()

    short_id = content_hash[:16]
    full_short_id = f"stone-{HASH_VERSION}:{short_id}"
    hierarchical_name = make_hierarchical_name(category, function_name)
    filepath = get_hash_path(content_hash)

    already_existed = os.path.exists(filepath)
    existing = load_hash(content_hash) if already_existed else None

    if not intent and existing:
        intent = existing.get("intent", "")

    entry = {
        "version": HASH_VERSION,
        "content_hash": content_hash,
        "short_id": full_short_id,
        "hierarchical_name": hierarchical_name,
        "function_name": function_name,
        "category": category,
        "intent": intent,
        "source_file": source_file,
        "normalized_length": len(normalized_code),
        "tests_passed": test_results.get("passed", 0),
        "tests_total": test_results.get("total", 0),
        "created_at": existing.get("created_at") if existing else datetime.now(timezone.utc).isoformat(),
        "updated_at": datetime.now(timezone.utc).isoformat(),
        "status": decide_status(category, test_results, intent),
        "seen_sources": list(set((existing.get("seen_sources") or []) + [source_file])) if existing else [source_file]
    }

    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(entry, f, indent=2)

    return filepath, full_short_id, already_existed, hierarchical_name

def decide_status(category: str, test_results: dict, intent: str = "") -> str:
    """verified_basic only when category is known and tests pass. Otherwise untested."""
    category = (category or "unknown").lower()
    passed = test_results.get("passed", 0)
    total = test_results.get("total", 0)
    strong_tests = total > 0 and passed >= total * 0.7
    if category not in ("", "unknown") and strong_tests:
        return "verified_basic"
    return "untested"

def list_hashes():
    ensure_library_dir()
    entries = []

    for filename in os.listdir(LIBRARY_DIR):
        if filename.endswith(".json"):
            filepath = os.path.join(LIBRARY_DIR, filename)
            try:
                with open(filepath, "r", encoding="utf-8") as f:
                    entries.append(json.load(f))
            except Exception:
                continue

    entries.sort(key=lambda x: x.get("updated_at", x.get("created_at", "")), reverse=True)
    return entries

def get_by_short_id(short_id: str):
    clean_id = short_id.replace("stone-v1:", "").replace("stone:", "").strip()
    filepath = os.path.join(LIBRARY_DIR, f"{clean_id}.json")
    if not os.path.exists(filepath):
        return None
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return None

def delete_hash(short_id: str) -> bool:
    clean_id = short_id.replace("stone-v1:", "").replace("stone:", "").strip()
    filepath = os.path.join(LIBRARY_DIR, f"{clean_id}.json")
    if not os.path.exists(filepath):
        return False
    try:
        os.remove(filepath)
        return True
    except Exception:
        return False

def search_by_intent(query: str):
    """Simple keyword search across intent, name, function, and category."""
    q = (query or "").strip().lower()
    if not q:
        return []

    words = [w for w in q.replace(":", " ").replace(".", " ").split() if w]
    results = []

    for entry in list_hashes():
        haystack = " ".join([
            str(entry.get("intent", "")),
            str(entry.get("hierarchical_name", "")),
            str(entry.get("function_name", "")),
            str(entry.get("category", "")),
        ]).lower()
        score = sum(1 for w in words if w in haystack)
        if score > 0:
            item = dict(entry)
            item["_score"] = score
            results.append(item)

    results.sort(key=lambda e: (e.get("_score", 0), e.get("updated_at", "")), reverse=True)
    return results

def find_by_name(name: str):
    """Find a library entry by hierarchical name, short id, or function name."""
    needle = (name or "").strip().lower()
    if not needle:
        return None
    for entry in list_hashes():
        names = [
            str(entry.get("hierarchical_name", "")).lower(),
            str(entry.get("short_id", "")).lower(),
            str(entry.get("function_name", "")).lower(),
        ]
        if needle in names:
            return entry
    return None
