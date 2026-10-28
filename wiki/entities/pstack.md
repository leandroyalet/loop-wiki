---
type: entity
branch: entities
tags: [loop-engineering, product, pstack, skills]
sources: ["[[src-tan-how-i-use-cursor]]", "[[src-tan-pstack-guide-poteto-mode]]", "[[src-tan-pstack-guide-principles]]", "[[src-tan-pstack-guide-overnight]]", "[[src-tan-x-short-posts]]", "[[src-pocock-getting-started-with-ralph]]", "[[src-inside-pstack-report]]"]
created: 2026-10-12
updated: 2026-10-15
status: solid
---
# pstack

[[lauren-tan]]'s plugin of skills *"for rigorous engineering with agents"*. It lives in Cursor's official plugin repo (`cursor/plugins/pstack`, MIT). The wiki's primary sources were fetched at v0.15.21, and the third-party report covers v0.15.25. It is also available in Grok Bot ([[src-tan-x-short-posts]]). It grew out of *"turning every recurring failure mode into a skill"* ([[src-tan-loops-you-can-trust]]). Its README goal: *"the goal is not to maximize loc, in fact it's the opposite"* ([[src-inside-pstack-report]]). Up: [[entities]].

## Shape
- **`/poteto-mode`:** a higher-order router. It reads the principles, matches one of **23 playbooks**, copies that playbook's steps into a todo list, and calls the other skills as needed ([[src-tan-pstack-guide-poteto-mode]]). A skipped step stays visible as `skip: <reason>` ([[src-inside-pstack-report]]).
- **24 principles**, each a skill. Agents must name the decision each principle changed ([[src-tan-pstack-guide-principles]]).
- **Workflow skills**, including `/how`, `/why`, `/architect`, `/arena`, `/interrogate`, `/tdd`, `/unslop`, `/swarm`, `/reflect`, `/figure-it-out`, `/show-me-your-work`, `/create-verification-skill`, `/maintain-verification-skill` and `/benchmark-checklist` ([[src-tan-how-i-use-cursor]], [[src-tan-pstack-guide-verify-and-ship]]).
- **Loop-relevant playbooks:** Autonomous run, Pause safely, Session pickup, Babysit, Shipping, Autopilot-full, Autopilot-stack, Orchestrate, Hillclimb ([[src-tan-pstack-guide-overnight]], [[src-tan-pstack-guide-poteto-mode]]).
- **Automation pack:** benny ([[src-tan-benny-automation]]).
- **At v0.15.25** ([[src-inside-pstack-report]]):
  - 54 SKILL.md files and 2 subagent definitions, plus about 7k lines of Bun/TS scripts with tests
  - 53 of the 54 skills are **explicit-only** (`disable-model-invocation: true`), so nothing loads by keyword match
  - the delegate wrapper `poteto-agent` makes every subagent read the router before it starts
  - `pstack-models.mdc` maps *roles* to models, so reviewers can come from different model families

## Rules that run as code
The report's point: prose only guides, and the scripts enforce. Each script *"replaces a rule the agent might otherwise forget"* ([[src-inside-pstack-report]]). See [[build-the-lever]].

| Script | Loop-relevant job |
|---|---|
| `watch-pr` | Returns a typed PR verdict through exit codes. A human-owned gate counts as a gate, so the watcher *"never sits waiting on a human"*. |
| `orch` | Bookkeeping for Orchestrate: units, a verification ledger keyed by PR + head SHA (*"a new SHA voids the verdict"*), frontier and standing orders. It has a self-healing PID lock and never spawns agents. |
| `check-plan.mjs` | Lints multi-phase plans and exits 1 on any problem. |
| `log.sh` | Writes append-only TSV decision rows with a formula-injection guard. |
| `worktree-audit.sh` | Read-only triage of worktrees. *"The bucket is advice, not permission."* |
| `bootstrap.ts` | Installs dependencies keyed by a hash, so a rerun does nothing. |

## Where it fits
pstack is **what runs inside each iteration**: the rigor. Cursor's `/loop` and Automations provide the trigger and the repetition ([[src-tan-pstack-guide-overnight]]). Compare AI Hero's line: *"Ralph is the loop. Skills are what's inside"* ([[src-pocock-getting-started-with-ralph]]). See [[loop-primitives]].

## History
From [[src-inside-pstack-report]]:
- It grew out of Tan's earlier repos: brainmaxxing, noodle and how.
- It launched in `cursor/plugins` on 22–25 May 2026 with 74 files and 18 principles.
- It kept growing through September.
- Since then it has been **pruned**. October brought *"10% smaller with no loss in behavior"*.
- **0.15.24–0.15.25 (13–14 Oct):**
  - effort and speed set per subagent role
  - one swarm per PR instead of one per push
  - Graphite removed
  - autopilots report through `/ketchup`
  - four principles rewritten from mechanisms into reasoning (#633)

## Critique
- **Token cost.** Panels and swarms are expensive. One tester took about 1 h with pstack vs about 30 min without, though the pstack run caught three false claims ([[src-inside-pstack-report]]). See [[budgets-and-cost]].
- **Ceremony** on small tasks, despite *"most changes need none of it"* ([[src-inside-pstack-report]]).
- **One person's stack and models.** The answer to that is `/automate-me`, which builds your own `-mode` from your transcripts ([[src-inside-pstack-report]]).

## Ports
Community ports to [[claude-code]] (michael-denyer/pstack-claude, backnotprop/pstack) keep the SKILL.md files as they are. They lose cross-family review: their reviewers differ *"by separate context, not by model family"* ([[src-inside-pstack-report]]).

## Related
[[cursor]] · [[verification-skill]] · [[build-the-lever]] · [[overnight-contract]]
