---
type: practice
branch: practice
tags: [loop-engineering, practice, scope, tracer-bullets, tdd]
sources: ["[[src-pocock-ralph-tips]]", "[[src-pocock-tracer-bullets]]", "[[src-pocock-tdd-skill]]", "[[src-huntley-ralph]]", "[[src-pocock-ai-coding-dictionary]]", "[[src-tan-pstack-loop-principles]]", "[[src-tan-loops-you-can-trust]]", "[[src-tan-pstack-guide-verify-and-ship]]", "[[src-agentos-docs]]", "[[src-osmani-claude-code-code-review]]"]
created: 2026-10-12
updated: 2026-10-27
status: draft
---
# Task sizing (one thing per iteration)

How much work belongs in one loop iteration. Every source converges on **small**. Huntley: *"One item per loop. I need to repeat myself here—one item per loop"* ([[src-huntley-ralph]]). Pocock: *"The rate at which you can get feedback is your speed limit. Never outrun your headlights"* ([[src-pocock-ralph-tips]]). Up: [[practice]].

## Why small
- **Feedback frequency:** less work happens before the next check. See [[backpressure]].
- **Context:** a smaller task stays in the [[smart-zone]]. *"Doing one task per session gives each task the sharpest part of the session"* ([[src-pocock-ai-coding-dictionary]]).
- **Honesty:** small vertical steps prevent faked tests and slop ([[src-pocock-tdd-skill]], [[src-pocock-tracer-bullets]]).

## The trade-off
Each iteration has startup costs: picking a task, exploring the repo, gathering context. *"you don't want Ralph renaming one variable per iteration."* Larger tasks mean less frequent feedback and lower quality. Smaller tasks mean higher quality but slower progress. Bias small, especially AFK ([[src-pocock-ralph-tips]]).

## Techniques
- **Tracer bullets:** build *"a tiny, end-to-end slice"* through all the layers first, get feedback, then expand in a fresh context ([[src-pocock-tracer-bullets]]).
- **Vertical TDD:** *"ONE test → ONE implementation → repeat"*. Bulk tests *"test imagined behavior, not observed behavior"* ([[src-pocock-tdd-skill]]).
- **Risk first:** architecture, integration points and unknown unknowns get high priority. Polish and quick wins come last. Without guidance, Ralph picks *"the first item in the list or whatever seems easiest"* ([[src-pocock-ralph-tips]]). See [[decision-step]].
- **Sequence verifiable units (Tan):** each unit is *"known-good state, one change, run the check, then proceed."* Order delivery so it proves itself, for example failing test first and then the fix ([[src-tan-pstack-loop-principles]]). *"Five narrow PRs beat one fat one"* ([[src-tan-pstack-guide-verify-and-ship]]).
- **Catch defects at the lowest-value stage:** after a ~400K-line migration PR, Tan's loop now migrates one component per day ([[src-tan-loops-you-can-trust]]).
- **Small changes are cheap to undo.** The Claude Code team's "you land it, you own it" rule relies on *"Small changes that are easy to review, debug, and revert"* ([[src-osmani-claude-code-code-review]]). See [[rollback-and-recovery]].
- **Prompt guidance:** one logical change per commit, split oversized tasks, and run checks after each change, not at the end ([[src-pocock-ralph-tips]]).

## Contradictions & open questions
- Huntley's later CURSED prompt asks for *"the most important 10 things"* per loop. He allows relaxing "one item" as a project matures, *"but if it starts going off the rails … narrow it down to just one item"* ([[src-huntley-ralph]]).

- **Audacious refactors.** [[agentos]]'s laws say *"Blast radius is not a cost — stale architecture is"*. They prefer *"the hardest, most audacious appropriate refactor"* that removes a root-cause inconsistency over *"Small safe patches"*. The justification is that pre-launch code has no users or migrations ([[src-agentos-docs]]). This cuts against every source above. *(synthesis)* The disagreement may be about **change** size, not **iteration** size: a large change can still be delivered as small, verified units (compare Tan's migrate-callers-then-delete in one wave).

## Related
[[action]] · [[writing-a-loop-prompt]] · [[building-a-ralph-loop]]
