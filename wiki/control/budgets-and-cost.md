---
type: concept
branch: control
tags: [loop-engineering, control, cost, tokens]
sources: ["[[src-osmani-loop-engineering]]", "[[src-tns-loop-engineering]]", "[[src-anthropic-building-effective-agents]]", "[[src-claude-code-scheduled-tasks]]", "[[src-huntley-ralph]]", "[[src-pocock-ralph-tips]]", "[[src-pocock-getting-started-with-ralph]]", "[[src-tan-x-short-posts]]", "[[src-tan-how-i-use-cursor]]", "[[src-tan-benny-automation]]"]
created: 2026-10-11
updated: 2026-10-12
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

- **Untrusted parallelism.** *"using multiple agents, especially frontier ones, use a lot of expensive tokens"* ([[src-tan-x-short-posts]]). *"Trying to parallelize agents you don't trust yet is a huge waste of tokens"* ([[src-tan-how-i-use-cursor]]).

## Levers
- **Per-stage budgets.** benny's configuration includes budgets for polling, verdict waits, follow-up, repro, rejection and fix ([[src-tan-benny-automation]]).
- **Levers save tokens.** A control CLI means agents *"consume fewer tokens"* than writing throwaway scripts ([[src-tan-complete-guide-pstack-pt1]]). See [[build-the-lever]].
- **Cap iterations.** The iteration argument exists *"to prevent runaway costs"* ([[src-pocock-getting-started-with-ralph]]).
- **Mostly HITL.** Pocock runs on the Anthropic 5x Max plan (about £90/month), and *"most of my usage is HITL"*. Local models are not good enough: *"you have to pay to play"* ([[src-pocock-ralph-tips]]).
- Start small: **one scheduled triage automation and one verifier sub-agent** captures *"most of the value at a fraction of the token spend"* ([[src-tns-loop-engineering]]).
- Choose cadence carefully. Cloud Routines have a 1-hour minimum ([[src-claude-code-scheduled-tasks]]), and self-paced loops back off when idle. See [[self-paced-loop]].
- Bound lifetime and iterations. See [[termination]].
- Use the simplest system that works ([[src-anthropic-building-effective-agents]]).

## Contradictions & open questions
- Huntley says *"these models yearn for tokens, so throw them at them"* ([[src-huntley-ralph]]). Osmani and TNS urge restraint. Pocock sits between them: Ralph is *"completely configurable to how much you want to spend"* ([[src-pocock-ralph-tips]]). The difference may come from different budgets ("token rich or poor").
- A plan with a flat subscription and a pay-per-token API change the cost calculation differently. No source compares them. See [[open-questions]].
- The iteration cap is the only spending limit any source describes. No ingested source describes a **hard dollar or token cap** as a stop condition. See [[open-questions]].

## Related
[[failure-modes]] · [[observability]]
