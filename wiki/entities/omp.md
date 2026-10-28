---
type: entity
branch: entities
tags: [loop-engineering, product, harness, open-source]
sources: ["[[src-omp]]"]
created: 2026-10-19
updated: 2026-10-19
status: stub
---
# omp (oh-my-pi)

**omp** (`omp.sh`, GitHub `can1357/oh-my-pi`) is an MIT-licensed terminal coding-agent harness by Can Bölük and Stencil Labs. It is a fork of **Pi** (`badlogic/pi-mono`) by Mario Zechner. It has ~36k stars, a native Rust core of ~80k lines, 60+ providers and 31 built-in tools. It runs four ways: an interactive TUI, one-shot `-p`, RPC over stdio, and ACP for editors ([[src-omp]]). Up: [[entities]].

## Why it matters for loops *(synthesis)*
- **It argues that the harness is the variable.** Changing only the edit format lifted 16 models by 15 points on average ([[src-omp]]). See [[action]] and [[agent-experience]].
- **Outer-loop primitives are built in:** `/goal`, `/loop --until`, `/ratchet`, the advisor, stream rules, `orchestrate` and `vibe`. See [[omp-loop-surfaces]].
- **It runs a working factory on itself.** **robomp** is a GitHub triage-and-fix bot that drives `omp --mode rpc` in per-issue worktrees. It has opened 2,773 PRs since 2026-05-14, of which 2,242 were merged. Another account merges them ([[src-omp]]). See [[software-factory]].

## Lineage
- **Pi** by Mario Zechner is the upstream, and Mario Zechner is still a top-3 contributor.
- `/ratchet` is adapted from Anthropic's `claude-api` skill guides for building evals and hill-climbing ([[src-omp]]).
- It reads the rule and config formats of Claude Code, Cursor, Codex, Cline, Copilot and others in place, without migration.

## Contradictions & open questions
- Its benchmarks are vendor-run. The README's *"benchmaxxed"* framing is marketing, and the per-model gains come from one benchmark family ([[src-omp]]).
- Its `/goal` is self-graded, unlike the separate-judge design described for Claude Code and Codex ([[src-osmani-loop-engineering]]). See [[goal-loop]] and [[open-questions]].
- The blog post accuses Anthropic and Google of hostility to third-party harnesses. That is one side's account and was not verified here.

## Related
[[claude-code]] · [[openai-codex]] · [[cursor]] · [[pstack]] · [[ouroboros]] (which supports omp as a runtime)
