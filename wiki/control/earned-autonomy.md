---
type: concept
branch: control
tags: [loop-engineering, control, trust, autonomy]
sources: ["[[src-tan-loops-you-can-trust]]", "[[src-tan-pstack-guide-overnight]]", "[[src-tan-how-i-use-cursor]]", "[[src-pocock-ralph-tips]]", "[[src-pocock-ai-coding-dictionary]]", "[[src-osmani-loop-engineering]]"]
created: 2026-10-12
updated: 2026-10-12
status: draft
---
# Earned autonomy (trust before loops)

**A loop has to earn autonomy before it runs unattended.** Tan: *"A loop you don't trust just produces unchecked work faster, and the mess compounds with every iteration"* ([[src-tan-pstack-guide-overnight]]). Pocock reaches the same rule from the operator's side: start HITL, and go AFK *"once you trust your prompt"* ([[src-pocock-ralph-tips]]). Up: [[control]].

## Why: verification is the limiting step
In Grove's breakfast factory, everything is scheduled around the three-minute egg, and faster toast doesn't help. In agentic development the egg is **reproduction and verification**, because they wait on humans. Until agents can verify, more loops and more parallel agents only grow the review queue: *"Parallelization just gave me more to review and discard"* ([[src-tan-loops-you-can-trust]]). *"Trying to parallelize agents you don't trust yet is a huge waste of tokens"* ([[src-tan-how-i-use-cursor]]). Osmani makes the same point from the human side: review bandwidth is the ceiling ([[src-osmani-loop-engineering]]). See [[operator-debts]].

## The trust ladder
From [[src-tan-loops-you-can-trust]] and [[src-tan-pstack-guide-overnight]]:
1. **Do the work by hand first**, so you know what good looks like.
2. **Give agents your tools and signals**: a verification skill, profiler, logs. See [[verification-skill]].
3. **Make every stage prove its work and stop the line** when it misses the bar. See [[verification]] and [[stage-gated-pipeline]].
4. **Read transcripts and turn recurring failures** into tools, skills or evals. See [[build-the-lever]].
5. **Make the loop autonomous only after it earns trust.** *"Until then, run it while you watch."*

## Same idea, other sources
| Source | Their version |
|---|---|
| Pocock | `ralph-once.sh` (HITL) → capped `afk-ralph.sh` (AFK), and use HITL for risky tasks ([[src-pocock-ralph-tips]]) |
| Pocock's dictionary | *"One cron job that runs one kind of session and opens one reviewable PR is a factory … reviewing them shows how far the loop can be trusted before it's widened"* ([[src-pocock-ai-coding-dictionary]]) |
| Osmani | *"a verifier you actually trust is the only reason you can walk away"* ([[src-osmani-loop-engineering]]) |
| Huntley | the operator watches the stream and tunes Ralph *"like a guitar"* ([[src-huntley-ralph]]) |

## Contradictions & open questions
- **What does full trust permit?** Tan's Autopilot-full merges PRs on a fresh verifier swarm's clean verdict, with no human review ([[src-tan-pstack-guide-overnight]]). She calls a *"dark factory for software"* a possible endpoint ([[src-tan-how-i-use-cursor]]). Pocock treats dark factories as a hazard ([[src-pocock-ai-coding-dictionary]]). See [[software-factory]].

## Related
[[afk]] · [[human-in-the-loop]] · [[overnight-contract]] · [[loop-design-checklist]]
