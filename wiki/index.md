# Index

Catalog of every wiki page, grouped by branch. Read this first when answering a question. Root: [[loop-engineering]] · Timeline: [[log]]

## Root
- [[loop-engineering]]: definition (alias: software factory), the two-loop mental model, branch map, core claims, gaps

## Anatomy ([[anatomy]])
- [[trigger]]: when an iteration starts (cron, self-paced, goal, event, human)
- [[goal-spec]]: the written definition of done (specs, `/goal` conditions, plans)
- [[context-and-state]]: memory on disk vs context in the window, and Ralph's context discipline
- [[decision-step]]: the model picks the next action, which is what separates a loop from cron
- [[action]]: tools, connectors, the ACI, one item per loop
- [[observation]]: ground truth from the environment, "loop back is everything"
- [[verification]]: the maker/checker split plus mechanical backpressure
- [[termination]]: stop conditions (goal, cap, 7-day TTL, self-stop, fallback, human)

## Patterns ([[patterns]])
- [[agent-loop]]: the inner loop, LLM + tools + feedback; workflows vs agents
- [[ralph-loop]]: `while :; do cat PROMPT.md | claude-code; done`
- [[scheduled-loop]]: cron or interval discovery and triage (the morning triage loop)
- [[self-paced-loop]]: the model chooses its next wake-up (1 min–1 h)
- [[goal-loop]]: run until a verifiable condition holds, graded by a separate model
- [[event-driven-loop]]: Channels and Monitor instead of polling
- [[babysitter-loop]]: tend a PR, deploy or release branch until green
- [[improvement-loops]]: coverage, lint, duplication, entropy and migration loops; one fix per iteration
- [[stage-gated-pipeline]]: triage → repro → fix → verify; every stage can stop the line and hands evidence forward
- [[software-factory]]: triggers start sessions; dark factory = nobody reviews the output
- [[afk]]: unattended runs; give input before, during and after; end in a PR
- [[orchestrator-workers]]: coordinator + sub-agents, controlled fan-out
- [[evaluator-optimizer]]: maker and checker iterate
- [[human-in-the-loop]]: design time, checkpoints, triage inbox, recovery, review

## Control ([[control]])
- [[budgets-and-cost]]: cost drivers and levers; start with one automation + one verifier
- [[guardrails-and-permissions]]: scope fences, authorization carry-over, permission surfaces
- [[backpressure]]: tests, types and analysers that reject bad output fast
- [[isolation]]: worktrees and sandboxes for parallel and unattended work
- [[observability]]: seeing what a loop did and why (streaming, notifications, logs; still thin)
- [[earned-autonomy]]: verification is the limiting step; the trust ladder before going unattended
- [[idempotency]]: safe re-runs after crashes, retries and duplicate fires
- [[smart-zone]]: context rot, dumb zone, fresh context per iteration
- [[agent-experience]]: AX, "the repo wins", deep and grey-box modules
- [[failure-modes]]: a table of how loops go wrong and the mitigations
- [[operator-debts]]: comprehension debt, cognitive surrender, intent debt, orchestration tax

## Practice ([[practice]])
- [[loop-primitives]]: five building blocks + memory, mapped to Claude Code and Codex
- [[writing-a-loop-prompt]]: structure, principles and Pocock's prompt blocks
- [[task-sizing]]: one thing per iteration, tracer bullets, vertical TDD, risk first
- [[building-a-ralph-loop]]: Pocock's recipe: HITL→AFK scripts, sandbox, streaming, guardrails
- [[seven-phases-of-ai-development]]: the workflow around the execution loop
- [[backlog-triage]]: the issue state machine ending in `ready-for-agent`
- [[verification-skill]]: app control CLI + Feature Map; create once, maintain daily
- [[overnight-contract]]: goal, finish predicate, isolation, permissions, decision log, escape hatch
- [[build-the-lever]]: scripts for deterministic steps; encode lessons in structure
- [[claude-code-loop]]: `/loop` modes, `loop.md`, stopping, limits
- [[claude-code-goal]]: `/goal` (second-hand, stub)
- [[claude-code-scheduling]]: Routines vs Desktop vs `/loop` vs GitHub Actions
- [[llm-wiki-pattern]]: Karpathy's LLM Wiki, read as a loop (this wiki's own design)

## Entities ([[entities]])
- [[addy-osmani]]: named loop engineering (2026-06-07)
- [[boris-cherny]]: head of Claude Code, "My job is to write loops"
- [[peter-steinberger]]: "design loops that prompt your agents"
- [[geoffrey-huntley]]: creator of Ralph
- [[matt-pocock]]: AI Hero; practical Ralph, AFK/HITL, factory vocabulary
- [[lauren-tan]]: pstack; verification as the limiting step, earned autonomy, the overnight contract
- [[andrej-karpathy]]: LLM Wiki pattern
- [[anthropic]]: lab; Building Effective Agents; Routines
- [[claude-code]]: product, loop surfaces
- [[openai-codex]]: product, Automations, `/goal` (second-hand)
- [[cursor]]: product; `/loop`, Automations, cloud agents, Projects (via Tan)
- [[pstack]]: Tan's skill plugin; `/poteto-mode`, 23 playbooks, 24 principles

## Sources ([[sources]])
- [[src-osmani-loop-engineering]]: Osmani, "Loop Engineering", 2026-06-07
- [[src-tns-loop-engineering]]: The New Stack, 2026-06-10
- [[src-claude-code-scheduled-tasks]]: Claude Code docs, "Run prompts on a schedule"
- [[src-huntley-ralph]]: Huntley, "Ralph Wiggum as a 'software engineer'", 2025-07-14
- [[src-anthropic-building-effective-agents]]: Anthropic, "Building Effective AI Agents", 2024-12-19
- [[src-karpathy-llm-wiki]]: Karpathy, "LLM Wiki" gist
- [[src-pocock-getting-started-with-ralph]]: Pocock, "Getting Started With Ralph", 2026-01-08
- [[src-pocock-ralph-tips]]: Pocock, "11 Tips For AI Coding With Ralph Wiggum", 2026-01-08
- [[src-pocock-feedback-loops-typescript]]: Pocock, "Essential AI Coding Feedback Loops For TypeScript", 2026-01-16
- [[src-pocock-ralph-plugin]]: Pocock, "Why the Anthropic Ralph plugin sucks", 2026-01-22
- [[src-pocock-afk-ralph-streaming]]: Pocock, "How To Stream Claude Code With AFK Ralph", 2026-01-22
- [[src-pocock-tracer-bullets]]: Pocock, "Tracer Bullets", 2026-01-22
- [[src-pocock-tdd-skill]]: Pocock, "My Skill Makes Claude Code GREAT At TDD", 2026-02-10
- [[src-pocock-git-guardrails-hook]]: Pocock, "This Hook Stops Claude Code Running Dangerous Git Commands", 2026-02-10
- [[src-pocock-codebases-agents-love]]: Pocock, "How To Make Codebases AI Agents Love", 2026-02-26
- [[src-pocock-seven-phases]]: Pocock, "My 7 Phases Of AI Development", 2026-03-16
- [[src-pocock-triage-skill]]: Pocock, "triage: Turn Backlog Mess Into Agent-Ready Work", 2026-05-05
- [[src-pocock-ai-coding-dictionary]]: Pocock, "AI Coding Dictionary" (index + 9 entries), 2026-09-24
- [[src-tan-how-i-use-cursor]]: Tan, "How I Use Cursor" (X), 2026-05-25
- [[src-tan-loops-you-can-trust]]: Tan, "Loops You Can Trust" (X), 2026-06-24
- [[src-tan-complete-guide-pstack-pt1]]: Tan, "The Complete Guide to pstack Pt. 1" (X), 2026-08-31
- [[src-tan-pstack-guide-poteto-mode]]: pstack guide 2, "Route work through /poteto-mode"
- [[src-tan-pstack-guide-verify-and-ship]]: pstack guide 6, "Verify the result and open a PR"
- [[src-tan-pstack-guide-overnight]]: pstack guide 7, "Run work while you sleep"
- [[src-tan-pstack-guide-principles]]: pstack guide 8, "Steer with principle names"
- [[src-tan-pstack-guide-recipes]]: pstack guide 10, "Recipes and pitfalls"
- [[src-tan-benny-automation]]: pstack benny automation pack (README + FOR_AGENTS)
- [[src-tan-pstack-loop-principles]]: six pstack principle skills relevant to loops
- [[src-tan-x-short-posts]]: four short X posts by @poteto

## Syntheses ([[syntheses]])
- [[loop-vs-prompt-engineering]]: what changed, the lineage, harder or easier
- [[loop-pattern-comparison]]: patterns compared slot by slot, with a chooser
- [[loop-design-checklist]]: pre-flight questions for any loop
- [[open-questions]]: gaps, contradictions, sources to find
