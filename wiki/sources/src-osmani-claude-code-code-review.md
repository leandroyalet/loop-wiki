---
type: source
branch: sources
tags: [loop-engineering, primary, code-review, verification, claude-code]
sources: []
url: https://x.com/addyosmani/status/2114604912520921136
author: Addy Osmani
published: 2026-10-26
raw: raw/2026-10-27-osmani-claude-code-code-review.md
created: 2026-10-27
updated: 2026-10-27
status: solid
---
# Osmani — "How the Claude Code team does code review" (2026-10-26)

**Author:** [[addy-osmani]], writing as "we", the [[claude-code]] team at [[anthropic]] · **Raw:** `raw/2026-10-27-osmani-claude-code-code-review.md` (six figures in `raw/assets/2026-10-27-osmani-claude-code-code-review-fig-*.jpg`) · Up: [[sources]]

## Summary
This is an X article describing how the Claude Code team reviews code now that Claude writes about 90% of it. The team didn't stop reviewing. It *"automated the majority of reading and tuned it to optimize for human time and effort"*, and it invested in making reverts fast. A change passes **six layers of checks with rollback underneath**: pre-PR verification, AI review, a blocking security review, blocking CI, risk-tiered human approval, and a merge queue with flags and staged rollout. Each layer misses some bugs, so no single layer is the gate. Between June and September, merged PRs more than doubled while the share reverted fell by more than 40%. The most loop-relevant part is the section on making the reviewer itself better. The reviewer is evaluated daily against a set of past incidents, and the team limited review cycles after an agent author and an agent reviewer **cycled more than fifty times overnight** on one PR.

The article ends *"A rewrite of our original article"* and links to an Anthropic/Claude blog post (`claude.dev/blog/solving-code-review-at-anthropic`) that has not been fetched. It also promotes Anthropic's own Code Review product, so read the product numbers as vendor-reported.

## Key claims
- **Scale.** Anthropic's monorepo went from about 2,500 merged changes per day in May to over 30,000 in September. Line-by-line manual review stops being possible at that pace. See [[anthropic]].
- **Reframe the question.** *"did someone read the code?"* is an imprecise stand-in for *"what could go wrong with this change, and what check - automated or human - is the right one to catch it?"* See [[verification]].
- **Review moves earlier.** It becomes *"more like a spellcheck that you continuously do while writing"*. Most changes have been reviewed and corrected by Claude at least once before a human sees them.
- **Human time is a two-sided cost:** time spent reviewing *plus* time spent fixing bugs that bad code introduced. The goal is that most PRs merge with at most one person in the loop, who may be the author, *"without an increase in reverts or incidents"*. Revert and incident rates act as the guardrail: if they rise, *"we haven't reduced human time, just relocated it."* See [[budgets-and-cost]] and [[observability]].
- **Layer 1, pre-PR verification.** Ask Claude for something runnable (tests, the build, a screenshot compared with the design): *"Instead of saying the task is done, we ask it to show us the result."* Then a subagent reviews the diff in a fresh context. [[boris-cherny]] estimates that giving Claude a verification process improves output quality by **2–3×** (as reported here). See [[verification]].
- **Fix recurring findings at the source.** If the reviewer keeps flagging the same issue, fix the skill, add a lint rule, or update `CLAUDE.md` or `REVIEW.md`. `REVIEW.md` is where code owners tell the reviewer what matters in their area. Good ones define what counts as failure, limit nitpicking, list ignored paths, require `file + line` references, and require a summary with a finding count and an explicit "no issues". See [[build-the-lever]].
- **Layer 2, AI review on every PR.** The diff is checked against the whole codebase and the stated intent. Several agents hunt for bugs in parallel, a **vote** keeps only findings with enough support, and style or cleanup findings are filtered out (A/B-tested first). Survivors are ranked by severity and labelled *Important*, *Nit* or *Pre-existing*. Every finding must be fixed or resolved with a reason. Internal PRs with substantive comments went from 16% to 54%. See [[evaluator-optimizer]].
- **Layers 3–4, blocking checks.** No PR merges with an open code-review or security-review finding. A finding auto-closes if a later commit fixes it, and false positives are closed with a short reason. CI covers lint, types, tests on all platforms and the build. The PR template asks how the change was tested and how to revert it.
- **Layer 5, human approval scaled by risk.** A classifier sets the tier from the *change*, not the author: **low** (docs, copy, internal-only, additive behind a flag) needs no human once automated review and security are green; **medium** (ordinary product changes, caching, the auto-updater, system prompts) needs one person; **high** needs two. Some paths, including CI workflow files and anything owners mark sensitive, always need a person. *"Agent approvals don't count as human approvals."* An approval is good for one commit only. The operator of an agent author always counts as a required reviewer. See [[human-in-the-loop]] and [[earned-autonomy]].
- **Layers 6–7, merge and recover.** A merge queue re-runs checks on main with the change applied. New features ship behind flags, go to employees first, then to the *latest* channel, with *stable* trailing. Flags can be turned off without a deploy. Incident reviews ask which layer *should* have caught the problem. There are no circuit breakers yet that tighten approval when reverts rise. See [[rollback-and-recovery]].
- **Incidents are the eval.** Incident-causing PRs, with expert-confirmed bug locations, form a set that the reviewer is scored against **every day**. Every change to the reviewer's prompts, tools or model is re-scored, and kept only if the score goes up. Noise is measured by how humans handle each comment (fixed, rejected, intentional, didn't matter) and by running the reviewer on known-clean PRs. See [[improvement-loops]].
- **Review must converge.** Agent-authored PRs pay more for each comment than human-authored ones: a human dismisses a nit in a second, but an agent makes another commit and triggers another review. One PR cycled 50+ times overnight. Blame showed ~59% of what the reviewer kept flagging was code from the PR's first pass, so it was finding old bugs a few at a time, not new ones. Fixes: ask the author to re-evaluate the approach after **three cycles**, re-review only the new diff after the first cycles, name the **class** of bug so the author fixes all instances, and don't re-report known issues. Mean reviews to pass fell from 2.08 to 1.32, and PRs needing five or more rounds fell from 8.9% to 1.5% (fig. E). See [[termination]] and [[failure-modes]].
- **What stays human:** whether to build it at all, auditing dangerous code (billing, the auto-updater, CI workflows), architecture, checking proofs, and taking responsibility. *"If you can't describe what the checks would miss, don't ask for a 👍, you need a real review!"*
- **Learning the codebase without reading diffs.** *"No member of the team has a full mental model of Claude Code in their head, nor do we think anyone needs to."* People ask Claude for an explainer, or a small visual artifact, on the exact slice they're about to change. See [[operator-debts]].
- **"You land it, you own it."** This works because changes are small, everything can be reverted, blast radius sets the bar, telemetry and internal use surface regressions fast, and the culture is blameless and open.
- **Where it's going:** in the team's own repos, owners already let some low-risk changes merge automatically when checks pass, *"And this boundary will continue to evolve."* When a reviewer misses something, the team asks *"what wasn't in the model's context"* and turns the answer into a `CLAUDE.md` entry, a skill or a new check. See [[software-factory]].

## Notable quotes
> "We didn't stop doing code review. Instead, we've automated the majority of reading and tuned it to optimize for human time and effort."

> "if these metrics increase, we haven't reduced human time, just relocated it."

> "The review process must converge. It's possible for an agent author and an agent reviewer to cycle forever."

> "Agent approvals don't count as human approvals. Automated review can clear a low-risk change, but it can't stand in for a human when one is required."

> "A person answers for every change that ships, whoever typed it."

## Pages touched
[[layered-code-review]], [[rollback-and-recovery]], [[verification]], [[evaluator-optimizer]], [[termination]], [[failure-modes]], [[human-in-the-loop]], [[earned-autonomy]], [[software-factory]], [[operator-debts]], [[build-the-lever]], [[budgets-and-cost]], [[observability]], [[improvement-loops]], [[stage-gated-pipeline]], [[task-sizing]], [[claude-code]], [[anthropic]], [[addy-osmani]], [[boris-cherny]], [[open-questions]]
