---
type: pattern
branch: patterns
tags: [loop-engineering, pattern, goal, stop-conditions]
sources: ["[[src-osmani-loop-engineering]]", "[[src-tns-loop-engineering]]", "[[src-claude-code-scheduled-tasks]]", "[[src-omp]]", "[[src-ouroboros]]"]
created: 2026-10-11
updated: 2026-10-19
status: draft
---
# Goal loop (run until condition)

A **goal loop** keeps taking turns until a written, verifiable condition is true, instead of running on a cadence. *"`/loop` re-runs on a cadence. `/goal` keeps going until a condition you wrote is actually true"* ([[src-osmani-loop-engineering]]). Up: [[patterns]].

## Where it sits in the loop
The [[goal-spec]] *is* the [[termination]] test. A **separate model** checks it after every turn, so *"the agent that wrote the code isnt the one grading it"*. This is the maker/checker split applied to the stop condition ([[src-osmani-loop-engineering]]). See [[verification]].

## Implementations
- [[claude-code-goal]]: Claude Code `/goal`, documented as working *"turn after turn toward a condition rather than on an interval"* ([[src-claude-code-scheduled-tasks]])
- Codex `/goal`, with pause, resume and clear ([[src-osmani-loop-engineering]]). See [[openai-codex]].

Both products expose it ([[src-tns-loop-engineering]]).
- [[omp]] `/goal`: **self-graded**. The doer ends the loop by calling `goal({op:"complete"})` after a mandatory audit (*"Verification scope = claim scope"*, *"Uncertainty = not achieved"*). A token budget flips the goal to `budget-limited`, and *"Budget exhaustion ≠ completion"* ([[src-omp]]). See [[omp-loop-surfaces]].
- omp `/loop --until '<cmd>'`: the condition is a shell command's exit code, so no model judges "done" at all ([[src-omp]]).
- [[ouroboros]] `ooo auto`: interview → grade-A Seed → run → 3-stage evaluation, where only executed checks can grant acceptance. Failed evaluations chain into a bounded [[evolutionary-loop]] (3 generations by default) ([[src-ouroboros]]).

## Writing good conditions
Make the condition machine-checkable, for example *"all tests in test/auth pass and lint is clean"* ([[src-osmani-loop-engineering]]). See [[writing-a-loop-prompt]].

## Contradictions & open questions
- What happens when the condition is unreachable? For Claude Code `/goal`, no ingested source documents a turn or budget cap. omp's `/goal` has a token budget but no runtime turn cap. Its `/guided-goal` interview requires an attempt cap in the objective text ([[src-omp]]). See [[open-questions]].
- **Separate judge or self-audit?** Osmani: a separate model checks *"so the agent that wrote the code isnt the one grading it"* ([[src-osmani-loop-engineering]]). omp lets the doer declare completion after a structured audit. Independence comes, optionally, from an advisor model that reads every turn and can block a premature yield ([[src-omp]]). No source compares the two. See [[evaluator-optimizer]].

## Related
[[evaluator-optimizer]] · [[loop-pattern-comparison]]
