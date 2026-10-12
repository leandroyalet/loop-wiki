---
type: source
branch: sources
tags: [loop-engineering, tan, pstack, verification]
sources: []
url: https://x.com/poteto/status/2094457600259842065
author: Lauren Tan
published: 2026-08-31
raw: raw/2026-10-12-tan-complete-guide-pstack-pt1.md
created: 2026-10-12
updated: 2026-10-12
status: solid
---
# Tan — "The Complete Guide to pstack Pt. 1: Verification is all you need" (X article, 2026-08-31)

**Author:** [[lauren-tan]] · **Raw:** `raw/2026-10-12-tan-complete-guide-pstack-pt1.md` · Up: [[sources]]

## Summary
How to build a **verification skill**, which Tan treats as *"critical infrastructure rather than 'just' a skill."* *"verification means that an agent can verify its own work. It can keep going until it succeeds at its task, because it can now close the loop without you being the bottleneck."* Written while she was gardening the Grok Bot codebase at xAI. She claims 2,000 PRs a month to production; this is self-reported. See [[verification-skill]].

## Key claims
- `/create-verification-skill` generates an app-specific skill with a **control CLI** and a **Feature Map**. Run `/maintain-verification-skill` daily.
- **Choose a debuggable stack.** *"The harder your tech stack is to debug and control, the more difficult it will be to use agents productively."* She would even choose a different stack for it. See [[agent-experience]].
- **Build the lever:** prefer tools to markdown. An agent-friendly CLI is composable (deep modules), has `--dry-run` on destructive commands, uses subcommands for progressive disclosure, gives descriptive errors and rich `--help`, and outputs JSON. See [[build-the-lever]].
- **Repeatable dev setup:** seeded DB, test users and auth, one command to bring the environment up.
- **Cloud agents instead of worktrees:** *"I would recommend against"* worktrees for parallelism. They cost disk and resources (*"up to 10 agents"*), while cloud agents get a real computer, and a snapshot makes later runs start fast. See [[isolation]].
- **The Feature Map is "materialized memory":** a searchable index of features and how to reach them. *"I think your codebase is the ultimate form of memory."* See [[context-and-state]].
- **Bots as coordinators:** tell the bot to *spawn a cloud agent* so its own context stays clean. See [[orchestrator-workers]].
- **`/swarm` with the verification skill:** fan out cloud agents to confirm a perf win with enough samples, or to fuzz for regressions.
- **The verification skill enables automation:** with a good verification skill and Feature Map, routines and automations can auto-reproduce, and even auto-fix, Slack reports. See [[stage-gated-pipeline]].
- *"Volume does matter"* once quality is maintained, which reverses her earlier view that PR counts were a vanity metric.

## Pages touched
[[verification-skill]], [[build-the-lever]], [[isolation]], [[context-and-state]], [[orchestrator-workers]], [[agent-experience]], [[stage-gated-pipeline]], [[operator-debts]], [[lauren-tan]], [[pstack]]
