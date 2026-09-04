# Stone Hash Engine

Design document. The current repo is an auto-hasher MVP, not a running game engine.

## Pitch

A game should ship keys, not private copies of every long function.
Stone opens a pre-tested implementation. Actor-Director decides what stays baked and what must go live.

## Layers

1. **Stone hashes** — packed, versioned, tested function implementations
2. **Baked world** — stable rules/results that do not need live simulation
3. **Director + Actors** — track only the objects that actually changed

The hash is a handshake to ready code. It is not "pre-run 699 lines and add a parenthesis."
Live inputs still have to be supplied. The function body should already be built.

## Current MVP

- Parse a file and extract a function name
- Normalize + basic tests, including a Python import check
- SHA-256 content hash with `stone-v1:` short IDs
- Local JSON library with list / show / delete
- Duplicate detection

## Not built yet

- Real AST extraction across a codebase
- Multiple backends per hash
- Benchmarks
- Runtime dispatcher
- Actor-Director integration
- Engine conversion (Doom-scale or otherwise)

## Build order

1. Keep hashing/storage reliable
2. Better parser and executable tests
3. Multiple implementations per hash
4. Simple backend selector
5. Hierarchical names
6. Tiny runtime that can call one hashed function
7. One real engine-style function demo
8. Director live-set tracking last

## Legal

Only hash code you wrote, permitted open code, or clean-room reimplementations.
Splitting a function out of a proprietary engine does not make it free to catalog.