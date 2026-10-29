# Stone goals

This file is the reference. Chat context is not.

## What Stone is

A catalog of jobs. A hash names one job. A job may have more than one backend. A backend is allowed only if it passes the same cases. The caller uses a verified local backend and may prefer the faster one. Packs group jobs. A run file chains calls. Parameters stay outside the hash.

Language is a label on a backend, not a separate folder. `call` may filter with `--language`. A missing language refuses. It does not fall through to another language.

Actor-Director is a separate project. It may choose Stone jobs later. It is not part of this repo.

## What works

- Hash, list, show, delete, intent search.
- Result cases in a sibling `.cases.json`.
- Category, hierarchical name, intent, `depends_on`, and a shared job name.
- `--category` overrides the guess when hashing. The content hash does not change.
- `verify-examples` checks a sequence of local files, names the language, and sorts the report. It does not hash or publish.
- `report` says MATCH, SIMILAR, or NEW for a local file. It does not hash or publish.
- Packs and verify. Missing jobs are reported, not downloaded.
- `call` and `run`. `$prev` passes the last result. A run `expect` fails the chain if the final value does not match.
- `--backend` forces one verified backend. `--language` filters by language.
- `bench` re-times verified Python backends and a recorded C backend. Timing is local and is not part of the hash. C bench time excludes compile.
- `record-external` can note a non-Python pass. For C it says the entry can be called if `gcc` is on PATH.
- A C call prints Expect from the sibling cases file and exits if the result does not match.
- `ADDING_A_LANGUAGE.md` documents how to add a loader. The verifier does not invent one.
- Publish stays off. `library/` stays off GitHub.

## Proven chains

- Python then C clamp returns `1` against `1`. A chain that expects `2` exits `1`.
- Damage, clamp, and heal return `65` against `65`.
- Gravity then clamp returns `8`. Overlap returns `True`. Lerp then clamp returns `4`. Saturate then heal returns `15`. Map range then clamp returns `40`.
- Sign then heal returns `16`. Absolute value then heal returns `15`. Square then heal returns `15`.
- Approach then heal returns `15`. Min then heal returns `15`. Max then heal returns `15`. Wrap then heal returns `15`. Deadzone then heal returns `15`. Drag then heal returns `15`.
- Abs, square, and min return `10` against `10` with no heal step.
- A mixed chain of damage, C clamp, and heal returns `65`. The same chain with expect `64` exits `1`.
- `pack:health.turn` verifies with `Missing: 0`. `pack:missing.one` exits `1` and does not download.

### Order timing

- time-runs compares two run files. Passes are the longer chain, with a floor of 5.
- A winner must stay ahead on every pass. If the passes split, it is a tie.
- The times stay local. They are not part of the hash and not a ranking for every machine.

## C

- `examples/clamp.c` and `examples/clamp_c_test.c` are on `main`.
- C backends for min, sign, max, abs, and square are on `main`. Each passed the same integer cases as the Python job.
- The desktop driver passed the same three clamp cases. `gcc` is available there through MSYS2.
- `--language c` compiles a sibling `.c` file locally and calls the recorded symbol. It does not install a compiler.
- A C call of clamp `5 0 1` returned `1` and expected `1`.
- On the first bench, Python won. `clamp_minmax` was about `0.179 us`, `clamp` about `0.259 us`, and `clamp_c` about `1.616 us`. The DLL call cost more than the C function saved.
- `build/` and the DLL stay local. A `verified_external` note may exist locally and is not pushed.

## Rules

- Do not scrape the web for code.
- Do not paste proprietary engines.
- Do not execute untrusted uploads.
- Do not auto-publish a failed or unreviewed hash.
- Do not rewrite `cli.py` when adding a function. The CLI changes only when a command changes.
- Do not treat a famous trick, or C, as faster until `bench` says so.
- One Newton step of the Quake bit trick fails the inverse-sqrt cases. Three steps pass, and it is slower in Python.
- Do not hash a `.c` file with the Python hasher.
- Do not rehash the catalog when an auto hasher arrives. Same normalized body keeps the same hash. A rule change is a new version, beside the old one, not over it. Similarity may report. It must not merge.

### Folder hashing

- hash-dir hashes every .py in a folder that has a sibling .cases.json.
- A file that already MATCHES is skipped so its category and times are kept.
- A new file is hashed with the guessed category.
- set-category changes the category on a local entry.
- It does not change the content hash.
- hash-dir takes an optional category.
- That category applies to new files only. A match is still skipped.
- A .c file is handed to the C path if it has two comments:
  - `// stone:job stone:util.clamp`
  - `// stone:function clamp_c`
- It needs a sibling .cases.json named `<file>.c.cases.json`.
- It is compiled once, tested, and recorded only if every case passes.
- If gcc is missing, it is refused.
- The C hash is now built from language, job, and function only.
- A matching C file is skipped.
- The six existing C entries were re-recorded under the new hash.
- The old entries are backed up in `%TEMP%\stone_library_backup_rerecord`.
- A .rs file is handed to the Rust path if it has two comments:
  - `// stone:job stone:util.clamp`
  - `// stone:function clamp_rs`
- It needs a sibling .cases.json named `<file>.rs.cases.json`.
- It is currently refused with "Rust loader not implemented yet."
- The C and Python paths are unchanged.
- A .go file is handed to the Go path if it has two comments:
  - `// stone:job stone:util.clamp`
  - `// stone:function clamp_go`
- It needs a sibling .cases.json named `<file>.go.cases.json`.
- It is currently refused with "Go loader not implemented yet."
- A .zig file is handed to the Zig path if it has two comments:
  - `// stone:job stone:util.clamp`
  - `// stone:function clamp_zig`
- It needs a sibling .cases.json named `<file>.zig.cases.json`.
- It is currently refused with "Zig loader not implemented yet."
- The C, Python, and Rust paths are unchanged.

## Decisions (2026-10-29)

### Auto-hasher
- The auto-hasher is next. It takes the friction out of the hash step.
- Cases and verify stay manual.
- It is additive only.
- The same normalized body keeps the same content hash.
- Existing entries are not rehashed.
- Similar hashes are not merged automatically.
- It does not scrape.
- A new hash version comes only if the normalization rules change.

### Pure jobs only
- Stone is for pure jobs.
- File reads, database writes, API calls, time, and randomness are out of scope for the current verification model.
- Impure jobs can be added later under a different protocol.

### Docs after the auto-hasher
- A one-sentence pitch at the top of the README.
- The pure-function limit.
- A short first-job walkthrough.
- An honest bench note. Small functions can lose to FFI overhead. Larger jobs or batch calls can reverse it.
- The human walkthrough and the AI walkthrough come after the auto-hasher is working.

### Catalog
- 118 Python jobs are local, with cases, chains, and packs.
- C has a few verified backends.
- Other languages are refused until loaders exist.
- The practical target before public contributions is a few hundred solid jobs overall, not per language.
- Each language should have at least some verified backends before a public release or a Doom demo on weak hardware.
## Not built

- An auto hasher. Hash by hand until then.
- A caller that does not need the original source file.
- A general C bench. This one uses the sibling cases file.
- A license check.
- A review step before publish.
- A real game runtime, Doom port, or engine pack.
- Automatic backend choice across machines. A time on one PC is not a universal ranking.
- On-rails parameter prompts, and an open mode that proposes a new body. Later. A changed body is a new backend and must pass the same cases.

## Order

1. Keep the catalog honest: cases, verified status, shared job names.
2. Language stays a label. Python is still the fast caller for clamp.
3. A faster C path has to win a bench before it becomes the default.
4. Packs for real use, still without copying an engine.
5. An auto hasher comes after that, and it adds to the existing hashes.
6. Order timing is built as `time-runs`.
7. Actor-Director integration stays later and separately licensed.

## Done

- Health category, `run`, inverse-sqrt backends, `bench`, clamp backends, category fix.
- Language field, language filter, C clamp caller, expect check, and a bench where Python won.
- Pass and fail chains, pass and fail packs, and hand-hashed jobs for damage, heal, clamp, gravity, overlap, lerp, saturate, map range, sign, absolute value, square, approach, min, max, wrap, deadzone, and drag.
- `report` for match, similar, or new. C backends for min, sign, max, abs, and square. The record-external message for C is accurate.
- Order timing of whole chains is built as `time-runs`.
