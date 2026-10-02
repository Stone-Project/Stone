# Changelog

## Unreleased

- Hash a function, store it locally, and refuse to call it unless status is verified_basic.
- Result cases live beside the function as `.cases.json`.
- Packs, verify, and a run command that chains verified calls with `$prev`.
- A job can have more than one backend. `call` uses a verified one. `--backend` forces one.
- `bench` re-times verified backends and prints the winner. Timing is local and is not part of the hash.
- Jobs with two backends: `stone:math.inverse_sqrt`, `stone:util.clamp`.
- Publish stays disabled. Local `library/` is not part of the repo.

## v0.1.0 (2026-04-25)

- Initial hasher implementation.
- Basic library storage and CLI.
