---
type: concept
branch: control
tags: [loop-engineering, control, idempotency, reliability]
sources: ["[[src-tan-pstack-loop-principles]]", "[[src-tan-benny-automation]]", "[[src-claude-code-scheduled-tasks]]", "[[src-pocock-triage-skill]]", "[[src-inside-pstack-report]]", "[[src-openprose]]", "[[src-omp]]", "[[src-ouroboros]]"]
created: 2026-10-12
updated: 2026-10-19
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

On 14 Oct 2026 the principle was rewritten as reasoning rather than mechanisms (#633): *"Derive each step from the state that exists, not from what the last run meant to do."* *"Anything a run leaves behind must be recognizable as stale by the next run, wherever the last one stopped"* ([[src-inside-pstack-report]]).

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
- **In pstack's own scripts** ([[src-inside-pstack-report]]):
  - `orch` has a PID lock that heals itself after a crash.
  - `bootstrap.ts` keys installs on a hash of `package.json` + `bun.lock`, so a rerun does nothing.
  - `setup-pstack` overwrites its config file in full *"so re-runs stay idempotent"*.
- **Verdicts keyed by content.** The orch ledger is keyed by PR + head SHA, so *"a new SHA voids the verdict"*. Shipping re-checks with `git patch-id` after rebases ([[src-inside-pstack-report]]). See [[verification]].
- **Assume the worker dies.** Autopilot-full owners *"push early and keep a decision trail a replacement can find"* ([[src-inside-pstack-report]]).
- **Memoised wakes and all-or-nothing commits.** OpenProse:
  - skips a render when `(contract-fingerprint, input-fingerprints)` hasn't moved
  - allows one render in flight per node, and coalesces wakes that arrive mid-render into one follow-up
  - commits nothing from a `failed` render, so *"prior truth stands"*

  Its kernel adds that *"Failure or cancellation does not imply rollback"*: recovery policy belongs to libraries or programs ([[src-openprose]]). See [[reconciler-loop]].
- **Webhook dedup and crash resume.** robomp dedups events on `X-GitHub-Delivery`, serializes work per `(owner, repo, n)`, flips `running` rows back to `queued` on startup, and resumes the same omp session from its JSONL transcript. It keeps *"One PR per issue"*: follow-ups amend the same branch ([[src-omp]]).
- **Isolated condition checks.** omp's `/loop --until` runs its condition in a separate shell session, so the check can't change the agent's state ([[src-omp]]).
- **One successor, deterministically named.** Ouroboros derives the lineage ID from a digest of the full Seed and run. Concurrent or replayed evaluation completions publish Gen 1 once and enqueue *"at most one Ralph successor"*. Retries reconnect to active and finished jobs. Chaining is *fail-open*: an enqueue failure never changes the verdict that preceded it ([[src-ouroboros]]).
- **Known non-idempotent failure:** without an `implemented` state, *"an AFK runner can queue finished tickets again"* ([[src-pocock-triage-skill]]). See [[failure-modes]].

## Related
[[failure-modes]] · [[guardrails-and-permissions]] · [[trigger]]
