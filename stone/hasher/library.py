# Stone library module - versioned hashing + storage
import json
import os
from datetime import datetime, timezone

LIBRARY_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "library")
HASH_VERSION = "v1"

def ensure_library_dir():
    """Make sure the library folder exists."""
    os.makedirs(LIBRARY_DIR, exist_ok=True)
    return LIBRARY_DIR

def get_hash_path(content_hash: str) -> str:
    short_id = content_hash[:16]
    return os.path.join(LIBRARY_DIR, f"{short_id}.json")

def load_hash(content_hash: str):
    """Load an existing hash entry if it exists."""
    filepath = get_hash_path(content_hash)
    if not os.path.exists(filepath):
        return None
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return None

def save_hash(content_hash: str, source_file: str, normalized_code: str, test_results: dict):
    """
    Save a successful hash entry.
    Returns: (filepath, short_id, already_existed)
    """
    ensure_library_dir()

    short_id = content_hash[:16]
    full_short_id = f"stone-{HASH_VERSION}:{short_id}"
    filepath = get_hash_path(content_hash)

    already_existed = os.path.exists(filepath)
    existing = load_hash(content_hash) if already_existed else None

    entry = {
        "version": HASH_VERSION,
        "content_hash": content_hash,
        "short_id": full_short_id,
        "source_file": source_file,
        "normalized_length": len(normalized_code),
        "tests_passed": test_results.get("passed", 0),
        "tests_total": test_results.get("total", 0),
        "created_at": existing.get("created_at") if existing else datetime.now(timezone.utc).isoformat(),
        "updated_at": datetime.now(timezone.utc).isoformat(),
        "status": "verified_basic",
        "seen_sources": list(set((existing.get("seen_sources") or []) + [source_file])) if existing else [source_file]
    }

    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(entry, f, indent=2)

    return filepath, full_short_id, already_existed

def list_hashes():
    """Return a list of all saved hash entries."""
    ensure_library_dir()
    entries = []

    for filename in os.listdir(LIBRARY_DIR):
        if filename.endswith(".json"):
            filepath = os.path.join(LIBRARY_DIR, filename)
            try:
                with open(filepath, "r", encoding="utf-8") as f:
                    entry = json.load(f)
                    entries.append(entry)
            except Exception:
                continue

    entries.sort(key=lambda x: x.get("updated_at", x.get("created_at", "")), reverse=True)
    return entries

def get_by_short_id(short_id: str):
    """
    Look up an entry by short ID.
    Accepts either 'stone-v1:abc123...' or just 'abc123...'
    """
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
    """
    Delete a hash entry by short ID.
    Returns True if deleted, False if not found.
    """
    clean_id = short_id.replace("stone-v1:", "").replace("stone:", "").strip()
    filepath = os.path.join(LIBRARY_DIR, f"{clean_id}.json")

    if not os.path.exists(filepath):
        return False

    try:
        os.remove(filepath)
        return True
    except Exception:
        return False