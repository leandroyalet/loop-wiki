---
type: entity
branch: entities
tags: [loop-engineering, product, cursor]
sources: ["[[src-tan-pstack-guide-overnight]]", "[[src-tan-loops-you-can-trust]]", "[[src-tan-complete-guide-pstack-pt1]]", "[[src-tan-benny-automation]]", "[[src-tns-loop-engineering]]"]
created: 2026-10-12
updated: 2026-10-12
status: stub
---
# Cursor

An AI code editor and agent platform. TNS noted in June 2026 that it orchestrates agents but had not *"named a loop as its unit of work"* ([[src-tns-loop-engineering]]). Tan's pstack material documents its loop surfaces. Up: [[entities]].

## Loop surfaces
From Tan's sources:
- **`/loop`:** Cursor's built-in wake mechanism. It re-checks a finish condition *"on events or a heartbeat"* ([[src-tan-pstack-guide-overnight]]). See [[overnight-contract]].
- **Automations** (launched March 2026): cloud agents that run on a schedule or on events such as new Slack messages ([[src-tan-loops-you-can-trust]], [[src-tan-how-i-use-cursor]]). See [[stage-gated-pipeline]].
- **Cloud agents and cloud subagents:** each gets its own VM and branch, can run the app and record video, and starts fast from a snapshot ([[src-tan-complete-guide-pstack-pt1]]). See [[isolation]].
- **Projects:** a persistent coordinator thread directing cloud subagents ([[src-tan-pstack-guide-overnight]]). See [[orchestrator-workers]].
- **Custom Modes:** pin a skill such as `/poteto-mode` to every turn ([[src-tan-complete-guide-pstack-pt1]]).
- **Plugins:** enabled per repo in `.cursor/settings.json` ([[src-tan-benny-automation]]).

## Contradictions & open questions
- Only Tan's sources are ingested, and she worked at Cursor. There are no Cursor docs yet. See [[open-questions]].

## Related
[[pstack]] · [[claude-code]] · [[openai-codex]] · [[loop-primitives]]
