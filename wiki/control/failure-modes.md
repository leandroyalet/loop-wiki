---
type: concept
branch: control
tags: [loop-engineering, control, failure-modes]
sources: ["[[src-huntley-ralph]]", "[[src-osmani-loop-engineering]]", "[[src-anthropic-building-effective-agents]]", "[[src-claude-code-scheduled-tasks]]", "[[src-pocock-ralph-tips]]", "[[src-pocock-ai-coding-dictionary]]", "[[src-pocock-ralph-plugin]]", "[[src-pocock-tdd-skill]]", "[[src-pocock-tracer-bullets]]", "[[src-pocock-triage-skill]]", "[[src-tan-pstack-guide-overnight]]", "[[src-tan-pstack-guide-recipes]]", "[[src-tan-pstack-guide-verify-and-ship]]", "[[src-tan-loops-you-can-trust]]", "[[src-inside-pstack-report]]", "[[src-omp]]", "[[src-ouroboros]]", "[[src-osmani-claude-code-code-review]]", "[[src-anthropic-fold-subagents]]"]
created: 2026-10-11
updated: 2026-10-27
status: draft
---
# Failure modes

These are the ways loops go wrong. The human-side failures are on [[operator-debts]]. Up: [[control]].

| Failure | What happens | Mitigation | Source |
|---|---|---|---|
| **Compounding errors** | Mistakes feed the next step unattended | Ground truth each step, sandboxes, guardrails | [[src-anthropic-building-effective-agents]] |
| **Placeholder cheating** | The model writes minimal or stub code because *"the reward function is compiling code"* | Explicit "no placeholders" signs, and more loops that hunt for placeholders | [[src-huntley-ralph]] |
| **False "not implemented"** | Non-deterministic code search wrongly concludes a feature is missing, which leads to duplicate implementations | *"don't assume not implemented"*, search with subagents first | [[src-huntley-ralph]] |
| **Context bloat** | The window fills and quality drops | One item per loop, offload to subagents | [[src-huntley-ralph]] |
| **Broken build overnight** | You wake up to a codebase that won't compile | Reset or rescue prompts. Commit only when green. | [[src-huntley-ralph]] |
| **Plan drift** | The to-do list goes stale or off track | Regenerate the plan often | [[src-huntley-ralph]] |
| **Bad spec** | The loop faithfully builds the wrong thing | Review specs. Blame the operator, not the tool. | [[src-huntley-ralph]] |
| **Self-grading** | The maker approves its own work | A separate checker agent | [[src-osmani-loop-engineering]] |
| **Forgotten loop** | A recurring task runs indefinitely | 7-day expiry, plus a fallback end for silent self-paced loops | [[src-claude-code-scheduled-tasks]] |
| **Parallel collisions** | Agents overwrite each other's files | Worktrees. See [[isolation]]. | [[src-osmani-loop-engineering]] |
| **Validation stampede** | Many parallel build and test runs | Only one subagent validates | [[src-huntley-ralph]] |
| **Cost blow-up** | The token spend surprises you | See [[budgets-and-cost]] | [[src-osmani-loop-engineering]] |
| **Premature victory** | Declares "done" after silently narrowing scope (it skipped "internal" commands) | Explicit files, stop condition and edge cases | [[src-pocock-ralph-tips]] |
| **Endless improvement** | A vague goal ("improve this codebase") means it may loop forever | Concrete scope plus an iteration cap | [[src-pocock-ralph-tips]] |
| **Early wrong call (AFK)** | *"hours of finished, confident work built on a wrong call made in the first ten minutes"* | Resolve ambiguity beforehand. End in a PR. | [[src-pocock-ai-coding-dictionary]] |
| **Dumb-zone drift** | Quality decays as one session accumulates iterations | A fresh process per iteration. See [[smart-zone]]. | [[src-pocock-ralph-plugin]] |
| **Fake tests** | Bulk tests of imagined behaviour, mocked internals, tests rewritten to pass | Vertical red-green TDD | [[src-pocock-tdd-skill]] |
| **Slop / outrunning headlights** | Whole layers built before anything is validated | Tracer bullets. See [[task-sizing]]. | [[src-pocock-tracer-bullets]] |
| **Entropy amplification** | The agent copies bad patterns, compounded by dozens of commits | Clean first, enforce with checks. See [[agent-experience]]. | [[src-pocock-ralph-tips]] |
| **Flaky checks** | The agent "fixes" good code or retries past real failures | Keep checks deterministic | [[src-pocock-ai-coding-dictionary]] |
| **Destructive git in the sandbox** | `reset --hard` or `push --force` inside the mounted repo | `PreToolUse` hook guardrail. See [[guardrails-and-permissions]]. | [[src-pocock-git-guardrails-hook]] |
| **Stale queue** | AFK runners take blocked tickets, or re-queue finished ones | Explicit `blocked` / `implemented` states (not yet shipped in the triage skill) | [[src-pocock-triage-skill]] |
| **Goal reinterpretation** | Hours of *"creative goal reinterpretation"*, or quietly relaxing the finish condition | A pass/fail predicate that never relaxes, plus an escape hatch that writes up why it stopped | [[src-tan-pstack-guide-overnight]] |
| **Motion without result** | A duration given as the goal ("work 4 hours") | A predicate, not a duration | [[src-tan-pstack-guide-overnight]] |
| **Riding regressions** | Changes that didn't help stay in | Commit or discard every iteration | [[src-tan-pstack-guide-overnight]] |
| **Green-build success** | "It compiles" reported as done | Prove it works on the real artifact | [[src-tan-pstack-guide-verify-and-ship]] |
| **Fake speedups** | Warm cache, debug build, or work outside the timed region | Seven-question benchmark checklist | [[src-tan-pstack-guide-verify-and-ship]] |
| **Untrusted parallelism** | More agents, more unchecked work: *"Parallelization just gave me more to review and discard"* | Earn trust first. See [[earned-autonomy]]. | [[src-tan-loops-you-can-trust]] |
| **Big-bang changes** | A ~400K-line migration PR hides z-index and specificity bugs that dogfooding finds later | One unit per run. Catch defects at the lowest-value stage. | [[src-tan-loops-you-can-trust]] |
| **Anchored search** | A theory of the cause given up front narrows the search | Ask for a restatement first | [[src-tan-pstack-guide-recipes]] |
| **Stale verdict** | A chain rebase moves every PR to a new SHA *"without failing any check"*, so an old verdict silently covers new code | Key verdicts to the head SHA, re-check with `git patch-id` | [[src-inside-pstack-report]] |
| **Dropped directives** | *"Interrupt-chained resumes silently drop directives"* | A fresh subagent with a consolidated brief | [[src-inside-pstack-report]] |
| **Gaming the gate** | A worker passes by weakening the check | *"reset and harden the contract"*, and fix a wrong gate in its own change | [[src-inside-pstack-report]] |
| **Too-easy pass** | The observation method is broken, not the system fixed | Suspect the measurement first | [[src-inside-pstack-report]] |
| **Vague brief** | Parallel workers *"fail quietly"* because they can't ask | Pilot one unit to falsify the brief before scaling | [[src-inside-pstack-report]] |
| **Blocked on a human** | A watcher waits forever on an approval gate | Report the gate as a typed state and move on | [[src-inside-pstack-report]] |
| **Shallow evidence** | A bulk triage pass relies on a cheap listing without comments | Require full context per item | [[src-pocock-triage-skill]] |
| **Typo'd stop condition** | A broken condition command reads as "false" and *"halts the loop looking exactly like finished work"* | Treat exit codes ≥2 as errors, not as false | [[src-omp]] |
| **Budget-out "done"** | The agent marks a goal complete because tokens are running out | *"Budget exhaustion ≠ completion"*: a budget-limited state that forbids `complete` | [[src-omp]] |
| **Shrunk objective** | Success is redefined as a smaller or already-done subset | *"NEVER redefine success"*. The goal can't be dropped and replaced. | [[src-omp]] |
| **Announce-and-stop** | The model says it will continue, then ends the turn | An automatic retry nudge (*"MUST call the next concrete tool now"*) with an attempt counter | [[src-omp]] |
| **Push loop** | The bot retries the same rejected push forever | Two identical rejections → fix, a justified bypass, or escalate | [[src-omp]] |
| **Edit-format failure** | Capable models fail on mechanical edit errors, which hides their real coding ability: *"You're blaming the pilot for the landing gear"* | An edit format anchored on content hashes (hashline) that rejects stale edits | [[src-omp]] |
| **Noisy reviewer** | A checker floods the doer with repeats and filler | Dedupe, a filler filter, per-update budgets, an interrupt cooldown | [[src-omp]] |
| **Safe-but-wrong output** | A locally safe, verifiable artifact that *"changes a material user-stated requirement"*, such as docs instead of a tool, or missing data reported as `OK`. *"worse than a clear blocker because it creates false confidence."* | Check the artifact class against the original contract. Block, ask, or regenerate the Seed. | [[src-ouroboros]] |
| **Model-granted acceptance** | An LLM verdict approves work that no executed check verified (Ouroboros #2449) | Models may only withhold. Without an executed check the result is `unverified`. | [[src-ouroboros]] |
| **Can't-fail check** | Something like `pytest --version` is recorded as verification evidence (open #2562) | Require checks that could actually fail | [[src-ouroboros]] |
| **Answer-key leak** | The worker sees the grading command or assertion and optimises for it | Hide the grader inputs from every worker-facing surface | [[src-ouroboros]] |
| **Non-converging review** | An agent author and an agent reviewer cycle 50+ times overnight; the reviewer finds a few more *old* bugs each round (~59% of flags were first-pass code) | Re-think after three cycles, re-review only the new diff, report the bug class, never re-report | [[src-osmani-claude-code-code-review]] |
| **Nit cost for agent authors** | Each nit an agent must address is another commit and another review round | Filter style and cleanup findings; label *Nit* and *Pre-existing* | [[src-osmani-claude-code-code-review]] |
| **Stale approval** | An approval carries over to an agent push or a hand-resolved merge | Approvals cover one commit; untrusted commits need re-approval | [[src-osmani-claude-code-code-review]] |
| **Broken main from green PRs** | Two PRs pass alone and break main together | A merge queue re-runs checks with the change applied to the latest main | [[src-osmani-claude-code-code-review]] |
| **Relocated human time** | Review time drops but bug-fixing time rises | Track revert and incident rates as a guardrail on human-effort metrics | [[src-osmani-claude-code-code-review]] |
| **Conway's-law architecture** | One subagent per team or problem type: *"a copy of their org chart"*, with hundreds of overlapping, ownerless subagents (**subagent sprawl**) | Fold into one loop; teams own skills and tools, a small central team owns the prompt | [[src-anthropic-fold-subagents]] |
| **Frankenprompt** | Every team adds a sentence to the system prompt, so rules conflict and the voice drifts | One owner for the system prompt; procedure moves into skills | [[src-anthropic-fold-subagents]] |
| **Over-localized evals** | Each team's evals fit its subtask, nobody owns the whole set, and leadership reads *"watered-down"* scores | One shared end-to-end eval owned centrally, plus per-skill sets | [[src-anthropic-fold-subagents]] |
| **Telephone game** | Agents split by problem type pass work back and forth, and each handoff loses fidelity | Divide by context; return compact results; keep shared context in one window | [[src-anthropic-fold-subagents]] |
| **Silent flip after a refactor** | Folding a subagent improves latency but one task breaks: the agent answers with the tool it holds and skips the specialist step. Seen in one run of two. | Read which tasks flipped, not the score; cover every production chain and hard rule; run each task more than once | [[src-anthropic-fold-subagents]] |
| **Tool overload** | Tool choice degrades past ~30–50 definitions in the prompt | Group tools by intent; tool search with deferred loading | [[src-anthropic-fold-subagents]] |
| **Stale-model scaffolding** | Rules and structure written for an older model make a newer one slower, more rigid, or stop it doing more of the work | Audit prompts, skills and tool descriptions after model upgrades (`prompt-audit`) | [[src-anthropic-fold-subagents]] |
| **Oscillation / stagnation** | Generations flip between two specs, or stop changing without passing | Detect period-2 cycles and stable windows, then `ooo unstuck` (change approach, not iteration count) | [[src-ouroboros]] |

## Related
[[termination]] · [[backpressure]] · [[verification]]
