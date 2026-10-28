---
type: source
branch: sources
tags: [loop-engineering, agentos, tool-surface, mcp, observability, ax]
sources: []
url: https://agentos.to/
author: Joe Contini
published: unknown (docs repo 2026-04-14 to 2026-07-17)
raw: raw/2026-10-16-agentos-docs.md
created: 2026-10-16
updated: 2026-10-16
status: draft
---
# AgentOS documentation (selected pages)

**Author:** Joe Contini (GitHub org `agentos-to`) · **Raw:** `raw/2026-10-16-agentos-docs.md` (16 of ~230 pages) · Up: [[sources]]

## Summary
[[agentos]] is *"a local operating system for human-AI collaboration … Built for agents first."* A Rust engine keeps a personal knowledge graph (the "memex", one SQLite file) and runs Python **skills**, which are adapters to outside services. It exposes everything over **MCP**, so Claude Code, Cursor and similar agents can use it as their tool surface. It is not a loop framework. It sits under the loop, as the [[action]] layer and part of the agent's [[context-and-state|state]]. The pages relevant to loops are:
- its design-for-agents doctrine ("agent empathy")
- the **observer bus**, which emits every tool call as an event
- an agent skill that runs a **propose ↔ adversarial review loop**

The project is pre-launch, with *"zero users"*. The engine source is not public, and the docs were last pushed 2026-07-17.

## Key claims
- **Two users, two problems.**
  - For humans: *"Anxiety = Uncertainty × Powerlessness"*. The AI *"screen-shares with you"* to remove the uncertainty, and *"You control what it can do"* to remove the powerlessness. If either factor is zero, anxiety is zero. See [[human-in-the-loop]].
  - For agents: *"Error Rate = f(Dependency Depth)"*. *"Every round-trip is a chance for errors to compound."* See [[agent-experience]].
- **The customer is the smallest model.** That means *"a 1B-parameter model running on a Raspberry Pi with a 4K context window. If that model can read our readme … and complete a task on the first try, we've succeeded."* The practice is called **agent empathy**:
  - observe an agent using what you built before you design
  - teach the domain, not the syntax
  - *"One call, not two"*
  - *"Dynamic beats static"*: put what the server already knows in the response
  - use an inline output format rather than tables, because *"Agents read tokens, not pixels"*
  - *"Absent is not false"*: a sparse graph must teach how missing fields behave, or the agent will *"confidently report that nothing exists"*

  See [[agent-experience]] and [[action]].
- **Observer bus.** Every tool call emits `started`, `completed` (with `latency_ms` and the result) or `failed` (with the error). Each event carries `session_id`, `client` and `working_dir`. Consumers include a CLI `watch`, a browser SSE stream and debuggers. The bus is *"lossy by design, which is the right trade for telemetry"*: a slow consumer gets a synthetic `lagged` event, and *"durability lives in the graph, not in the channel."* See [[observability]].
- **Agent activity is data.** `session` (client, project, branch, token count) and `tool_call` (name, input, output, `isError`, `durationMs`) are graph entities. Both align with OpenTelemetry GenAI conventions, so you can query *"every tool call that errored."* *"Changes are entities"* (W3C PROV-O). *"Every change has a who"*, whether the human or a specific agent. See [[observability]].
- **The problem-solving loop** (the `problem-solving` agent skill). See [[evaluator-optimizer]], [[goal-spec]] and [[termination]].
  1. Interview the user, then write `pain.md`.
  2. `evaluate_problem` gates it. On fail, it returns clarifying questions for the user.
  3. `solution` runs a *"propose ↔ review loop"*: a proposal agent writes `proposal.md`, and an adversarial reviewer returns *implement / revise / rethink*.
  4. The budget is **up to 5 rounds**. *"If the 5th round still isn't implement, the problem is probably wrong — come back to the user and rewrite the pain."*
  5. Implement, then `closeout` writes what actually shipped from the git log.
  6. Why it works: *"the reviewer starts fresh with no bias from proposal writing, which is the key property."*
- **Scope fences.** The *"Explicit non-problems"* section of `pain.md` is *"the single most load-bearing section — it's what keeps the solution from overreaching."* *"Pre-shrinking the problem to make the solution feel smaller is the single most common failure mode."* See [[goal-spec]].
- **A commit-time reviewer.** `evaluate_commit` scores a diff against the project's principles docs and refactoring specs. It has a pass threshold (default 90) and uses a configurable model. See [[backpressure]].
- **Isolation by architecture.** Skills and apps *"never know about each other"*. The engine is the *"sole broker"* and dispatches by capability, not by name. Each skill call is a fresh subprocess, with *"no shared state between skill runs"*. Connections are sandboxed identities keyed by domain, so a compromised skill *"cannot reach across identities"*. The docs are candid about the gaps, under "Honest caveats": decoupling is enforced by convention and code review, not by the engine, and the credential store falls back to plaintext without Keychain. See [[guardrails-and-permissions]] and [[isolation]].
- **Build posture.**
  - *"Test through real services, not mocks. No unit tests. Integration tests via MCP against the running engine."*
  - *"Blast radius is not a cost — stale architecture is"*: prefer *"the hardest, most audacious appropriate refactor"* over small patches, but only for *"a root-cause inconsistency you can name."*
  - Human and AI act as *"co-CTOs"*.

## Notable quotes
- *"The agent is the primary customer. AgentOS is the operating system for agents, not around them."*
- *"If an agent reaches for a skill when an entity query would have worked, the documentation failed, not the agent."*
- *"A readme that says 'you have 142 people and 1,204 messages in your graph' is worth more than a readme that says 'use list to find out what's in your graph.' The former orients; the latter assigns homework."*

## Contradictions with the wiki
- **Small model vs pay to play.** AgentOS designs for a 1B local model. Pocock says local models are not good enough for coding loops: *"you have to pay to play"* ([[src-pocock-ralph-tips]]). The two may be compatible *(synthesis)*: AgentOS sizes its *tool surface* for the weakest caller, while Pocock is choosing the *driver* model.
- **Audacious refactors vs small steps.** *"Blast radius is not a cost"* cuts against [[task-sizing]] (one thing per iteration, five narrow PRs), at least for pre-launch code with no users. AgentOS frames it as a project-stage rule, not a loop rule.
- **Numbers or labels.** The roadmap page prefers pass/fail/partial labels over numeric scores, yet `evaluate_commit` returns a numeric score with a threshold. The source is inconsistent with itself.

## Not covered
I did not ingest the ontology reference (~90 shapes), the per-service skill reference (~50 skills), `research/*` or `reverse-engineering/*`. These are about a personal knowledge graph, which is out of scope here. I also did not ingest `interfaces/*` and the remaining architecture pages (dispatch, auth, local-first, shape extraction).

## Pages touched
[[agentos]], [[agent-experience]], [[action]], [[observability]], [[human-in-the-loop]], [[evaluator-optimizer]], [[goal-spec]], [[termination]], [[backpressure]], [[guardrails-and-permissions]], [[isolation]], [[context-and-state]], [[task-sizing]], [[open-questions]]
