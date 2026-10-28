---
type: entity
branch: entities
tags: [loop-engineering, product, contracts, goal-spec, reconciler]
sources: ["[[src-openprose]]"]
created: 2026-10-19
updated: 2026-10-19
status: stub
---
# OpenProse

OpenProse (`prose.md`, GitHub `openprose/prose`) is a Y Combinator-backed, MIT-licensed project from OpenProse, Inc. Its repo description is *"A new kind of language for a new kind of computer."* It is a library and format of **Markdown contracts** that state requirements rather than steps, which an existing coding agent then carries out ([[src-openprose]]). Up: [[entities]].

## What it is
All of the following is from [[src-openprose]]:
- **Contracts:** Markdown files at stable, versioned addresses (`pkg.prose.md/releases/<release>/...`). A `Uses` section adopts reusable conventions, for example `std/result.md` and `std/source-grounding.md`.
- **Kernel:** an *"operating agreement"* that tells the executing agent how to resolve references, keep inputs separate from requirements, and report results.
- **Skill:** `npx skills add openprose/prose` installs it into Claude Code, Codex CLI or OpenCode. `prose run <file>` runs a contract there: *"the session itself embodies the VM"*.
- **Kinds:** `responsibility` (a standing goal), `function` (a one-time call), `gateway` (external ingress), `pattern`, and `test`. **ProseScript** is used where step order matters.
- **Responsibility Runtime:** `prose compile` builds a subscription DAG (the "Forme" wiring), plus canonicalizers and postcondition validators. `prose serve` runs a deterministic **reconciler** over local cron and HTTP triggers. The reference harness, Reactor, is alpha.

## Where it fits in a loop *(synthesis)*
- **[[goal-spec]]:** contracts are a composable, versioned definition-of-done format. A responsibility's `### Maintains` postconditions are the goal.
- **[[verification]]:** the executor/evaluator split, *"a result is a claim supported by evidence"*, and a citation-checking convention.
- **[[trigger]]:** three wake sources (input, self-cadence, external).
- **[[idempotency]] and [[budgets-and-cost]]:** a fingerprint memo skips unchanged work, there is one render in flight per node, and a failed render commits nothing.
- **A whole outer loop:** the Responsibility Runtime is the clearest example in the wiki of a [[reconciler-loop]].

## History
- `v0.12.0`: Responsibility Runtime release.
- `v0.15.0` (`runtime_contract` 1 → 2): the *"judge → verdict → pressure → fulfillment loop is retired wholesale"* and replaced by the fingerprint reconciler. Old ledgers are *"abandoned, not migrated."*
- `v0.18.1`: settled the executor/evaluator terminology.

The landing page, dated around October 2026, still pins package release `0.3.0-rc.3` ([[src-openprose]]).

## Contradictions & open questions
- **Unproven.** It is experimental, and benchmarks are *"openly pending"*. The project's own visual guide says the evidence is *"bounded mathematical, synthetic, and mocked"* ([[src-openprose]]).
- **Judge or reconciler?** OpenProse removed an LLM judge from its wake/commit decision. `/goal` puts one there ([[src-osmani-loop-engineering]]). Is this a real disagreement, or just a different place for the judgement? See [[decision-step]] and [[open-questions]].
- **Portability.** OpenProse is the first source in the wiki that claims portable loop *definitions* across hosts. See [[loop-primitives]] and [[open-questions]].

## Related
[[reconciler-loop]] · [[claude-code]] · [[openai-codex]] · [[evaluator-optimizer]]
