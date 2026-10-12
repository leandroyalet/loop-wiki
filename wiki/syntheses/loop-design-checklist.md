---
type: synthesis
branch: syntheses
tags: [loop-engineering, synthesis, checklist]
sources: ["[[src-osmani-loop-engineering]]", "[[src-huntley-ralph]]", "[[src-claude-code-scheduled-tasks]]", "[[src-anthropic-building-effective-agents]]", "[[src-tns-loop-engineering]]", "[[src-pocock-ralph-tips]]", "[[src-pocock-ai-coding-dictionary]]", "[[src-pocock-git-guardrails-hook]]", "[[src-pocock-afk-ralph-streaming]]", "[[src-tan-loops-you-can-trust]]", "[[src-tan-pstack-guide-overnight]]", "[[src-tan-pstack-loop-principles]]"]
created: 2026-10-11
updated: 2026-10-12
status: draft
---
# Loop design checklist

Questions to answer before turning a loop on. Each one is distilled from the linked pages, which hold the citations. Up: [[syntheses]].

**Has it earned autonomy?** (Tan's ladder, [[earned-autonomy]])
- [ ] Have you done the task by hand once, so you know what good looks like?
- [ ] Does the agent have your tools and signals, such as a verification skill, profiler and logs? ([[verification-skill]])
- [ ] Does every stage prove its work and stop the line when it misses the bar? ([[stage-gated-pipeline]])
- [ ] Have repeated failures been turned into tools, skills or checks? ([[build-the-lever]])

**Should this be a loop at all?**
- [ ] Would a single prompt or a fixed workflow do the job? ([[agent-loop]], [[loop-vs-prompt-engineering]])
- [ ] Have you run it HITL until you trust the prompt, before going AFK? ([[human-in-the-loop]], [[afk]])

**Anatomy**
- [ ] **Trigger:** cron, self-paced, goal or event? Is polling really necessary? ([[trigger]])
- [ ] **Goal:** is "done" written down, and is it machine-checkable where possible? ([[goal-spec]])
- [ ] **State:** where does the loop remember what it did, and is it loaded the same way every run? ([[context-and-state]])
- [ ] **Scope per iteration:** one item per loop, as a thin vertical slice, risk first? ([[task-sizing]])
- [ ] **Fresh context:** does each iteration start in a fresh session, or does history accumulate? ([[smart-zone]])
- [ ] **Scope precision:** are the files, stop condition and edge cases explicit enough that the loop can't "declare victory" early? ([[goal-spec]])
- [ ] **Verification:** is there mechanical backpressure, *and* a checker separate from the maker? ([[backpressure]], [[evaluator-optimizer]])
- [ ] **Finish predicate:** can it pass or fail? Is it a predicate rather than a duration? Can it never quietly relax? ([[overnight-contract]])
- [ ] **Escape hatch:** what does the loop do when it's truly stuck: stop and write up why? ([[termination]])
- [ ] **Termination:** is there a goal condition, an iteration cap, a TTL or expiry, and a kill switch? ([[termination]])

**Control**
- [ ] **Cost:** what is the expected spend per iteration × the cadence? Could you start with one triage automation and one verifier? ([[budgets-and-cost]])
- [ ] **Permissions:** which irreversible actions are allowed without a human? Are destructive git commands blocked by a hook? ([[guardrails-and-permissions]])
- [ ] **Output:** does an AFK run end in a reviewable PR, not a merge? ([[afk]])
- [ ] **Idempotency:** what happens if an iteration runs twice, or crashes at any point? Does re-running converge? ([[idempotency]])
- [ ] **Isolation:** does parallel work run in separate worktrees or sandboxes? ([[isolation]])
- [ ] **Visibility:** where do findings land? Can you watch an AFK run live and get notified when it ends? Can you reconstruct what happened? ([[observability]])
- [ ] **AX:** is the codebase clean, modular and well-checked enough that "the repo wins" works for you, not against you? ([[agent-experience]])
- [ ] **Audit:** is there a decision log you can review in minutes, checked by a different model? ([[observability]])
- [ ] **Recovery:** what is the plan when you wake up to a broken build? ([[failure-modes]])

**You**
- [ ] Can you actually review what this loop produces at this cadence? If nobody will, you are building a dark factory: decide that on purpose. ([[operator-debts]], [[software-factory]])
