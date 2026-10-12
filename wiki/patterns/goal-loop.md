---
type: pattern
branch: patterns
tags: [loop-engineering, pattern, goal, stop-conditions]
sources: ["[[src-osmani-loop-engineering]]", "[[src-tns-loop-engineering]]", "[[src-claude-code-scheduled-tasks]]"]
created: 2026-10-11
updated: 2026-10-11
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

## Writing good conditions
Make the condition machine-checkable, for example *"all tests in test/auth pass and lint is clean"* ([[src-osmani-loop-engineering]]). See [[writing-a-loop-prompt]].

## Contradictions & open questions
- What happens when the condition is unreachable? No ingested source documents a turn or budget cap for `/goal`. See [[open-questions]].

## Related
[[evaluator-optimizer]] · [[loop-pattern-comparison]]
