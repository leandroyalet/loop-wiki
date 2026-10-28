---
type: practice
branch: practice
tags: [loop-engineering, practice, code-review, verification, claude-code]
sources: ["[[src-osmani-claude-code-code-review]]", "[[src-pocock-ai-coding-dictionary]]", "[[src-tan-pstack-guide-verify-and-ship]]", "[[src-tan-pstack-guide-overnight]]", "[[src-inside-pstack-report]]", "[[src-ouroboros]]"]
created: 2026-10-27
updated: 2026-10-27
status: draft
---
# Layered code review (the Claude Code team's pipeline)

**Layered code review** is how the [[claude-code]] team reviews code that agents mostly write. Instead of one human gate per PR, a change passes several imperfect layers of automated and human checks, with fast rollback under all of them. Human attention goes only where risk calls for it. *"Each layer catches some bugs while missing others. Few bugs get through all of the layers, and if some do, we have a rollback mechanism in place"* ([[src-osmani-claude-code-code-review]]). Up: [[practice]].

## Where it sits in the loop
It is [[verification]] spread across the whole life of a change rather than placed at one step. Pre-PR checks run inside the authoring loop. The AI reviewer and the author form an [[evaluator-optimizer]] loop that needs its own [[termination]]. Risk-tiered approval is where the [[human-in-the-loop]] sits, and flags and reverts handle [[rollback-and-recovery]] after the loop has "finished".

## The question it replaces
*"did someone read the code?"* is treated as an imprecise stand-in for *"what could go wrong with this change, and what check - automated or human - is the right one to catch it?"* ([[src-osmani-claude-code-code-review]]).

## The layers
From [[src-osmani-claude-code-code-review]] (figs. A and B):

| # | Layer | What runs | Blocks? |
|---|---|---|---|
| 1 | Pre-PR verification | Claude runs tests, build, linter or a screenshot diff and *shows* the result. A subagent reviews the diff in fresh context. Optional skills: bug hunt, diff reduction, end-to-end validation, design-guideline check. | — (before the PR exists) |
| 2 | AI review | Parallel bug-hunting agents, a validity vote, style findings filtered out. Findings are ranked and labelled *Important / Nit / Pre-existing*. | every finding must be fixed or resolved with a reason |
| 3 | Security review | a separate automated pass | yes, while any finding is open |
| 4 | Required CI | lint, types, tests on every platform, build and packaging. The PR template asks how it was tested and how to revert it. | yes |
| 5 | Risk-based approval | a classifier sets the tier (below) | yes, for the required number of humans |
| 6 | Merge queue, flags, staged rollout | checks re-run on the latest main; feature flag, employees first; *latest* channel before *stable* | yes (queue) |
| — | Fast feedback and rollback | the author and on-call watch; flags off without a deploy; one-step revert | recovery, not a gate |

## Risk tiers
The tier is set **by the change, not the author** (fig. C, [[src-osmani-claude-code-code-review]]):

| Risk | Examples | Human approvals |
|---|---|---|
| Low | docs, copy, internal-only features, additive changes behind a flag | none, once automated review and security checks are green |
| Medium | ordinary product changes; sensitive areas such as caching, the auto-updater, system prompts | one |
| High | the highest-risk code, plus paths that always need two people | two |

Rules around the tiers:
- A second classifier can require an extra approval even when the tier doesn't. Paths marked sensitive by owners, and every CI workflow file, always need a person.
- Only authors on the repo's trusted list get relaxed requirements.
- *"Agent approvals don't count as human approvals."*
- When an agent authors a PR, its operator always counts as one of the required reviewers.
- An approval covers one commit. An untrusted new commit, such as an agent push or a hand-resolved merge, needs re-approval. *(synthesis)* This is the same rule as pstack's head-SHA-keyed verdicts: a verdict expires when the code changes ([[src-inside-pstack-report]]). See [[verification]].

## Tuning the reviewer
From [[src-osmani-claude-code-code-review]]:
- **`REVIEW.md` per area.** Code owners say what matters. Good ones are short and define failure (*"the docs should not lie; the config should not misroute"*). They limit nitpicking, list ignored paths, require `file + line` references, and require a summary with a finding count and an explicit "no issues". The team checks separately that the reviewer actually follows them.
- **Fix recurring findings at the source:** in the skill, a lint rule, or `CLAUDE.md`. See [[build-the-lever]].
- **Score against incidents daily.** Expert-confirmed incident PRs make up the eval set. Each change to the reviewer's prompts, tools or model is kept only if the score rises (fig. D). See [[improvement-loops]].
- **Measure noise** from how authors resolve comments (fixed / rejected / intentional / didn't matter) and from runs on known-clean PRs.
- **Make it converge.** Re-evaluate the approach after three cycles, re-review only the new diff after that, name the bug *class*, and never re-report a known issue. See [[evaluator-optimizer]].
- **Scale effort to risk.** Code Review has Quick, Standard and Deep levels. Deep is for code where *"the cost of missing a single bug is higher than the time spent reviewing code"*.

## What is measured
Median and p95 human approvals per PR, number of human comments, time a PR waits on a person, cycles-to-pass alongside recall, and revert and incident rates as the guardrail ([[src-osmani-claude-code-code-review]]). See [[observability]].

## Rollout recipe
The article's "How to implement" list, condensed ([[src-osmani-claude-code-code-review]]):
1. **Before the PR:** a short `CLAUDE.md` listing the checks the agent can run, formatters and linters via hooks, `/code-review` and `/security-review` (or a fresh-context subagent) locally, and a `REVIEW.md` that collects recurring issues.
2. **On every PR:** enforced CI; a PR template with *Testing*, *Risk* and *How to revert*; an AI reviewer on **one repo first**, iterating on `REVIEW.md` for a few weeks before wider rollout; automated security review; all threads resolved before merge; rigor scaled to risk; a cap on review rounds.
3. **Approval:** risk levels set by the change. *"Start strict, and progressively relax as you see evidence."* Lenient paths only for trusted authors. Bot approvals never satisfy a required approval. Dismiss approvals on new commits. Humans own auth, billing, CI, release and installer code via CODEOWNERS and branch protection.
4. **Merge and after:** merge queue, feature flags, internal users first, staged rollout, one-step revert, an eval set built from incidents and reverts, a rescore whenever the reviewer changes, and human effort tracked against revert and incident rates.

## Compared with other sources *(synthesis)*
| | Claude Code team | Pocock | pstack |
|---|---|---|---|
| Role of AI review | blocks until each finding is resolved; can clear low-risk changes alone | *"a filter that raises the floor before a human looks, not a gate that replaces one"* | a fresh verifier swarm; Autopilot-full merges on its verdict |
| Human gate | scaled by risk: 0, 1 or 2 people | human review on the PRs | optional at the top of the ladder |
| Source | [[src-osmani-claude-code-code-review]] | [[src-pocock-ai-coding-dictionary]] | [[src-tan-pstack-guide-verify-and-ship]], [[src-tan-pstack-guide-overnight]] |

## Contradictions & open questions
- **Can a model clear a change?** Here, automated review plus green checks clears a low-risk change with no human. Ouroboros says models may only *withhold* approval and never grant it ([[src-ouroboros]]). Pocock says automated review is a filter, not a gate ([[src-pocock-ai-coding-dictionary]]). The Claude Code version leans on its risk classifier and on rollback to make that safe. See [[open-questions]].
- **Gate or filter?** Open AI-review findings block the merge, which makes the reviewer a gate. But the author can close any finding with a short reason, so in practice it is a gate the author can lift ([[src-osmani-claude-code-code-review]]).
- **Vendor source.** The numbers (16% → 54% substantive comments, reverts down more than 40%) are self-reported by the team that sells Code Review ([[src-osmani-claude-code-code-review]]).
- **No circuit breaker yet.** Approval requirements don't tighten automatically when reverts rise. The team says it is looking into it ([[src-osmani-claude-code-code-review]]).

## Related
[[stage-gated-pipeline]] · [[backpressure]] · [[earned-autonomy]] · [[software-factory]] · [[claude-code-goal]]
