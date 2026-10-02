Stone goals

This file is the reference. Chat context is not.

What Stone is

A catalog of jobs. A hash names one job. A job may have more than one backend. A backend is allowed only if it passes the same cases. The caller uses a verified local backend and may prefer the faster one. Packs group jobs. A run file chains calls. Parameters stay outside the hash.

Language is a label on a backend, not a separate folder. call may filter with --language. A missing language refuses. It does not fall through to another language.

Actor-Director is a separate project. It may choose Stone jobs later. It is not part of this repo.

What works

Hash, list, show, delete, intent search.

Result cases in a sibling .cases.json.

Category, hierarchical name, intent, depends_on, and a shared job name.

Packs and verify. Missing jobs are reported, not downloaded.

call and run. $prev passes the last result.

--backend forces one verified backend. --language filters by language.

bench re-times verified Python backends. Timing is local and is not part of the hash.

record-external can note a non-Python pass. Status verified_external is not callable.

Publish stays off. library/ stays off GitHub.

C

examples/clamp.c and examples/clamp_c_test.c are on main.

The desktop driver passed the same three clamp cases. gcc is available there through MSYS2.

--language c refuses. The caller cannot run C yet.

A local verified_external entry may exist. It is not pushed. It is not a backend bench can pick.

Stone does not install compilers. A missing compiler is reported, not downloaded.

Rules

Do not scrape the web for code.

Do not paste proprietary engines.

Do not execute untrusted uploads.

Do not auto-publish a failed or unreviewed hash.

Do not rewrite cli.py when adding a function. The CLI changes only when a command changes.

Do not treat a famous trick as faster until bench says so.

One Newton step of the Quake bit trick fails the inverse-sqrt cases. Three steps pass, and it is slower in Python.

Do not hash a .c file with the Python hasher.

Not built

A caller that can run C, or any caller that does not need the original source file.

A license check.

A review step before publish.

A real game runtime, Doom port, or engine pack.

Automatic backend choice across machines. A time on one PC is not a universal ranking.

Order

Keep the catalog honest: cases, verified status, shared job names.

Language stays a label. Python remains the only callable language.

A C caller comes later, and only when asked. It must pass the same cases.

Then packs for real use, still without copying an engine.

Actor-Director integration stays later and separately licensed.

Done

Health category, run, inverse-sqrt backends, bench, clamp backends, category fix.

Language field and language filter.

C clamp source, case driver, and external record. Caller still cannot run C.
