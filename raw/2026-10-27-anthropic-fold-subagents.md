---
title: "Building agents: When to fold subagents into your main agent loop"
url: https://claude.com/resources/articles/building-agents-when-to-fold-subagents-into-your-main-agent-loop
author: Diane Sarkis (Member of Technical Staff, Anthropic; Applied AI team)
publisher: Anthropic (claude.com resources)
published: 2026-10-22
fetched: 2026-10-27
category: Best practices, Perspectives · Claude Platform · 18 min read
companion_repo: https://github.com/anthropics/single-agent-loop-kit
extraction: "Condensed section-by-section notes with short quotes, NOT the full article text (copyright). Taken from the claude.com HTML on 2026-10-27. Section headings are verbatim; everything else is paraphrased unless in quotes. Re-read the URL for exact wording. Figures (remote, not downloaded): 'subagent design' (GIF), 'subagents split by problem' (PNG), 'folding in subagents' (GIF)."
---

# Building agents: When to fold subagents into your main agent loop

## (Intro)
- Promotes a **migration kit** (github.com/anthropics/single-agent-loop-kit): a guided workflow to find your multi-agent patterns, evaluate alternatives and verify the best approach, with a demo on a mock system.
- Defines subagents as agents with their own context window, tools and instructions, coordinated by an orchestrator. Says they are good at verification, parallel work and modular permissioning, and that Anthropic uses them itself (links its multi-agent research system).
- The Applied AI team has seen a pattern of enterprise deployments that improved by **folding routers, planners and domain subagents into the main loop**. In comparisons across several enterprise deployments, "a single agent with skills" frequently beat both the one-prompt-for-everything design and the subagent design on quality, often at lower cost and latency per task.
- Example: one company's customer-facing agent had about a dozen specialist subagents; a consistent on-brand experience was hard to keep and the latency hurt UX.
- A common proposed design: intent classifier → fixed multi-step reasoning pipeline → user-segment buckets → separate recommendation branches → multi-agent orchestrator on top. Feedback is often that this structure does work "the model no longer needed done for it", and that one clear system prompt, **4–5 thin data tools** and firm output guardrails cover most of the use case.
- **When subagents still make sense** (three conditions):
  1. a single loop shows measurable degradation from context bloat;
  2. several tasks need to run in parallel with fresh, discardable context windows;
  3. a single agent struggles to pick tools, or the system prompt has conflicting instructions.
- Warns that enterprises often give each team or problem type its own subagent, so the architecture copies the org chart ("Conway's law at work").

## Agent building failure modes for large organizations
- Typical setup: each capability's team builds its own agent; a central platform team adds an orchestrator (orchestrator-subagent, or one agent with team agents exposed as MCP tools).
- Failure modes listed:
  - **Context management:** deciding what context passes between agents; details get lost in the back-and-forth.
  - **Subagent sprawl:** hundreds of overlapping subagents, no enforced standards, no clear owner.
  - **The Frankenprompt:** every team adds a sentence to the system prompt → conflicting rules, no consistent voice.
  - **Unvetted, overly localized evals:** each team's evals over-fit its subtask; nobody owns the whole set; leadership decides on "watered-down, overly localized scores".
  - **Latency:** one customer measured roughly **2× faster runtime** for a single agent loop vs its multi-agent harness.

## Using an agent loop with progressive disclosure
- Alternative: **progressively disclose context via skills** and **tools via tool search**. The agent sees short descriptions; full content loads only when needed.
- Three reasons:
  - **Shared context produces better answers:** for longer-running agents, results of earlier steps stay in one window, so the agent can connect them; better than summaries handed back by subagents; fewer windows, fewer lossy handoffs.
  - **Progressive disclosure prevents context bloat:** removes the main reason teams split work across subagents. Claims Anthropic cut Claude Code's system prompt for more advanced models by **over 80%**, partly through progressive disclosure of skills and tools (links "The new rules of context engineering for Claude 5 generation models").
  - **Models are more capable:** from Opus 4.5 on, models handle far more in one loop than teams expected. Thinking can't be turned off on Opus 5.5 and Fable 5.1; recent models narrate progress and check their work, making some harness elements redundant. Each new model lets you move more decision-making from harness into model. In migrations, rigid multi-agent structures were often what stopped the new model doing more of the work.
- The single-loop design "requires discipline": a carefully managed system prompt, skill and tool descriptions that trigger at the right time, deliberate handling of context windows, memory and note-taking.
- **One small central team** owns end-to-end quality and the system prompt and vets every new tool and eval before it ships.
- If you do go multi-agent: start with the simplest pattern (generator-verifier, orchestrator-subagent, ...). **Divide by context, not by problem type**: give each subagent work that needs little from the rest of the system and returns a compact result (independent research paths, components with clean interfaces, black-box verification). Splitting by problem type creates a "telephone game" where each handoff degrades fidelity.

## How to fold subagents into the main agent loop
Target single-loop design:
- One model, one context window, an open-ended tool loop; **limits set in the harness** (turn and cost budgets, write gates).
- Each turn the model emits a **batch of tool calls**; the harness runs them in parallel and returns raw results to the same model, which chooses: another batch, a question to the user, or an answer.
- The loop **stops when the model answers or hits a budget** (links task-budgets docs). A goal or verifier check can optionally run after the answer.
- The model **writes its plan in context on the first turn and revises it** as results arrive — called the main change from orchestrator + specialists: the planner is the executor, so it can change the plan mid-turn.
- Context is still loaded but managed by the agent:
  - a code step that rewrites the plan from a rule catalog is no longer needed;
  - ordering and domain procedure → **skills**;
  - hard limits (validation, approval gates) and mid-conversation needs (e.g. memory lookup) → **tools**;
  - code still loads cheap, almost-always-relevant context (e.g. entity resolution) and handles mechanical parts (payload construction, stream parsing, resuming a clarification) inside tools.
- Says this suits the end state many teams want (an agent that understands a user's high-level goals and acts for them) because everything learned stays in one context.

### Task-completion evals
- First build an eval set to decide whether to fold a subagent. Structure that works: **one shared end-to-end set owned by the central team** + smaller sets shipped with each skill by its owning team. "Even a set of 10 golden examples is enough to start."
- Start by grading the final message against a rubric. With an orchestrator, also track **routing accuracy**; after folding, check whether the agent **loaded the right skill or called the right tool**. Work toward task-completion evals, which matter most when comparing architectures.
- Where systems are hard to replay and users hard to simulate: record **timestamps on important events** so they can be replayed later as targeted evals.

### Reducing subagents over time
- Fold subagents into tools and skills by: merging domain subagents, calling them as tools, or replacing them with skills + tools.

### Combining domain agents
- Build a small end-to-end eval before the first merge. "fold in by shared context starting with subagents that have the most use."
- Merge specialists that chain on each other's output, touch the same data, or are often called together. If much production traffic is specialist A then specialist B, that tightly coupled pair is a merge candidate.

### Subagents called as tools
- When one of the three conditions holds and you keep a subagent, have the main agent **call it as a tool** so the main agent keeps the conversation with the user.
- Full handoff (subagent takes over the conversation) only when it must talk to the user directly; everything else can be a skill plus tools.
- Benefits: a shared response schema for subagents, the main agent verifies the conclusion against real data, trimmed input to final synthesis; no rewrite needed; gives a **baseline** on the task-completion eval.
- Remaining failure modes: each specialist still has its own prompt, context, owner team and evals; each call still returns a lossy summary; each call is a nested model loop adding latency.

### Folding subagents into the main agent via skills and tools
- Fold **one at a time**: the subagent's prompts become skills, its API calls become MCP tools. Compare evals with and without; decide which to keep.
- Don't just read the final score — **look at which tasks flipped**. On a sample support agent, folding one subagent into another lowered latency but broke a previously passing process: the main agent held the order-lookup tool and answered by itself without asking the shipping specialist for the delivery date.
- Before each change, the eval needs a task for **every chain of agents that runs together in production** and **every rule the agent must not break**; run each task **more than once** — that break showed up in only one run out of two.

## How several teams can contribute to a single agent
- Domain reasoning comes from knowledge bases, skills and MCP tools. Teams move ownership from agents to skills and tools; the small central team keeps the system prompt and end-to-end quality and vets new skills, tools and evals.

### MCP tools
- Fit: take an action, read live data, or return a result in a fixed shape. Also a way to keep calling subagents during migration.
- **Group tools by user intent, not one per API**: past **30–50 tool definitions** in the system prompt, tool choice tends to degrade.
- Use tool search with deferred loading. Limit hard preconditions and move needed ones **into the tools**: if Y needs X's output, Y's tool checks and returns an instruction the model can act on.
- **Per-user permissions** the same way: each tool checks what the caller may see/do and returns a plain refusal the model can read — one loop serves users with different access, no separate agent per permission level.

### Skills
- Fit: how a team does work — steps, rules and judgment calls a specialist subagent's prompt used to hold.
- Give maintenance back to skill authors; Claude can build, test and prune skills. Prevent skill sprawl with per-team DRIs who keep skills well crafted, distinct and shipped with evals.
- `/skill-creator`: author well-formed skills; audit existing ones to trim, dedupe, restructure.
- `/skill-doctor`: shows each skill's cost and usage; delete dead weight.

### Knowledge bases
- Fit: reference material needed only some of the time (policies, metric definitions, product specs), behind a search/lookup tool or as reference files inside a skill. Avoid code that retrieves and pastes this context into prompts (links "Seeing like an agent").

## Tools to accelerate this work
- Claude API skills, chained by the migration kit into one guided workflow (with a demo):
  - `/claude-api build-eval`: first end-to-end set for the central team, or small per-skill evals.
  - `/claude-api prompt-audit`: flags instructions written for older models in prompts, skills and tool descriptions; proposes a diff. Finds rules added for an earlier model that now make the agent slower or more rigid. Each DRI can run it on their own skills/tools.
  - `/claude-api hillclimb`: iteratively improves an app against an existing eval; used for the "folded in vs kept" comparison (iterate on the folded skill + tool descriptions and see if it matches or beats the subagent), and on the system prompt.
  - `/claude-api cost-optimize`: profiles where calls go; proposes savings (prompt caching, trimming tokens, effort, model choice) **one change at a time**.
- Closing principle: any one architecture matters less than "measure, change one thing at a time, and keep what holds up." As models improve and agents run longer, more subagents can become skills and tools; do it stepwise — small end-to-end eval, fold one subagent, keep it as a subagent only if the folded version scores worse, repeat.
