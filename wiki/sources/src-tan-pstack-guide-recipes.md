---
type: source
branch: sources
tags: [loop-engineering, tan, pstack, recipes, guide]
sources: []
url: https://github.com/cursor/plugins/blob/997ffc7fe26b/pstack/docs/guide/10-recipes-and-pitfalls.md
author: Lauren Tan
published: unknown (repo HEAD 2026-10-12)
raw: raw/2026-10-12-tan-pstack-guide-recipes.md
created: 2026-10-12
updated: 2026-10-12
status: solid
---
# pstack guide 10 — "Recipes and pitfalls"

**Author:** [[lauren-tan]] · **Raw:** `raw/2026-10-12-tan-pstack-guide-recipes.md` · Up: [[sources]]

## Summary
Prompts worth copying, *"deliberately informal"*, and a list of pitfalls. The most loop-relevant recipe is the short overnight form: *"im going to bed, keep going autonomously until every fixture passes. do not stop. keep a decision log i can audit in the morning."* See [[overnight-contract]].

## Key claims
- **Steering prompts are one line,** for example *"apply prove it works. show me the real output, not the build log."* See [[writing-a-loop-prompt]].
- **Fix bugs through a failing test only if it's cheap:** *"Forcing a test through brittle mocks proves less than running the real command."* See [[backpressure]].
- **`/correct`** lands a repeated correction as architecture, a type, a lint or a test, *"so the next agent can't make the mistake."* See [[build-the-lever]].
- **`/swarm`** partitions work into slices and returns one `PASS`, `ISSUES` or `BLOCKED` report instead of raw worker dumps. See [[orchestrator-workers]].
- **Pitfalls relevant to loops:**
  - a vague finish condition (*"gives /loop nothing to check"*)
  - **looping before you trust the loop** (*"only makes unchecked work faster"*)
  - parallel agents in one worktree
  - reporting success off a green build
  - trusting an unvetted number
  - correcting the same mistake by hand
  - listing skills in the prompt
  - leading with your theory of the cause
  - accepting every review comment

  See [[failure-modes]].

## Pages touched
[[overnight-contract]], [[writing-a-loop-prompt]], [[failure-modes]], [[backpressure]], [[build-the-lever]], [[orchestrator-workers]]
