---
type: practice
branch: practice
tags: [loop-engineering, practice, omp, goal, loop, hillclimb, advisor]
sources: ["[[src-omp]]"]
created: 2026-10-19
updated: 2026-10-19
status: draft
---
# omp loop surfaces (`/goal`, `/loop`, `/ratchet`, advisor, TTSR, orchestrate)

[[omp]] ships most outer-loop primitives as built-in commands, and the prompts behind them are readable in its repo. This page maps each one to the wiki's anatomy, as [[claude-code-loop]] and [[claude-code-goal]] do for Claude Code ([[src-omp]]). Up: [[practice]].

## Where it sits in the loop
| Surface | Pattern | Anatomy slots |
|---|---|---|
| `/goal`, `/guided-goal` | [[goal-loop]] | [[goal-spec]], [[verification]], [[termination]] |
| `/loop [N\|duration] [--until\|--while '<cmd>']` | [[ralph-loop]] in one session, gated like a [[goal-loop]] | [[trigger]], [[termination]] |
| `/ratchet` | [[improvement-loops]] (eval hill-climb) | [[verification]], [[decision-step]] |
| advisor | [[evaluator-optimizer]], running alongside the agent | [[verification]], [[observation]] |
| TTSR | [[backpressure]] on the output stream | [[action]], [[context-and-state]] |
| `orchestrate`, `/vibe` | [[orchestrator-workers]] | [[decision-step]], [[verification]] |

## `/goal`
All from [[src-omp]]:
- **The loop.** A hidden continuation message (*"Autonomous continuation; objective persists across turns"*) re-prompts the agent after each turn until it calls `goal({op:"complete"})`. The doer grades itself. There is no separate judge in the goal runtime.
- **The completion audit,** required before `complete`:
  1. objective → concrete deliverables
  2. each deliverable → its authoritative evidence
  3. inspect the actual current state
  4. *"Verification scope = claim scope"*
  5. *"Uncertainty = not achieved"*
  6. *"Budget exhaustion ≠ completion"*
- **Budget.** `token_budget` is optional. When it is reached, status becomes `budget-limited` and the agent is steered to wrap up, not to declare done. Time is tracked but not capped. Esc pauses the goal, and the agent must `resume` it before continuing.
- **No goal swapping.** `drop` ends goal mode and removes the tool, so the agent cannot quietly replace its own objective.
- **`/guided-goal`** interviews the user first, one question at a time, ≤6 questions, until five fields are fixed: success criteria, verification, an attempt cap, boundaries, and stop conditions. *(synthesis)* In the runtime code read, the token budget is the only cap the runtime enforces. The attempt cap lives in the objective text, so the model is the one that has to honour it.

## `/loop`
All from [[src-omp]]:
- **Re-submits the prompt after every yield.** Esc suspends the loop, and `/loop` again turns it off.
- **Limits:** a bare integer is an iteration count, and `10m` or `1h30m` is a duration. A token that looks like a limit but doesn't parse is a hard error, so a typo can't silently become prompt text.
- **Conditions:** `--until '<cmd>'` continues while the command fails, and `--while` continues while it succeeds. The condition is re-evaluated before each iteration in its own shell session, so a `cd` inside it can't move the agent's working directory.
- **Exit code 1 is the only "false".** Codes ≥2, such as a syntax error or command not found, halt the loop with an error. *"otherwise a typo'd condition halts the loop looking exactly like finished work."*

*(synthesis)* `/loop --until 'bun test'` is the wiki's "machine-checkable goal" in its most literal form: the stop decision belongs to the test suite, not to any model.

## `/ratchet`
All from [[src-omp]]:
1. **Grill.** One batched question covers the flow, the input source, the goal, what may change, and the stop rule.
2. **Build.** 15–100 cases, both positives and negatives. Use the cheapest grader that works, in order: programmatic, then a pairwise blind judge, then a rubric, then a human. Pre-flight checks: an oracle should score ~100%, a null answer ~0%, and the same output graded twice should get the same grade.
3. **Approve.** Three dialogs: inputs, grader, plan. Each approval is bound to a content hash, so a later edit makes it stale.
4. **Climb, unattended.** Each round:
   - a fresh analyzer reads the *train* traces and proposes **one** diff
   - run the eval
   - `gate()` returns `keep` / `revert` / `rerun`, computed on the **held-out test split**, whose transcripts are never written
5. **Stall → categorize, don't grind.** Classify each failure as artifact gap, grader, harness, structural or variance, and act on the category.
6. **Report.** Tag each change as test delta ± noise, `[REQUIRED]` or `[TUNE]`.

## Advisor
All from [[src-omp]]:
- **Reads every primary turn** (`reviewMode: turn`), including reasoning. It runs on its own model (the `advisor` role, falling back to the `slow` role, not the primary model) and its own context.
- **Read-only by default** (`read`/`grep`/`glob`). `WATCHDOG.yml` can grant more tools, which still go through the session's approval policy.
- **Severities:**
  - `nit`: an aside at the next turn boundary
  - `concern`: may interrupt, and may wake an idle agent
  - `blocker`: interrupts even partial work
- **Noise control:** at most 4 non-blocker notes per update, a dedupe and filler-phrase filter, and a 3-turn cooldown after an interrupting concern. A deliberate user interrupt stops the advisor from auto-resuming the agent.
- **Subagents run unadvised** unless an agent definition opts in.

## TTSR (time-traveling stream rules)
A rule's regex or AST pattern is matched against the streaming output, including thinking, and tool-call content. On a match the stream aborts, the rule is injected as a `<system-interrupt reason="rule_violation">`, and the turn retries. The default is `repeatMode: once`, or `after-gap` (10 turns). Rules written as `question`s are judged after the output completes and cannot interrupt ([[src-omp]]).

## `orchestrate` and `/vibe`
- **`orchestrate`** (a magic keyword). Its rules: never yield before closure, expand every list into todos, dispatch parallel self-contained subagents, *"Subagents NEVER verify"*, and the orchestrator runs the gates once per phase and dispatches fix-ups on red. See [[orchestrator-workers]].
- **`/vibe`.** A read-only director runs persistent `fast` (cheap) and `good` (judgment) workers. *"worker completion means the turn settled, not that its claims are correct."*

All from [[src-omp]].

## Contradictions & open questions
- **Self-graded `/goal` vs separate-judge `/goal`.** See [[goal-loop]] and [[open-questions]].
- **Model-enforced caps.** The attempt cap from `/guided-goal` isn't enforced by the runtime code that was read *(synthesis)*. Compare Pocock's script-level cap ([[src-pocock-getting-started-with-ralph]]).
- **In-session context.** `/goal` and `/loop` continue in one session and rely on compaction, which was not ingested. See [[smart-zone]].

## Related
[[claude-code-loop]] · [[claude-code-goal]] · [[loop-primitives]] · [[omp]]
