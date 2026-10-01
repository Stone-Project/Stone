import importlib.util
import json
import os
import traceback


def run_basic_tests(code: str, function_name: str = "unknown", filepath: str = ""):
    """Run basic correctness and sanity tests on the function."""
    print(f"Running basic tests for {function_name}...")

    results = {
        "passed": 0,
        "total": 0,
        "details": [],
        "executed": False
    }

    try:
        results["total"] += 1
        if len(code.strip()) > 20:
            results["passed"] += 1
            results["details"].append("Code length check passed")
        else:
            results["details"].append("Code too short")

        results["total"] += 1
        lower = code.lower()
        if "def " in code or "function " in lower or "fn " in lower:
            results["passed"] += 1
            results["details"].append("Contains function definition")
        else:
            results["details"].append("No obvious function definition found")

        results["total"] += 1
        code_without_comments = "\n".join(
            line for line in code.splitlines()
            if not line.strip().startswith("#") and line.strip()
        )
        if len(code_without_comments.strip()) > 15:
            results["passed"] += 1
            results["details"].append("Contains real code (not only comments)")
        else:
            results["details"].append("Appears to be mostly comments or empty")

        results["total"] += 1
        fn = load_python_function(function_name, filepath)
        if fn is not None:
            results["passed"] += 1
            results["executed"] = True
            results["details"].append("Python function imported successfully")
        else:
            results["details"].append("Could not execute/import function yet")

        case_path = cases_path_for(filepath)
        if case_path and os.path.exists(case_path):
            run_result_cases(fn, case_path, results)

        print(f"Tests passed: {results['passed']}/{results['total']}")
        return results

    except Exception as e:
        print(f"Tester error: {e}")
        return {"passed": 0, "total": 1, "details": [f"Error: {e}"], "executed": False}


def cases_path_for(filepath: str) -> str:
    if not filepath or not filepath.endswith(".py"):
        return ""
    return filepath[:-3] + ".cases.json"


def load_python_function(function_name: str, filepath: str = ""):
    """Load a local trusted function. Do not use this on untrusted uploads."""
    candidate = filepath if filepath and filepath.endswith(".py") else os.path.join("examples", "test_func.py")
    if not os.path.exists(candidate):
        return None
    try:
        spec = importlib.util.spec_from_file_location("stone_test_mod", candidate)
        if spec is None or spec.loader is None:
            return None
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        fn = getattr(module, function_name, None)
        return fn if callable(fn) else None
    except Exception:
        traceback.print_exc()
        return None


def values_match(actual, expected) -> bool:
    if isinstance(expected, float) or isinstance(actual, float):
        try:
            return abs(float(actual) - float(expected)) < 1e-6
        except (TypeError, ValueError):
            return False
    return actual == expected


def run_result_cases(fn, case_path: str, results: dict):
    try:
        with open(case_path, "r", encoding="utf-8") as f:
            cases = json.load(f)
    except Exception as e:
        results["total"] += 1
        results["details"].append(f"Could not read cases: {e}")
        return

    if not isinstance(cases, list) or not cases:
        results["total"] += 1
        results["details"].append("Cases file was empty")
        return

    if fn is None:
        results["total"] += 1
        results["details"].append("Cases exist but function was not loaded")
        return

    for index, case in enumerate(cases, start=1):
        results["total"] += 1
        args = case.get("args", [])
        expected = case.get("expect")
        try:
            actual = fn(*args)
            if values_match(actual, expected):
                results["passed"] += 1
                results["details"].append(f"Case {index} passed")
            else:
                results["details"].append(f"Case {index} failed: got {actual}, expected {expected}")
        except Exception as e:
            results["details"].append(f"Case {index} raised: {e}")


def try_import_python_function(function_name: str, filepath: str = "") -> bool:
    return load_python_function(function_name, filepath) is not None


def is_safe_for_hashing(test_results):
    """Decide if this function is good enough to hash."""
    if test_results["total"] == 0:
        return False
    return test_results["passed"] >= test_results["total"] * 0.7
