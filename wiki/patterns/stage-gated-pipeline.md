---
type: pattern
branch: patterns
tags: [loop-engineering, pattern, pipeline, maintenance, automation]
sources: ["[[src-tan-loops-you-can-trust]]", "[[src-tan-benny-automation]]", "[[src-tan-how-i-use-cursor]]", "[[src-tan-pstack-guide-overnight]]"]
created: 2026-10-12
updated: 2026-10-12
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

## Why staged *(synthesis)*
Each stage has its own small [[goal-spec]] and its own [[verification]]. This is Grove's *"catch defects at the lowest value stage"* ([[src-tan-loops-you-can-trust]]) applied to the pipeline as a whole. Compare Osmani's single morning triage loop, which runs triage, fix and review inside one automation ([[src-osmani-loop-engineering]]), and Pocock's human-gated triage ([[src-pocock-triage-skill]]).

## Related
[[event-driven-loop]] · [[backlog-triage]] · [[earned-autonomy]] · [[idempotency]]
