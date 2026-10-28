---
type: concept
branch: control
tags: [loop-engineering, control, worktrees, parallelism]
sources: ["[[src-osmani-loop-engineering]]", "[[src-tns-loop-engineering]]", "[[src-anthropic-building-effective-agents]]", "[[src-pocock-getting-started-with-ralph]]", "[[src-pocock-ralph-tips]]", "[[src-pocock-git-guardrails-hook]]", "[[src-tan-complete-guide-pstack-pt1]]", "[[src-tan-pstack-guide-poteto-mode]]", "[[src-tan-loops-you-can-trust]]", "[[src-agentos-docs]]"]
created: 2026-10-11
updated: 2026-10-16
status: draft
---
# Isolation (worktrees and sandboxes)

**Isolation** keeps parallel or unattended work from colliding with other work or damaging it. *"The second you run more than one agent the files start colliding"*. A git worktree, *"a separate working directory on its own branch sharing the same repo history"*, means one agent's edits *"literally can not touch the other one's checkout"* ([[src-osmani-loop-engineering]]). Up: [[control]].

## Implementations
- **[[openai-codex]]:** a built-in worktree per thread ([[src-osmani-loop-engineering]]).
- **[[claude-code]]:** `git worktree`, the `--worktree` flag, and `isolation: worktree` on a subagent, which gives each helper a fresh checkout that cleans itself up ([[src-osmani-loop-engineering]]).
- **Sandboxes:** test agents in sandboxed environments ([[src-anthropic-building-effective-agents]]).
- **Docker sandboxes:** `docker sandbox run claude` (Docker Desktop 4.50+) runs the agent in a microVM. Only the current directory is mounted, at the same path. Git config is injected, and there is one persistent sandbox per workspace ([[src-pocock-getting-started-with-ralph]], [[src-pocock-git-guardrails-hook]]). The trade-off is that your global `AGENTS.md` and user skills aren't loaded. Pocock calls them *"essential insurance"* for overnight AFK runs, and optional for HITL ([[src-pocock-ralph-tips]]).

Worktrees let teams *"run agents in parallel … without corrupting the main branch"* ([[src-tns-loop-engineering]]).

- **Cloud agents (Cursor):** each gets its own VM and branch, so it can install dependencies, run the app and record video without touching your machine. A snapshot makes later starts fast ([[src-tan-complete-guide-pstack-pt1]], [[src-tan-pstack-guide-poteto-mode]]).
- **Runtime isolation, not just files:** shared ports, processes and user data made two agents on one dev build *"interfere with each other in hilarious ways."* Each needs its own checkout, build, ports and browser state ([[src-tan-loops-you-can-trust]]).

- **Tool-layer isolation ([[agentos]]):** each skill call runs in a fresh subprocess with *"no shared state between skill runs"*. Each connection is a sandboxed identity keyed by domain, so a compromised skill *"cannot reach across identities"*. Skills and apps only meet through the engine, by capability ([[src-agentos-docs]]). The docs admit that this decoupling is enforced by convention and review, not by the engine binary.

## Limits
- A sandbox isolates **where**, not **what**. Destructive git commands inside the mounted repo still work, so add hook guardrails ([[src-pocock-git-guardrails-hook]]). See [[guardrails-and-permissions]].
Isolation removes the *mechanical* collision, not the *human* bottleneck. Review bandwidth is the ceiling ([[src-osmani-loop-engineering]]). See [[operator-debts]].

## Contradictions & open questions
- **Worktrees or cloud agents?** Osmani lists worktrees as a core primitive ([[src-osmani-loop-engineering]]). Tan: *"I would recommend against"* worktrees for parallelism. They are disk- and resource-heavy (*"up to 10 agents"*), and cloud agents scale further ([[src-tan-complete-guide-pstack-pt1]]). Her own guide still uses one worktree per task when work must stay local ([[src-tan-pstack-guide-poteto-mode]]).

## Related
[[orchestrator-workers]] · [[guardrails-and-permissions]] · [[loop-primitives]]
