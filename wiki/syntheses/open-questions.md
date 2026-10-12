---
type: synthesis
branch: syntheses
tags: [loop-engineering, synthesis, gaps]
sources: ["[[src-tns-loop-engineering]]", "[[src-osmani-loop-engineering]]", "[[src-huntley-ralph]]", "[[src-pocock-ralph-plugin]]", "[[src-pocock-ai-coding-dictionary]]", "[[src-pocock-ralph-tips]]", "[[src-tan-pstack-loop-principles]]", "[[src-tan-complete-guide-pstack-pt1]]", "[[src-tan-pstack-guide-overnight]]"]
created: 2026-10-11
updated: 2026-10-12
status: draft
---
# Open questions

Gaps, unresolved contradictions, and sources worth finding. Lint passes add to this list. Up: [[syntheses]].

## Open questions
1. **Portability.** Will loop *definitions* become portable across tools? TNS predicts the vendor who does it *"will take pole position"* ([[src-tns-loop-engineering]]). Huntley's view that prompts are operator-specific cuts against it ([[src-huntley-ralph]]). See [[loop-primitives]].
2. **Budget-based termination.** No source yet describes hard token or dollar caps as a stop condition. See [[budgets-and-cost]] and [[termination]].
3. **`/goal` limits.** What happens when a goal is unreachable? Are there turn caps? See [[claude-code-goal]].
4. ~~**Idempotency.**~~ **Partly answered (2026-10-12):** Tan's *Make Operations Idempotent* principle gives a test and patterns ([[src-tan-pstack-loop-principles]]). What's still missing is a worked failure case for external side effects (messages, tickets). See [[idempotency]].
5. **Existing codebases.** Huntley says greenfield only. Osmani runs loops daily on existing repos. What separates the two cases? See [[ralph-loop]].
6. **Multi-agent coordination.** Hierarchical subagents are widely endorsed, but peer agent teams are contested. See [[orchestrator-workers]].
7. **In-session vs fresh-context loops.** Pocock says loops inside one session (the Anthropic Ralph plugin) slide into the dumb zone ([[src-pocock-ralph-plugin]]). Do Claude Code's `/loop` and `/goal` have this problem, or do they clear or compact between iterations? See [[smart-zone]], [[claude-code-loop]] and [[claude-code-goal]].
8. **Where is the dumb zone?** About 40% of the window ([[src-pocock-ralph-plugin]]) vs 125K–150K tokens ([[src-pocock-ai-coding-dictionary]]). Is it a fraction of the window or an absolute count? Does it vary by model?
9. **Terminology.** "Backpressure" / "feedback loop" vs "automated check" ([[src-pocock-ai-coding-dictionary]]). This wiki uses backpressure to mean deterministic checks only. See [[backpressure]].
10. **When is a dark factory acceptable?** Huntley says maintainability by humans is optional. Pocock and Osmani say human review is the main safeguard. See [[software-factory]].
11. **Flat plan vs API pricing.** How does a subscription plan (Pocock's 5x Max) change loop design compared with pay-per-token APIs? See [[budgets-and-cost]].
12. **Human merge gate.** Tan's Autopilot-full merges on a fresh verifier swarm's clean verdict, while benny is draft-only ([[src-tan-pstack-guide-overnight]], [[src-tan-benny-automation]]). Pocock and Osmani keep humans on PRs. What evidence justifies removing the human? See [[software-factory]] and [[earned-autonomy]].
13. **Worktrees or cloud agents** for parallelism ([[src-tan-complete-guide-pstack-pt1]] vs [[src-osmani-loop-engineering]])? See [[isolation]].
14. **Cap or pivot?** Iteration caps (Pocock) vs "a plateau means pivot, not stop" plus a time-based escape hatch (Tan). See [[termination]].
15. **Source bias.** Tan's Cursor material comes from a Cursor employee, now at xAI, and her throughput claims (2,000 PRs/month) are self-reported.

## Sources to find
- Osmani's **July 2026 follow-up** to the loop engineering post. It is mentioned in secondary coverage but not yet located.
- Anthropic, **"Effective harnesses for long-running agents"**. **High priority:** it is cited by TNS for the maker/checker split ([[src-tns-loop-engineering]]) and by Pocock as the origin of `passes`-flag PRDs and progress files ([[src-pocock-ralph-tips]]).
- Huntley, **"Everything is a Ralph loop"**, which came up in a search on 2026-10-12 and was not fetched.
- Pocock's dictionary entries not yet ingested: **compaction**, **progressive disclosure**, **AX**, **spec**/**ticket**, **memory system**.
- Docker **Sandboxes** docs, which are the isolation substrate for AFK Ralph.
- Tan's **"Complete Guide to pstack" Pt. 2+**, which were announced but not yet found. Also the pstack playbooks themselves: `autonomous-run.md`, `autopilot-full.md`, `orchestrate.md`, `pause-safely.md`, and `/show-me-your-work` and `/figure-it-out`.
- **Cursor docs** for Automations, `/loop`, cloud agents and Projects. Today only Tan describes them. See [[cursor]].
- Andy Grove, *High Output Management*, the source of the limiting-step and managerial-leverage ideas Tan applies ([[src-tan-loops-you-can-trust]]).
- Tan's talk on trust before parallelism, summarized by a third party at redreamality.com.
- Osmani's related posts: **agent harness engineering**, **long-running agents**, **comprehension debt** ([[src-osmani-loop-engineering]]).
- Official **Claude Code `/goal`** and **Routines** docs.
- First-party **Codex Automations** and **Codex `/goal`** docs. See [[openai-codex]].
- dassum, *"Loop Engineering with Agents"* (Medium). Fetching returned 403 on 2026-10-11, so it could not be ingested.
- Anything on loop **observability** (tracing, cost dashboards) or **sandboxing and credential scoping**. See [[observability]] and [[guardrails-and-permissions]].
- **Ramp Inspect** write-up: bespoke closed-loop infrastructure ([[src-tns-loop-engineering]]).
