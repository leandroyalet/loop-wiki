---
type: hub
branch: control
tags: [loop-engineering, hub, control, safety]
sources: []
created: 2026-10-11
updated: 2026-10-12
status: draft
---
# Control: keeping loops bounded, safe and correct

A loop running unattended *"is also a loop making mistakes unattended"* ([[src-osmani-loop-engineering]]). This branch collects the mechanisms that keep loops under control. Up: [[loop-engineering]].

- [[termination]]: stop conditions. Its page lives in [[anatomy]], but it is the first control to design.
- [[budgets-and-cost]]: tokens, sub-agent spend, polling vs events.
- [[guardrails-and-permissions]]: what the loop may do without asking.
- [[backpressure]]: mechanical checks that reject bad output fast.
- [[isolation]]: worktrees and sandboxes so parallel work doesn't collide.
- [[observability]]: seeing what the loop did and why.
- [[earned-autonomy]]: verification is the limiting step, so trust comes before loops.
- [[idempotency]]: safe re-runs after crashes, retries and duplicate fires.
- [[smart-zone]]: context rot, and why each iteration should start fresh.
- [[agent-experience]]: a codebase the loop can navigate and check (*"the repo wins"*).
- [[failure-modes]]: how loops go wrong.
- [[operator-debts]]: how the *human* goes wrong (intent, comprehension, surrender).

Checklist form: [[loop-design-checklist]].
