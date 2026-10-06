Adding a language

Stone does not invent a loader when it sees an unknown file. A person or an AI adds a language with this sequence. Skip a step and the file stays unrecognized or held.

1. Name it

Add one row in stone/hasher/languages.py.

- language: short name, such as rust
- extensions: file suffixes, such as .rs
- tools: the compiler or runtime that must already be on PATH
- loader: false until a caller exists

verify-examples can then say "known language, no loader yet" instead of "unknown language."

2. Do not install the tool

Stone does not download a compiler. The how-to can name the install command. The user runs it. If the tool is missing, the verifier says the loader exists and the tool is missing.

3. Add a caller

A caller compiles or loads one local file and calls one symbol. Python's caller is the importer. C's caller is stone/hasher/c_caller.py. A new language gets its own file. It does not share the C compiler flags.

The caller must:

- refuse if the tool is not on PATH
- build only the file it was given
- not download source
- return the function result, not print over the result

4. Pass the same cases

Pick a job that already has cases, or add a small function and a sibling .cases.json. The new language must return the same values. A C clamp passed the Python clamp cases. A new language does not get a weaker set.

5. Record, then call

record-external can note a pass before the caller exists. Status verified_external is not callable. After the caller exists, call --language <name> may run it. bench may time it. It becomes the default only if it is faster on that machine.

6. Do not rehash the catalog

The new caller does not rewrite old hashes. Same normalized body keeps the same hash. A new language is another backend on the same job.

What not to do

- Do not scrape the web for an implementation.
- Do not run an unknown file to discover the language.
- Do not auto-merge a near match.
- Do not publish the library entry. library/ stays local.
