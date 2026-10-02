# Stone goals

This file is the reference. Chat context is not.

## What Stone is

A catalog of jobs. A hash names one job. A job may have more than one backend. A backend is allowed only if it passes the same cases. The caller uses a verified local backend and may prefer the faster one. Packs group jobs. A run file chains calls. Parameters stay outside the hash.

Actor-Director is a separate project. It may choose Stone jobs later. It is not part of this repo.

## What works

- Hash, list, show, delete, intent search.
- Result cases in a sibling `.cases.json`.
- Category, hierarchical name, intent, `depends_on`, and a shared job name.
- Packs and verify. Missing jobs are reported, not downloaded.
- `call` and `run`. `$prev` passes the last result.
- `--backend` forces one verified backend.
- `bench` re-times verified backends. Timing is local and is not part of the hash.
- Publish stays off. `library/` stays off GitHub.

## Rules

- Do not scrape the web for code.
- Do not paste proprietary engines.
- Do not execute untrusted uploads.
- Do not auto-publish a failed or unreviewed hash.
- Do not rewrite `cli.py` when adding a function. The CLI changes only when a command changes.
- Do not treat a famous trick as faster until `bench` says so.
- One Newton step of the Quake bit trick fails the inverse-sqrt cases. Three steps pass, and it is slower in Python.

## Not built

- A caller that does not need the original source file.
- More than one language. Everything so far is Python.
- A license check.
- A review step before publish.
- A real game runtime, Doom port, or engine pack.
- Automatic backend choice across machines. A time on one PC is not a universal ranking.

## Order

- Keep the catalog honest: cases, verified status, shared job names.
- Mark the language of a backend, so a later C or Rust file can sit beside Python.
- Add a second language only for a job that already has cases.
- Then packs for real use, still without copying an engine.
- Actor-Director integration stays later and separately licensed.

## Done today

Health category, `run` command, inverse-sqrt backends, `bench`, clamp backends, category fix.
