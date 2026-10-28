---
type: source
branch: sources
tags: [loop-engineering, ouroboros, goal-spec, verification, evolution, hidden-grading]
sources: []
url: https://ouroboros.page/
author: Ouro Labs (GitHub Q00/ouroboros; top committers Q00, shaun0927)
published: unknown (repo 2026-01-14 to 2026-10-19; guide verified against v0.51.5 on 2026-08-14; latest release v0.59.0)
raw: raw/2026-10-19-ouroboros.md
created: 2026-10-19
updated: 2026-10-19
status: draft
---
# Ouroboros (ouroboros.page): guide, README, evaluation and evolution docs

**Author:** Ouro Labs (MIT, ~6.2k GitHub stars; the repo is tagged `loop-engineering`) · **Raw:** `raw/2026-10-19-ouroboros.md` (23 sections: landing page, the 12-chapter English guide, README, the evolution-loop, evaluation-pipeline, execution-vs-evaluation, safe-but-wrong and hidden-checklist docs, verifier-evidence policy excerpts, the roadmap, GitHub API fetch notes) · Up: [[sources]]

## Summary
[[ouroboros]] is a **management layer** that runs on top of a coding agent: *"Your coding agent writes the code. Ouroboros verifies the result."* It supports 14 runtimes, including Claude Code, Codex CLI, OpenCode, Kiro and [[omp]], and talks to them over MCP. Its loop is:

**Interview → Seed → Execute → Evaluate → Evolve**

- A Socratic interview drives an **ambiguity score** to ≤ 0.2.
- The answers become an immutable YAML **Seed** (the spec).
- The runtime executes it.
- A **3-stage evaluation** (mechanical → semantic → consensus) judges the result.
- **Evolve** feeds the findings back into the *next* Seed. `ooo ralph` repeats this until the spec's data model converges (similarity ≥ 0.95) or another stop condition fires.

*"This is where the Ouroboros eats its tail: the output of evaluation becomes the input for the next generation's seed specification."* Its claim: *"Most AI coding fails at the **input**, not the output."*

**Is it loop engineering?** Yes, and it says so (the repo carries the `loop-engineering` topic). *(synthesis)* It is a full outer loop focused on the [[goal-spec]] and [[verification]] slots, and it adds a loop shape the wiki didn't have: the [[evolutionary-loop]], in which evaluation rewrites the spec.

## Key claims
- **Two numeric gates.** *"Ambiguity <= 0.2 — Do not build until you are clear"* and *"Similarity >= 0.95 — Do not stop evolving until you are stable."* Ambiguity is 1 − the weighted clarity of goal (40%), constraints (30%) and success criteria (30%). *"A low score can still hide wrong content, so review the summary."* See [[goal-spec]].
- **The Seed is the contract.** Its fields are `goal`, `constraints`, `acceptance_criteria`, `ontology_schema`, `evaluation_principles` and `exit_conditions`. Non-goals and assumptions go to a separate **Ledger**. The Seed *"does not change within that run."* Seeds are graded A/B/C, and `ooo auto` executes only grade A. *"Because Core and the runtime are separate, the same Seed can be used with a different runtime."*
- **Only executed checks can grant acceptance.** *"Model judgment may clarify, construct checks, and withhold approval. It cannot grant acceptance; acceptance comes from executed verification."*
  - Stage 1 (lint/build/test/coverage, *"No LLM involved"*) is the only stage that can approve.
  - Stage 2 (an LLM scores against the ACs; ≥ 0.8 required) and Stage 3 (multi-model vote; ≥ 0.66 required) can only *withhold*.
  - If no Stage 1 check ran, the result is `unverified`, not approved.
  - This was fixed in #2449 (closed 2026-09-27), whose title says model verdicts had been granting acceptance without executed verification.

  See [[verification]] and [[backpressure]].
- **A reward-hacking veto.** Stage 2 returns a `reward_hacking_risk` score, defined as *"Suspicion that the artifact games the evaluator instead of solving the task"*. At ≥ 0.7 it vetoes approval. The evaluator must also list the `questions_used` and `evidence` behind its verdict.
- **Hidden grading.** Every harness-owned `verify_command` and `output_assertion` is hidden from worker prompts, context, events and retries, *"without a configuration escape hatch"*. Retry hints are built from *sanitized* verification output. *"No answer-key configuration knob. Hidden grading is a correctness boundary, not a tuning option."* The raw Seed stays with the parent process, and workers get only an opaque handle. The limit is stated honestly: *"Confidentiality is a transport boundary"*, and filesystem isolation is the operator's job. The README tagline: *"The grading command and expected result never make it into the success contract we hand it."* See [[guardrails-and-permissions]].
- **Execution is not evaluation.** *"Execution is not evaluation. Completion is not approval. Task failure is not semantic drift."* Worker task states (`completed`/`failed`) are kept apart from AC verdicts (`pass`/`fail`/`not_evaluated`). *"partial verifier coverage cannot approve a run."*
- **Fabrication vs mismatch.** The verifier separates two failures:
  - `FABRICATION_SUSPECTED`: no runtime transcript evidence exists for the claim.
  - `EVIDENCE_FORM_MISMATCH`: related work is visible, but its form can't prove the claim, so retry with a proof form that fits.

  The core verifier stays *"domain- and language-agnostic"* and doesn't grow per-test-runner parsers.
- **Safe-but-wrong output** is named as a failure mode: an artifact that is *"locally safe and verifiable, but changes a material user-stated requirement"*. Examples: handoff docs instead of the requested tool, or missing data reported as `OK`/`0`. *"That is worse than a clear blocker because it creates false confidence."* See [[failure-modes]].
- **The evolutionary loop.** Each generation runs Wonder (*"What do we still not know?"*), then Reflect (refines the ACs and mutates the ontology), then execute, then evaluate. From Gen 2 on it is *"fully autonomous — the Wonder and Reflect engines replace human input."* See [[evolutionary-loop]].
- **When it stops.** Evolution stops at the first of:
  - convergence: ontology similarity ≥ 0.95, where similarity = 0.5·name overlap + 0.3·type match + 0.2·exact match
  - stagnation: 3 stable generations in a row
  - oscillation: generation N ≈ generation N−2
  - the cap of 30 generations, with at least 2 generations before the first three checks apply

  `ooo ralph` also stops on a QA pass, cancellation, an unrecoverable failure, a regressing grade, or a time limit. When chained automatically after a failed evaluation, the default budget is 3 generations. See [[termination]].
- **A human stop list.** *"More automatic iterations do not guarantee quality."* Stop when the criteria are already met, the same failure repeats, changes are small relative to cost, or *"The product direction itself needs a human decision."* On repeated failure, `ooo unstuck` offers five lateral-thinking personas. See [[human-in-the-loop]].
- **Durable, replayable state.**
  - Every event goes to a local SQLite EventStore, and Ralph steps are *"stateless: the EventStore reconstructs the full lineage"*.
  - Lineage IDs are deterministic.
  - Concurrent completions enqueue *"at most one Ralph successor"*.
  - Chaining is *fail-open*: a failed enqueue never changes the verdict that came before it.

  See [[idempotency]] and [[context-and-state]].
- **Cost routing.** The "PAL Router" escalates Frugal (1×) → Standard (10×) → Frontier (30×) on failure and downgrades on success. Cheap evaluation stages run first, and consensus runs only when triggered: the Seed was modified, the goal was reinterpreted, drift > 0.3, or uncertainty > 0.3. See [[budgets-and-cost]].

## Notable quotes
- *"It gets smarter on its own. We just hold the line."*
- *"Execution is not evaluation. Completion is not approval."*
- *"Three votes labeled `default` are not three independent reviewers."*

## Contradictions with the wiki
- **The spec evolves on its own.** From Gen 2 on, Reflect rewrites the ACs and the ontology without a human. Tan's rule is that *"the finish condition never quietly relaxes"* ([[src-tan-pstack-guide-overnight]]), and omp's is *"NEVER redefine success"* ([[src-omp]]). Ouroboros's safeguard is that a modified Seed, a reinterpreted goal or high drift *triggers multi-model consensus*. Since #2449 (closed 2026-09-27), that consensus can only withhold approval, not grant it. See [[evolutionary-loop]].
- **Should the agent see the grader?** Ouroboros hides the grading commands and assertions from workers. Pocock wants the agent to run checks itself, because *"Ralph can't declare victory if the tests are red"* ([[src-pocock-ralph-tips]]). Tan's aim is to *"Make the agent able to"* verify ([[src-tan-pstack-guide-verify-and-ship]]). *(synthesis)* The two can be combined: the agent runs its own checks, and the harness keeps a held-out set it never sees, as omp's `/ratchet` does with its test split ([[src-omp]]). See [[verification]].
- **What can a model judge?** Osmani's `/goal` lets a small model decide "done" ([[src-osmani-loop-engineering]]). Ouroboros forbids any model from granting acceptance. That is the strictest position in the wiki.
- **Is convergence success?** Ralph's main stop signal is that the *spec's data model* stopped changing, which is not the same as the result being correct *(synthesis)*. A QA pass and the evaluation gate are separate stop paths.

## Caveats and internal inconsistencies
- **The guide lags the code.** The site guide (verified against v0.51.5) says Stage 3 approves on a two-thirds majority and lists 6 consensus triggers. The repo docs at `main` (v0.59) make Stage 3 advisory only and list 7 triggers.
- **Ralph's budget appears twice:** 30 generations as the general cap, and 3 as the default when chained after a failed evaluation.
- **Known gaps in the mechanical gate.** Open issue #2562 reports that Stage 1 can record *"commands that cannot fail (e.g. `pytest --version`)"* as evidence. The docs also say plainly that model labels in consensus don't prove that separate vendors voted.
- **"Agent OS" is a naming collision.** Ouroboros calls itself an "Agent OS", which is unrelated to [[agentos]]. Its README also says it is not the separate "Ouroboros" self-modifying agent (`razzant/ouroboros`).
- **No field evidence yet.** The roadmap is a go-to-market document, and its own claim table marks the pilot and partnership evidence as planned or proposed.

## Not covered
I did not ingest the ko/zh guides, `docs/agentos/*` (TraceGuard, workflow IR), active-conductor, auto-live-kanban, the CLI/config references, the `ouroboros-plugins` and `ourocode` repos, or the roadmap PDF.

## Pages touched
[[ouroboros]], [[evolutionary-loop]], [[goal-spec]], [[verification]], [[evaluator-optimizer]], [[backpressure]], [[termination]], [[goal-loop]], [[ralph-loop]], [[failure-modes]], [[context-and-state]], [[idempotency]], [[observability]], [[human-in-the-loop]], [[budgets-and-cost]], [[guardrails-and-permissions]], [[loop-primitives]], [[omp]], [[open-questions]]
