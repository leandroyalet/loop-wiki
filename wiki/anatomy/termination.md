---
type: concept
branch: anatomy
tags: [loop-engineering, anatomy, stop-conditions, safety]
sources: ["[[src-anthropic-building-effective-agents]]", "[[src-claude-code-scheduled-tasks]]", "[[src-osmani-loop-engineering]]", "[[src-huntley-ralph]]", "[[src-pocock-getting-started-with-ralph]]", "[[src-pocock-ralph-tips]]", "[[src-pocock-ralph-plugin]]", "[[src-tan-pstack-guide-overnight]]", "[[src-inside-pstack-report]]", "[[src-agentos-docs]]", "[[src-openprose]]", "[[src-omp]]", "[[src-ouroboros]]", "[[src-osmani-claude-code-code-review]]", "[[src-anthropic-fold-subagents]]"]
created: 2026-10-11
updated: 2026-10-27
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
| Predicate with a floor | Hillclimb's stop predicate sets both a target and a minimum number of attempts (*"≥50% better and ≥10 iterations"*). *"Stop at the predicate. Never relax it."* | [[src-inside-pstack-report]] |
| Budget threshold | Orchestrate *stops spawning* new workers at ~70% of the budget and lets in-flight work land | [[src-inside-pstack-report]] |
| Operator stop | Autopilot-full stands down at once on the operator's stop | [[src-inside-pstack-report]] |
| Round cap → re-scope | The propose ↔ review loop allows up to 5 rounds. *"If the 5th round still isn't implement, the problem is probably wrong — come back to the user and rewrite the pain."* | [[src-agentos-docs]] |
| Outcome channel | each invocation returns `out` (*fulfilled* or *not fulfilled*, with evidence) or `error` (execution failure, with partial work kept). There is no "unknown" channel, because uncertainty goes inside the result. | [[src-openprose]] |
| No end state | a standing responsibility never finishes. Each render is bounded, and the reconciler waits for the next wake: *"The conversation always ends. The responsibility shouldn't have to."* | [[src-openprose]] |
| Token budget | omp `/goal` flips to `budget-limited` at `tokensUsed ≥ tokenBudget`, and the agent is steered to wrap up: *"Budget exhaustion ≠ completion"* | [[src-omp]] |
| Exit-code condition | omp `/loop --until '<cmd>'` / `--while`: exit 1 means false, and ≥2 means the *condition* is broken, so the loop halts with an error | [[src-omp]] |
| Count / duration | omp `/loop 10` or `/loop 1h30m`. A malformed limit is a hard error, not prompt text. | [[src-omp]] |
| Interrupt pauses | Esc pauses an omp goal, which must be explicitly resumed | [[src-omp]] |
| Answer or budget | In Anthropic's single agent loop the run ends when the model answers or hits a turn or cost budget set in the harness. A goal or verifier check *can optionally* run after the answer. | [[src-anthropic-fold-subagents]] |
| Exactly one turn-ending action | robomp must end each bug turn by opening a PR, marking it unable-to-reproduce, or aborting. Otherwise a reminder sends it back. | [[src-omp]] |
| Repair-round cap | robomp's release sentinel allows at most 5 automated repair rounds | [[src-omp]] |
| Spec convergence | Ouroboros evolution stops at ontology similarity ≥ 0.95, at 3 stable generations (stagnation), when generation N ≈ generation N−2 (oscillation), or at a 30-generation cap. These checks apply only after 2 generations. | [[src-ouroboros]] |
| Gated start | `ooo auto` won't execute until the ambiguity score is ≤ 0.2 and the Seed is grade A. *"premature code"* is blocked without explicit `force`. | [[src-ouroboros]] |
| Review-cycle cap → re-think | the Claude Code reviewer asks the author to *re-evaluate the approach* after three cycles, and re-reviews only the new diff after that. Added after one PR cycled 50+ times overnight. | [[src-osmani-claude-code-code-review]] |
| Plan exhausted | Ralph runs out of to-do items, so you regenerate the plan or stop | [[src-huntley-ralph]] |

## Contradictions & open questions
- Huntley's original Ralph has **no built-in stop**: `while :` runs forever by design, and it relies on a human watching ([[src-huntley-ralph]]). Pocock's Ralph adds both a cap and a sigil ([[src-pocock-getting-started-with-ralph]]). See [[ralph-loop]] and [[failure-modes]].
- A self-declared stop like the sigil is *the maker grading itself*. Pocock pairs it with checks that block commits ([[src-pocock-ralph-tips]]). `/goal` uses a separate model instead ([[src-osmani-loop-engineering]]). See [[verification]].
- **Never relax the condition.** *"the finish condition never quietly relaxes to declare victory"*, and *"a duration is not a finish condition"* ([[src-tan-pstack-guide-overnight]]).
- **Cap or pivot?** Pocock caps iterations because *"Infinite loops are dangerous"* ([[src-pocock-ralph-tips]]). Tan's overnight loop treats a plateau as a reason to *pivot, not stop*, and bounds the run only with a time-based escape hatch ([[src-tan-pstack-guide-overnight]]). AgentOS suggests a third reading: hitting the cap is a *diagnosis*. Non-convergence means the goal spec is wrong, so control goes back to the human to rewrite it ([[src-agentos-docs]]).
- **A maker/checker pair needs its own stop.** An agent author and an agent reviewer *"cycle forever"* unless something ends it. The Claude Code team's answer is close to AgentOS's: a cap that triggers a re-think rather than a silent stop ([[src-osmani-claude-code-code-review]], [[src-agentos-docs]]). See [[evaluator-optimizer]].
- Vague scope makes stops unreliable either way: Ralph *"might loop forever … Or … declar[e] victory"* early ([[src-pocock-ralph-tips]]). See [[goal-spec]].
- **Is ending the point?** Every other source bounds the loop. OpenProse's responsibilities bound only each render, and leave the loop open-ended by design ([[src-openprose]]). See [[reconciler-loop]].
- **Stop on what?** Most stops in this table test the *output* (a predicate, tests, a verdict). Ouroboros's main evolution stop tests the *spec*: its data model stopped changing. A QA pass is a separate exit ([[src-ouroboros]]). See [[evolutionary-loop]].
- **Budget-based stops: partly answered.** pstack's Orchestrate stops *spawning* at ~70% of budget ([[src-inside-pstack-report]]). That is a soft drain, not a hard token or dollar kill switch, and the source does not say how the budget is measured. See [[budgets-and-cost]]. *Update (2026-10-19):* omp's `/goal` has a **hard token budget** that changes runtime state, though it ends in a steered wrap-up, not an abrupt kill ([[src-omp]]).
- **The floor sharpens cap vs pivot.** Hillclimb's minimum-attempt floor (≥10 iterations) is the opposite of a cap: it forbids stopping *early*. Autonomous run states *"A plateau is not a stop"* ([[src-inside-pstack-report]]).

## Related
[[failure-modes]] · [[goal-loop]] · [[control]]
