---
type: source
branch: sources
tags: [loop-engineering, tan, pstack, depth-first]
sources: []
url: https://x.com/poteto/status/2058975157503570132
author: Lauren Tan
published: 2026-05-25
raw: raw/2026-10-12-tan-how-i-use-cursor.md
created: 2026-10-12
updated: 2026-10-12
status: solid
---
# Tan — "How I Use Cursor" (X article, 2026-05-25)

**Author:** [[lauren-tan]] · **Raw:** `raw/2026-10-12-tan-how-i-use-cursor.md` · Up: [[sources]]

## Summary
The launch post for pstack, written after Tan moved from Meta (a Claude Code user) to Cursor. Her thesis: orchestration tools built around CLIs *"just makes you, the human, the orchestrator"*. The real goal is **building trust in agents**, which means going **depth-first** (rigor) before breadth-first (parallelism). *"The bottleneck with agents is verification."*

## Key claims
- Agents are *"new hires in a constant state of amnesia and idiocy … capable yet stupid, and very teachable."* Treat each failure mode as something to teach. See [[build-the-lever]].
- *"Naive parallelization just makes them write slop faster."* *"Trying to parallelize agents you don't trust yet is a huge waste of tokens."* See [[earned-autonomy]].
- `/poteto-mode` is a higher-order skill that picks a playbook. The goal is *"maximum impact with the least amount of code."* Debugging works by binary search over hypotheses. See [[pstack]].
- Multi-model work, such as adversarial review by different models (`/interrogate`), and *"agent orchestration, but applied depth first."* See [[evaluator-optimizer]].
- *"When you can get there, true agent parallelism, like in a dark factory for software, might be possible."* See [[software-factory]].
- **Benny** is a maintenance factory: triage with Slack, git history and Notion (*"is it a bug, or was it designed to work this way?"*), then repro through computer use in a cloud Cursor, then fix, then subplanner verification workers, then a before/after video in the PR. See [[stage-gated-pipeline]].
- *"the key for building your own software factory is trust. Unless you can trust an agent to own a problem end-to-end, including verification, you cannot automate your processes."*
- On compaction (anecdotal): it took *"many minutes"* in Claude Code, and the model felt *"super dumb after compaction"*, while in Cursor it was fast. See [[smart-zone]].

## Pages touched
[[earned-autonomy]], [[software-factory]], [[stage-gated-pipeline]], [[evaluator-optimizer]], [[smart-zone]], [[build-the-lever]], [[pstack]], [[lauren-tan]], [[cursor]]
