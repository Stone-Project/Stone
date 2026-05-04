def run_basic_tests(code: str, function_name: str = "unknown"):
    """Run basic correctness and sanity tests on the function."""
    print(f"🧪 Running basic tests for {function_name}...")

    results = {
        "passed": 0,
        "total": 0,
        "details": []
    }

    # Very basic tests for now (we'll expand this heavily)
    try:
        # Test 1: Code is not empty
        results["total"] += 1
        if len(code.strip()) > 10:
            results["passed"] += 1
            results["details"].append("✅ Code length check passed")
        else:
            results["details"].append("❌ Code too short")

        # Test 2: Basic syntax check (for Python)
        results["total"] += 1
        if "def " in code or "function" in code.lower():
            results["passed"] += 1
            results["details"].append("✅ Contains function definition")
        else:
            results["details"].append("⚠️ No obvious function definition found")

        print(f"🧪 Tests passed: {results['passed']}/{results['total']}")
        return results

    except Exception as e:
        print(f"❌ Tester error: {e}")
        return {"passed": 0, "total": 1, "details": [f"Error: {e}"]}


def is_safe_for_hashing(test_results):
    """Decide if this function is good enough to hash."""
    return test_results["passed"] >= test_results["total"] * 0.8
