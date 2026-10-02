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

bench re-times verified Python backends and a recorded C backend. Timing is local and is not part of the hash. C bench time excludes compile.

record-external can note a non-Python pass. A C entry can be called if gcc is on PATH.

A C call prints Expect from the sibling cases file and exits if the result does not match.

Publish stays off. library/ stays off GitHub.

C

examples/clamp.c and examples/clamp_c_test.c are on main.

The desktop driver passed the same three clamp cases. gcc is available there through MSYS2.

--language c compiles clamp.c locally and calls clamp_c. It does not install a compiler.

A C call of 5 0 1 returned 1 and expected 1.

On the first bench, Python won. clamp_minmax was about 0.179 us, clamp about 0.259 us, and clamp_c about 1.616 us. The DLL call cost more than the C function saved.

build/ and the DLL stay local. A verified_external note may exist locally and is not pushed.

Rules

Do not scrape the web for code.

Do not paste proprietary engines.

Do not execute untrusted uploads.

Do not auto-publish a failed or unreviewed hash.

Do not rewrite cli.py when adding a function. The CLI changes only when a command changes.

Do not treat a famous trick, or C, as faster until bench says so.

One Newton step of the Quake bit trick fails the inverse-sqrt cases. Three steps pass, and it is slower in Python.

Do not hash a .c file with the Python hasher.

Not built

A caller that does not need the original source file.

A general C bench. This one uses the sibling cases file.

A license check.

A review step before publish.

A real game runtime, Doom port, or engine pack.

Automatic backend choice across machines. A time on one PC is not a universal ranking.

Order

Keep the catalog honest: cases, verified status, shared job names.

Language stays a label. Python is still the fast caller for clamp.

A faster C path has to win a bench before it becomes the default.

Then packs for real use, still without copying an engine.

Actor-Director integration stays later and separately licensed.

Done

Health category, run, inverse-sqrt backends, bench, clamp backends, category fix.

Language field and language filter.

C clamp source, case driver, local compile caller, expect check, and a bench where Python won.
