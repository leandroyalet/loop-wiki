---
type: hub
branch: patterns
tags: [loop-engineering, hub, patterns]
sources: []
created: 2026-10-11
updated: 2026-10-12
status: draft
---
# Loop patterns

Recurring loop shapes. Each one makes a particular choice for the [[anatomy]] slots, especially [[trigger]] and [[termination]]. Up: [[loop-engineering]]. Side-by-side: [[loop-pattern-comparison]].

**Inner loop (the agent itself)**
- [[agent-loop]]: an LLM uses tools on environmental feedback until done.

**Outer loops (what you engineer)**
- [[ralph-loop]]: a bash `while` loop that re-feeds the same prompt and does one item per iteration.
- [[scheduled-loop]]: fires on a cron or interval and does discovery and triage.
- [[self-paced-loop]]: the model picks its own next wake-up time.
- [[goal-loop]]: keeps taking turns until a verifiable condition holds.
- [[event-driven-loop]]: wakes on pushed events instead of polling.
- [[babysitter-loop]]: tends a PR or deploy until it is green.
- [[improvement-loops]]: drive a metric such as coverage, lint, duplication or entropy, one fix per iteration.

**Systems of loops**
- [[software-factory]]: triggers, not humans, start sessions. In a dark factory, nobody reviews the output.
- [[stage-gated-pipeline]]: triage → repro → fix → verify. Every stage can stop the line and hands evidence forward.

**Structural patterns used inside loops**
- [[orchestrator-workers]]: one coordinator, many sub-agents.
- [[evaluator-optimizer]]: a maker and a checker iterate.
- [[human-in-the-loop]]: where people stay in the cycle.
- [[afk]]: the unattended mode, and what it demands before, during and after a run.
