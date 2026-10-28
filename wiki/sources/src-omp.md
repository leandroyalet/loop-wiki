---
type: source
branch: sources
tags: [loop-engineering, omp, harness, goal, advisor, factory, hillclimb]
sources: []
url: https://omp.sh/
author: Can Bölük (can1357) / Stencil Labs, Inc.; fork of Pi by Mario Zechner
published: unknown (repo 2025-12-31 to 2026-10-19; blog post 2026-02-12)
raw: raw/2026-10-19-omp.md
created: 2026-10-19
updated: 2026-10-19
status: draft
---
# omp (oh-my-pi): README, harness post, loop docs and prompts, robomp

**Author:** Can Bölük / Stencil Labs (MIT, ~36k GitHub stars, a fork of [Pi](https://github.com/badlogic/pi-mono) by Mario Zechner) · **Raw:** `raw/2026-10-19-omp.md` (33 sections: README, the "harness problem" blog post, goal-mode prompts, `/loop` and `/ratchet`, the advisor, stream rules, the orchestrate and vibe contracts, retry policy, the repo's own `fix-issues`/`triage` commands, the **robomp** bot and its prompts, plus GitHub API fetch notes) · Up: [[sources]]

## Summary
[[omp]] is a terminal coding-agent **harness**: *"A coding agent with the IDE wired in."* It works with 60+ providers and ships 31 built-in tools. Its pitch is that the harness, not the model, is often the bottleneck: *"the model is but a parameter. The real variable is the harness."*

For loop engineering it is unusually rich, because it ships most outer-loop primitives built in and its prompts are readable in the repo:
- **`/goal`:** a self-graded goal loop with a token budget and a mandatory completion audit.
- **`/loop`:** re-submits a prompt after every yield. It can be bounded by a count or duration, or gated by a shell command's **exit code**.
- **`/ratchet`:** an unattended eval hill-climb that keeps a change only if it wins on held-out cases.
- **The advisor:** a second model that reads every turn and can steer.
- **Time-traveling stream rules (TTSR):** rules that interrupt the output mid-stream when they match.
- **`orchestrate` / `vibe`:** coordinator contracts for fanning out work to subagents.

The repo also runs **robomp**, a self-hosted GitHub bot that triages, reproduces and fixes issues on omp itself. It has opened **2,773 PRs since 2026-05-14, of which 2,242 were merged** (GitHub API, 2026-10-19). That is the largest real-world [[software-factory]] the wiki has data on.

**Is it loop engineering?** Yes *(synthesis)*. omp is a harness for the inner [[agent-loop]] that ships a full outer-loop toolkit, and robomp is a working factory built on it.

## Key claims
- **Goal mode is self-graded, with an audit.** The doing agent ends the loop itself by calling `goal({op:"complete"})`, which is allowed *"only when actually done and every deliverable verified against current evidence. NEVER because budget low or turn ending."* A hidden continuation steer re-prompts each turn and requires the agent to:
  - map the objective to concrete deliverables
  - name the authoritative evidence for each one
  - inspect the current state (*"NEVER rely on earlier-session memory"*)

  It adds *"Verification scope = claim scope"* and *"Uncertainty = not achieved."* See [[goal-loop]] and [[verification]].
- **No shrinking the goal.** *"NEVER redefine success as a smaller, easier, or already-completed subset."* A goal can't be dropped and replaced: *"To change the objective, NEVER drop; ask the user."* See [[goal-spec]].
- **A token budget is a hard runtime state.** When `tokensUsed ≥ tokenBudget`, the runtime flips the goal to `budget-limited` and steers the agent: *"NEVER start new substantive work … Budget exhaustion ≠ completion."* Interrupting with Esc pauses the goal. See [[termination]] and [[budgets-and-cost]].
- **`/guided-goal` interviews you before the loop starts.** It asks at most ~6 questions, one at a time, until five fields are fixed:
  1. binary success criteria
  2. a verification method
  3. an **attempt cap**
  4. scope boundaries, with a denylist
  5. stop/escalation conditions

  It rejects *"uncapped iteration ('until CI is green', 'keep going until it works')"* and *"self-graded success without verification command."* The objective must use the headings `## Objective / Success criteria / Verification / Boundaries / Stop conditions`. See [[goal-spec]].
- **`/loop` has deterministic gates.** It *"re-submits after every yield"*, bounded by a count or duration (`10`, `1h30m`) or gated by `--until '<cmd>'` / `--while '<cmd>'`. *"Exit status is authoritative and stdout is ignored."* Only exit 1 means "false". Anything higher (127, 126, 2) is an **error**, because otherwise *"a typo'd condition halts the loop looking exactly like finished work."* See [[termination]] and [[backpressure]].
- **`/ratchet` hill-climbs unattended.** It builds a trusted eval and then makes one change per round, keeping only changes that win on a frozen **held-out test split**:
  - *"Host owns truth: approvals (content-hashed), the frozen split, completeness, held-out isolation, and keep/revert."*
  - It stops for approval three times (inputs, grader, plan) and then runs *"round after round without checking in until `plateau` or `done`."*
  - Grader checks run before the climb: an oracle should score ~100% and a null answer ~0%. The judge model must differ from the model under test.
  - On a stall it *"categorize[s], don't grind[s]"*: each failure is sorted as `artifact_gap` / `grader` / `harness` / `structural` / `variance`.
  - It is *"Adapted from the claude-api skill's build-eval, eval-audit, and hillclimb guides (Apache-2.0, github.com/anthropics/skills)."*

  See [[improvement-loops]].
- **The advisor is a checker that watches every turn.** A second model on its own context, with read-only tools by default, *"reads every turn the main agent takes"*, including its reasoning. It sends `nit` / `concern` / `blocker` notes:
  - Its prompt says *"Silence preferred when agent on track."*
  - It must *"Challenge premature 'done', thin verification"*, and block when the agent *"Yields before explicit convergence condition … is met"*.
  - An emission guard drops duplicates and filler phrases like `lgtm`. A cooldown (`immuneTurns`, default 3) limits how often it interrupts.
  - It *"does not approve actions"* and is *"never a peer"*.

  See [[evaluator-optimizer]].
- **Time-traveling stream rules (TTSR).** Rules are regex or AST patterns that *"sit dormant until the model goes off-script. A regex match aborts the stream mid-token, injects the rule as a system reminder, and retries from the same point,"* so there is no *"context tax on every turn"*. By default a rule fires **once**. Rules phrased as questions go to a `judge` model after the output completes, and these *"cannot interrupt."* See [[backpressure]] and [[context-and-state]].
- **The `orchestrate` contract:**
  - *"NEVER yield before closure."*
  - Enumerate the full surface (*"'Most'/'important' items is failure"*), and dispatch parallel, self-contained subagents.
  - *"Subagents NEVER verify, lint, or format"*. The orchestrator verifies each phase and *"NEVER declare[s] a red tree done."*
  - No relabelling unfinished work as *"follow-up", "v1", or "MVP"*.

  See [[orchestrator-workers]].
- **Vibe mode.** The top-level session becomes a *director* with only `read` and `todo`, steering persistent `fast` and `good` worker sessions. *"worker completion means the turn settled, not that its claims are correct."*
- **Retry is bounded.** Up to 10 retries with backoff from 500 ms to 8 s and 75–100% jitter, a 5-minute cap, and model fallback chains. If the agent stalls mid-task, it gets the nudge *"You said you would continue … but stopped … MUST call the next concrete tool now"* with an attempt counter. See [[failure-modes]].
- **The harness problem (blog post, 2026-02-12).** Changing only the edit tool to **hashline** gave *"+15pts avg over patch, 16 models"*. Hashline tags each line with a short content hash, and edits against a stale hash are rejected. Grok Code Fast 1 went from 6.7% to 68.3%, and Grok 4 Fast used 61% fewer output tokens *"because it stopped burning tokens on retry loops."* The benchmark was 3 runs × 180 tasks, a fresh session each time, about $300. *"You're blaming the pilot for the landing gear."* See [[action]] and [[agent-experience]].
- **robomp, a factory on omp itself.** See [[software-factory]], [[stage-gated-pipeline]] and [[backlog-triage]].
  - **Flow:** a webhook goes into a sqlite queue that dedups on the delivery ID. Each issue gets its own worktree, where omp runs in RPC mode with a model drawn at random from a pool.
  - **Classify first,** behind a 5-part `bug` merit gate. *"No PR without a recorded repro."*
  - **Pre-PR gates:** `bun run fix`, `bun check`, then the full test suite (up to 1 h). Any failure goes back to the agent.
  - **Exactly one turn-ending action:** push and open a PR, `mark_unable_to_reproduce`, or `abort_task`. If the turn ends without one, a reminder tells the agent to continue.
  - **No retry loops:** *"Two identical consecutive push rejections → fix, justified bypass, or escalate; NEVER loop."*
  - **Hands off its own instructions:** *"NEVER edit `prompts/**/*.md`, system prompts, tool descriptions"*.
  - **Credentials:** the PAT lives only in a separate proxy container.
- **A human-in-the-loop variant.** The repo's own `/fix-issues` command fans out one subagent per issue: reproduce on `main` first, then fix in a worktree and commit. *"Do NOT push; human pushes/opens PR."*

## Fetch notes (GitHub API, 2026-10-19)
- `roboomp` is the #2 committer (4,274 commits).
- Its PRs: 2,773 total, 2,242 merged (~81%), 343 closed unmerged (~12%), 188 open.
- The 20 most recently merged roboomp PRs were all merged by another account (`H4vC`), often in batches with the same timestamp, with 0–6 review comments each. So the bot opens PRs and another account merges them.

## Notable quotes
- *"The model is the moat. The harness is the bridge."*
- *"Budget exhaustion ≠ completion."*
- *"a typo'd condition halts the loop looking exactly like finished work, which is the failure mode this whole feature exists to avoid."*

## Contradictions with the wiki
- **Who judges "done"?** omp's `/goal` lets the doer call `complete` after a self-audit. Osmani describes `/goal` in Claude Code and Codex as judged by *"a separate small model"* ([[src-osmani-loop-engineering]]). pstack says the judge is *never* the author ([[src-tan-pstack-guide-verify-and-ship]]). omp's answer to independence is the optional, concurrent advisor rather than a gate on completion. See [[goal-loop]].
- **The advisor must not police scope.** *"Large diff, wholesale rewrite, expanding plan alone NOT a problem"*, and it must *"NEVER tell agent to seek clarification, confirm scope."* That cuts against the small-steps bias in [[task-sizing]] and against Tan's restate-first habit ([[src-tan-pstack-guide-poteto-mode]]). The advisor's lane is correctness and verification, not intent.
- **In-session continuation.** Goal mode continues in the *same* session, with compaction. Pocock argues loops need a fresh process per iteration ([[src-pocock-ralph-plugin]]). omp's compaction docs were not ingested. See [[smart-zone]].
- **Mid-stream rule injection vs always-on instructions.** TTSR keeps rules out of context until they are violated. The wiki's other sources load `AGENTS.md` and skills every iteration. See [[context-and-state]].

## Caveats
- omp is the vendor's own documentation, and its benchmarks are self-run (~$300, one task family based on React mutations).
- The `omp.sh/docs/*` pages render client-side, so the repo's `docs/` folder and prompt files were used instead. Both live in the same repo and may differ in timing.
- The robomp merge data is a 20-PR sample. Whether `H4vC` is a human is not verified.

## Not covered
I did not ingest the compaction, handoff and approval-mode docs, memory backends, subagents/`task` docs, the session tree, collab, or the advisor's `WATCHDOG.md` files. I also did not ingest Pi (pi-mono) itself.

## Pages touched
[[omp]], [[omp-loop-surfaces]], [[goal-loop]], [[goal-spec]], [[termination]], [[verification]], [[evaluator-optimizer]], [[backpressure]], [[action]], [[agent-experience]], [[orchestrator-workers]], [[improvement-loops]], [[software-factory]], [[stage-gated-pipeline]], [[backlog-triage]], [[guardrails-and-permissions]], [[idempotency]], [[budgets-and-cost]], [[observability]], [[failure-modes]], [[context-and-state]], [[open-questions]]
