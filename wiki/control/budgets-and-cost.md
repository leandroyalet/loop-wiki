---
type: concept
branch: control
tags: [loop-engineering, control, cost, tokens]
sources: ["[[src-osmani-loop-engineering]]", "[[src-tns-loop-engineering]]", "[[src-anthropic-building-effective-agents]]", "[[src-claude-code-scheduled-tasks]]", "[[src-huntley-ralph]]", "[[src-pocock-ralph-tips]]", "[[src-pocock-getting-started-with-ralph]]", "[[src-tan-x-short-posts]]", "[[src-tan-how-i-use-cursor]]", "[[src-tan-benny-automation]]", "[[src-inside-pstack-report]]", "[[src-openprose]]", "[[src-omp]]", "[[src-ouroboros]]", "[[src-osmani-claude-code-code-review]]", "[[src-anthropic-fold-subagents]]"]
created: 2026-10-11
updated: 2026-10-27
status: draft
---
# Budgets and cost

Loops spend tokens while nobody is watching. Osmani's first caveat is that *"you absolutely have to be careful about token costs (usage patterns can vary wildly if you are token rich or poor)"* ([[src-osmani-loop-engineering]]). Up: [[control]].

## Cost drivers
- **Autonomy itself.** Agents trade latency and cost for performance, and their autonomy *"means higher costs"* ([[src-anthropic-building-effective-agents]]).
- **Sub-agents.** *"each one does its own model and tool work, so spend them where a second opinion is worth paying for"* ([[src-osmani-loop-engineering]]).
- **Re-loading context every loop.** Ralph accepts this as wasteful by design ([[src-huntley-ralph]]). See [[context-and-state]].
- **Polling.** Re-running a prompt to check status costs more than streaming events via Monitor ([[src-claude-code-scheduled-tasks]]). See [[event-driven-loop]].

- **Per-iteration startup.** Each fresh iteration pays to pick a task, explore and gather context ([[src-pocock-ralph-tips]]). See [[task-sizing]].

- **Rigor itself.** pstack's panels, swarms and cross-model reviews are *"quite token intensive"*. One tester took about an hour with pstack vs about 30 min without, but the pstack run *"caught three false claims"* ([[src-inside-pstack-report]]). *(synthesis)* That is the cost of verification bought up front instead of paid later in review.

- **Human time, counted both ways.** The Claude Code team counts the time people spend reviewing *and* the time they spend fixing bugs that bad code let through: *"If we reduce the first without reducing the second, we're not really saving human time"* ([[src-osmani-claude-code-code-review]]).
- **Review rounds for agent authors.** Each comment an agent must address costs another commit and another review cycle, so the reviewer's noise is a direct cost ([[src-osmani-claude-code-code-review]]). See [[evaluator-optimizer]].
- **Agent count and nesting.** Every subagent call is *"a nested model loop that adds latency"*. One customer measured roughly **2× faster** runs after replacing a multi-agent harness with a single loop ([[src-anthropic-fold-subagents]]). See [[folding-subagents]].
- **Untrusted parallelism.** *"using multiple agents, especially frontier ones, use a lot of expensive tokens"* ([[src-tan-x-short-posts]]). *"Trying to parallelize agents you don't trust yet is a huge waste of tokens"* ([[src-tan-how-i-use-cursor]]).

## Levers
- **Per-stage budgets.** benny's configuration includes budgets for polling, verdict waits, follow-up, repro, rejection and fix ([[src-tan-benny-automation]]).
- **Levers save tokens.** A control CLI means agents *"consume fewer tokens"* than writing throwaway scripts ([[src-tan-complete-guide-pstack-pt1]]). See [[build-the-lever]].
- **Stop spawning at a budget threshold.** pstack's Orchestrate stops spawning new workers at ~70% of budget ([[src-inside-pstack-report]]). See [[termination]].
- **Size effort per role.** Since pstack 0.15.24, each subagent moves its effort level from its role's default: one step up for the hardest work, two or more down for routine work. Fast mode is reserved for when *"CI or trunk is red or someone is blocked right now"*, and the model family stays fixed ([[src-inside-pstack-report]]).
- **One swarm per PR, not per push.** A rebase or minor fix gets a single verifier instead of a new swarm (#613) ([[src-inside-pstack-report]]).
- **A token budget per goal.** omp `/goal` takes a `token_budget` (cache reads excluded) and flips to `budget-limited` when it is spent ([[src-omp]]).
- **Fix the harness before buying a model.** Changing only the edit format cut Grok 4 Fast's output tokens by 61%, *"because it stopped burning tokens on retry loops"* ([[src-omp]]). See [[action]].
- **Route by role.** omp sends cheap fan-out to a `smol` role and deep reasoning to `slow`, and robomp draws each run's model at random from a pool ([[src-omp]]).
- **Escalate tiers on failure.** Ouroboros's router goes Frugal (1×) → Standard (10×) → Frontier (30×) on failure and steps down on success. Evaluation runs the free mechanical stage first, and multi-model consensus only when triggered ([[src-ouroboros]]).
- **Skip unchanged work.** When no input or contract fingerprint has moved, OpenProse's reconciler writes a cheap `skipped` receipt and spawns nothing. Wakes that arrive mid-render collapse into one follow-up ([[src-openprose]]). See [[reconciler-loop]].
- **Scale review depth to risk.** Code Review's Quick, Standard and Deep levels; Deep is for code where *"the cost of missing a single bug is higher than the time spent reviewing code"* ([[src-osmani-claude-code-code-review]]). See [[layered-code-review]].
- **Turn and cost budgets in the harness.** Anthropic's single loop sets them outside the model and stops on the answer or the budget ([[src-anthropic-fold-subagents]]). Its `cost-optimize` skill profiles where calls go and proposes savings (caching, trimming tokens, effort, model choice) **one change at a time** ([[src-anthropic-fold-subagents]]).
- **Fewer, intent-level tools.** Tool definitions are context too. Group them by user intent and defer-load the rest ([[src-anthropic-fold-subagents]]). See [[progressive-disclosure]].
- **Cap iterations.** The iteration argument exists *"to prevent runaway costs"* ([[src-pocock-getting-started-with-ralph]]).
- **Mostly HITL.** Pocock runs on the Anthropic 5x Max plan (about £90/month), and *"most of my usage is HITL"*. Local models are not good enough: *"you have to pay to play"* ([[src-pocock-ralph-tips]]).
- Start small: **one scheduled triage automation and one verifier sub-agent** captures *"most of the value at a fraction of the token spend"* ([[src-tns-loop-engineering]]).
- Choose cadence carefully. Cloud Routines have a 1-hour minimum ([[src-claude-code-scheduled-tasks]]), and self-paced loops back off when idle. See [[self-paced-loop]].
- Bound lifetime and iterations. See [[termination]].
- Use the simplest system that works ([[src-anthropic-building-effective-agents]]).

## Contradictions & open questions
- Huntley says *"these models yearn for tokens, so throw them at them"* ([[src-huntley-ralph]]). Osmani and TNS urge restraint. Pocock sits between them: Ralph is *"completely configurable to how much you want to spend"* ([[src-pocock-ralph-tips]]). The difference may come from different budgets ("token rich or poor").
- A plan with a flat subscription and a pay-per-token API change the cost calculation differently. No source compares them. See [[open-questions]].
- Iteration caps and Orchestrate's ~70% spawn threshold are the only spending limits any source describes ([[src-inside-pstack-report]]). Until omp, no ingested source described a **hard token limit**. omp's `/goal` budget is one, measured in tokens, not dollars ([[src-omp]]). A dollar kill switch is still undocumented. See [[open-questions]].
- OpenProse ranks *"Safety outranks cost; cost outranks silence"*, and treats cost as *"observed, never an enforced budget the gates run against"* ([[src-openprose]]). That is a deliberate choice against hard budget stops, not just a gap in the docs.

## Related
[[failure-modes]] · [[observability]]
