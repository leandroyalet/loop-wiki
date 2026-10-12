---
type: concept
branch: control
tags: [loop-engineering, control, idempotency, reliability]
sources: ["[[src-tan-pstack-loop-principles]]", "[[src-tan-benny-automation]]", "[[src-claude-code-scheduled-tasks]]", "[[src-pocock-triage-skill]]"]
created: 2026-10-12
updated: 2026-10-12
status: draft
---
# Idempotency (safe re-runs)

Loops re-run constantly. They fire again, retry, crash halfway and get resumed. An operation is **idempotent** when it *"converge[s] to the correct state regardless of how many times they run or where they start from"* ([[src-tan-pstack-loop-principles]]). This was open question #4 in [[open-questions]]. Up: [[control]].

## The test
From [[src-tan-pstack-loop-principles]]:
1. What happens if this runs twice in a row?
2. What happens if the previous run crashed at **every possible point**?
3. Does re-running it converge to the same end state?

*"If any answer is 'it depends on what state was left behind,' the operation needs a reconciliation step."*

## Patterns
From [[src-tan-pstack-loop-principles]]:
- **Convergent startup:** scan for existing state, clean stale artifacts, adopt live sessions.
- **Content-based cleanup:** compare by content, not by creation order.
- **Self-healing locks:** detect stale locks by PID.
- **Idempotent scheduling:** failed work respawns cleanly, and fresh input is regenerated after each cycle.

## In loop designs seen so far *(synthesis)*
- **Check before you create.** benny searches for duplicates and updates a confident duplicate rather than filing a new ticket. If a PR may already fix the bug, it verifies that PR instead of writing a competing one ([[src-tan-benny-automation]]). Pocock's triage does the same, checking for redundancy and prior rejections first ([[src-pocock-triage-skill]]).
- **Stable coordinates.** benny keeps *"the source channel and root thread coordinates … immutable for the whole run"* and posts *exactly one* triage reply ([[src-tan-benny-automation]]).
- **Duplicate and missed fires happen.** Claude Code collapses missed fires into one run and restores tasks on `--resume` ([[src-claude-code-scheduled-tasks]]). Each iteration must therefore tolerate running late, twice, or after a gap.
- **Checkpoint and resume.** pstack's *Pause safely* commits a WIP checkpoint and writes a resume note ([[src-tan-pstack-guide-overnight]]). See [[context-and-state]].
- **Known non-idempotent failure:** without an `implemented` state, *"an AFK runner can queue finished tickets again"* ([[src-pocock-triage-skill]]). See [[failure-modes]].

## Related
[[failure-modes]] · [[guardrails-and-permissions]] · [[trigger]]
