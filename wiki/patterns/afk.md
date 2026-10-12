---
type: pattern
branch: patterns
tags: [loop-engineering, pattern, afk, autonomy]
sources: ["[[src-pocock-ai-coding-dictionary]]", "[[src-pocock-ralph-tips]]", "[[src-pocock-getting-started-with-ralph]]", "[[src-pocock-seven-phases]]", "[[src-tan-pstack-guide-overnight]]"]
created: 2026-10-12
updated: 2026-10-12
status: draft
---
# AFK (away from keyboard)

**AFK** is the working pattern where *"the user kicks off a session and leaves the agent to run unattended"*. It is *"the throughput multiplier of AI coding"* and usually needs a permissive permission mode **plus** a sandbox ([[src-pocock-ai-coding-dictionary]]). It is the opposite of [[human-in-the-loop]] (HITL). Pocock prefers "AFK" to "background agent" because it names what matters: *the user isn't watching*. Up: [[patterns]].

## The characteristic failure
With nobody watching, ambiguity gets resolved by a silent default, and every later decision builds on it: *"hours of finished, confident work built on a wrong call made in the first ten minutes … coherent about the wrong thing"* ([[src-pocock-ai-coding-dictionary]]). See [[failure-modes]].

## Give input before, during and after
From [[src-pocock-ai-coding-dictionary]]:
- **Before:** resolve the ambiguity with grilling and a spec. See [[goal-spec]] and [[seven-phases-of-ai-development]].
- **During:** automated checks and automated review *"stand in for the attention you're not giving."* See [[verification]].
- **After:** end in *"a PR, not changes already merged."* AFK defers human review rather than removing it.

## Graduating to AFK
- Start HITL (`ralph-once.sh`), refine the prompt, then go AFK. *"always cap your iterations"* ([[src-pocock-ralph-tips]], [[src-pocock-getting-started-with-ralph]]). See [[building-a-ralph-loop]].
- AFK suits *"well-specified, low-risk, easy-to-verify"* work. Keep schema migrations and design calls HITL ([[src-pocock-ai-coding-dictionary]]).
- Use small PRD items when AFK, so the agent stays *"on top form when you're not watching"* ([[src-pocock-ralph-tips]]). See [[task-sizing]].
- With research, prototype, PRD and tickets in place, AFK execution *"get[s] excellent results"* ([[src-pocock-seven-phases]]).
- **AX matters most in AFK runs**: *"with no one watching, the environment is the only support the agent gets"* ([[src-pocock-ai-coding-dictionary]]). See [[agent-experience]].

## Tan's version
The **[[overnight-contract]]**: goal, pass/fail finish condition, isolation, pre-answered permissions, decision log and escape hatch. Before any of that, the loop must have earned trust ([[src-tan-pstack-guide-overnight]]). See [[earned-autonomy]].

## Related
[[software-factory]] · [[isolation]] · [[observability]] · [[overnight-contract]]
