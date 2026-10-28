---
type: practice
branch: practice
tags: [loop-engineering, practice, claude-code, goal]
sources: ["[[src-osmani-loop-engineering]]", "[[src-tns-loop-engineering]]", "[[src-claude-code-scheduled-tasks]]", "[[src-pocock-ralph-plugin]]", "[[src-omp]]"]
created: 2026-10-11
updated: 2026-10-19
status: stub
---
# Claude Code `/goal`

`/goal` keeps a [[claude-code]] session working *"turn after turn toward a condition rather than on an interval"* ([[src-claude-code-scheduled-tasks]]). It is the product form of the [[goal-loop]]. Up: [[practice]].

## How it works
From the secondary descriptions:
- You state a verifiable condition, for example *"all tests in test/auth pass and lint is clean"*, and walk away ([[src-osmani-loop-engineering]]).
- After every turn, **a separate small model checks whether you are done**, so the agent that wrote the code isn't the one grading it ([[src-osmani-loop-engineering]], [[src-tns-loop-engineering]]). See [[evaluator-optimizer]].
- Codex has an equivalent `/goal` with pause, resume and clear ([[src-osmani-loop-engineering]]).

## Contradictions & open questions
- `/goal` keeps working *across turns* in one session. Pocock's [[smart-zone]] critique of in-session loops may apply ([[src-pocock-ralph-plugin]]). Unverified. See [[open-questions]].
- The official `/goal` docs page has **not been ingested**. Details such as turn limits, budgets and how the checker model is chosen are unconfirmed. See [[open-questions]].
- **Compare omp's `/goal`,** which is documented first-hand: it is self-graded with a completion audit, has a token budget, and pauses on interrupt ([[src-omp]]). See [[omp-loop-surfaces]].

## Related
[[claude-code-loop]] · [[termination]] · [[verification]]
