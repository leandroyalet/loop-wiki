---
type: pattern
branch: patterns
tags: [loop-engineering, pattern, events]
sources: ["[[src-claude-code-scheduled-tasks]]", "[[src-tan-loops-you-can-trust]]", "[[src-tan-benny-automation]]"]
created: 2026-10-11
updated: 2026-10-12
status: draft
---
# Event-driven loop

An **event-driven loop** wakes up when something happens instead of polling on a schedule. Claude Code documents two mechanisms ([[src-claude-code-scheduled-tasks]]):
- **Channels:** *"your CI can push the failure into the session directly."*
- **Monitor tool:** runs a background script and streams each output line back, which is *"often more token-efficient and responsive than re-running a prompt on an interval."*

Cloud Routines can also fire on GitHub events. Up: [[patterns]].

## Where it sits in the loop
It is an alternative [[trigger]] and a cheaper form of [[observation]].

## Worked example: Slack-triggered maintenance
Tan's **benny** is a pair of Cursor Automations triggered by each new top-level report in a Slack issue channel. A second automation is triggered by the first one's verdict marker in the thread ([[src-tan-loops-you-can-trust]], [[src-tan-benny-automation]]). See [[stage-gated-pipeline]].

## Contradictions & open questions
- There are still no first-party docs for Claude Code Channels in the wiki. See [[open-questions]].

## Related
[[scheduled-loop]] · [[budgets-and-cost]]
