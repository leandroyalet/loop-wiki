---
type: source
branch: sources
tags: [loop-engineering, primary, naming]
sources: []
url: https://addyosmani.com/blog/loop-engineering/
author: Addy Osmani
published: 2026-06-07
raw: raw/2026-10-11-osmani-loop-engineering.md
created: 2026-10-11
updated: 2026-10-11
status: solid
---
# Osmani — "Loop Engineering" (2026-06-07)

**Author:** [[addy-osmani]] · **Raw:** `raw/2026-10-11-osmani-loop-engineering.md` · Up: [[sources]]

## Summary
This is the essay that gave **loop engineering** its name. Osmani defines it as *"replacing yourself as the person who prompts the agent. You design the system that does it instead."* He frames a loop as *"a recursive goal where you define a purpose and the AI iterates until complete."* The essay was prompted by quotes from [[peter-steinberger]] ("design loops that prompt your agents") and [[boris-cherny]] ("My job is to write loops"). The author is openly skeptical and repeatedly warns about token cost.

## Key claims
- A loop is a small system that **finds the work, hands it out, checks it, writes down what is done, and decides the next thing**. See [[loop-engineering]].
- Loop engineering sits **"one floor above"** agent harness engineering: *"The harness but it runs on a timer, it spawns little helpers, and it feeds itself."* See [[loop-vs-prompt-engineering]].
- The building blocks have stopped being DIY bash and now ship in both [[claude-code]] and [[openai-codex]]. Design the loop to be tool-agnostic. See [[loop-primitives]].
- **Five primitives plus memory:** automations, worktrees, skills, plugins/connectors, sub-agents, and then state. See [[loop-primitives]].
- **Memory belongs on disk:** *"The agent forgets, the repo doesnt."* See [[context-and-state]].
- `/loop` re-runs on a cadence, while `/goal` runs until a written condition is true and is checked by a separate small model. See [[goal-loop]] and [[claude-code-goal]].
- **Maker/checker split** is *"the most useful structural thing in a loop, by far."* A verifier you trust is the only reason you can walk away. See [[verification]] and [[evaluator-optimizer]].
- **Worktrees** remove mechanical collisions, but your review bandwidth is the ceiling ("orchestration tax"). See [[isolation]].
- Example shape: a morning triage automation feeds isolated sub-agent fixes and a reviewer sub-agent, then opens a PR via connectors. A state file is the spine. See [[scheduled-loop]].
- **Three problems get sharper as loops get better:** verification is still on you, comprehension debt, and cognitive surrender. See [[operator-debts]].

## Notable quotes
> "Loop engineering is replacing yourself as the person who prompts the agent."
> "'done' is a claim and not a proof."
> "That's what makes loop design harder than prompt engineering, not easier. … the leverage point moved."

## Pages touched
[[loop-engineering]], [[loop-primitives]], [[context-and-state]], [[verification]], [[termination]], [[trigger]], [[goal-loop]], [[scheduled-loop]], [[evaluator-optimizer]], [[orchestrator-workers]], [[isolation]], [[budgets-and-cost]], [[operator-debts]], [[failure-modes]], [[claude-code-goal]], [[openai-codex]], [[addy-osmani]], [[loop-vs-prompt-engineering]]
