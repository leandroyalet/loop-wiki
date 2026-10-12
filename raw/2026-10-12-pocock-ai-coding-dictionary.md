---
title: "AI Coding Dictionary (index + selected entries)"
url: https://www.aihero.dev/ai-coding-dictionary
author: Matt Pocock
published: 2026-09-24
fetched: 2026-10-12
extraction: "trafilatura HTML→markdown; index page plus 9 entry pages concatenated: software-factory, dark-factory, afk, human-in-the-loop, smart-zone, automated-check, automated-review, handoff-artifact, harness"
---

> Raw source. Immutable; do not edit. Summary lives in the wiki under sources/.

# The vocabulary of AI coding,

in plain English.

Skimmable definitions for the terms that make agentic coding click. Search 71 entries below, or jump into a section.

[5,042mattpocock/dictionary-of-ai-coding](https://github.com/mattpocock/dictionary-of-ai-coding)

## The Model

16 terms
[AIA moving label, not a technology. Points at whatever computers can newly, impressively do — right now, large language models.](https://www.aihero.dev/ai-coding-dictionary/ai)

[ModelThe parameters. Stateless — does next-token prediction and nothing else. Cannot do anything agentic on its own.](https://www.aihero.dev/ai-coding-dictionary/model)

[ParametersThe numbers inside a model — often billions — tuned during training. Everything the model knows lives in them. Also called weights.](https://www.aihero.dev/ai-coding-dictionary/parameters)

[TrainingThe process that sets a model's parameters by exposing it to vast amounts of text and adjusting to improve next-token prediction.](https://www.aihero.dev/ai-coding-dictionary/training)

[InferenceRunning a trained model to generate output — what happens on every model provider request. Parameters stay fixed.](https://www.aihero.dev/ai-coding-dictionary/inference)

[EffortA dial for how much reasoning the model does before it answers. More effort spends more output tokens for a better shot at hard problems.](https://www.aihero.dev/ai-coding-dictionary/effort)

[TokenThe atomic unit a model reads and writes. Roughly word-sized but not exactly. Context window size, cost, and latency all count tokens.](https://www.aihero.dev/ai-coding-dictionary/token)

[Next-token predictionWhat the model actually does. Samples one next token from the context, appends it, and runs again. Its only mode of operation.](https://www.aihero.dev/ai-coding-dictionary/next-token-prediction)

[Non-determinismThe same input can produce different output. A property of how models generate text and how providers serve requests.](https://www.aihero.dev/ai-coding-dictionary/non-determinism)

[Model providerWhatever serves a model for inference. Usually remote (Anthropic, OpenAI, Google), but can also be local (Ollama, llama.cpp).](https://www.aihero.dev/ai-coding-dictionary/model-provider)

[HarnessEverything around the model that turns it into an agent: tools, system prompt, context-window management, permissions, hooks.](https://www.aihero.dev/ai-coding-dictionary/harness)

[Model provider requestOne round-trip from the harness to the model provider. The harness sends context; the provider returns one response.](https://www.aihero.dev/ai-coding-dictionary/model-provider-request)

[Input tokensTokens the harness sends on each model provider request. Billed at a lower rate than output tokens.](https://www.aihero.dev/ai-coding-dictionary/input-tokens)

[Output tokensTokens the model generates back. Billed at a higher rate than input tokens, since they cost more compute to produce.](https://www.aihero.dev/ai-coding-dictionary/output-tokens)

[Prefix cacheThe provider-side store that lets consecutive requests skip re-processing a shared prefix, billing those tokens at a lower rate.](https://www.aihero.dev/ai-coding-dictionary/prefix-cache)

[Cache tokensInput tokens the provider has cached from a previous request via its prefix cache, billed at a much lower rate.](https://www.aihero.dev/ai-coding-dictionary/cache-tokens)

## Sessions, Context Windows & Turns

8 terms
[StatelessCarries no information forward. The model is stateless across requests; an agent is stateless across sessions by default.](https://www.aihero.dev/ai-coding-dictionary/stateless)

[ContextThe relevant information the agent has access to right now — what the agent knows that's pertinent to the task.](https://www.aihero.dev/ai-coding-dictionary/context)

[Context windowEverything the model sees on each model provider request. Finite, model-specific, the only surface through which the model perceives.](https://www.aihero.dev/ai-coding-dictionary/context-window)

[StatefulCarries information forward. Sessions are stateful across turns; agents can be made stateful across sessions via a memory system.](https://www.aihero.dev/ai-coding-dictionary/stateful)

[AgentA model harnessed with tools, a system prompt, and a context window, that takes turns with a user. The model in motion.](https://www.aihero.dev/ai-coding-dictionary/agent)

[System promptThe instructions the harness prepends to every model provider request — the agent's standing brief. Usually stable across a session.](https://www.aihero.dev/ai-coding-dictionary/system-prompt)

[SessionOne bounded run of interaction with an agent. Starts empty, accumulates, ends when cleared, closed, or compacted into a fresh session.](https://www.aihero.dev/ai-coding-dictionary/session)

[TurnOne user message plus everything the agent does in response, up until it yields back to the user. Contains one or more provider requests.](https://www.aihero.dev/ai-coding-dictionary/turn)

## Tools & Environment

10 terms
[EnvironmentThe world the agent acts on — anything outside the harness that the agent perceives via tool results and changes via tool calls.](https://www.aihero.dev/ai-coding-dictionary/environment)

[FilesystemA tree of files and directories the agent reads from, writes to, and executes within — the default environment for a coding agent.](https://www.aihero.dev/ai-coding-dictionary/filesystem)

[ToolA function the harness exposes for the agent to call — Read, Write, Bash, Search. How an agent perceives and acts on the environment.](https://www.aihero.dev/ai-coding-dictionary/tool)

[Tool callThe model's output naming a tool and its arguments — just structured text. The harness has to read it and execute.](https://www.aihero.dev/ai-coding-dictionary/tool-call)

[Tool resultWhat the harness sends back after executing a tool call — file contents, output, or error. The agent's only view of the environment.](https://www.aihero.dev/ai-coding-dictionary/tool-result)

[MCPA protocol for plugging external tool servers into a harness — how an agent gets tools beyond what the harness ships with.](https://www.aihero.dev/ai-coding-dictionary/mcp)

[Permission requestWhat the harness shows the user before executing a tool call that isn't pre-approved. The mechanism for putting a human in the loop.](https://www.aihero.dev/ai-coding-dictionary/permission-request)

[Permission modeThe permission-gating slice of an agent mode — which tool calls trigger a permission request and which run automatically.](https://www.aihero.dev/ai-coding-dictionary/permission-mode)

[Agent modeA preset bundling a permission mode with behavioral instructions injected into the system prompt. Can flip mid-session.](https://www.aihero.dev/ai-coding-dictionary/agent-mode)

[SandboxAn isolated environment the agent runs inside — container, VM, or restricted shell. Limits the blast radius of agent actions.](https://www.aihero.dev/ai-coding-dictionary/sandbox)

## Failure Modes

9 terms
[SycophancyConfidently agreeable model output. Caused by training that shaped the model to favor answers humans liked — including agreement.](https://www.aihero.dev/ai-coding-dictionary/sycophancy)

[HallucinationConfidently-wrong model output. Two flavors: factuality (invented facts) and faithfulness (drift from loaded context).](https://www.aihero.dev/ai-coding-dictionary/hallucination)

[Parametric knowledgeWhat the model knows from training, stored in its parameters. Frozen at training time. Counterpart to contextual knowledge.](https://www.aihero.dev/ai-coding-dictionary/parametric-knowledge)

[Knowledge cutoffThe date past which a model has no parametric knowledge. Post-cutoff libraries and APIs are fabrication traps unless docs are loaded.](https://www.aihero.dev/ai-coding-dictionary/knowledge-cutoff)

[Contextual knowledgeFacts the agent can read directly from the context right now. Counterpart to parametric knowledge.](https://www.aihero.dev/ai-coding-dictionary/contextual-knowledge)

[Attention relationshipThe pairing between two tokens — meaningful pairs influence each other more than unrelated ones. A context of N tokens has \~N² of these.](https://www.aihero.dev/ai-coding-dictionary/attention-relationship)

[Attention budgetEach token has a finite amount of influence to distribute across the rest of the context. Per-token, doesn't grow when context does.](https://www.aihero.dev/ai-coding-dictionary/attention-budget)

[Attention degradationAs a session grows, each token's attention budget spreads across more competitors; signal on meaningful relationships shrinks.](https://www.aihero.dev/ai-coding-dictionary/attention-degradation)

[Smart zoneEarly in a session the agent is sharp and focused. As the session grows it drifts into a dumb zone: sloppier, forgetful, more mistakes.](https://www.aihero.dev/ai-coding-dictionary/smart-zone)

## Handoffs

9 terms
[ClearingEnding the current session and starting a fresh one. The next message begins with an empty session and an empty context window.](https://www.aihero.dev/ai-coding-dictionary/clearing)

[HandoffTransferring agent context from one session to another, with no return path. Carry mechanism varies — artifact, compaction, others.](https://www.aihero.dev/ai-coding-dictionary/handoff)

[Primary sourceThe thing itself — code, transcripts, raw data. Complete and authoritative, but expensive to load into context.](https://www.aihero.dev/ai-coding-dictionary/primary-source)

[Secondary sourceAn account of a primary source, one step removed — summaries, docs, compaction summaries. Cheap to load, lossy by construction.](https://www.aihero.dev/ai-coding-dictionary/secondary-source)

[Handoff artifactA document used as the carry mechanism for a handoff — written by one session to be read by another.](https://www.aihero.dev/ai-coding-dictionary/handoff-artifact)

[SpecA handoff artifact describing a multi-session piece of work — what's being built, not how each session does its share. Made of tickets.](https://www.aihero.dev/ai-coding-dictionary/spec)

[TicketA handoff artifact scoping one session of work. Stands alone or hangs off a spec. Can block or be blocked by sibling tickets.](https://www.aihero.dev/ai-coding-dictionary/ticket)

[CompactionA handoff done in-memory: the previous session's history is summarised and seeds a fresh session. Lossy — detail traded for headroom.](https://www.aihero.dev/ai-coding-dictionary/compaction)

[AutocompactCompaction triggered automatically by the harness when the context window approaches full.](https://www.aihero.dev/ai-coding-dictionary/autocompact)

## Memory and Steering

6 terms
[Memory systemA system that attempts to make an agent stateful across sessions by persisting to the environment and reloading at session start.](https://www.aihero.dev/ai-coding-dictionary/memory-system)

[AGENTS.mdA file in the environment that the harness loads into the context window at session start — the project's standing brief to the agent.](https://www.aihero.dev/ai-coding-dictionary/agents-md)

[Progressive disclosureLoading only the context an agent needs right now, with context pointers to the rest. Borrowed from UI design.](https://www.aihero.dev/ai-coding-dictionary/progressive-disclosure)

[Context pointerA mention in one document that points to another, so the agent can pull it into context only when the task calls for it.](https://www.aihero.dev/ai-coding-dictionary/context-pointer)

[SkillA teachable capability bundled as a unit — kept out of the context window until a context pointer pulls it in for the task at hand.](https://www.aihero.dev/ai-coding-dictionary/skill)

[SubagentAn agent spawned by another agent via a tool call. Runs in its own session, reports a single tool result. Cannot spawn further subagents.](https://www.aihero.dev/ai-coding-dictionary/subagent)

## Patterns of Work

13 terms
[Human-in-the-loopA working pattern where one or more humans pair with the agent during a session — reviewing, redirecting, or collaborating in real time.](https://www.aihero.dev/ai-coding-dictionary/human-in-the-loop)

[AFKA working pattern where the user kicks off a session and leaves the agent to run unattended (away from keyboard).](https://www.aihero.dev/ai-coding-dictionary/afk)

[Automated checkA deterministic verification that runs in the environment — tests, type checks, lints, build, pre-commit hooks. Pass/fail, no judgement.](https://www.aihero.dev/ai-coding-dictionary/automated-check)

[Automated reviewAn agent reviewing another agent's work, often with a different model or system prompt. Non-deterministic: it forms a judgement.](https://www.aihero.dev/ai-coding-dictionary/automated-review)

[Human reviewThe user reading the code the agent produced and forming a judgement on it. Reading the diff counts; reading the summary doesn't.](https://www.aihero.dev/ai-coding-dictionary/human-review)

[Vibe codingA working pattern where the user accepts the agent's code without human review. The diff is treated as opaque.](https://www.aihero.dev/ai-coding-dictionary/vibe-coding)

[Design conceptThe shared understanding of what's being built, held in common between user and agent but separate from any asset.](https://www.aihero.dev/ai-coding-dictionary/design-concept)

[GrillingA technique for developing a design concept: the agent interviews the user Socratically, one decision at a time.](https://www.aihero.dev/ai-coding-dictionary/grilling)

[PrototypingHaving the agent build a quick, rough version when conversation is too low-fidelity and you need a real artifact to talk about.](https://www.aihero.dev/ai-coding-dictionary/prototyping)

[DXDeveloper experience: how easy a codebase and its toolchain make it for humans to do good work — docs, feedback speed, errors.](https://www.aihero.dev/ai-coding-dictionary/dx)

[AXAgent experience: how well the environment is set up for an agent to do good work — checks, architecture, and free context.](https://www.aihero.dev/ai-coding-dictionary/ax)

[Software factoryA system of work where triggers, not humans, start agent sessions, so more work runs AFK and HITL time is saved for what needs it.](https://www.aihero.dev/ai-coding-dictionary/software-factory)

[Dark factoryA codebase, or part of one, where a software factory writes the code and no human ever reviews it.](https://www.aihero.dev/ai-coding-dictionary/dark-factory)
---

# Selected full entries (fetched individually from https://www.aihero.dev/ai-coding-dictionary/<term>)

## Entry: software-factory

A system of work where [agent](https://www.aihero.dev/ai-coding-dictionary/agent) [sessions](https://www.aihero.dev/ai-coding-dictionary/session) are started by triggers — an issue being created, a schedule, a CI failure, another session finishing — rather than by a human, so more work runs [AFK](https://www.aihero.dev/ai-coding-dictionary/afk) and human attention is spent on the [human-in-the-loop](https://www.aihero.dev/ai-coding-dictionary/human-in-the-loop) decisions that remain.

Without a factory, every session starts because someone started it. Even fully AFK work waits on a person to open the session, point it at the [ticket](https://www.aihero.dev/ai-coding-dictionary/ticket), and set it going. Teams want to ship more than that allows. A factory takes the human out of starting sessions, and not necessarily out of anything else.

Common triggers and the sessions they start:

| Trigger | Session it starts | Example | 
|---|---|---|
| Issue created or labelled | Exploration, bug fix, implementation | An issue labelled `ready-for-agent` gets a session that opens a PR | 
| Schedule (cron) | Recurring maintenance | One lint rule fixed per night | 
| CI failure or monitoring alert | Diagnosis, fix attempt | A failing build on main gets a session that finds the breaking commit and proposes a fix | 
| Another session finishing | Follow-on work | A PR opened by one agent triggers an [automated review](https://www.aihero.dev/ai-coding-dictionary/automated-review), whose comments trigger a fix-up session | 

A factory doesn't have to cover the whole software process. One cron job that runs one kind of session and opens one reviewable PR is a factory. Starting that small is useful: a narrow loop produces small, similar PRs, and reviewing them shows how far the loop can be trusted before it's widened.

Humans can sit anywhere in a factory — writing and labelling the issues that trigger sessions, approving a plan before implementation starts, doing [human review](https://www.aihero.dev/ai-coding-dictionary/human-review) before merge. Deciding which of those decisions stay human is the main design question. A codebase, or part of one, where no human reviews the factory's output is a [dark factory](https://www.aihero.dev/ai-coding-dictionary/dark-factory).

*Usage:*

"Who fixed all the `no-floating-promises` violations?"

"The factory. Cron job picks one lint rule a night, opens a PR. I just review it in the morning."
## Entry: dark-factory

A codebase, or part of one, where a [software factory](https://www.aihero.dev/ai-coding-dictionary/software-factory) writes the code and no human reads it. There is no [human review](https://www.aihero.dev/ai-coding-dictionary/human-review). Humans can still write the issues that start the work. But nobody reads the code that comes out. The name comes from "lights-out" factories, which make things with no people on the floor.

A dark factory is [vibe coding](https://www.aihero.dev/ai-coding-dictionary/vibe-coding) for an area of code, not for one change. When you vibe code, you choose not to read a change that you asked for. But you know that the change exists. In a dark factory, the team makes that choice one time, for the full area. After that, no person asks for each change or sees it. Changes arrive as fast as the triggers start new work.

The problem shows when something breaks. You do not know what changed, because nobody read the changes. You must debug code that nobody on the team has read. The cause can be in any of many changes, and each one passed the checks.

[Automated checks](https://www.aihero.dev/ai-coding-dictionary/automated-check) and [automated review](https://www.aihero.dev/ai-coding-dictionary/automated-review) are the only gates. If they do not find a problem, the problem goes into the code.

*Avoid:* calling a codebase "dark" only because its factory runs with nobody watching. If [agent](https://www.aihero.dev/ai-coding-dictionary/agent) [sessions](https://www.aihero.dev/ai-coding-dictionary/session) run [AFK](https://www.aihero.dev/ai-coding-dictionary/afk) and a human reviews their PRs, that is a software factory. It is not a dark factory.

*Usage:*

"Who changed the retry logic in the billing service? Nobody on the team remembers it."

"The billing service is a dark factory. The agents merge all changes that pass CI. Nobody read that change."
## Entry: afk

Away from keyboard. A working pattern where the user kicks off a [session](https://www.aihero.dev/ai-coding-dictionary/session) and leaves the [agent](https://www.aihero.dev/ai-coding-dictionary/agent) to run unattended. The throughput multiplier of [AI](https://www.aihero.dev/ai-coding-dictionary/ai) coding — many AFK sessions can run in parallel while you sleep, eat, or work on something else. Usually requires a permissive [permission mode](https://www.aihero.dev/ai-coding-dictionary/permission-mode) plus [sandboxing](https://www.aihero.dev/ai-coding-dictionary/sandbox) to be safe.

When you're not there, the agent handles ambiguity differently. While you're watching, an ambiguous decision surfaces as a question and you answer it; once you've walked away, the agent picks a default and keeps going, and every later decision builds on that guess. The characteristic failure is coming back to hours of finished, confident work built on a wrong call made in the first ten minutes. The work isn't sloppy — it's coherent, just coherent about the wrong thing.

Since you can't give input during the run, give it before and after instead. Before: resolve the ambiguity up front — a [grilling](https://www.aihero.dev/ai-coding-dictionary/grilling) session, a written [spec](https://www.aihero.dev/ai-coding-dictionary/spec) — so there are fewer gaps for the agent to fill alone. During: [automated checks](https://www.aihero.dev/ai-coding-dictionary/automated-check) and [automated review](https://www.aihero.dev/ai-coding-dictionary/automated-review) stand in for the attention you're not giving, failing fast on what can be caught mechanically. After: the run ends in something reviewable — a PR, not changes already merged. AFK doesn't remove [human review](https://www.aihero.dev/ai-coding-dictionary/human-review); it defers all of it to the end, which is why what arrives at the end has to be worth reviewing. This is also why [AX](https://www.aihero.dev/ai-coding-dictionary/ax) matters most in AFK runs — with no one watching, the environment is the only support the agent gets.

*Avoid:* "background agent" — centers the machine ("running in the background") rather than the human pattern ("user has walked away"). AFK names the fact that matters: the user isn't watching.

*Usage:*

"I'm running this AFK — three sandboxed agents on the refactor, reviewing the PRs in the morning."

"Yeah, read-only [filesystem](https://www.aihero.dev/ai-coding-dictionary/filesystem), no network."
## Entry: human-in-the-loop

A working pattern where one or more humans pair with the [agent](https://www.aihero.dev/ai-coding-dictionary/agent) during a [session](https://www.aihero.dev/ai-coding-dictionary/session) — reviewing, redirecting, or collaborating in real time. The human is present and engaged, not just gating individual actions.

The contrast is with [AFK](https://www.aihero.dev/ai-coding-dictionary/afk) work, where the agent runs unattended and you judge the result afterwards. Human-in-the-loop means catching problems while they're still cheap: you see the agent reach for the wrong file, misread the requirement, or start down a dead end, and you redirect it in one sentence — rather than discovering twenty minutes of confident work built on that mistake. Agents don't reliably know when they're off track; left alone, they tend to push forward rather than stop and ask.

Which pattern fits depends on the work. Well-specified, low-risk, easy-to-verify tasks suit AFK. Tasks that are ambiguous, irreversible, or where you'd struggle to review the finished result — a schema migration, a tricky design decision, anything touching production — suit staying in the loop. The judgement call is essentially: how expensive is a wrong turn, and how late would you catch it?

Some work is in-the-loop by nature, because your reactions are the input. [Grilling](https://www.aihero.dev/ai-coding-dictionary/grilling) only works with you there to answer the questions; [prototyping](https://www.aihero.dev/ai-coding-dictionary/prototyping) only works with you there to react to the artifact.

Staying in the loop costs your attention, which is the scarce resource. Part of getting better with agents is moving more work safely out of the loop — with plans, [automated checks](https://www.aihero.dev/ai-coding-dictionary/automated-check), and [human review](https://www.aihero.dev/ai-coding-dictionary/human-review) at the end instead of supervision throughout. A [software factory](https://www.aihero.dev/ai-coding-dictionary/software-factory) takes this further by starting sessions from triggers, so even kicking off the work doesn't need you.

*Usage:*

"Run this AFK overnight?"

"No, schema migration — keep it human-in-the-loop. I want to see each step and steer if it picks the wrong column to backfill from."
## Entry: smart-zone

Early in a [session](https://www.aihero.dev/ai-coding-dictionary/session) the [agent](https://www.aihero.dev/ai-coding-dictionary/agent) is in a "smart zone" — sharp, focused, recall is good. As the session grows it drifts into a "dumb zone": sloppier, forgetful, more mistakes — and more faithfulness [hallucinations](https://www.aihero.dev/ai-coding-dictionary/hallucination). Same [model](https://www.aihero.dev/ai-coding-dictionary/model), same [harness](https://www.aihero.dev/ai-coding-dictionary/harness) — just more [context](https://www.aihero.dev/ai-coding-dictionary/context). The felt effect of [attention degradation](https://www.aihero.dev/ai-coding-dictionary/attention-degradation). On frontier models, the dumb zone commonly begins around 125K-150K [tokens](https://www.aihero.dev/ai-coding-dictionary/token) — though this is debated. [Clear](https://www.aihero.dev/ai-coding-dictionary/clearing) or [compact](https://www.aihero.dev/ai-coding-dictionary/compaction) when the session bloats; don't push through.

The decline is gradual, which makes it easy to miss. There's no error message and no visible boundary; the agent just starts performing slightly worse, then noticeably worse. Common signs: it forgets an instruction you gave twenty turns ago, repeats a mistake it had already corrected, or confidently asserts something the context contradicts. Because the slide is smooth, the usual response is to push through and re-explain — which adds more context and makes the problem worse.

The zones don't track the [context window](https://www.aihero.dev/ai-coding-dictionary/context-window) limit. A session can be deep in the dumb zone with most of the window still free: the limit is where the harness refuses to continue, but quality falls off long before that. Plan around the smart zone, not the window — the practical budget for a task is the tokens the agent works well within, not the tokens it can technically hold.

The smart zone is a budget, and unrelated work spends it. Every task done in a session uses up tokens, so starting a second task in the same session means starting it closer to the dumb zone. Doing one task per session gives each task the sharpest part of the session. When a single task is bigger than one smart zone, split it: [hand off](https://www.aihero.dev/ai-coding-dictionary/handoff) or compact at a natural boundary, and let a fresh session do the next piece.

*Usage:*

"It nailed the first three components and just butchered the fourth."

"You're out of the smart zone — same model, just deep into the dumb zone now. Compact and reload the plan, the next component will land."
## Entry: automated-check

A deterministic verification that runs in the [environment](https://www.aihero.dev/ai-coding-dictionary/environment) — tests, type checks, lints, build, pre-commit hooks. Pass/fail, no judgement. The signal an [agent](https://www.aihero.dev/ai-coding-dictionary/agent) can self-correct from without involving anyone else. A flaky test is a broken check, not a non-check; automated checks are deterministic *by design*.

Self-correction works as a loop. The agent makes a change, runs the check as a [tool call](https://www.aihero.dev/ai-coding-dictionary/tool-call), and the failure output lands in its [context window](https://www.aihero.dev/ai-coding-dictionary/context-window) — a type error with a file and line, a failing assertion with expected and actual values. That's enough for the agent to fix the problem and run the check again, around and around until it passes, with no human in the loop. Determinism is what makes the loop trustworthy: the same code always produces the same verdict, so a pass means something. A flaky check poisons this — the agent "fixes" code that was fine, or retries past a real failure.

This is why good checks are a large part of a codebase's [AX](https://www.aihero.dev/ai-coding-dictionary/ax). An agent in a repo with strict types, a fast test suite, and a linter catches most of its own mistakes before you see them; an agent in a repo with none of those ships whatever it produces. The difference matters most in [AFK](https://www.aihero.dev/ai-coding-dictionary/afk) runs, where checks are the only verification happening during the run. But a check only catches what it asserts — green checks mean the asserted properties hold, not that the code is right. The judgement-shaped gaps are what [automated review](https://www.aihero.dev/ai-coding-dictionary/automated-review) and [human review](https://www.aihero.dev/ai-coding-dictionary/human-review) are for.

*Avoid:* "feedback loop" / "backpressure" — both lump checks together with review. *Avoid:* "test" — tests are automated checks, but not all automated checks are tests.

*Usage:*

"The agent keeps shipping broken code in the AFK runs."

"What automated checks are wired into the [sandbox](https://www.aihero.dev/ai-coding-dictionary/sandbox)?"

"Just the unit tests."

"Add typecheck and lint — it'll self-correct from those before the PR ever lands."
## Entry: automated-review

An [agent](https://www.aihero.dev/ai-coding-dictionary/agent) reviewing another agent's work, often with a different [model](https://www.aihero.dev/ai-coding-dictionary/model) or [system prompt](https://www.aihero.dev/ai-coding-dictionary/system-prompt). Non-deterministic: it forms a judgement. Runs anywhere — pre-merge on a PR, post-hoc on commit history, mid-session as a [subagent](https://www.aihero.dev/ai-coding-dictionary/subagent). An LLM-as-judge in CI is automated review, not an [automated check](https://www.aihero.dev/ai-coding-dictionary/automated-check); what the assertion *does* decides the category, not where it runs.

The separation from the working agent is what makes it work. Asking the agent that wrote the code to review its own work gets you very little — the [session](https://www.aihero.dev/ai-coding-dictionary/session) that produced the bug also contains the reasoning that produced it, and the agent reads its own conclusions back as confirmation. A reviewer with a fresh [context window](https://www.aihero.dev/ai-coding-dictionary/context-window) has none of that attachment: it sees the diff the way a stranger would, which is what review depends on. A different model or a review-specific system prompt sharpens this further — different blind spots, and a system prompt scoped to what you actually care about (security, API contracts, performance) rather than a vague "look for problems".

It slots between the other review layers. Automated checks are deterministic and catch what can be asserted mechanically; [human review](https://www.aihero.dev/ai-coding-dictionary/human-review) is expensive and scales worst. Automated review sits in the middle: it catches judgement-shaped problems — a misleading function name, a missed edge case — at machine cost. Because it's non-deterministic, it can miss things and flag non-issues; treat it as a filter that raises the floor before a human looks, not a gate that replaces one.

*Avoid:* "AI review" / "agent review" — too vague to distinguish from the working agent itself.

*Usage:*

"We're getting too many bad PRs from the [AFK](https://www.aihero.dev/ai-coding-dictionary/afk) runs."

"Add an automated review step before merge — different model, separate system prompt, scoped to security and contract changes."
## Entry: handoff-artifact

A document used as the carry mechanism for a [handoff](https://www.aihero.dev/ai-coding-dictionary/handoff) — written to the [environment](https://www.aihero.dev/ai-coding-dictionary/environment) by one [session](https://www.aihero.dev/ai-coding-dictionary/session) to be read by another. [Specs](https://www.aihero.dev/ai-coding-dictionary/spec), [tickets](https://www.aihero.dev/ai-coding-dictionary/ticket), and plan docs are all handoff artifacts.

The reason to write one: the [model](https://www.aihero.dev/ai-coding-dictionary/model) is [stateless](https://www.aihero.dev/ai-coding-dictionary/stateless), so nothing in a session survives [clearing](https://www.aihero.dev/ai-coding-dictionary/clearing) it. Decisions, constraints, half-finished plans — all gone with the [context](https://www.aihero.dev/ai-coding-dictionary/context) that held them. The environment persists. Writing the important state into a file moves it somewhere the next session can read it back from.

The artifact is a [secondary source](https://www.aihero.dev/ai-coding-dictionary/secondary-source) — an account of the session's work, not the work itself. That's what makes it small enough to brief a fresh session, and also why it can mislead one: it records what the writing session believed, and anything it left out or got wrong is invisible to the reader. Where a claim matters, the next session should verify it against the [primary source](https://www.aihero.dev/ai-coding-dictionary/primary-source) — the code, the tests — rather than inherit it.

A good artifact is written to be read into a session that has zero context. Concrete file paths rather than "the file we discussed". What was decided and why, so the next session doesn't relitigate it. What's done and what's left. It helps to tell the writing session where the artifact is headed: "write a handoff doc for a fresh session that knows nothing about this work".

The alternative carry mechanism is [compaction](https://www.aihero.dev/ai-coding-dictionary/compaction), which summarises in-memory. The artifact has two advantages: it lives on disk where you can read and correct it before anything depends on it, and it can be reused — the same spec can brief five parallel sessions.

*Usage:*

"How do I split this between the planning [agent](https://www.aihero.dev/ai-coding-dictionary/agent) and the implementing one?"

"Have the planner write a handoff artifact — file paths, decisions, constraints. The implementer's session opens with a pointer to the artifact and works from it as its brief."
## Entry: harness

Everything around the [model](https://www.aihero.dev/ai-coding-dictionary/model) that turns it into an [agent](https://www.aihero.dev/ai-coding-dictionary/agent): [tools](https://www.aihero.dev/ai-coding-dictionary/tool), [system prompt](https://www.aihero.dev/ai-coding-dictionary/system-prompt), [context-window management](https://www.aihero.dev/ai-coding-dictionary/context-window), permissions, hooks. **Claude.ai** and **Claude Code** run on the same model but behave differently because their harnesses differ.

The model itself only does one thing: take text in, produce text out. It can't read a file, run a command, or remember the last [turn](https://www.aihero.dev/ai-coding-dictionary/turn). The harness supplies all of that. It assembles the [context](https://www.aihero.dev/ai-coding-dictionary/context) for each [model provider request](https://www.aihero.dev/ai-coding-dictionary/model-provider-request), executes the [tool calls](https://www.aihero.dev/ai-coding-dictionary/tool-call) the model asks for, feeds the [tool results](https://www.aihero.dev/ai-coding-dictionary/tool-result) back in, stores the [session](https://www.aihero.dev/ai-coding-dictionary/session) history, asks you for permission before risky actions, and decides when to [compact](https://www.aihero.dev/ai-coding-dictionary/compaction). The agent loop — model proposes, harness executes, repeat — is run by the harness.

This matters for diagnosis. When behaviour differs between two products, or between yesterday and today, the model is often not the variable — the harness is. A different system prompt, a different set of tools, a changed permission default, or a new context-management strategy all change behaviour without any change to the model. It also means the harness is where most of your configuration lives: [AGENTS.md](https://www.aihero.dev/ai-coding-dictionary/agents-md) files, permission settings, and hooks are all instructions to the harness, not the model.

Examples: Claude Code, Cursor, Codex CLI — and Claude.ai, which is a chat harness rather than a coding one.

*Usage:*

"Same model, why is Claude Code editing files and Claude.ai just answering questions?"

"Different harnesses — Claude Code has [filesystem](https://www.aihero.dev/ai-coding-dictionary/filesystem) tools, a different system prompt, and a permission layer. The model isn't the variable here."