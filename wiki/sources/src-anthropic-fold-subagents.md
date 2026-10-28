---
type: source
branch: sources
tags: [loop-engineering, primary, sub-agents, multi-agent, progressive-disclosure, evals]
sources: []
url: https://claude.com/resources/articles/building-agents-when-to-fold-subagents-into-your-main-agent-loop
author: Diane Sarkis (Anthropic, Applied AI)
published: 2026-10-22
raw: raw/2026-10-27-anthropic-fold-subagents.md
created: 2026-10-27
updated: 2026-10-27
status: solid
---
# Anthropic — "Building agents: When to fold subagents into your main agent loop" (2026-10-22)

**Author:** Diane Sarkis, Member of Technical Staff at [[anthropic]], writing for the Applied AI team · **Raw:** `raw/2026-10-27-anthropic-fold-subagents.md` (condensed notes with short quotes, not the full text) · **Companion:** the `anthropics/single-agent-loop-kit` migration kit · Up: [[sources]]

## Summary
This is a best-practice article from Anthropic's Applied AI team, written for enterprises that have built **multi-agent** systems on the Claude Platform. It argues that many of them should fold their routers, planners and domain subagents back into **one agent loop**. In that loop the model plans and acts in a single context window, **skills** hold domain procedure, **tools** hold live data and hard limits, and both load through **progressive disclosure**. Across several enterprise deployments, *"a single agent with skills"* frequently beat both one-prompt-for-everything and subagent designs on quality, often at lower cost and latency. Subagents keep three jobs: relieving measured context bloat, parallel work in fresh throwaway windows, and fixing tool-selection or instruction conflicts. The migration it proposes is itself a careful loop. Build a task-completion eval, fold in **one subagent at a time**, check which tasks flipped (not just the score), run each task more than once, and keep the subagent only if the folded version scores worse.

The article is about the **inner** [[agent-loop]] of enterprise agents, often customer-facing, rather than outer loops that run unattended. It also promotes Anthropic's own migration kit and `/claude-api` skills. Its numbers are qualitative or single-customer ("frequently", "roughly 2x").

## Key claims
- **When to keep subagents.** Use them when (1) a single loop shows *measurable* degradation from context bloat, (2) tasks need to run in parallel with fresh context windows that can be thrown away afterwards, or (3) one agent struggles to choose tools or its system prompt has conflicting instructions. See [[orchestrator-workers]].
- **Conway's law.** Enterprises often give each team or problem type its own subagent, so the architecture becomes *"a copy of their org chart"*.
- **Over-built designs.** A common proposal stacks an intent classifier, a fixed reasoning pipeline, user-segment buckets, recommendation branches and an orchestrator on top. Most of that structure does work the model no longer needs done for it. One clear system prompt, 4–5 thin data tools and firm output guardrails cover most of the use case. See [[agent-loop]].
- **Org-scale failure modes:** lossy context passed between agents, **subagent sprawl** (hundreds of overlapping agents with no owner), the **Frankenprompt** (every team adds a sentence and the rules conflict), **over-localized evals** that nobody owns end to end, and latency. One customer measured roughly **2× faster** runs with a single loop. See [[failure-modes]].
- **Progressive disclosure replaces splitting.** The agent sees short descriptions of skills and tools and loads the full content only when it needs it, so one agent can cover many tasks without a giant system prompt. This *"removes the main reason teams previously split work across subagents."* Anthropic says it cut Claude Code's system prompt for advanced models by over 80%, partly this way. See [[progressive-disclosure]] and [[claude-code]].
- **Shared context beats handed-back summaries.** An agent that has seen every earlier step's result can connect them. A set of subagent summaries can't, and every handoff loses detail. See [[context-and-state]].
- **Move decisions from harness to model.** From Opus 4.5 on, models handle far more in one loop than teams expected. Recent models narrate progress and check their work, which makes some harness elements redundant. In migrations, rigid multi-agent structures were often *what stopped the new model doing more of the work*. See [[decision-step]].
- **If you do split, divide by context, not by problem type.** Give each subagent work that needs little from the rest of the system and returns a compact result: independent research paths, components with clean interfaces, black-box verification. Splitting by problem type plays a *"telephone game"*.
- **The target single loop:** one model and one window run an open-ended tool loop. The **harness** sets the limits (turn and cost budgets, write gates). Each turn the model emits a **batch** of tool calls, which the harness runs in parallel and returns raw. The model then chooses another batch, a question for the user, or an answer. The loop **stops on the answer or a budget**, and a goal or verifier check *can optionally* run afterwards. The model **writes its plan in context on turn one and revises it**, so the planner and the executor are the same agent. See [[agent-loop]] and [[termination]].
- **Where things go:** ordering and domain procedure → skills. Hard limits (validation, approval gates) and mid-conversation needs such as memory lookup → tools. Code still loads cheap, almost-always-relevant context (e.g. entity resolution) and does mechanical work (payload building, stream parsing) inside tools. See [[build-the-lever]].
- **Task-completion evals come first.** One end-to-end set owned by a central team, plus small sets each team ships with its skills. *"Even a set of 10 golden examples is enough to start."* Grade the final message against a rubric. Track routing accuracy while an orchestrator exists, then whether the right skill or tool was used. Where replay is hard, record timestamps on important events so they can be replayed as targeted evals. See [[verification]].
- **Migration path:** merge domain agents that chain, share data or are called together (if much traffic is A then B, that pair is a candidate). Call the remaining subagents **as tools** so the main agent keeps the conversation, which gives a shared response schema and a baseline without a rewrite. Fold them in **one at a time**, with prompts becoming skills and API calls becoming MCP tools. See [[folding-subagents]].
- **Check which tasks flipped.** On a sample support agent, folding one subagent cut latency but broke a passing process: the main agent held the order-lookup tool and answered alone, without asking the shipping specialist for the delivery date. The eval needs a task for every chain of agents that runs together in production and every rule the agent must not break, and each task needs **more than one run**, because that break showed up in only one of two. See [[failure-modes]].
- **Tools:** for actions, live data or fixed-shape results. **Group them by user intent, not one per API**, because tool choice tends to degrade past **30–50 definitions**. Use tool search with deferred loading. Put preconditions *inside* tools: if Y needs X's output, Y's tool checks and returns an instruction the model can act on. See [[action]].
- **Permissions inside tools.** Each tool checks what the calling user may see or do and returns a plain refusal the model can read, so one loop serves users with different access. See [[guardrails-and-permissions]].
- **Skills** hold how a team works: the steps, rules and judgment calls a specialist's prompt used to hold. Per-team DRIs prevent skill sprawl. `/skill-creator` authors and audits skills; `/skill-doctor` shows each skill's cost and usage so dead weight can go.
- **Knowledge bases** hold reference material that is needed only sometimes, behind a lookup tool or as reference files in a skill. Don't have code retrieve it and paste it into prompts.
- **One small central team** owns the system prompt and end-to-end quality and vets every new skill, tool and eval. Teams move from owning agents to owning skills and tools.
- **Accelerators:** `/claude-api build-eval`, `prompt-audit` (flags instructions written for older models that now make the agent slower or more rigid), `hillclimb` (iterate the folded version against the eval) and `cost-optimize` (one change at a time). The migration kit chains them. See [[improvement-loops]].
- **The principle above any architecture:** *"measure, change one thing at a time, and keep what holds up."*

## Notable quotes
> "a single agent with skills frequently outperformed both the one-prompt-for-everything design and the subagent design on quality"

> "the agent architecture becoming a copy of their org chart (Conway's law at work)"

> "the model that writes the plan is also the one carrying it out, so it can change the plan mid-turn."

> "measure, change one thing at a time, and keep what holds up."

## Pages touched
[[folding-subagents]], [[progressive-disclosure]], [[orchestrator-workers]], [[agent-loop]], [[decision-step]], [[context-and-state]], [[smart-zone]], [[action]], [[termination]], [[guardrails-and-permissions]], [[budgets-and-cost]], [[failure-modes]], [[evaluator-optimizer]], [[verification]], [[improvement-loops]], [[build-the-lever]], [[agent-experience]], [[claude-code]], [[anthropic]], [[open-questions]], [[loop-design-checklist]], [[loop-pattern-comparison]]
