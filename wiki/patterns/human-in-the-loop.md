---
type: pattern
branch: patterns
tags: [loop-engineering, pattern, oversight]
sources: ["[[src-anthropic-building-effective-agents]]", "[[src-osmani-loop-engineering]]", "[[src-huntley-ralph]]", "[[src-tns-loop-engineering]]", "[[src-pocock-ai-coding-dictionary]]", "[[src-pocock-ralph-tips]]", "[[src-pocock-seven-phases]]", "[[src-pocock-triage-skill]]", "[[src-tan-pstack-loop-principles]]", "[[src-tan-loops-you-can-trust]]", "[[src-agentos-docs]]", "[[src-ouroboros]]", "[[src-osmani-claude-code-code-review]]"]
created: 2026-10-11
updated: 2026-10-27
status: draft
---
# Human in the loop

A loop removes the human as **scheduler and quality gate** for every turn ([[src-tns-loop-engineering]]). It does not remove the human altogether: *"The loop changes the work, it does not delete you from it"* ([[src-osmani-loop-engineering]]). Up: [[patterns]].

## HITL vs AFK
Pocock's definition: humans *"pair with the agent during a session — reviewing, redirecting, or collaborating in real time"*. The opposite is [[afk]] ([[src-pocock-ai-coding-dictionary]]).
- **Choose by asking** *"how expensive is a wrong turn, and how late would you catch it?"* Ambiguous, irreversible or hard-to-review work (schema migrations, design decisions, production) stays HITL ([[src-pocock-ai-coding-dictionary]]).
- *"Agents don't reliably know when they're off track; left alone, they tend to push forward rather than stop and ask"* ([[src-pocock-ai-coding-dictionary]]).
- **HITL Ralph** (`ralph-once.sh`) is how you learn and refine a loop prompt, and how you handle risky architectural tasks *"the code from these tasks stays forever"* ([[src-pocock-ralph-tips]]).
- *"Staying in the loop costs your attention, which is the scarce resource."* The skill is moving work safely *out* of the loop ([[src-pocock-ai-coding-dictionary]]).

## Never block on the human (Tan)
*"The human supervises asynchronously. Agents must stay unblocked."* Proceed on **reversible** work (code, notes, splitting tasks) and present the result. **Irreversible** actions (force-push, deleting prod data, sending external messages) still need confirmation. *"Product direction comes from the human. Execution should not block"* ([[src-tan-pstack-loop-principles]]). Her maintenance line leaves the Slack thread open for humans to *correct or reject the repro* before the fix starts, so oversight is optional rather than blocking ([[src-tan-loops-you-can-trust]]).

## Anxiety = uncertainty × powerlessness (AgentOS)
[[agentos]] gives a reason for keeping the human visible: *"When AI acts, you feel uncertain ('what is it doing?') and powerless ('can I stop it?')."* Its answer is that the AI *"screen-shares with you"*, which removes the uncertainty, and *"You control what it can do"*, which removes the powerlessness. *"If either factor is zero, anxiety is zero"* ([[src-agentos-docs]]). *(synthesis)* This maps onto the wiki's two levers: [[observability]] lowers uncertainty, and [[guardrails-and-permissions]] lowers powerlessness.

## Where humans sit
| Touchpoint | Example |
|---|---|
| Design time | Writing specs, skills, `loop.md`, and the stop condition. See [[goal-spec]]. |
| Checkpoints and blockers | Agents *"pause for human feedback at checkpoints or when encountering blockers"* ([[src-anthropic-building-effective-agents]]) |
| Escalation inbox | Runs that find something go to a **triage inbox**. Anything the loop can't handle *"lands in the triage inbox for me"* ([[src-osmani-loop-engineering]]) |
| Watching and tuning | Huntley watches the stream *"looking for patterns of bad behaviour—opportunities to tune Ralph"* ([[src-huntley-ralph]]) |
| Recovery | Deciding between `git reset --hard` and rescue prompts after waking to a broken build ([[src-huntley-ralph]]) |
| Review | *"your job is to ship code you confirmed works"* ([[src-osmani-loop-engineering]]) |
| Triage gate | a skill recommends `ready-for-agent` / `ready-for-human` and waits for your approval ([[src-pocock-triage-skill]]). See [[backlog-triage]]. |
| Problem gate | when the spec fails review, the agent asks the human the evaluator's clarifying questions. When the design loop fails to converge in 5 rounds, the problem goes back to the human ([[src-agentos-docs]]) |
| QA outer loop | an agent writes a QA plan, a human tests and reviews, and new tickets go back to execution ([[src-pocock-seven-phases]]) |

## Humans scaled by risk (Claude Code team)
From [[src-osmani-claude-code-code-review]]. The goal is that most PRs merge with **at most one person** in the loop, who may be the author, without more reverts or incidents. A classifier sets each change's tier from the *change*, not the author: low risk needs no human once automated checks are green, medium needs one, high needs two. Some paths (sensitive areas, CI workflow files) always need a person. *"Agent approvals don't count as human approvals"*, and the operator of an agent author always counts as a required reviewer. See [[layered-code-review]].

What stays human:
- **Should we even build this?** Vision, taste and goals. Pivot early in the thread rather than block a finished PR: *"Because it was easy to write the code in the first place, it doesn't feel like a loss to close the PR."*
- **Auditing dangerous code:** billing, the auto-updater, CI workflows.
- **Architecture,** *"because those choices set the conventions others follow."*
- **Checking proofs** (test output, commands, screenshots, reviewer comments). *"If you can't describe what the checks would miss, don't ask for a 👍, you need a real review!"*
- **Taking responsibility.** *"A person answers for every change that ships, whoever typed it."*

## Interview first, then stop on judgement (Ouroboros)
[[ouroboros]] puts the human at the **front**: a Socratic interview until the ambiguity score is ≤ 0.2, followed by Seed approval. From Gen 2 on, the evolutionary loop runs without the human. Its guide lists when a human should step back in: *"The completion criteria are already met. The same question or failure repeats. The changes are small relative to the cost of running. The product direction itself needs a human decision"* ([[src-ouroboros]]).

## Contradictions
- **Ask or proceed?** Anthropic: agents *"pause for human feedback at checkpoints or when encountering blockers"* ([[src-anthropic-building-effective-agents]]). Pocock: agents *"tend to push forward rather than stop and ask"*, and that is a *risk* ([[src-pocock-ai-coding-dictionary]]). Tan: *don't* ask on reversible work ([[src-tan-pstack-loop-principles]]). These are reconcilable by reversibility and the cost of a wrong turn *(synthesis)*. Tan resolves ambiguity *before* the run with a finish condition and restatement, which matches Pocock's "give input before".

## Capacity limit
Worktrees remove mechanical collisions, but *"YOU are still the ceiling, your review bandwith decides how many you can actually run"*. Osmani calls this the orchestration tax ([[src-osmani-loop-engineering]]). See [[operator-debts]].

## Related
[[verification]] · [[guardrails-and-permissions]]
