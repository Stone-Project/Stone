import os
import subprocess
import sys

def call_c(source_file: str, function_name: str, args: list):
    """Compile a local C file and call one function. Does not download a compiler."""
    if not source_file or not os.path.isfile(source_file):
        raise FileNotFoundError(f"C source not found: {source_file}")
    gcc = find_gcc()
    if not gcc:
        raise RuntimeError("C backend requested, no gcc or clang on PATH")
    build_dir = os.path.join(os.getcwd(), "build")
    os.makedirs(build_dir, exist_ok=True)
    dll_path = os.path.join(build_dir, "stone_c.dll")
    command = [gcc, "-shared", "-o", dll_path, source_file, "-Wl,--export-all-symbols"]
    built = subprocess.run(command, capture_output=True, text=True)
    if built.returncode != 0:
        raise RuntimeError(built.stderr.strip() or "C compile failed")
    import ctypes
    lib = ctypes.CDLL(dll_path)
    fn = getattr(lib, function_name)
    fn.restype = ctypes.c_int
    fn.argtypes = [ctypes.c_int] * len(args)
    int_args = [int(item) for item in args]
    return int(fn(*int_args))

def find_gcc():
    for name in ("gcc", "clang"):
        try:
            found = subprocess.run([name, "--version"], capture_output=True, text=True)
        except FileNotFoundError:
            continue
        if found.returncode == 0:
            return name
    return ""
