Stone

Write once. Hash the job. Keep the fastest clean backend later.

Stone is a content-addressed function catalog. A hash names one job. Packs group jobs and their order. A runtime that calls those hashes is not built yet.

What works now

python -m stone.cli hash-function examples/heal.py --intent "add health up to a maximum"
python -m stone.cli list
python -m stone.cli intent "health"
python -m stone.cli packs
python -m stone.cli verify health_basic.json
python -m stone.cli publish

publish refuses. Failed tests are not hashed. Local library/ stays off GitHub.

Add a function

1. Put one function in examples/your_job.py.
2. Add examples/your_job.cases.json with inputs and expected results.
3. Hash it:

python -m stone.cli hash-function examples/your_job.py --intent "what this job does" --depends stone:math.lerp

4. If it belongs with other jobs, add the hierarchical name to a file in packs/.
5. Run python -m stone.cli verify your_pack.json.

Do not paste proprietary engine code. Do not execute untrusted uploads. Unknown jobs stay untested until a category fits.

Status

Catalog starter. Hashes, names, intents, packs, dependency checks, and result cases exist. Multiple language backends, a caller, and web scraping do not.

Stone core is MIT. Actor-Director is a separate project.
