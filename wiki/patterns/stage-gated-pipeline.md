---
type: pattern
branch: patterns
tags: [loop-engineering, pattern, pipeline, maintenance, automation]
sources: ["[[src-tan-loops-you-can-trust]]", "[[src-tan-benny-automation]]", "[[src-tan-how-i-use-cursor]]", "[[src-tan-pstack-guide-overnight]]", "[[src-omp]]", "[[src-osmani-claude-code-code-review]]"]
created: 2026-10-12
updated: 2026-10-27
status: draft
---
# Stage-gated pipeline (triage → repro → fix → verify)

A chain of automations, each owning one stage and **handing evidence to the next**. Any stage may **stop the line**. Tan's maintenance line, *benny*, is the reference ([[src-tan-loops-you-can-trust]], [[src-tan-benny-automation]]). It is a [[software-factory]] whose stages are separate loops. Up: [[patterns]].

## The line
From [[src-tan-loops-you-can-trust]] and [[src-tan-benny-automation]]:

| Stage | Trigger | Work | Can stop with | Hands over |
|---|---|---|---|---|
| Triage | a new top-level Slack report | read the thread and attachments, classify, find the owning layer, search duplicates, check version and history | "expected behaviour", duplicate, reroute | a ticket (clear net-new bugs only) plus a `[benny:bug]` marker |
| Repro | the triage marker | open a real build in the cloud and follow the reporter's path. **Hit the exact broken state twice.** | "can't reproduce", someone already owns the fix, an existing PR verified instead | screenshots, video, a state cross-check, a warm build |
| Fix | repro evidence, **after a window for humans to object** | a test when cheap, *"the smallest fix it can prove"*, a blast-radius check | "too risky" | a **draft** PR with before/after proof |
| Verify | the fix | before/after run, subplanner verification workers ([[src-tan-how-i-use-cursor]]) | a failed check | evidence in the PR |

## The two rules
From [[src-tan-pstack-guide-overnight]]:
- **Every stage can stop the line.** *"Those are all useful outcomes because they keep bad work from flowing into the next stage, where it gets much more expensive to correct."*
- **Every stage hands over evidence,** so *"A human can then check that the agent fixed the right thing before reading a line of code."*

## Guardrails in the pack
From [[src-tan-benny-automation]]:
- Draft PRs only, never merge or deploy.
- Fail closed when config is uncertain.
- Subagents get no Slack credentials.
- Never post a root channel message.
- Per-stage budgets.

See [[guardrails-and-permissions]].

## A second line: robomp (omp)
From [[src-omp]]. This one runs as **one session per issue**, with stages enforced by prompts and host tools rather than by separate automations:

| Stage | Can stop with | Gate |
|---|---|---|
| Classify (before any comment, push or PR) | `wontfix`, `question`, `duplicate`, `invalid`, `enhancement` | a 5-part `bug` merit gate: broken contract, demonstrated impact, not a deliberate tradeoff, this repo's defect, true premise |
| Reproduce | `mark_unable_to_reproduce`: asks the reporter for details and resumes the same session on reply | *"No PR without a recorded repro"* (`repro_record`) |
| Fix | `abort_task` for environment faults | root cause only. *"NEVER suppress warnings, special-case inputs"*. |
| Publish | push refusals. *"Two identical consecutive push rejections → … escalate; NEVER loop"* | `bun run fix` + `bun check` + the full test suite before `gh_open_pr`. The PR body must have `## Repro / Cause / Fix / Verification`. |

The same handoff rule as benny applies: the PR carries the evidence. A maintainer's "works as designed" at any stage makes the bot stop at once, without arguing.

## A third line: the life of a change (Claude Code team)
From [[src-osmani-claude-code-code-review]]. This line gates a *change* rather than a bug report: pre-PR verification → AI review → security review → CI → risk-tiered human approval → merge queue → flag and staged rollout, with fast rollback under all of it. Open findings from either review, red CI, or a missing required approval each stop the line. Its difference from benny and robomp is that the stages are **layers that each miss some bugs**, and recovery is designed in as a last layer instead of assumed away. Full page: [[layered-code-review]].

## Why staged *(synthesis)*
Each stage has its own small [[goal-spec]] and its own [[verification]]. This is Grove's *"catch defects at the lowest value stage"* ([[src-tan-loops-you-can-trust]]) applied to the pipeline as a whole. Compare Osmani's single morning triage loop, which runs triage, fix and review inside one automation ([[src-osmani-loop-engineering]]), and Pocock's human-gated triage ([[src-pocock-triage-skill]]).

## Related
[[event-driven-loop]] · [[backlog-triage]] · [[earned-autonomy]] · [[idempotency]]
