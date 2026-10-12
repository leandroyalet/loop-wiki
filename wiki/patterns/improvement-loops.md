---
type: pattern
branch: patterns
tags: [loop-engineering, pattern, maintenance, ralph]
sources: ["[[src-pocock-ralph-tips]]", "[[src-pocock-getting-started-with-ralph]]", "[[src-pocock-ai-coding-dictionary]]", "[[src-claude-code-scheduled-tasks]]", "[[src-tan-loops-you-can-trust]]"]
created: 2026-10-12
updated: 2026-10-12
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
| Maintenance prompt | bare `/loop` | when nothing else is pending, run *"bug hunts or simplification"* | [[src-claude-code-scheduled-tasks]] |

## Why they work well *(synthesis)*
The [[goal-spec]] is a number with an obvious stop condition (a coverage target, zero lint errors). The [[verification]] is the same tool that produced the signal. Each iteration is naturally small. That makes them good first candidates for a [[software-factory]].

## Related
[[ralph-loop]] · [[scheduled-loop]] · [[task-sizing]]
