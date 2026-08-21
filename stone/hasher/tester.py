def run_basic_tests(code: str, function_name: str = "unknown"):
    """Run basic correctness and sanity tests on the function."""
    print(f"🧪 Running basic tests for {function_name}...")

    results = {
        "passed": 0,
        "total": 0,
        "details": []
    }

    try:
        # Test 1: Code is not empty / too short
        results["total"] += 1
        if len(code.strip()) > 20:
            results["passed"] += 1
            results["details"].append("✅ Code length check passed")
        else:
            results["details"].append("❌ Code too short")

        # Test 2: Looks like it contains a function definition
        results["total"] += 1
        lower = code.lower()
        if "def " in code or "function " in lower or "fn " in lower:
            results["passed"] += 1
            results["details"].append("✅ Contains function definition")
        else:
            results["details"].append("⚠️ No obvious function definition found")

        # Test 3: Not just comments or whitespace
        results["total"] += 1
        code_without_comments = "\n".join(
            line for line in code.splitlines()
            if not line.strip().startswith("#") and line.strip()
        )
        if len(code_without_comments.strip()) > 15:
            results["passed"] += 1
            results["details"].append("✅ Contains real code (not only comments)")
        else:
            results["details"].append("❌ Appears to be mostly comments or empty")

        print(f"🧪 Tests passed: {results['passed']}/{results['total']}")
        return results

    except Exception as e:
        print(f"❌ Tester error: {e}")
        return {"passed": 0, "total": 1, "details": [f"Error: {e}"]}

def is_safe_for_hashing(test_results):
    """Decide if this function is good enough to hash."""
    if test_results["total"] == 0:
        return False
    return test_results["passed"] >= test_results["total"] * 0.7