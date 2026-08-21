# Contributing to Stone

Thank you for considering a contribution!

### Important Rules

1. **Provenance is mandatory**
   - Only contribute original code or code from public domain / permissively licensed sources (e.g. Quake/DOOM GPL code, standard algorithms).
   - **Never** contribute anything derived from proprietary engines (Unreal, Unity closed-source parts, commercial middleware, etc.).
   - You must confirm in your PR: "This is original or from allowed sources."

2. **Hashing Workflow**
   - Use `stone hash-function` to add new functions.
   - All submissions must pass the automatic test suite.

3. **Code of Conduct**
   - Be respectful, constructive, and professional.

### Development Setup
```bash
git clone https://github.com/stone-lang/stone.git
cd stone
pip install -e .
Then run:
Bashstone hash-function examples/test_func.py
We welcome:

New hashed functions
Improvements to the hasher
Better tests and benchmarks
Documentation

Thank you for helping build a better optimization layer.
