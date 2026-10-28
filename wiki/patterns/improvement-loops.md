---
type: pattern
branch: patterns
tags: [loop-engineering, pattern, maintenance, ralph]
sources: ["[[src-pocock-ralph-tips]]", "[[src-pocock-getting-started-with-ralph]]", "[[src-pocock-ai-coding-dictionary]]", "[[src-claude-code-scheduled-tasks]]", "[[src-tan-loops-you-can-trust]]", "[[src-omp]]", "[[src-osmani-claude-code-code-review]]", "[[src-anthropic-fold-subagents]]"]
created: 2026-10-12
updated: 2026-10-27
status: draft
---
# Improvement loops (coverage, lint, duplication, entropy)

**Improvement loops** are Ralph-style loops aimed at a measurable codebase metric instead of a feature backlog. *"Any task that can be described as 'look at repo, improve something, report findings' fits the Ralph pattern. The loop is the same. Only the prompt changes"* ([[src-pocock-ralph-tips]]). Up: [[patterns]].

| Loop | Signal | One iteration | Source |
|---|---|---|---|
| Test coverage | a coverage report | write tests for the most critical uncovered paths, re-run coverage (16% → 100% on the AI Hero CLI) | [[src-pocock-ralph-tips]] |
| Linting | `npm run lint` | fix **one** lint error, re-run the linter | [[src-pocock-ralph-tips]] |
| Duplication | `jscpd` | refactor clones into shared utilities | [[src-pocock-ralph-tips]] |
| Entropy | code smells | fix **one** issue (unused exports, dead code, inconsistent patterns) and log it | [[src-pocock-ralph-tips]] |
| Nightly lint rule | cron | *"picks one lint rule a night, opens a PR"* | [[src-pocock-ai-coding-dictionary]] |
| Migration (StyleX) | computed styles before/after across themes and states, plus paired screenshots reviewed by another agent | migrate **one leaf component**, checking warning signs and consumers first. A failed build or parity check ends the run. | [[src-tan-loops-you-can-trust]] |
| Eval hill-climb (`/ratchet`) | a frozen held-out test split, graded by the cheapest grader that measures the property | a fresh analyzer reads train traces and proposes **one** diff, then the host's `gate()` keeps or reverts it. Runs until plateau. | [[src-omp]] |
| Historical bug sweep | the PR review agents, pointed at the current codebase | run overnight on existing code *"helping us identify historical bugs before they propagate"* | [[src-osmani-claude-code-code-review]] |
| Reviewer eval (incidents) | a set of expert-confirmed incident PRs, run daily | change the reviewer's prompts, tools or model; keep the change only if the score goes up | [[src-osmani-claude-code-code-review]] |
| Maintenance prompt | bare `/loop` | when nothing else is pending, run *"bug hunts or simplification"* | [[src-claude-code-scheduled-tasks]] |

## Why they work well *(synthesis)*
The [[goal-spec]] is a number with an obvious stop condition (a coverage target, zero lint errors). The [[verification]] is the same tool that produced the signal. Each iteration is naturally small. That makes them good first candidates for a [[software-factory]].

## The ratchet: hill-climbing an LLM flow
omp's `/ratchet` applies the improvement loop to a *prompt or flow* rather than to code ([[src-omp]]):
- **The host, not the agent, owns truth:** content-hashed approvals, the frozen split, held-out isolation, and keep/revert.
- **The number that matters** is the test-split delta against baseline. *"Train movement is process, not result."*
- **Grill, then three approvals** (inputs, grader, plan), then unattended rounds until `plateau` or `done`.
- **On a stall, classify each failure** as `artifact_gap`, `grader`, `harness`, `structural` or `variance`, and respond by category. *"Categorize, don't grind."*
- **Lineage:** adapted from the `build-eval` / `hillclimb` guides in Anthropic's `claude-api` skill. pstack's Hillclimb playbook has the same shape ([[src-inside-pstack-report]]).

## Architecture as a hill-climb (Anthropic)
Anthropic frames moving from many agents to one loop as the same keep-or-discard climb: build a small end-to-end eval, fold in **one** subagent, keep the folded version unless it scores worse, *"then rinse and repeat"*. Its `hillclimb` skill iterates the folded skill and tool descriptions against that eval. The stated principle: *"measure, change one thing at a time, and keep what holds up"* ([[src-anthropic-fold-subagents]]). See [[folding-subagents]].

## Related
[[ralph-loop]] · [[scheduled-loop]] · [[task-sizing]]
