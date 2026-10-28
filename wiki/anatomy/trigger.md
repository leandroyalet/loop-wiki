---
type: concept
branch: anatomy
tags: [loop-engineering, anatomy, scheduling]
sources: ["[[src-osmani-loop-engineering]]", "[[src-claude-code-scheduled-tasks]]", "[[src-huntley-ralph]]", "[[src-pocock-ai-coding-dictionary]]", "[[src-pocock-getting-started-with-ralph]]", "[[src-tan-loops-you-can-trust]]", "[[src-tan-pstack-guide-overnight]]", "[[src-openprose]]", "[[src-omp]]"]
created: 2026-10-11
updated: 2026-10-19
status: draft
---
# Trigger

The **trigger** decides when an iteration starts. It is what turns *"one run you did once"* into a loop. Osmani calls automations *"the heartbeat"* ([[src-osmani-loop-engineering]]). Up: [[anatomy]].

## Where it sits in the loop
It is step 1 and the re-entry point after [[termination]] decides "go again."

## Kinds of trigger
| Trigger | Example | Pattern |
|---|---|---|
| Immediate re-run | `while :; do cat PROMPT.md \| claude-code; done` ([[src-huntley-ralph]]), or a capped `for` loop ([[src-pocock-getting-started-with-ralph]]) | [[ralph-loop]] |
| Fixed interval / cron | `/loop 5m check the deploy`, Codex Automations, GitHub Actions `schedule` | [[scheduled-loop]] |
| Model-chosen delay | `/loop <prompt>` without an interval: 1 min–1 h based on what it observed ([[src-claude-code-scheduled-tasks]]) | [[self-paced-loop]] |
| Condition not yet met | `/goal "all tests pass"` keeps taking turns | [[goal-loop]] |
| External event | CI pushes a failure via Channels; the Monitor tool streams lines | [[event-driven-loop]] |
| Slack report | a new top-level message in an issue channel starts a Cursor Automation ([[src-tan-loops-you-can-trust]]) | [[stage-gated-pipeline]] |
| Previous stage's verdict | the repro automation waits for the triage marker in the thread ([[src-tan-loops-you-can-trust]]) | [[stage-gated-pipeline]] |
| Events or heartbeat | Cursor `/loop` re-checks the finish condition ([[src-tan-pstack-guide-overnight]]) | [[overnight-contract]] |
| Issue labelled | `ready-for-agent` label → session that opens a PR ([[src-pocock-ai-coding-dictionary]]) | [[software-factory]], [[backlog-triage]] |
| Another session finishing | PR opened → automated review → fix-up session ([[src-pocock-ai-coding-dictionary]]) | [[software-factory]] |
| Previous turn yielded | omp `/loop` re-submits the prompt after every yield, optionally gated by `--until`/`--while` ([[src-omp]]) | [[omp-loop-surfaces]] |
| GitHub webhook | robomp: `issues.opened`, comments, reviews and `workflow_run` go into a dedup queue, which starts a per-issue session ([[src-omp]]) | [[software-factory]] |
| Upstream change, cadence tick, gateway event | the three wake sources of OpenProse responsibilities (input-, self- and external-driven). If no fingerprint moved, the wake is skipped ([[src-openprose]]) | [[reconciler-loop]] |
| Human | a prompt, or a triage-inbox item picked up | [[human-in-the-loop]] |

When triggers rather than people start sessions, you have a [[software-factory]] ([[src-pocock-ai-coding-dictionary]]).

## Mechanics worth knowing (Claude Code)
All of these are from [[src-claude-code-scheduled-tasks]]:
- A scheduled prompt fires **between turns** and never mid-response. It is enqueued at low priority.
- **Jitter:** recurring tasks run late by a fixed per-task offset of up to 30 min. One-shots set for :00 or :30 may fire up to 90 s early. Schedule off the hour when timing matters.
- **No catch-up:** missed fires collapse into one run when the session is idle.

## Contradictions & open questions
- When is polling the right choice over events? The docs say Monitor is *"often more token-efficient and responsive"* than polling. See [[event-driven-loop]] and [[budgets-and-cost]].

## Related
[[claude-code-scheduling]] · [[claude-code-loop]] · [[loop-primitives]]
