---
type: concept
branch: anatomy
tags: [loop-engineering, anatomy, stop-conditions, safety]
sources: ["[[src-anthropic-building-effective-agents]]", "[[src-claude-code-scheduled-tasks]]", "[[src-osmani-loop-engineering]]", "[[src-huntley-ralph]]", "[[src-pocock-getting-started-with-ralph]]", "[[src-pocock-ralph-tips]]", "[[src-pocock-ralph-plugin]]", "[[src-tan-pstack-guide-overnight]]"]
created: 2026-10-11
updated: 2026-10-12
status: solid
---
# Termination

**Termination** decides whether to stop or go round again. Agents usually end on completion, *"but it's also common to include stopping conditions (such as a maximum number of iterations) to maintain control"* ([[src-anthropic-building-effective-agents]]). Up: [[anatomy]].

## Where it sits in the loop
It is the last step of each iteration and reads the result of [[verification]] against the [[goal-spec]].

## Stop conditions, by kind
| Kind | Example | Source |
|---|---|---|
| Goal reached | `/goal` condition judged true by a separate model | [[src-osmani-loop-engineering]] |
| Iteration cap | max N turns | [[src-anthropic-building-effective-agents]] |
| Iteration cap (Ralph) | `afk-ralph.sh 20` caps the outer loop. *"Infinite loops are dangerous with stochastic systems"*. 5–10 for small jobs, 30–50 for large ones. | [[src-pocock-getting-started-with-ralph]], [[src-pocock-ralph-tips]] |
| Completion sigil | the agent prints `<promise>COMPLETE</promise>` when the PRD is done, and the script greps for it and exits. The Anthropic Ralph plugin has the same thing as `--completion-promise` plus `--max-iterations`. | [[src-pocock-getting-started-with-ralph]], [[src-pocock-ralph-plugin]] |
| Time-to-live | recurring Claude Code tasks expire after **7 days**, which *"bounds how long a forgotten loop can run"* | [[src-claude-code-scheduled-tasks]] |
| Self-stop | a self-paced loop calls `ScheduleWakeup(stop: true)` | [[src-claude-code-scheduled-tasks]] |
| Fail-safe | an iteration that neither reschedules nor stops gets one fallback wakeup about 20 min later, then ends | [[src-claude-code-scheduled-tasks]] |
| Human | `Esc`, `CronDelete`, `git reset --hard` and restart | [[src-claude-code-scheduled-tasks]], [[src-huntley-ralph]] |
| Escape hatch | *"if you're truly stuck after a few hours, stop and write up why"*. It *"beats eight hours of creative goal reinterpretation"* | [[src-tan-pstack-guide-overnight]] |
| Pause safely | finish or back out of the step, commit a WIP checkpoint, write a resume note | [[src-tan-pstack-guide-overnight]] |
| Plan exhausted | Ralph runs out of to-do items, so you regenerate the plan or stop | [[src-huntley-ralph]] |

## Contradictions & open questions
- Huntley's original Ralph has **no built-in stop**: `while :` runs forever by design, and it relies on a human watching ([[src-huntley-ralph]]). Pocock's Ralph adds both a cap and a sigil ([[src-pocock-getting-started-with-ralph]]). See [[ralph-loop]] and [[failure-modes]].
- A self-declared stop like the sigil is *the maker grading itself*. Pocock pairs it with checks that block commits ([[src-pocock-ralph-tips]]). `/goal` uses a separate model instead ([[src-osmani-loop-engineering]]). See [[verification]].
- **Never relax the condition.** *"the finish condition never quietly relaxes to declare victory"*, and *"a duration is not a finish condition"* ([[src-tan-pstack-guide-overnight]]).
- **Cap or pivot?** Pocock caps iterations because *"Infinite loops are dangerous"* ([[src-pocock-ralph-tips]]). Tan's overnight loop treats a plateau as a reason to *pivot, not stop*, and bounds the run only with a time-based escape hatch ([[src-tan-pstack-guide-overnight]]).
- Vague scope makes stops unreliable either way: Ralph *"might loop forever … Or … declar[e] victory"* early ([[src-pocock-ralph-tips]]). See [[goal-spec]].
- The wiki has no source yet on **budget-based** stops, such as a hard token or dollar limit. See [[budgets-and-cost]].

## Related
[[failure-modes]] · [[goal-loop]] · [[control]]
