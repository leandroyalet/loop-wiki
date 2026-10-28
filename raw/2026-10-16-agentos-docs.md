---
title: "AgentOS documentation (selected pages)"
url: https://agentos.to/
author: Joe Contini (agentos-to GitHub org; docs refer to "Joe")
published: unknown (docs repo agentos-to/site created 2026-04-14, last pushed 2026-07-17)
fetched: 2026-10-16
extraction: "HTML from agentos.to, <main> stripped to text; nav footers and 'Section titled' anchors removed. 16 of ~230 sitemap pages: the ones relevant to agent loops. Not ingested: per-shape reference (~90), per-service skill reference (~50), research/*, reverse-engineering/*, interfaces/mcp|cli|http, remaining architecture pages."
---

> Raw source. Immutable; do not edit. Summary lives in the wiki under sources/.



---
<!-- page: https://agentos.to/introduction/what-is-agentos/ -->

# What is AgentOS

“The hope is that, in not too many years, human brains and computing machines will be coupled together very tightly, and that the resulting partnership will think as no human brain has ever thought.” — J.C.R. Licklider, “Human-Computer Symbiosis,” 1960

AgentOS is a local operating system for human-AI collaboration. Your data stays on your machine. AI agents get real tools that work. You see everything they do. Together, you and AI think better than either can alone.

We’re building toward Licklider’s vision of human-computer symbiosis — not AI that replaces human thinking, but AI that amplifies it. The human sets direction, makes judgments, asks the right questions. The AI does the routinizable work that prepares the way for insight.

The agent is the primary customer. AgentOS is the operating system for agents, not around them.

## The pieces

The engine — a Rust binary that runs the graph (a SQLite database — the “memex”), executes skills, resolves auth, and speaks [MCP](/interfaces/mcp/) so any MCP-capable agent (Claude Code, Cursor, etc.) can use AgentOS as its tool surface.

[Skills](/skills/overview/) — Python adapters that connect to external services (macOS apps, cloud services, keychains) or act as pure agent tools. They declare the capabilities they provide (@provides(llm), @provides(web_search)), and the engine matchmakes requests to the best available provider.

[GUI](/apps/overview/) — an optional layer for humans (TypeScript/React, served by the engine, browsed via Tauri or a standard browser). Think Linux plus an optional desktop environment: the [CLI](/interfaces/cli/) and engine work fully without it.

The graph — your personal knowledge store. Everything is an entity; entities connect via relationships. It all lives in a single portable SQLite file at ~/.agentos/data/agentos.db.

Skills and apps never know about each other. The engine is the sole broker — security by architecture.

## The graph

“Consider a future device… in which an individual stores all his books, records, and communications, and which is mechanized so that it may be consulted with exceeding speed and flexibility.” — Vannevar Bush, “As We May Think,” 1945

We call your graph your memex, after Vannevar Bush’s 1945 vision of a personal device for storing, linking, and traversing all of one’s knowledge. Everything is an entity, and entities connect through relationships. The graph doesn’t care where data came from (Todoist, iMessage, YouTube) — it cares about what things are and how they connect.

A task, a person, a message, a video, a webpage, a calendar event — they’re all entities in your graph. Relationships are the connections between them. This isn’t just a database design. It’s a way of thinking. When you ask “what am I working on?” the answer isn’t in one app — it’s in the connections between your tasks, your messages, your calendar, the people involved. The graph makes those connections visible.

Your memex is a portable SQLite file — your entire mind in a .db file. Copy it, back it up, load it on another machine. Domain memex (astronomy, law, medicine) can be mounted read-only into agent simulations — plug in expertise like a CD-ROM. When AgentOS users connect to each other, their memex form a network — Licklider’s intergalactic network, but for knowledge graphs instead of terminals.

Everything is an entity means:

- A YouTube channel is a community. A YouTube comment is a post. A transcript is a document.

- A WhatsApp contact and an iMessage contact with the same phone number are the same person.

- A skill that connects to a service is itself an entity. The system models itself.

- If something exists and has properties and relationships, it belongs in your graph.

The graph is the foundation. Every feature — search, feeds, timelines, recommendations, agents — reads from the same graph. Get the graph right, and features compose naturally. Get it wrong, and everything built on top is a special case.

## Local and remote are the same thing

People are used to two mental models for files: local (on my computer, only changes when I change it) and cloud (iCloud, Dropbox, Drive — somewhere out there, syncing in the background). These feel like different things. AgentOS dissolves that boundary.

A document in your graph can be backed by a local file, a GitHub repo, an API response, or all three simultaneously. The NEPOMUK ontology calls this the separation between content (the information itself) and storage (where it lives). One document, many access paths. The graph tracks the content; skills handle the storage.

## What it looks like when it works

You say: “What did I miss this week?”

The agent queries your graph: messages received, tasks completed by others, calendar events that happened, posts from communities you follow, videos published by channels you subscribe to. It cross-references people — who sent messages AND completed tasks AND posted content. It notices patterns — “Sarah mentioned the project in Slack, completed 3 tasks in Linear, and posted a video update.”

All of this from one graph. No special integrations. No “Slack + Linear” connector. Your graph already has the entities and relationships. The agent just traverses.

That’s the vision. We’re not there yet. But every entity we model correctly, every relationship we capture, every skill we build — it gets closer.

   [   Next  Inspiration  ](/introduction/inspiration/)


---
<!-- page: https://agentos.to/introduction/two-users/ -->

# The two users

    AgentOS serves humans and AI agents as equal first-class citizens. Each has a different core problem, and the whole system is shaped by both.

## For humans: anxiety

Anxiety = Uncertainty × Powerlessness

When AI acts, you feel uncertain (“what is it doing?”) and powerless (“can I stop it?”). AgentOS solves both:

- The AI screen-shares with you — uncertainty drops to zero.

- You control what it can do — powerlessness drops to zero.

If either factor is zero, anxiety is zero. This is the reason the human-facing layer exists at all: to keep the human in the loop, seeing everything and in control of everything.

## For agents: error propagation

Error Rate = f(Dependency Depth)

Every round-trip is a chance for errors to compound. We collapse complexity: smart defaults, self-teaching responses, schema validation, minimal round-trips. If a small local model can complete the task, we’ve done our job.

The customer is the smallest model. Not Opus. Not Sonnet. The smallest model that can do tool calling — a 1B-parameter model running on a Raspberry Pi with a 4K context window. If that model can read our readme, understand the domain, and complete a task on the first try, we’ve succeeded. If it can’t, no amount of capability in larger models compensates for the failure.

This is our accessibility standard: design for the most constrained agent, and every agent benefits.

## Why this matters beyond agents

These principles make the system better for humans too. A readme that a 1B model can follow is a readme a new contributor can follow. An API that minimizes round-trips is an API that’s fast. Dynamic responses that include context are responses that save everyone’s time.

Designing for the most constrained user has always been the shortcut to designing for everyone. The accessibility movement proved this for humans. We’re proving it for agents.

For the full practice of designing-for-agents, see [Agent empathy](/skills/agent-empathy/).

  [   Previous  Inspiration  ](/introduction/inspiration/) [   Next  Roadmap & proposals  ](/introduction/roadmap-and-proposals/)


---
<!-- page: https://agentos.to/introduction/how-we-build/ -->

# How we build

    We are co-CTOs — human and AI — making strategic decisions together. This is not task execution. It’s collaborative architecture.

## The posture

- Foundation first. The most foundational thing that prevents tech debt is always the priority. Not quick wins, not “almost done” items, not cleanup. The thing everything else builds on.

- Spec before code. Design the right thing, then build it. A wrong implementation done fast is worse than no implementation.

- Delete fearlessly. No attachment to past code. If the model changes, the code changes. We write for the current best understanding, not for backwards compatibility.

- Infinite time horizon. No customers, no deadlines, no pressure to ship. The right architecture at the right time.

- Pain-driven. If you can’t articulate the pain, don’t build it.

- Blast radius is not a cost — stale architecture is. An “audacious” refactor that touches the engine and every skill in one shot is not more expensive than a one-line fix. Pre-launch means zero migration cost.

See [Architectural laws](/architecture/architectural-laws/) for the full rule set.

## Skills

Each skill is a directory with a readme.md (YAML frontmatter for identity + connections, markdown body for the agent-facing guide) plus one or more .py files whose @returns-decorated functions are the tools. No separate manifest — operations are extracted from the Python AST at load time. The community repo tracks shipped skills under skills/.

Start at the [Skills overview](/skills/overview/).

## Shapes

The ontology is a directory of YAML files — one shape per file — at docs/shapes/. Shapes describe entity types (fields, relations, display hints, operations). Add a shape, reseed, restart the engine; the graph now knows about a new entity type. No Rust change required.

Read the [Shape design principles](/shapes/shape-design-principles/) before proposing a new shape.

## Apps

TypeScript/React UIs for humans. Each app is self-contained and built against @agentos/sdk from the sdk-apps/ sibling repo. Apps never talk to skills directly — they ask the engine for a capability, the engine routes to a skill that @provides(...) it.

See [Apps overview](/apps/overview/).

## Proposals & roadmap

Design thinking lives in _roadmap/ — pain, proposal, review, closeout. The pipeline is described in [Roadmap & proposals](/introduction/roadmap-and-proposals/).

Proposals must include prior art. Don’t design in a vacuum — search for how others solved similar problems before proposing.

## Build discipline

- Test through real services, not mocks. No unit tests. Integration tests via MCP against the running engine.

- Architecture over quick. Always choose the right long-term architecture. No shortcuts.

- Dogfooding is the whole point. Every session, building with the SDK should get easier. DX wins beat feature wins. If something isn’t intuitive, improve the SDK, don’t work around it.

   [   Next  Overview  ](/architecture/overview/)


---
<!-- page: https://agentos.to/introduction/inspiration/ -->

# Inspiration

    AgentOS draws from decades of research in knowledge representation, personal information management, and human-computer interaction. We cite our influences because they deserve it, and because understanding where ideas come from is itself a graph.

## The visionaries

- Vannevar Bush — “As We May Think” (1945). The memex: a device for storing, linking, and traversing personal knowledge. Our memex concept — a portable SQLite knowledge graph — is his vision, built 80 years later.

- J.C.R. Licklider — “Human-Computer Symbiosis” (1960), the “Intergalactic Computer Network” memo (1963). The foundational vision of humans and computers as partners. Our social layer — memex connecting to other memex — is named for his intergalactic network.

- Doug Engelbart — “Augmenting Human Intellect” (1962), “The Mother of All Demos” (1968). Interactive computing, hypertext, shared screens. His “knowledge workshop” concept is what AgentOS simulations are.

- Ted Nelson — coined “hypertext” and “hypermedia.” Project Xanadu: bidirectional links, transclusion, the dream of a universal document network. His “docuverse” anticipated the graph-as-world concept.

- Alan Kay — Dynabook, Smalltalk. The computer as a medium for human expression.

- Claude Shannon — information theory (1948). Proved that knowledge is measurable and transmittable. The namesake of Anthropic’s Claude.

- Alan Turing — the Turing machine, computable numbers, “can machines think?” The theoretical foundation for everything.

- Bret Victor — Inventing on Principle. Direct manipulation, immediate feedback, tools that match how humans think.

## The ontologies

- NEPOMUK — the Semantic Desktop. Content vs. storage separation, personal information ontologies.

- Dublin Core — 15 essential metadata elements for describing any document. The library science foundation.

- Schema.org — structured data vocabulary for the web. CreativeWork, Person, Organization.

- ActivityStreams / ActivityPub — the fediverse protocol. Decentralized social data.

- W3C PROV-O — provenance ontology. Why changes are first-class entities in our graph.

## How this shows up in the code

These aren’t credits in a footer. They’re architectural. The memex is the graph. The intergalactic network is how memex will connect to each other. PROV-O is why every change is an entity on the graph. Schema.org is where a lot of our shape naming comes from.

See [Research](/research/ontology/relationship-modeling/) for deeper dives on specific ontologies and platforms we’ve studied.

  [   Previous  What is AgentOS  ](/introduction/what-is-agentos/) [   Next  The two users  ](/introduction/two-users/)


---
<!-- page: https://agentos.to/introduction/roadmap-and-proposals/ -->

# Roadmap & proposals

    Design thinking for AgentOS lives in a design-thinking pipeline, not in scattered GitHub issues. Every non-trivial change flows through the same four artifacts.

## The pipeline

Each project is a folder with files in pipeline order:

-
```

pain.md         What's broken and why it matters

proposal.md     The plan (required: prior art / web research)

review.md       Adversarial review (one or more rounds: v1, v2, …)

closeout.md     What actually shipped vs. what was proposed

```

No numeric prefixes — files sort alphabetically, and that matches the pipeline order well enough.

## Priorities

```

_roadmap/

  p1/             Priority 1 — active

  p2/             Priority 2 — queued

  p3/             Priority 3 — backlog

  _archive/       Completed projects (historical record)

  _drafts/        Rejected proposals (kept for rationale)

  _research/      Background research informing proposals

```

The priority is the parent folder — moving a project between p2/ and p1/ is how prioritization is recorded. Completed projects graduate to _archive/. Rejected proposals go to _drafts/ (the rationale is often more useful than the proposal itself).

## Why it’s separate from the engine

Engine repos (core, skills, site, apps) stay focused on code and the ontology. Roadmap material is design thinking — reasoning about architecture, not the architecture itself. Mixing them pollutes git history with churn that has no bearing on the engine and leaks half-formed ideas into the public surface.

_roadmap/ is private. Nothing there is API.

## The role of adversarial review

Proposals get adversarial reviews — an agent (or Joe) reads the proposal and tries to break it. Typical review output:

- Is the pain real and clearly articulated?

- Does the proposal actually solve it, or just the symptoms?

- What prior art was missed?

- What’s the weakest link? What assumption, if wrong, collapses the plan?

- Where are the escape hatches? If this is wrong, can we roll back, or does it lock us in?

A single critical blocker means revise. All critical pass means implement. See [Agent empathy → Scoring](/skills/agent-empathy/) for why we use pass/fail/partial labels instead of numeric scores.

## Closeout

After a project ships, a closeout.md captures what actually happened vs. what was proposed. This is how the pipeline learns. Closeouts feed into future proposals as prior-art references.

## See also

- [How we build](/introduction/how-we-build/) — the posture behind the pipeline.

- [Architectural laws](/architecture/architectural-laws/) — the rules a proposal is evaluated against.

  [   Previous  The two users  ](/introduction/two-users/) [   Next  Overview  ](/apps/overview/)


---
<!-- page: https://agentos.to/architecture/overview/ -->

# Overview

    AgentOS is a Rust engine that brokers between Python [skills](/skills/overview/) (that write to the graph) and [apps](/apps/overview/) (that read from it). The engine is the matchmaker: apps ask for capabilities, the engine picks a skill that provides them, and neither side learns the other’s name.

The entire system is built from a small number of primitives. Learn these and the rest of the docs fall into place.

## The graph

Three kinds of thing live in SQLite at ~/.agentos/data/agentos.db:

- Nodes — bare identities. A node has an ID and timestamps; nothing else.

- Edges — labeled, directional links between two nodes (tagged_with, replied_to, parent).

- Values — keyed fields on a node or an edge (name = "Joe", done = true).

That’s the whole schema. There is no “tasks” table, no “messages” table, no type column on nodes. Semantic types are defined by [shapes](/shapes/overview/) — YAML files loaded into the graph at engine startup. The engine is shape-aware but entity-agnostic: it can coerce priority (integer) without knowing what “priority” means.

Read more: [Memex & the graph](/shapes/memex-and-graph/) · [Identity & change](/shapes/identity-and-change/)

## The four boundaries

Data moves across four inter-process boundaries. Understanding these is how you reason about security, failure modes, and where code belongs.

### 1. [MCP](/interfaces/mcp/) STDIO → engine socket

AI clients (Cursor, Claude Code, Claude Desktop) speak Model Context Protocol over STDIO to agentos-mcp, a thin proxy. The proxy translates MCP calls to JSON-RPC and forwards them over the engine’s Unix socket.

### 2. Engine Unix socket (~/.agentos/engine.sock)

The engine daemon is a single Rust binary. One engine per machine, enforced by a flock on ~/.agentos/engine.lock. The socket accepts JSON-RPC from MCP, from the agentos [CLI](/interfaces/cli/), and from the web bridge. Everything funnels through here.

### 3. Python subprocess dispatch

Skills are Python. When a skill is called, the engine spawns a fresh Python subprocess, loads the skill module, and runs the SOP. The SDK in the worker (from agentos import http, secrets, sql) forwards requests back to the engine over a wire protocol — every outbound HTTP call, every credential lookup, every graph write returns to the engine for brokering.

Per-call subprocess, not a long-lived daemon. Clean exit, no shared state between skill runs.

### 4. Web bridge HTTP (127.0.0.1:3456)

Optional. For apps that want a browser UI, the web bridge serves /graph, /observer/stream (SSE), /user, and /shapes from a read-only SQLite connection. The engine retains write monopoly.

## What runs where

-
```

flowchart LR

    AI["AI client<br/>(Cursor, etc)"] -->|STDIO| MCP["agentos-mcp<br/>(proxy)"]

    MCP -->|JSON-RPC<br/>Unix sock| ENG["Engine daemon<br/>(Rust, Tokio)"]

    ENG -->|subprocess| PY["Python skill worker<br/>(reads, writes, http, auth)"]

    ENG -->|SQLite pool| DB["~/.agentos/data/agentos.db<br/>(graph + encrypted creds)"]

    ENG -->|HTTP :3456| BR["Web bridge"]

    BR --> APPS["apps (React, TS)"]

```

|STDIO| MCP["agentos-mcp
(proxy)"]    MCP -->|JSON-RPC
Unix sock| ENG["Engine daemon
(Rust, Tokio)"]    ENG -->|subprocess| PY["Python skill worker
(reads, writes, http, auth)"]    ENG -->|SQLite pool| DB["~/.agentos/data/agentos.db
(graph + encrypted creds)"]    ENG -->|HTTP :3456| BR["Web bridge"]    BR --> APPS["apps (React, TS)"]">

## The capability broker

Skills never name apps. Apps never name skills. They meet through capabilities.

A skill declares what it offers with a decorator:

```

@provides("llm")

def chat(messages): ...

```

An app asks for a capability by name:

```

await agentos.capability("llm").invoke({ messages })

```

The engine picks the skill. If you install five LLM skills, the engine resolves by user preference and freshness — no hardcoded provider order. If a skill is uninstalled, dependent apps keep working as long as some skill provides the capability.

This is the decoupling law. Installing or uninstalling an app has zero impact on skills, and vice versa. The engine is the sole broker.

[Security](/architecture/security/) explains why this matters for trust and auth.

## Where state lives

```

~/.agentos/

  data/agentos.db        The graph + encrypted credentials (one SQLite file)

  logs/                  engine.log, mcp.log, engine-io.jsonl

  engine.sock, mcp.sock  IPC endpoints

  engine.pid, engine.lock  Singleton guards

```

One directory. Portable. Back it up, copy it, nuke it. [Local-first](/architecture/local-first/) explains what is and isn’t committed to that directory.

  [   Previous  How we build  ](/introduction/how-we-build/) [   Next  Design principles  ](/architecture/design-principles/)


---
<!-- page: https://agentos.to/architecture/design-principles/ -->

# Design principles

    These are the first-principles rules that hold the system together. Every architectural decision traces back to one of them.

## Everything on the graph

No shadow tables, no side stores, no parallel data structures. If something is worth tracking — changes, provenance, audit trails, agent memory — it’s an entity with relationships. If you find yourself designing a separate SQL table for something, stop and model it as entities instead.

## Computed, not stored

Properties that can be derived from the graph are never stored as fields — they’re computed at query time or inferred by traversal. A task’s status is computed from its completion state and blockers. A contact card is a view computed from graph traversals over a person’s claimed accounts. The graph stores atoms; intelligence computes molecules.

See [Shape design principles](/shapes/shape-design-principles/) for how this shapes the ontology — in particular #2 no counts on shapes.

## The user owns the graph

[Skills](/skills/overview/) are connectors, not owners. They sync data in, but the graph is the authority. Installing a skill imports data; uninstalling it doesn’t delete what was imported. “Source of truth” is the graph, always — skills are remotes you pull from, not landlords who control your data.

## Changes are entities

When an entity is created, updated, or deleted, the operation itself becomes a change entity on the graph. A change has relationships to the actor (who did it), the target (what changed), and optionally the source (where data came from). This follows the pattern established by W3C PROV-O, ActivityStreams, and Git: make events first-class objects, not edges. Provenance isn’t a static field — it’s the full chain of change entities. Walk backwards to reconstruct any previous state.

See [Identity & change](/shapes/identity-and-change/).

## Every actor has an identity

The human owner, each AI agent, and the system itself — all are entities on the graph. When the human edits a task, the change is attributed to them. When an agent creates a plan, it’s attributed to that agent. Every change has a who. This is identification, not authentication — on a single-user local system, localhost binding is the access boundary.

## The graph bootstraps itself

Entities describe data. But entities, skills, and relationships are also data. The system models itself — skills as entities, schemas as entities, the meta-layer that describes the graph. This is how the system becomes self-aware and self-documenting.

## Three concerns

Entities, skills, and apps are independent concerns that compose into the full experience.

Entity types define the ontology — what things are. A video has a title, duration, and view count. A person has a name and relationships. You can have entities without skills (manually entered data).

Skills are the capability layer — connecting to external services, providing agent instructions. A YouTube skill knows how to fetch video metadata. A Todoist skill knows how to create tasks via their API. Skills can also be pure markdown — instructions that help AI agents understand a domain, with no API bindings at all. You can have skills without apps (AI-only workflows).

[Apps](/apps/overview/) are optional UI experiences for humans. The Videos app renders video entities with an embed player. The default entity viewer renders any entity with schema-driven components. A headless AgentOS — API and AI only — works perfectly without apps. You can have apps without skills (local-only data).

## See also

- [Architectural laws](/architecture/architectural-laws/) — the structural constraints that keep the engine generic.

- [Agent empathy](/skills/agent-empathy/) — the practice of building for the smallest model.

- [Shape design principles](/shapes/shape-design-principles/) — how these apply at the ontology level.

  [   Previous  Overview  ](/architecture/overview/) [   Next  Architectural laws  ](/architecture/architectural-laws/)


---
<!-- page: https://agentos.to/architecture/architectural-laws/ -->

# Architectural laws

    The laws of the codebase. Every change is evaluated against these.

## 1. Rust is a generic engine

The Rust code knows about entities, relationships, schemas, and operations. It never knows about “tasks”, “messages”, “people”, or any specific entity type. Zero entity-specific or relationship-specific code in Rust. Hard no.

If you see any of these in Rust, raise it immediately — it’s a bug in the architecture:

- Hardcoded field names (priority, done, blocks, blocked_by)

- Grouping, sorting, or partitioning logic for specific entity types

- Display/formatting/rendering decisions for specific entity types

- Conditional branches on entity type names

- Bespoke data-fetching functions for specific entity types

Where specific behavior belongs:

LayerResponsibilityFormat
Entity schemasProperties, validation, display hints, sort order, operationsShape YAMLs (docs/shapes/)
TemplatesRendering, layout, grouping, formattingMiniJinja markdown
SkillsAPI mappings, field transformsPython + YAML frontmatter

## 2. Templates do the work

Rendering is never the Rust code’s job. Rust provides small, composable filters — listing, table, tree, props. Templates compose them. Layout decisions live in templates, never in Rust.

A filter should do one thing. If a filter is making layout decisions (choosing headings, grouping by priority, separating done/not-done), it’s too big. Break it up.

## 3. Foundation first

The most foundational work that prevents tech debt, always. If you’re choosing between a feature and fixing an abstraction, fix the abstraction.

## 4. The graph is the source of truth

Every entity modeled correctly, every relationship captured. Skills sync data in; the graph is the authority for reads.

## 5. We have infinite time

No customers, no deadlines, no shortcuts. Do it right or don’t do it.

## 5b. Blast radius is not a cost — stale architecture is

AgentOS is pre-launch with zero users, no data to protect, no backward compatibility, no migration path. An “audacious” refactor that touches the Rust dispatch pipeline, the SDK bridge, every executor, and every skill in one shot is not more expensive than a one-line fix — the constraint is correctness, not disruption.

When you find a bug, ask: is this a leaf symptom, or is there an inconsistency in the abstraction underneath? If two code paths exist where one would do, two wire-format shapes exist where one would do, or a sync wrapper sits on top of an async call, the right fix is to delete the asymmetry at the root — even if it means rewriting the executor, the bridge, and every caller.

The hardest, most audacious appropriate refactor is usually the right answer. Small safe patches that leave the inconsistency in place are worse than large refactors that remove it. Reject pragmatic band-aids in code review. Reward scope in proposals. When in doubt, tear it up and do it right.

Caveat: “appropriate.” This is not a license to burn down code that is correct just because it looks ugly. The trigger is a root-cause inconsistency you can name. If you can’t name the inconsistency, the refactor isn’t audacious — it’s churn.

## 6. Co-CTOs

Present the hard design question, decide together. Don’t make big architectural choices silently.

## 7. Pain-driven

If you can’t articulate the pain, don’t build it.

## 7b. Delete dead code on sight

Pre-launch means zero legacy obligations. Code containing any of these signals should be challenged in every review:

- legacy, compat, backwards, deprecated, migration, fallback

- TODO remove, TODO delete, temporary, one-time, workaround

- Feature flags, capability checks for removed features, commented-out code

- Silent-skip branches (exit 0 on failure, empty catch blocks that swallow errors)

- Fallback chains (“try X, if that fails try Y”) where only one path is correct

- URL redirects preserving old paths — move pages, update links, delete the old URL. No redirects.

The question is always: does this still serve a purpose? If not, delete it — don’t comment it out, don’t leave it “for reference,” don’t rename it with an underscore. Git has the history if we ever need it back.

## The Campsite Rule

Leave every module better than you found it. Before writing code, ask yourself: Is anything bugging me about these abstractions, naming, or architecture? If yes — tell the user. Propose the cleanup before moving forward.

  [   Previous  Design principles  ](/architecture/design-principles/) [   Next  Security  ](/architecture/security/)


---
<!-- page: https://agentos.to/architecture/security/ -->

# Security

    Security in AgentOS is not a layer of permissions bolted onto a permissive core. It’s the shape of how the pieces connect. If two components can’t name each other, they can’t trust each other, and the engine remains the only broker.

## Capability brokering

Skills and apps never know about each other. This is the load-bearing invariant.

A skill declares what it provides:

-
```

@provides("llm")

def chat(messages): ...

```

An app asks for a capability:

```

await agentos.capability("llm").invoke({ messages })

```

Between those two calls, the engine picks the skill. Neither side learns the other’s identity. Uninstalling a skill has zero runtime impact on apps as long as some skill still provides the capability. Uninstalling an app is invisible to skills.

This isn’t a policy check. It’s a name-resolution architecture. There is no API an app could call that would let it invoke a specific skill by name — the engine’s dispatch layer only takes capabilities.

## Connections are sandboxed identities

Every time a skill reaches an external service, it does so through a
connection — a module-level connection("name", ...) declaration
in the skill’s .py file. Each connection is a sandboxed identity
profile with its own cookies, its own auth, and its own mode. Tools
on different connections never share state.

Isolation is by construction, not by policy check:

- Connections key into the credential store on (domain, identifier), not (skill, connection_name). The connection’s
base_url derives the domain (api.exa.ai →  exa.ai). Two
skills that both declare a connection named portal don’t
collide — they resolve to different domains because their
base_urls point at different services.

- Cookies live in two jars. The credential store is the
persistent vault — encrypted at rest, keyed on (domain, identifier). The per-call jar is ambient inside the SDK for
the duration of one tool call — seeded from the store on entry,
diffed back on exit. Plaintext cookies exist only in the Python
worker’s memory, only while the tool body runs.

- A compromised skill cannot reach across identities. Its
resolved connection maps to exactly one credential row. It has
no way to enumerate rows, open a jar for a different domain, or
read another connection’s cookies.

- Skill rename / reorganize is safe. Move amazon.py, rename
its web connection to account — cookies stay put because
they’re keyed on amazon.com, not on the skill’s directory.

See [Connections as browsers](/architecture/connections-as-browsers/)
for the full model, including the three modes (browser, fetch,
api), the per-call jar lifecycle, and how Set-Cookie writeback
keeps rotating session tokens current across engine restarts.

## Auth resolution — freshest wins

When a skill needs a session (cookie, bearer token, OAuth pair), it asks the engine via the SDK. The engine looks in three places:

- In-memory cache — resolved sessions from the current engine lifetime.

- Credential store — encrypted entries in ~/.agentos/data/agentos.db.

- Browser providers — live extractions from Brave / Firefox / Chrome via CDP.

Each candidate carries a per-cookie timestamp. The freshest candidate wins. There is no fixed priority, no provider ranking. A recently-extracted browser session beats an older stored credential, even if the store entry was “configured” first.

The engine then runs the skill’s own account.check on the resolved session to validate identity. If check fails, the engine falls through to the next candidate. Skills see only the resolved session — never the raw credential store, never another source’s entry.

## Encryption at rest

Credential values in the database are encrypted with AES-256-GCM. The 32-byte key lives in the macOS Keychain under service "AgentOS Credential Store", account "encryption-key", and is read once per engine lifetime into a OnceLock.

- Key generation — first run generates 32 random bytes via getrandom and writes to Keychain through the security CLI.

- Nonce — 12-byte random nonce per encryption, standard for GCM.

- Key never on disk — the database contains ciphertext + nonce + auth tag; the key only ever lives in the Keychain and process memory.

If Keychain is unreachable (non-macOS, locked), the credential store currently falls back to unencrypted with a warning. That fallback is a known rough edge, not a design goal.

## What the engine refuses to do

The Rust engine is a generic entity store. It knows about nodes, edges, values, shapes, operations. It does not know about tasks, messages, people, or any specific entity type.

Things the engine will not do:

- Hardcode a field name (priority, done, blocks, blocked_by).

- Branch on an entity type’s name.

- Sort, group, partition, or render based on entity type.

- Call out to a bespoke fetcher for a specific kind of record.

Violations are architecture bugs, caught at code review. The reason is structural: if the engine grows an opinion about what a “task” is, then skills and apps can no longer define new entity types without modifying the Rust binary. The ontology lives in [shapes](/shapes/overview/), not in the engine.

## Boundaries and trust

Each of the [four boundaries](/architecture/overview/#the-four-boundaries) is a trust boundary:

BoundaryTrust relationship
MCP STDIO → agentos-mcpLocal-only; MCP client is trusted to act on the user’s behalf.
agentos-mcp → engine socketUnix socket, filesystem-permission-gated.
Engine → Python subprocessSkill runs user-space; SDK dispatches back for any side-effect.
Engine → web bridge (HTTP)Localhost only (127.0.0.1:3456). Read-only DB handle; writes go through the engine socket.

A compromised skill can’t touch the credential store directly — it has to dispatch a secrets.get(...) back to the engine, which applies the auth-resolution policy above. A compromised app can’t write to the graph directly — its HTTP reads are served from a read-only connection; writes require a capability call.

## Honest caveats

A few things that CLAUDE.md and the principles assert but the code does not fully enforce:

- Decoupling is SDK-layer, not engine-layer. Nothing in the engine binary stops a rogue skill from hardcoding an app name in a dispatch. The isolation is convention + decorator patterns, enforced at skill validation and code review.

- Multi-device is not implemented. The graph is portable (one file, copy it), but there is no sync daemon, conflict resolution, or merge layer. If two machines edit the same graph file, last-writer-wins via filesystem timestamps.

- Keychain fallback is unencrypted. On systems without Keychain, the credential store currently emits a warning and stores values in plaintext.

See [Architectural laws](/architecture/architectural-laws/) for the full structural constraints.

  [   Previous  Architectural laws  ](/architecture/architectural-laws/) [   Next  Local-first  ](/architecture/local-first/)


---
<!-- page: https://agentos.to/architecture/observer-bus/ -->

# Observer bus

    The observer bus is how AgentOS turns every tool call into a live event you can watch from a browser. The [HTTP page](/interfaces/http/) shows the two routes (/observer/history, /observer/stream); this page is the deep dive — what’s behind those routes, why it’s shaped the way it is, and how it survives restarts and slow consumers.

## The bus

At the heart of the engine is a single in-process [tokio::sync::broadcast](https://docs.rs/tokio/latest/tokio/sync/broadcast/index.html) channel:

-
```

static OBSERVER_EVENTS: Lazy<broadcast::Sender<Value>> = Lazy::new(|| {

    let (tx, _) = broadcast::channel(256);

    tx

});

```

> = Lazy::new(|| {    let (tx, _) = broadcast::channel(256);    tx});">

core/crates/engine/src/lib.rs:130-133. One sender, many receivers. Anything in the engine can call observer_events::emit(&event); every active subscriber sees a clone.

Why broadcast and not mpsc? mpsc is a queue: each item is consumed by exactly one receiver. The observer bus has the opposite shape — N independent consumers that all want the same stream. The CLI’s agentos watch, the bridge’s SSE endpoint, an mcp-watch debugger, and a future TUI can all subscribe simultaneously without stealing events from each other. Each subscribe() returns a fresh Receiver that begins reading from the channel head at the moment of subscription (lib.rs:135-137).

## Event lifecycle

A single tool call (graph read, skill run, etc.) emits at three points:

PhaseSiteWhen
startedlib.rs:447Before dispatch, with start_body placeholder (“Searching…”, “Loading…”).
completedlib.rs:533On success, with latency_ms and the rendered result.
failedlib.rs:547On error, with latency_ms and the error string.

Display metadata (title, address, icon, body_markdown, accent_color) is computed by observer_display() (lib.rs:236-273) and embedded into every event so consumers don’t have to re-derive it. Skill colors are looked up from the skill manifest at emit time.

```

flowchart TD

    H["engine handler<br/>call_tool()<br/>lib.rs:430"] -->|"observer_event(...)"| BC["broadcast::Sender&lt;Value&gt; (cap 256)<br/>lib.rs:130"]

    BC -->|"fan-out (clone per subscriber)"| S1["observer.sock<br/>conn #1"]

    BC --> S2["observer.sock<br/>conn #2"]

    BC --> CLI["CLI watcher<br/>(subscriber)"]

    S1 -->|"JSON line + '\n' — write_observer_line lib.rs:390"| WB["web bridge<br/>tail + filter<br/>connect_observer() web-bridge/src/lib.rs:68"]

    WB -->|SSE frame| ES["EventSource<br/>(browser)"]

```

|"observer_event(...)"| BC["broadcast::Sender&lt;Value&gt; (cap 256)
lib.rs:130"]    BC -->|"fan-out (clone per subscriber)"| S1["observer.sock
conn #1"]    BC --> S2["observer.sock
conn #2"]    BC --> CLI["CLI watcher
(subscriber)"]    S1 -->|"JSON line + '\n' — write_observer_line lib.rs:390"| WB["web bridge
tail + filter
connect_observer() web-bridge/src/lib.rs:68"]    WB -->|SSE frame| ES["EventSource
(browser)"]">

The observer connection handler (handle_observer_connection, lib.rs:1537) calls subscribe(), optionally drains a history prefix from the graph, then loops rx.recv() → write_observer_line().

## Event taxonomy

Every event is a JSON object. Two flavors share the wire — live events from observer_event() and history events from observer_history_event() — distinguished by phase.

phasetool examplesNotable fields
startedread, search, run, boot, create, delete, accountsrequest_id, skill?, operation, arguments, display
completedsameadds latency_ms, result
failedsameadds latency_ms, error
historyactivityreplayed past activity from graph::observer_history; display.title is the activity summary
lagged—broadcast receiver fell behind; error carries the skipped count (lib.rs:1615-1631)
history_failed—observer history query failed during the prefix replay

Every event carries ts, session_id, client, working_dir, and a display block (title, address, icon, body_markdown, accent_color). See observer_event() at lib.rs:275-306 for the exact schema.

A concrete completed payload for a Goodreads skill call:

```

{

  "ts": "2026-04-14T11:42:08.317",

  "request_id": "req-918",

  "phase": "completed",

  "tool": "run",

  "skill": "goodreads",

  "operation": "get_book",

  "session_id": "claude-code-9f3b",

  "client": "Claude Code",

  "working_dir": "/Users/joe/dev/agentos",

  "arguments": { "skill": "goodreads", "tool": "get_book",

                 "params": { "isbn": "9780140449136" } },

  "display": {

    "title": "goodreads · get_book",

    "address": "9780140449136",

    "icon": "⚡",

    "body_markdown": "## Meditations\n*Marcus Aurelius* · 254 pages",

    "accent_color": "#8a5a44"

  },

  "latency_ms": 412,

  "result": { "isbn13": "9780140449136", "title": "Meditations", "...": "..." },

  "error": null

}

```

## Buffering, ordering, back-pressure

The channel capacity is 256 events (lib.rs:131). Tokio’s broadcast is a ring: when the buffer fills and a new event is sent, the oldest event is dropped from the buffer for any receiver still pointing at it. That receiver’s next recv() returns RecvError::Lagged(n) carrying how many events it missed.

The observer connection handler turns that into a synthetic event rather than disconnecting:

```

Err(broadcast::error::RecvError::Lagged(skipped)) => {

    let notice = json!({ "phase": "lagged",

                         "error": format!("observer client skipped {} events", skipped),

                         /* ... */ });

    if !write_observer_line(&mut write_half, &notice).await { break; }

}

```

 {    let notice = json!({ "phase": "lagged",                         "error": format!("observer client skipped {} events", skipped),                         /* ... */ });    if !write_observer_line(&mut write_half, &notice).await { break; }}">

lib.rs:1615-1631. The slow consumer keeps its connection but learns it lost N events. Fast events are never blocked by slow consumers — broadcast is lossy by design, which is the right trade for telemetry.

The bridge has its own back-pressure story. connect_observer() retries up to 20 times with 250 ms between attempts (web-bridge/src/lib.rs:68-83) — enough to ride out an agentos restart (~10 s) while the engine relays its singleton lock and reopens observer.sock. After 20 attempts it gives up and the route returns 503 SERVICE_UNAVAILABLE.

Writes from the engine to a single observer socket are line-buffered JSON: write_observer_line() writes the serialized event, a \n, and flushes (lib.rs:390-405). One event per line, no framing layer needed — BufReader::read_line on the bridge side just works.

## Replay semantics

The two routes serve different shapes of the same stream:

- /observer/history — one-shot. Bridge connects, sends a subscribe line with history_limit, reads up to N lines, returns them as a JSON array, closes. No live tail. (web-bridge/src/lib.rs:124-170.)

- /observer/stream — SSE. Bridge subscribes with the same parameters, the engine first drains a history prefix from graph::observer_history (newest first, then reversed so the prefix is chronological — lib.rs:1567-1572), then switches to live tailing. The bridge yields each engine line as an SSE data: frame (web-bridge/src/lib.rs:205-236).

Last-Event-ID resumption is honored at the SSE protocol level via the prefix replay window. The “ring buffer” is really two layers stacked: the broadcast channel’s 256-event tail for in-flight events, and graph::observer_history for the durable record persisted in the graph. A reconnecting client gets up to 200 history items (lib.rs:1558) and seamlessly resumes live.

EventSource reconnects automatically. The engine’s observer.sock accepts new connections at any time, so a transient close — bridge restart, network blip — heals on its own as long as the engine is alive.

## Why a separate socket

The engine exposes two distinct Unix sockets:

SocketDirectionProtocolMultiplicity
~/.agentos/engine.sockbidirectionalJSON-RPC, request/responsemany concurrent clients
~/.agentos/observer.sockserver → client fan-outnewline-delimited JSON, no responsesmany concurrent subscribers

They could in principle share one socket. They don’t, for three reasons:

- Framing. Engine RPC pairs id ↔ response; observer is a free-running unidirectional stream. Multiplexing them on one socket means inventing a tag layer, and every consumer becomes a partial demuxer. Separate sockets, separate framing, no demuxer.

- Back-pressure. A slow observer subscriber must not stall RPC writes. With one shared socket, a stuck reader pauses the writer for both protocols; with two sockets the kernel’s per-socket buffers isolate them.

- Trust surface. Observer is read-only; engine is write-capable. Separate sockets let us tighten observer permissions independently if we ever want unprivileged subscribers (today both are user-private).

Same daemon, same flock — just two listening sockets.

## Failure modes

FailureWhat happens
Engine restartobserver.sock closes. Bridge sees EOF on its read_line, the SSE stream ends. Browser EventSource reconnects; the bridge re-runs connect_observer() with the 20×250 ms retry, picks up the new socket, replays history prefix, resumes live. Total user-visible gap: ~10 s.
Bridge restartEngine drops the bridge’s broadcast Receiver (Closed). All EventSource connections terminate. Browser auto-reconnects to the new bridge process.
Skill emits faster than the channel drainsBroadcast ring overruns the slow subscriber. That subscriber gets RecvError::Lagged(n), which the engine surfaces as a synthetic phase: "lagged" event over the wire. Fast subscribers are unaffected. The graph’s persistent activity log is unaffected — durability lives in the graph, not in the channel.
Bridge can’t reach the engineAfter 20 failed connect attempts, /observer/stream and /observer/history return 503. /healthz reports engine: false (web-bridge/src/lib.rs:99-103).
Observer socket exists but engine is wedgedBridge connects, sends subscribe line, reads zero lines; read_line returns Ok(0) and the SSE stream closes cleanly. No retry inside a single connection — the browser’s EventSource will reconnect and try again.

  [   Previous  Auth resolution  ](/architecture/auth-resolution/) [   Next  Shape extraction  ](/architecture/shape-extraction/)


---
<!-- page: https://agentos.to/skills/agent-empathy/ -->

# Agent empathy

“The real problem is not whether machines think but whether men do.” — B.F. Skinner

We serve two users. The human side has decades of UX research, design systems, and accessibility standards. The agent side has almost nothing. We’re writing the playbook.

The customer is the smallest model. Not Opus. Not Sonnet. The smallest model that can do tool calling — a 1B-parameter model running on a Raspberry Pi with a 4K context window. If that model can read our readme, understand the domain, and complete a task on the first try, we’ve succeeded. If it can’t, no amount of capability in larger models compensates for the failure. This is our accessibility standard: design for the most constrained agent, and every agent benefits.

This isn’t hypothetical generosity. It’s engineering discipline. A readme that works for a small model is a readme that’s clear. An API that needs one call instead of two is an API with less surface area for bugs. Constraints on the consumer force clarity in the producer.

## The practice

Agent empathy is not a feeling. It’s a practice — a set of things you do every time you build something an agent will touch.

Observe before designing. Watch an agent use what you built. Not in theory — actually do it. Call the readme, read what comes back, and follow the path a small model would take. Where does it reach for the wrong tool? Where does it misinterpret silence as absence? Where does it waste a round-trip on something the server already knows? The pain is in the observation, not in the spec.

Understanding precedes empathy. Empathy precedes solutions. You cannot design for agents until you have felt their confusion. Read the readme as if you had no prior context. Try to complete a task using only what the documentation tells you, nothing you happen to know. The gap between what you know and what the document teaches is the exact gap every new agent falls into.

Teach the model, not the syntax. An agent that understands the domain makes good decisions even with imperfect information. An agent that only knows the API surface makes random decisions confidently. Always establish what things are and why they work this way before how to call them. Mental model first, reference card second.

One call, not two. Every round-trip is a chance for error, confusion, context loss, and token waste. If two steps can be collapsed into one step, collapse them. If the server knows something the agent will need, include it in the response — don’t make the agent ask. The agent’s context window is finite and precious. Respect it.

Show, don’t list. A tree with counts teaches spatial relationships that a 60-row alphabetical table never can. An example you can copy teaches more than a syntax reference you have to interpret. Concrete beats abstract. Always.

Dynamic beats static. If the system knows the answer at response time, put it in the response. Don’t make the agent query for context the server already has. A readme that says “you have 142 people and 1,204 messages in your graph” is worth more than a readme that says “use list to find out what’s in your graph.” The former orients; the latter assigns homework.

Inline, not tabular. Agents read tokens, not pixels. Markdown tables waste tokens on pipe characters, header separators, and padding. The inline format is our standard for agent-facing output: one entity per line, name first, metadata in parentheses — Task Name (high, ready, updated Feb 27, abc123). For detail views, properties are simple key: value lines, not table rows. Relationships are type: Name (id) lines. A self-teaching footer lists available fields and relationships the agent didn’t ask for but could. Everything an agent needs to act on — the entity ID, the status, the related entity IDs — is right there in the text, no parsing required. This is our accessibility format: if a 1B model can extract the ID from a parenthetical, we’ve succeeded.

Entities first, skills second. The graph covers 90% of what an agent needs. Skills are the escape hatch for capabilities the graph can’t provide — searching the web, sending a message, calling an external API. If an agent reaches for a skill when an entity query would have worked, the documentation failed, not the agent.

Absent is not false. This is the foundational data semantics rule. In a sparse graph, most entities don’t have most fields. Filtering by done=false doesn’t mean “not done” — it means “the done field exists AND equals false.” An agent that doesn’t understand this will query itself into a wall, get zero results, and confidently report that nothing exists. Every interface we build must account for how absence, presence, and computed values actually work — and teach it.

## The test

When you build something an agent will touch — a readme, a tool response, an error message, a data format — ask yourself:

- Could a small model complete the task after reading this once?

- Does this teach the domain or just the API?

- Am I making the agent ask for something I already know?

- If the agent gets zero results, will it understand why?

- What’s the fewest number of round-trips to success?

If the answer to #1 is no, the rest doesn’t matter yet. Start there.

## Why this matters beyond agents

These principles make the system better for humans too. A readme that a 1B model can follow is a readme a new contributor can follow. An API that minimizes round-trips is an API that’s fast. Dynamic responses that include context are responses that save everyone’s time. Error messages that explain absence are error messages that don’t waste anyone’s afternoon.

Designing for the most constrained user has always been the shortcut to designing for everyone. The accessibility movement proved this for humans. We’re proving it for agents.

  [   Previous  Overview  ](/skills/overview/) [   Next  Connections  ](/skills/connections/)


---
<!-- page: https://agentos.to/skills/reference/agents/problem-solving/ -->

# Problem Solving

MetadataValue
Categoryagents
Capabilitiesllm, shell
Website[https://agentos.to](https://agentos.to)

## Readme

You are talking to the user right now. You are the interface. Don’t
spawn sub-agents to interview them — use the conversation you’re already
in. This skill gives you three tools and a workflow. That’s it.

## The loop

- Interview the user until you think you have a clear problem definition.

- Write _projects/p<N>/<slug>/pain.md — YAML frontmatter + markdown body.

- Call evaluate_problem(path="<absolute path to pain.md>").

- Read the result. If pass: false, ask the user the clarifying questions in feedback, rewrite the file, call again. If pass: true, continue.

- Call solution(project="<absolute path to project dir>"). This kicks off the adversarial propose ↔ review loop against your problem definition.

- Once that returns verdict: implement, you own the implementation. Do the work.

- When the work is shipped, call closeout(project="<project dir>") to write closeout.md from the git log.

Priority <N> is 1, 2, or 3. Ask the user if it’s unclear — don’t guess.

## Execution modes

Skill dispatch (when engine is healthy): Use the tools above (evaluate_problem, solution, closeout) through normal engine dispatch.

Sub-agent mode (always works): When the engine dispatch is broken or unavailable, run the same loop manually with general-purpose sub-agents:

- Write pain.md yourself (interview the user directly)

- Write proposal.md (with web research / prior art)

- Spawn a general-purpose sub-agent as adversarial reviewer — give it full Read/Grep/Glob access, tell it to verify every claim against source code (file:line), find blockers (wrong signatures, crate boundary violations, missing edge cases). It writes review.md with a verdict.

- If fail: fix the proposal, re-run the reviewer agent. Iterate until pass.

- If pass: implement.

The sub-agent approach is the primary fallback. It produces equivalent quality to the skill dispatch — the reviewer starts fresh with no bias from proposal writing, which is the key property.

## What makes a good problem definition

You’re writing pain.md, not a solution. Pretend you are a skeptical
colleague hearing about the problem for the first time. A good problem
definition:

- Names the pain in one sentence. If you can’t, you don’t understand the problem yet. Go back to the user.

- Identifies personas. Who hurts? Skill author? End user at a GUI? Engine maintainer? A specific external API? List every party affected and how their pain differs.

- Cites evidence. File paths, line numbers, exact error messages, concrete scenarios that fail today. “The agent can’t ask questions” is weak. “handle_engine_dispatch_async in crates/core/src/skills/executor.rs:1451 has branches for __progress__, __browser_*, __oauth_exchange__, but no __ask_user__ — so the interview agent at project_management.py:568-619 runs one-shot with no way to clarify” is strong.

- Lists forward-looking pain. What gets worse if we don’t fix this? What future work is blocked?

- Fences the scope. An explicit non-problems section: things a solution might try to bundle but shouldn’t. This is the single most load-bearing section — it’s what keeps the solution from overreaching.

- Is honest about what you don’t know yet. A “What we don’t know” section is fine. Pain is not solution — you don’t have to have answers.

- Stays at the scope the real fix needs. AgentOS is pre-launch. No users, no data to protect, no backward compat. If the real fix is gutting an executor and every downstream skill, scope the problem at that level. Pre-shrinking the problem to make the solution feel smaller is the single most common failure mode.

### Required YAML frontmatter

-
```

---

title: "<Name> — Pain"

type: pain

priority: 1  # 1, 2, or 3

labels: [engine, dispatch, ...]  # subsystems this touches

pain: |

  <the one-sentence version of the pain>

---

```

 — Pain"type: painpriority: 1  # 1, 2, or 3labels: [engine, dispatch, ...]  # subsystems this touchespain: |  ---">

evaluate_problem will add reviews: entries to this frontmatter on
each call. Don’t hand-write that field — let the tool stamp it.

### Body structure (suggested — adapt to the problem)

```

# <Name> — Pain

## One sentence

<the one-sentence pain>

## Personas

| Persona | Who they are |

|---------|--------------|

| ... | ... |

## Per-persona pain, with evidence

### <persona>

**Pain:** ...

**Evidence:** <file:line citations, exact errors, concrete scenarios>

## Forward-looking pain

What gets worse if we don't fix this. Blocked work, compounding costs.

## Explicit non-problems (scope fences)

- **Not X.** <why>

- **Not Y.** <why>

## What we specifically do NOT know yet

<open questions that are solution-land, not pain-land>

```

 — Pain## One sentence## Personas| Persona | Who they are ||---------|--------------|| ... | ... |## Per-persona pain, with evidence### **Pain:** ...**Evidence:** ## Forward-looking painWhat gets worse if we don't fix this. Blocked work, compounding costs.## Explicit non-problems (scope fences)- **Not X.** - **Not Y.** ## What we specifically do NOT know yet">

Length target: as long as it needs to be to be concrete. A 40-line
pain doc with file:line evidence beats a 400-line pain doc full of
hand-waving. The example at _projects/p1/ask-user-primitive/pain.md
is a good reference for depth of evidence — but don’t cargo-cult its
structure. Every problem is shaped differently.

## evaluate_problem — what it does

evaluate_problem(path="...") reads your pain file, runs it through an
adversarial evaluator, and stamps the result into the file’s YAML
frontmatter under reviews:. Returns:

```

{

  "pass": true | false,

  "feedback": "<markdown>",

  "path": "<path you passed in>"

}

```

",  "path": ""}">

- pass: false: feedback is a list of specific clarifying questions the evaluator wants answered. Ask the user those questions (not all at once — pick the important ones), rewrite pain.md, call evaluate_problem again.

- pass: true: You’re cleared to proceed. Call solution(project=...).

The evaluator is harsh on substance, kind on prose. It looks for:
concrete evidence, clear persona-level pain, tight scope fences, and
honest unknowns. It rejects vague pain, solutioneering, and
overscoped problems that bundle unrelated work.

## solution — what it does

solution(project="<project dir>") runs the propose ↔ review loop:

- A proposal agent reads pain.md and writes proposal.md — a file-level design with exact files, functions, diff sketches, edge cases, and a gate test verification plan.

- An adversarial reviewer scores it against the pain’s evaluation criteria and writes review.md with a verdict: implement, revise, or rethink.

- If revise or rethink, the loop iterates. Previous rounds move to _drafts/v<N>-*.

- Once implement, the loop exits. Returns {verdict, score, proposal_path, review_path, rounds}.

Budget: up to 5 rounds. If the 5th round still isn’t implement, the
problem is probably wrong — come back to the user and rewrite the pain.

You do not do the implementation work inside solution(). That’s
your job after solution returns implement. Read proposal.md,
read review.md, and then go build it.

## closeout — what it does

closeout(project="<project dir>") discovers the commits that shipped
the work (scoped to files named in the proposal’s Files Changed table),
writes closeout.md with a five-section format: Problem, What
shipped, Gate results, Deviations, Deleted. Call this after you’ve
actually merged the work, not before.

## File layout

```

_projects/

  p1/                           <- priority 1 (active)

    <slug>/

      pain.md                   <- problem definition (you write, tool stamps reviews)

      proposal.md               <- winning proposal (solution writes)

      review.md                 <- winning review     (solution writes)

      closeout.md               <- what actually shipped (closeout writes)

      _drafts/

        vproposal.md

        v1-review.md

  _archive/<slug>/              <- completed projects (manually moved)

```

/      pain.md                   /

No numeric prefixes — pain, proposal, review, closeout sort alphabetically.
Priority is the parent folder — move a project between p1/, p2/,
p3/ to change priority. No other state lives anywhere else.

## Feedback

This skill and the SDK are under active development. When you finish a
run — especially if anything was unclear, frustrating, or could be
better — call give_feedback(content="..."). Even “all clear” helps.

  [   Previous  PostHog  ](/skills/reference/web/posthog/) [   Next  Reddit  ](/skills/reference/media/reddit/)


---
<!-- page: https://agentos.to/skills/reference/agents/code-review/ -->

# Code Review

MetadataValue
Categoryagents
Capabilitiesllm, shell
Website[https://agentos.to](https://agentos.to)

## Readme

Evaluate code changes against project principles and architectural direction.
Reads the principles docs, active refactoring specs, and crate architecture
to score diffs and catch violations at commit time.

## Knowledge Base

The evaluator reads these documents before scoring:

SourceWhatWhen to apply
core/principles.mdEngine principles — Rust is generic, templates do the work, etc.Every Rust commit
docs/src/content/docs/principles.mdShape principles — no counts, edges are verbs, etc.Shape/ontology changes
docs/src/content/docs/skills.mdSkill SDK reference — how skills are builtAny skill/Python commit
core/docs/specs/refactoring/*.mdActive refactoring specs — what’s flagged for cleanupAny commit touching flagged files
./dev.sh arch outputLive crate/module sizes, dependency chain, largest filesStructural awareness

## Tools

### evaluate_commit

Score a git diff against the project’s principles and refactoring specs.

Parameters:

- diff (required) — the staged git diff

- files — newline-separated list of changed file paths

- threshold — minimum passing score (default: 90)

- model — LLM model to use (default: sonnet)

Returns: { score, maxScore, pass, violations, summary }

## Future Tools

- review_pr — evaluate all commits in a PR

  [   Previous  Claude  ](/skills/reference/ai/claude/) [   Next  Copilot Money  ](/skills/reference/finance/copilot-money/)


---
<!-- page: https://agentos.to/shapes/reference/session/ -->

# session

    An MCP session — a client connected, made some calls, disconnected.
One node per unique client+project+branch combo, updated on reconnection.

MetadataValue
Pluralsessions
Subtitle fieldclient
Identityclient, projectId, gitBranch

## Fields

FieldType
clientstring
projectIdstring
gitBranchstring
sessionTypestring
startedAtdatetime
endedAtdatetime
messageCountinteger
tokenCountinteger

## Relations

RelationTarget
participant[actor](/shapes/reference/actor/)
folder[folder](/shapes/reference/folder/)

## Prior art

External standards this shape draws from or aligns with. See [Shape design principles](/shapes/shape-design-principles/) for how prior art informs shape design.

- [Model Context Protocol (MCP) session](https://modelcontextprotocol.io/specification) — Direct source. Our client/sessionType come from MCP’s client/transport concepts (STDIO, HTTP+SSE).

- [OpenTelemetry Spans (root span ≈ session)](https://opentelemetry.io/docs/concepts/signals/traces/) — Our startedAt/endedAt/messageCount/tokenCount align with span lifecycle + attributes in a trace context.

- [OpenID Connect Session Management 1.0](https://openid.net/specs/openid-connect-session-1_0.html) — Classical web-session model. Our participant ≈ authenticated subject; projectId/gitBranch are AgentOS-specific scoping.

## Skills that produce this shape

- [cursor](/skills/reference/dev/cursor/) — op_list_sessions, op_backfill_session, op_get_session

  [   Previous  search  ](/shapes/reference/search/) [   Next  shelf  ](/shapes/reference/shelf/)


---
<!-- page: https://agentos.to/shapes/reference/tool_call/ -->

# tool_call

    A single tool invocation made by an agent during a message.
Captures the tool name, input arguments, and the result that came back.
Tool calls are first-class entities so you can query “every time Claude
ran Grep on this repo” or “every tool call that errored.”
any agent framework that records tool use.

MetadataValue
Pluraltool_calls
Subtitle fieldname
Identityplatform, id

## Fields

FieldType
namestring
inputtext
outputtext
isErrorboolean
durationMsinteger

## Relations

RelationTarget
platform[product](/shapes/reference/product/)
from[actor](/shapes/reference/actor/)
inMessage[message](/shapes/reference/message/)
repliesTo[tool_call](/shapes/reference/tool_call/)

## Prior art

External standards this shape draws from or aligns with. See [Shape design principles](/shapes/shape-design-principles/) for how prior art informs shape design.

- [Anthropic Tool Use API](https://docs.anthropic.com/en/docs/build-with-claude/tool-use) — Our name/input/output/isError map to tool_use/tool_result blocks in Claude’s message API.

- [OpenAI Function Calling / tool_calls](https://platform.openai.com/docs/guides/function-calling) — Our name/input = function.name/function.arguments; output is the tool-result message content.

- [OpenTelemetry GenAI semconv](https://opentelemetry.io/docs/specs/semconv/gen-ai/) — Emerging observability standard. Our durationMs/isError align with gen_ai.tool.* span attributes.

  [   Previous  theme  ](/shapes/reference/theme/) [   Next  transaction  ](/shapes/reference/transaction/)


---
<!-- page: https://agentos.to/shapes/reference/task/ -->

# task

    A work item — issue, ticket, or to-do. Supports hierarchy (parent/children)
and dependency tracking (blocked_by/blocks).

MetadataValue
Pluraltasks
Subtitle fieldstate
Identityplatform, id

## Fields

FieldType
remoteIdstring
priorityinteger
statestring
labelsstring[]
startedAtdatetime
targetDatedatetime

## Relations

RelationTarget
assignedTo[person](/shapes/reference/person/)
project[project](/shapes/reference/project/)
repository[repository](/shapes/reference/repository/)
parent[task](/shapes/reference/task/)
children[task[]](/shapes/reference/task/)
blockedBy[task[]](/shapes/reference/task/)
blocks[task[]](/shapes/reference/task/)

## Used as a base by

- [spec](/shapes/reference/spec/)

## Prior art

External standards this shape draws from or aligns with. See [Shape design principles](/shapes/shape-design-principles/) for how prior art informs shape design.

- [GitHub REST API — Issues](https://docs.github.com/en/rest/issues/issues) — Direct source. Our remoteId/state/labels/assignedTo/parent/ children/blockedBy/blocks map to GitHub Issue + sub-issues + task-list tracking.

- [Linear GraphQL API — Issue](https://developers.linear.app/docs/graphql/working-with-the-graphql-api) — Practical canonical. Our priority/state/project/targetDate align with Linear’s Issue model exactly.

- [Todoist REST API v2 — Tasks](https://developer.todoist.com/rest/v2/) — Consumer-grade task model. Our startedAt/targetDate ≈ created_at/due; labels match directly.

## Skills that produce this shape

- [todoist](/skills/reference/productivity/todoist/) — list_tasks, list_all_tasks, filter_task, get_task, create_task, update_task, move_task

- [linear](/skills/reference/dev/linear/) — list_tasks, get_task, create_task, update_task

- [github](/skills/reference/dev/github/) — list_tasks, get_task

  [   Previous  tag  ](/shapes/reference/tag/) [   Next  theme  ](/shapes/reference/theme/)
