---
type: concept
branch: control
tags: [loop-engineering, control, failure-modes]
sources: ["[[src-huntley-ralph]]", "[[src-osmani-loop-engineering]]", "[[src-anthropic-building-effective-agents]]", "[[src-claude-code-scheduled-tasks]]", "[[src-pocock-ralph-tips]]", "[[src-pocock-ai-coding-dictionary]]", "[[src-pocock-ralph-plugin]]", "[[src-pocock-tdd-skill]]", "[[src-pocock-tracer-bullets]]", "[[src-pocock-triage-skill]]", "[[src-tan-pstack-guide-overnight]]", "[[src-tan-pstack-guide-recipes]]", "[[src-tan-pstack-guide-verify-and-ship]]", "[[src-tan-loops-you-can-trust]]"]
created: 2026-10-11
updated: 2026-10-12
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
| **Shallow evidence** | A bulk triage pass relies on a cheap listing without comments | Require full context per item | [[src-pocock-triage-skill]] |

## Related
[[termination]] · [[backpressure]] · [[verification]]
