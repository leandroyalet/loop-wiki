---
type: source
branch: sources
tags: [loop-engineering, pstack, tan, secondary, report]
sources: []
url: https://claude.ai/artifact/JNBnuspjGxGw3vW1k9sMiY
author: unknown (third-party research report)
published: 2026-10-14
raw: raw/2026-10-15-inside-pstack-report.md
created: 2026-10-15
updated: 2026-10-15
status: solid
---
# "Inside pstack" (third-party research report, v0.15.25)

**Author:** not named. This is a **secondary source** about [[lauren-tan]]'s [[pstack]], not written by her. · **Raw:** `raw/2026-10-15-inside-pstack-report.md` · Up: [[sources]]

## Summary
The report reads every file in pstack at **v0.15.25**. The wiki's other Tan sources were fetched at v0.15.21. It explains how the pack is built, quotes Tan's posts, assesses the pack, and ranks ten ideas to copy. Its central reading: *"verification comes before parallelism"*. Go deep with one agent until its output can be checked, then scale out. It adds four things the wiki lacked:
- what the **enforcement scripts** actually do
- the **0.15.24–0.15.25 changes** (13–14 Oct 2026)
- an outside **critique** covering cost, ceremony and self-reported numbers
- a **port mapping** to Claude Code

Treat it as an informed reader's interpretation. Where it quotes pstack files or Tan's posts, the quotes can be checked against the primary sources.

## Key claims
- **Shape at v0.15.25:**
  - 54 SKILL.md files, 23 playbooks and 24 one-rule principles
  - 2 subagent definitions (`poteto-agent`, `comment-sicko`)
  - about 7k lines of Bun/TypeScript scripts with ~63 tests
  - 129 commits since 22 May 2026

  53 of the 54 skills set `disable-model-invocation: true`, so *"No skill loads just because a word in your prompt matched."* The exception is `setup-pstack`. See [[pstack]].
- **Skills keep shrinking.** One principle file is 34 words long. Cut passes include #329 (−633 lines), #419 (*"19 more instructions Opus 5.5 does not need"*), #538 (−736 lines), and October's *"pstack is now 10% smaller with no loss in behavior."* Tan expects most skills to *"compress into short principles or workflows"* as models improve.
- **Scripts enforce the rules that matter most** (*"Each script replaces a rule the agent might otherwise forget"*). See [[build-the-lever]].
  - `check-plan.mjs` lints plan files and exits 1 on any problem.
  - `watch-pr` returns a typed verdict through exit codes: READY 0, conflicts 2, review threads 3, failing checks 4, timeout 5, merge gate 6, query failure 7. A gate waiting on a human counts as a gate, *"so the watcher never sits waiting on a human"*.
  - `orch` does file-based bookkeeping. Its verification ledger is keyed by PR + head SHA, so *"a new SHA voids the verdict"*. It has a self-healing PID lock and never spawns agents.
  - `worktree-audit.sh` is read-only. *"The bucket is advice, not permission."*
  - `log.sh` guards against spreadsheet formula injection.
  - `bootstrap.ts` installs dependencies keyed by a hash, so a rerun does nothing.
- **Author ≠ critic, across model families.** Reviews pair different model families because *"agreement is high-signal"*. Arena's judge and the decision-trail reviewer must come from a different family than the author. In `/interrogate`, *"The adversarial signal comes from model diversity, not assigned personas."* See [[evaluator-optimizer]].
- **Fresh subagents by default** (since 0.15.24). A fix round, retry or next queue item goes to a new agent with a consolidated brief, because *"Interrupt-chained resumes silently drop directives."* Each spawn's effort and speed are tuned per job, but the model family never changes, *"so a diverse panel stays diverse."* See [[orchestrator-workers]].
- **Loop-relevant playbook rules** (from the embedded playbook data):
  - *Hillclimb:* one metric, plus a stop predicate *with a floor on attempts* (*"≥50% better and ≥10 iterations"*). Freeze the harness, then *one change, one measurement, keep or revert*. Push past the first plateau. *"Stop at the predicate. Never relax it."*
  - *Autonomous run:* the wake is *"a watcher on an event, or a heartbeat sized to when the result is worth re-checking"*. *"A plateau is not a stop."*
  - *Orchestrate:* a rolling window of ~10 in flight, never blocking batches. **Stop spawning at ~70% of budget.** *"The brief is the product. A vague brief fails quietly, because a worker cannot ask you a question."*
  - *Autopilot-full:* *"Assume the VM dies: push early and keep a decision trail a replacement can find."* An hourly `/loop` audit judges agents *by side effects*.
  - *Shipping:* re-check verdicts with `git patch-id`, *"because a chain rebase moves every PR to a new SHA without failing any check."* Since #613 there is one full swarm per PR at its code-ready head instead of one per push.
  - *figure-it-out:* verdicts are VERIFIED / NOT VERIFIED / INCONCLUSIVE. *"When something passes too easily, suspect the observation method before the system."* *"If a worker games the gate, reset and harden the contract."*
  - *Swarm:* *"A gap does not count as a pass."*

  See [[termination]], [[budgets-and-cost]] and [[failure-modes]].
- **Autonomy line.** Reversible work proceeds without asking. Irreversible writes always pause: force-pushes to shared branches, deploys, data deletion and customer messages. Outside input is labelled *"untrusted data"*, and reply text is never put into a shell command. See [[guardrails-and-permissions]].
- **Evidence ladder** (`blast-radius`): *"1 You said so. 2 You pointed at the line. 3 You showed the bad case can't happen. 4 You ran it. 5 You reproduced it in the running app."* Every claim is labelled measured, inferred or guess. See [[verification]].
- **`/correct` ladder.** A mistake counts as a class once it has happened twice. Fix it at the highest level that works: architecture → types or a lint whose error names the fix → behaviour tests → docs last. Keep a **rule → enforcer table** in the agent instruction file. *"If the rule was already there and nothing enforces it, that's a repeat."* See [[build-the-lever]].
- **`/ketchup` catch-ups.** Under 150 words, with pictures first and *"Never make up a call to fill the reply."* The autopilots now end every tick that changed something with one (#616). See [[observability]].
- **#633 (14 Oct)** rewrote four principles, including make-operations-idempotent, *"from specific mechanisms into the reasoning behind them"*. The new idempotency rule: *"Derive each step from the state that exists, not from what the last run meant to do."* See [[idempotency]].

## Assessment (the report's own view)
- **Copy these:** evidence at every step, author ≠ critic, rules moved into structure, short skills, explicit invocation.
- **Costs:**
  - Tokens. One tester, cited by The Neuron, took about 30 minutes without pstack and about an hour with it, but *"the pstack run caught three false claims"*.
  - Ceremony on small tasks. Flavio Copes: *"sometimes more ceremony than a task needs"*.
  - *"Written prose only guides. Only the scripts actually enforce anything."*
- **Limits:** it is one person's habits, models (Opus 5.5 + Grok 4.7) and stack. Throughput figures are self-reported and **inconsistent with each other**: ~1,000 PRs/month (29 Jul), 221 in 2 days (7 Aug), 2,500/month (21 Sep talk), ~2,000/month (guide). Tan told Pocock *"They're not obviously like 2,500 features."* She has a commercial interest in Cursor and Grok Bot.
- **Tension it flags:** on 11 Oct Tan wrote that maintainability still mattering is something she *"would argue … is no longer true"*. That sits uneasily with pstack's own *minimize-reader-load* principle. The report's reconciliation: the reader who matters is now the next agent.

## Porting to Claude Code
SKILL.md carries over unchanged. Agent definitions map to `.claude/agents/`. `/loop` maps to `/loop` under the same rule: *"loop on a check that can pass or fail, never on a duration"*. Worktrees map to `isolation: "worktree"` or `"remote"`. The thing lost is **model-family diversity**. Community ports (michael-denyer/pstack-claude, backnotprop/pstack) have reviewers that differ *"by separate context, not by model family."* See [[claude-code]].

## Notable quotes
- *"the goal is not to maximize loc, in fact it's the opposite."* (README)
- *"the thing about loops is that you need to build trust first. a low trust loop is just a waste of tokens."* (X, 8 Jun 2026)
- *"every time you intervene and correct your agent, you should think about how to eliminate it entirely"* (X, 16 Aug 2026; later became `/correct`)
- *"abstract plans only give you the illusion of progress."* (Pt. 2, 9 Sep 2026)
- *"I think your codebase is the ultimate form of memory."*

## Caveats
- The author is anonymous, and the report was published as a public artifact. Biographical claims are unverified here: *"SpaceXAI"* since 17 Aug 2026, *"after SpaceX acquired Cursor"*. The wiki's primary sources only say her GitHub lists xAI ([[src-tan-complete-guide-pstack-pt1]]).
- The report excludes a *"10,000 agent runs a week"* figure as unverifiable.
- It names primary sources the wiki does not yet hold: Pt. 2 of the Complete Guide, the 21 Sep talk, the Pocock interview, and the community ports. See [[open-questions]].

## Pages touched
[[pstack]], [[lauren-tan]], [[build-the-lever]], [[verification]], [[evaluator-optimizer]], [[orchestrator-workers]], [[termination]], [[budgets-and-cost]], [[idempotency]], [[observability]], [[guardrails-and-permissions]], [[failure-modes]], [[claude-code]], [[open-questions]]
