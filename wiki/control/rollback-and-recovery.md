---
type: concept
branch: control
tags: [loop-engineering, control, rollback, recovery, safety]
sources: ["[[src-osmani-claude-code-code-review]]", "[[src-huntley-ralph]]", "[[src-pocock-ralph-tips]]", "[[src-tan-pstack-guide-overnight]]", "[[src-omp]]", "[[src-openprose]]", "[[src-tan-pstack-loop-principles]]"]
created: 2026-10-27
updated: 2026-10-27
status: draft
---
# Rollback and recovery

**Rollback and recovery** is the control that assumes some bad output *will* get past [[verification]], and makes undoing it cheap and fast. The [[claude-code]] team puts it under every other check: *"Some bad merges will inevitably make it through. This is our last line of defense"*, and its priority is *"improving our ability to identify and correct issues quickly"* rather than slowing down ([[src-osmani-claude-code-code-review]]). Up: [[control]].

## Where it sits in the loop
It acts after [[termination]], once the loop's output has landed. Inside a loop, the same idea shows up as **keep or revert** on each iteration's result, which is part of the [[decision-step]] and depends on [[context-and-state]] living in git.

## Two scales *(synthesis)*
| Scale | Mechanism | Source |
|---|---|---|
| **Per iteration** | Commit if the iteration made progress, discard it if not, so regressions don't ride along | [[src-tan-pstack-guide-overnight]] |
| | `/ratchet`'s host-owned `gate()` returns keep / revert / rerun, scored on a held-out split | [[src-omp]] |
| | One commit per feature gives *"a rollback point"* | [[src-pocock-ralph-tips]] |
| | After a broken night, choose between `git reset --hard` and rescue prompts | [[src-huntley-ralph]] |
| **Per shipped change** | Feature flags that can be turned off without a deploy | [[src-osmani-claude-code-code-review]] |
| | Staged rollout: employees first, then the *latest* channel, with *stable* trailing | [[src-osmani-claude-code-code-review]] |
| | A one-step revert; a PR template that asks *"How to revert"* | [[src-osmani-claude-code-code-review]] |
| | A merge queue, so two green PRs can't combine into a broken main | [[src-osmani-claude-code-code-review]] |

## Recovery is what buys lighter review
The Claude Code team's case is that cheap reversal is what lets a merge need fewer humans. *"You land it, you own it"* works because ([[src-osmani-claude-code-code-review]]):
- changes are small, so they are easy to review, debug and revert (see [[task-sizing]])
- *"Everything can be reverted. Feature flags, reverts, and staged rollouts can reverse most mistakes in minutes."*
- *"Blast radius sets the bar."* More expensive code gets more eyes.
- telemetry and heavy internal use surface regressions quickly
- it is blameless: whoever fixes the problem owns it because they have the most context, and incident reviews look at the system

The low-risk tier in its approval scheme is defined partly by reversibility: *"additive changes behind a flag"* need no human ([[src-osmani-claude-code-code-review]]). *(synthesis)* This matches Tan's rule that reversible work proceeds without blocking while irreversible work waits for a human ([[src-tan-pstack-loop-principles]]). See [[guardrails-and-permissions]].

## Closing the loop on misses
Every incident review asks which layer *should* have caught the problem ([[src-osmani-claude-code-code-review]]). Incident PRs and reverts then become the eval set for the automated reviewer, so recovery feeds the next round of verification. See [[layered-code-review]] and [[improvement-loops]].

## Contradictions & open questions
- **Rollback is not automatic.** OpenProse states *"Failure or cancellation does not imply rollback"*: a failed render commits nothing, and anything further is left to the program ([[src-openprose]]). The Claude Code team still relies on the author and on-call to *notice* bad merges ([[src-osmani-claude-code-code-review]]).
- **No circuit breaker yet.** The team has no mechanism that tightens approval requirements when revert or incident rates rise, though it is *"something we're looking into"* ([[src-osmani-claude-code-code-review]]). See [[open-questions]].
- Only one source treats release-level recovery in depth. Sources on flags and staged rollout for agent-written code are still wanted.

## Related
[[idempotency]] · [[failure-modes]] · [[earned-autonomy]] · [[human-in-the-loop]]
