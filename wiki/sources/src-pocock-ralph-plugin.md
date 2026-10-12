---
type: source
branch: sources
tags: [loop-engineering, pocock, ralph, context]
sources: []
url: https://www.aihero.dev/why-the-anthropic-ralph-plugin-sucks
author: Matt Pocock
published: 2026-01-22
raw: raw/2026-10-12-pocock-ralph-plugin.md
created: 2026-10-12
updated: 2026-10-12
status: solid
---
# Pocock — "Why the Anthropic Ralph plugin sucks (use a bash loop instead)" (2026-01-22)

**Author:** [[matt-pocock]] · **Raw:** `raw/2026-10-12-pocock-ralph-plugin.md` · Up: [[sources]]

## Summary
Anthropic shipped an official Ralph plugin for Claude Code (`/ralph-loop "…" --completion-promise "COMPLETE" --max-iterations 50`). It loops **inside one session**, using a stop hook that intercepts exit attempts and feeds the prompt back in. Pocock argues this defeats Ralph's whole point: **a fresh context window per iteration** keeps the model in the [[smart-zone]].

## Key claims
- Token relationships scale quadratically, so models have a **smart zone** (about the first 40% of context) and a **dumb zone** (the last 60%). *"Most people debate exactly where this boundary is, but everyone agrees the boundary exists."*
- A bash loop restarts Claude with an empty context each time: the PRD and progress go in, one task gets done, and the process exits. *"The context window never fills up with cruft."*
- The plugin accumulates history. Context is about 20% full after iteration 1, 35% after 2, and 50% after 3, which is the dumb zone. *"the plugin guarantees that you're going to fill up the smart zone."*
- *"Ralph works because it's ruthlessly simple. Keep it that way."*

## Contradictions
- The threshold differs from Pocock's own dictionary, which puts the dumb zone at about 125K–150K tokens ([[src-pocock-ai-coding-dictionary]]). See [[smart-zone]].
- (synthesis) The same critique may apply to any **in-session** loop, such as Claude Code's self-paced `/loop` or `/goal` ([[src-claude-code-scheduled-tasks]], [[src-osmani-loop-engineering]]). See [[claude-code-loop]] and [[open-questions]].

## Pages touched
[[smart-zone]], [[ralph-loop]], [[context-and-state]], [[claude-code-loop]], [[claude-code-goal]], [[failure-modes]], [[anthropic]], [[open-questions]]
