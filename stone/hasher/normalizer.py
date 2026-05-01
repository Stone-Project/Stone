def normalize(code: str):
    """Basic normalizer stub."""
    if not code:
        return ""
    
    # Very simple normalization for now
    normalized = code.strip()
    normalized = " ".join(normalized.split())  # collapse whitespace
    print("🔧 Basic normalization complete")
    return normalized
