---
type: pattern
branch: patterns
tags: [loop-engineering, pattern, ralph, outer-loop]
sources: ["[[src-huntley-ralph]]", "[[src-pocock-getting-started-with-ralph]]", "[[src-pocock-ralph-tips]]", "[[src-pocock-ralph-plugin]]"]
created: 2026-10-11
updated: 2026-10-12
status: draft
---
# Ralph loop

**Ralph** is [[geoffrey-huntley]]'s technique. *"In its purest form, Ralph is a Bash loop"* that feeds the same prompt to a coding agent forever ([[src-huntley-ralph]]):

```bash
while :; do cat PROMPT.md | claude-code ; done
```

It is *"deterministically bad in an undeterministic world"*. Its failures are predictable enough to fix by tuning the prompt. It is the pre-2026 ancestor of loop engineering. Up: [[patterns]].

## Anatomy choices
| Slot | Ralph's choice |
|---|---|
| [[trigger]] | Immediate re-run as soon as the last run ends |
| [[goal-spec]] | Spec files + `fix_plan.md`, loaded every loop |
| [[context-and-state]] | Plan, specs and `AGENT.md` on disk. The main context acts as a scheduler. |
| [[decision-step]] | *"choose the most important thing"* from the plan |
| [[action]] | **One item per loop**, with subagents for search and writes |
| [[verification]] | [[backpressure]]: the unit's tests, type checker, static analysis. Only one subagent runs build and test. |
| [[termination]] | None built in. A human watches the stream and intervenes. Pocock's variant adds an iteration cap plus a `<promise>COMPLETE</promise>` sigil ([[src-pocock-getting-started-with-ralph]]). |

## Operating it
- **Two modes:** a *planning* prompt regenerates `fix_plan.md` by comparing the code against the specs, and a *building* prompt works through it. The human throws out the plan often and regenerates it.
- **Tune with signs:** each observed bad behaviour gets an instruction, like a sign next to the slide reading *"SLIDE DOWN, DON'T JUMP"*. See [[writing-a-loop-prompt]].
- **Expect breakage:** *"you'll wake up to a broken codebase."* Choose between `git reset --hard` and rescue prompts.
- **Commit on green:** update the plan, commit, push, and tag when the build and tests pass.

## Pocock's variant (2026)
[[matt-pocock]] turned Ralph into a reusable recipe. Details are in [[building-a-ralph-loop]].
- **HITL → AFK:** a `ralph-once.sh` you watch, then a capped `afk-ralph.sh N` in a Docker sandbox ([[src-pocock-getting-started-with-ralph]]).
- **State:** a PRD (optionally JSON with `passes` flags) plus `progress.txt` plus one commit per feature ([[src-pocock-ralph-tips]]).
- **Why it works:** *"Each iteration of Ralph uses a fresh context window"*, keeping the model in the [[smart-zone]] ([[src-pocock-ralph-plugin]]).
- **Beyond features:** coverage, lint, duplication and entropy loops ([[src-pocock-ralph-tips]]). See [[improvement-loops]].

## Where it fits
It is best for **greenfield** work and gets you about 90% of the way. *"There's no way in heck would I use Ralph in an existing code base"* ([[src-huntley-ralph]]).

## Contradictions & open questions
- **Monolithic vs multi-agent.** Huntley rejects agent-to-agent multiplexing (*"a red hot mess"*) yet uses hundreds of subagents as context offloaders. [[src-osmani-loop-engineering]] treats sub-agents as a core primitive. Both agree on subagents as workers. The disagreement is about peer agents that coordinate with each other.
- **Existing codebases.** Osmani's flagship example runs daily on an existing repo ([[src-osmani-loop-engineering]]). Huntley would not use Ralph there. Pocock ran it on his own existing projects, AI Hero CLI tests and course-video-manager features, and warns that *"the repo wins"*, so clean up first ([[src-pocock-ralph-tips]]). See [[agent-experience]].
- **Bash loop vs in-session plugin.** Anthropic's official Ralph plugin loops inside one session via a stop hook. Pocock says this *"guarantees"* a slide into the dumb zone, and recommends the bash loop ([[src-pocock-ralph-plugin]]).
- **Maintainability.** Huntley asks *"by whom?"* and argues loops can fix what loops break. Osmani warns of comprehension debt. See [[operator-debts]].

## Related
[[failure-modes]] · [[loop-pattern-comparison]]
