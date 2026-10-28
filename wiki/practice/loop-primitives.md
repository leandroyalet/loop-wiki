---
type: practice
branch: practice
tags: [loop-engineering, practice, building-blocks]
sources: ["[[src-osmani-loop-engineering]]", "[[src-tns-loop-engineering]]", "[[src-pocock-git-guardrails-hook]]", "[[src-pocock-getting-started-with-ralph]]", "[[src-tan-complete-guide-pstack-pt1]]", "[[src-tan-pstack-guide-overnight]]", "[[src-openprose]]", "[[src-ouroboros]]"]
created: 2026-10-11
updated: 2026-10-19
status: solid
---
# Loop primitives (the building blocks)

Osmani's checklist for any loop: *"A loop needs five things and then one place to remember stuff"* ([[src-osmani-loop-engineering]]). Both [[claude-code]] and [[openai-codex]] now ship all of them, so the loop no longer has to be *"a pile of bash … yours and only yours"*. Up: [[practice]].

| Primitive | Job in the loop | Anatomy slot | Codex | Claude Code |
|---|---|---|---|---|
| **Automations** | discovery and triage on a schedule | [[trigger]] | Automations tab, Triage inbox, `/goal` | scheduled tasks and cron, `/loop`, `/goal`, hooks, GitHub Actions |
| **Worktrees** | isolate parallel work | [[isolation]] | a worktree per thread | `git worktree`, `--worktree`, `isolation: worktree` |
| **Skills** | codify project knowledge | [[context-and-state]] | `SKILL.md`, invoked with `$name` or implicitly | `SKILL.md` |
| **Plugins / connectors** | reach your real tools | [[action]] | MCP connectors and plugins | MCP servers and plugins |
| **Sub-agents** | ideate and verify separately | [[verification]], [[orchestrator-workers]] | TOML in `.codex/agents/` | `.claude/agents/`, agent teams |
| **State / memory** | track what's done and next | [[context-and-state]] | markdown, Memories, Linear | `AGENTS.md`/`CLAUDE.md`, progress files, auto memory, Linear via MCP |

The table merges [[src-osmani-loop-engineering]] and [[src-tns-loop-engineering]].

**[[cursor]], third column (from Tan's sources):**
- Automations: scheduled or event-triggered cloud agents, plus `/loop`.
- Worktrees or, as Tan prefers, **cloud agents** with their own VM.
- Skills and plugins, such as [[pstack]].
- Subagents and cloud subagents, with **Projects** as a persistent coordinator.
- State: the codebase plus a Feature Map as *"materialized memory"*.

Sources: [[src-tan-complete-guide-pstack-pt1]], [[src-tan-pstack-guide-overnight]].

## Notes
- **A skill is the authoring format and a plugin is how you ship it**, in both tools ([[src-osmani-loop-engineering]]).
- An automation should **call a skill** rather than paste a wall of instructions *"into a schedule that nobody will ever update"* ([[src-osmani-loop-engineering]]).
- A **tight, boring skill description** beats a clever one, because the description drives implicit invocation ([[src-osmani-loop-engineering]]).
- MCP connectors written for one tool *"usually just work in the other"* ([[src-osmani-loop-engineering]]).
- **Two primitives not in Osmani's list** matter in practice *(synthesis)*:
  - **Sandboxes**, such as `docker sandbox run claude` ([[src-pocock-getting-started-with-ralph]]). See [[isolation]].
  - **Hooks as hard guardrails**, such as `PreToolUse` blocking destructive git ([[src-pocock-git-guardrails-hook]]). See [[guardrails-and-permissions]].

  Osmani lists hooks only as a trigger mechanism.
- **A verification skill as a primitive.** Tan treats an app-control skill as *"critical infrastructure"* that every loop depends on ([[src-tan-complete-guide-pstack-pt1]]). See [[verification-skill]].

## Contradictions & open questions
- **Five or six?** Osmani's text lists five primitives *"and then one place to remember stuff"*, but his table has six rows. TNS calls them *"six building blocks"* ([[src-tns-loop-engineering]]). This is a counting convention, not a substantive disagreement.
- **Portability:** the primitives match, but loop *definitions* don't move between tools. TNS predicts that whoever makes them portable wins ([[src-tns-loop-engineering]]). [[openprose]] is the first attempt in the wiki: harness-agnostic Markdown contracts that any *"Prose-Complete"* host can run. Its caveat is that *"Portability does not imply identical model results or provide missing tools"* ([[src-openprose]]). [[ouroboros]] makes the same bet with a YAML Seed that runs on 14 host agents: *"the same Seed can be used with a different runtime"* ([[src-ouroboros]]). See [[open-questions]].

## Related
[[scheduled-loop]] · [[loop-design-checklist]]
