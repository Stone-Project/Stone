# Stone

**Write once. Hash once. Run optimally everywhere.**

Stone is a high-level portable code layer that automatically converts functions into stable, semantically-hashed implementations. It picks the fastest, most reliable backend from any language based on real benchmarks and verified tests.

### Core Philosophy
- One hash = battle-tested, bug-resistant function
- Natural language → correct hash (`stone intent "fast inverse square root like Quake"`)
- Extreme optimization for long, complex functions while respecting native strengths for short ones
- Hierarchical naming + content hashing (near-zero collision risk)

### Quick Start
```bash
# After installation
stone intent "safe fast inverse square root for low-power hardware"
stone hash-function my_hot_function.py

Project Status (April 2026)

Auto-hasher MVP in progress
Basic library structure defined
Focused on correctness, performance, and portability

Vision
A global library where developers and LLMs contribute optimized functions. Long complex logic shrinks to a single reliable hash. Future applications include high-performance games, simulations, embedded systems, and cross-platform engines.
Stone is fully open source (MIT).
