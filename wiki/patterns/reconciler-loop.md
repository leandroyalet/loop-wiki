---
type: pattern
branch: patterns
tags: [loop-engineering, pattern, standing-goal, reconciler, events]
sources: ["[[src-openprose]]"]
created: 2026-10-19
updated: 2026-10-19
status: stub
---
# Reconciler loop (standing goal)

A **reconciler loop** keeps a *standing* goal true over time, instead of driving toward a one-time finish. Something wakes the loop. It checks deterministically whether anything material has changed. Only if something has does it run one bounded agent session to bring the maintained state back in line with its postconditions. [[openprose]] calls the goal a **responsibility**: a standing goal *"that must remain true over time"*, served *"through bounded renders woken over time"* ([[src-openprose]]). Up: [[patterns]].

## Where it sits in the loop
- **[[trigger]]:** three wake sources. *Input-driven* means an upstream node's output changed. *Self-driven* means a declared freshness cadence ticks. *External-driven* means a webhook, cron or manual request arrives through a gateway ([[src-openprose]]).
- **[[decision-step]]:** split in two. Whether to run is decided by code (a fingerprint comparison). What to do is decided by the model, inside the render. *"The harness never asks an LLM 'did this change'"* ([[src-openprose]]).
- **[[verification]]:** postconditions in `### Maintains` are compiled to validators. They are checked deterministically where that can be expressed, and attested by the render where the check is semantic ([[src-openprose]]).
- **[[termination]]:** each render is bounded. The loop as a whole has no end state.
- **[[context-and-state]]:** the persisted world-model and an append-only receipt ledger hold state, never a long-running session.

## Mechanics (OpenProse's reconciler)
All of these are from [[src-openprose]]:
1. A wake arrives as a **receipt**.
2. **Memo / skip.** The key is `(contract-fingerprint, input-fingerprints)`. If neither has moved, it writes a `skipped` receipt and spawns nothing.
3. **Single-flight + coalescing.** Only one render runs per node at a time. Wakes that arrive mid-render mark the node dirty and collapse into one follow-up render.
4. **Render.** The render reads its evidence and the prior world-model by reference, satisfies the postconditions, and signs a receipt. The receipt is either `rendered` (committed) or `failed` (*"nothing committed; prior truth stands"*).
5. **Propagate.** Only a `rendered` receipt with a moved fingerprint wakes the downstream nodes that subscribe to the facet that changed.

**Staleness is a change too.** Freshness *state* (`valid_until`, `confidence`) lives in the world-model, and freshness *policy* (the recheck cadence) lives in `### Continuity`. When a `valid_until` lapses, the fingerprint moves, so *"time becoming material"* propagates like any other change ([[src-openprose]]).

## How it differs from neighbours *(synthesis)*
| | [[goal-loop]] | [[scheduled-loop]] | [[event-driven-loop]] | Reconciler loop |
|---|---|---|---|---|
| Goal | one-time condition | a recurring task | react to an event | an invariant kept true |
| Who decides to run | the loop, until a judge says done | the clock | the event | a deterministic fingerprint diff |
| Does an idle wake cost tokens? | n/a | yes, it re-runs the prompt | sometimes | no, it writes a `skipped` receipt |
| Ends? | yes | TTL or a human | yes | no (each render is bounded) |

*(synthesis)* The shape resembles a desired-state controller as in infrastructure tooling. That is lineage only, and the source does not draw the comparison.

## Contradictions & open questions
- **A judge was tried and removed.** OpenProse ran an LLM *"judge → verdict → pressure → fulfillment loop"* before v0.15.0 and retired it *"wholesale"* ([[src-openprose]]). The source gives the replacement, not a measured reason. Is an LLM judge in the outer loop a mistake in general, or only for standing goals? Compare `/goal`'s fresh-model judge ([[src-osmani-loop-engineering]]). See [[open-questions]].
- **Compile-time judgement.** The model decides *once* at compile time what counts as a material change. If that canonicalizer is wrong, real drift is silently skipped *(synthesis)*. No source covers this failure mode yet. See [[failure-modes]].
- It has a single source, and that source is experimental, with benchmarks pending.

## Related
[[patterns]] · [[idempotency]] · [[budgets-and-cost]] · [[loop-pattern-comparison]]
