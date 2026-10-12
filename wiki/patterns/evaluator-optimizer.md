---
type: pattern
branch: patterns
tags: [loop-engineering, pattern, maker-checker, verification]
sources: ["[[src-anthropic-building-effective-agents]]", "[[src-osmani-loop-engineering]]", "[[src-tns-loop-engineering]]", "[[src-pocock-ai-coding-dictionary]]", "[[src-tan-pstack-guide-overnight]]", "[[src-tan-pstack-guide-verify-and-ship]]", "[[src-tan-how-i-use-cursor]]"]
created: 2026-10-11
updated: 2026-10-12
status: draft
---
# Evaluator–optimizer (maker / checker)

In the **evaluator-optimizer** pattern, *"one LLM call generates a response while another provides evaluation and feedback in a loop"* ([[src-anthropic-building-effective-agents]]). Loop-engineering sources call this the **maker/checker split** and treat it as the most important structural decision in a loop ([[src-osmani-loop-engineering]], [[src-tns-loop-engineering]]). Up: [[patterns]].

## When it fits
From [[src-anthropic-building-effective-agents]]:
- There are clear evaluation criteria, and iterating improves results measurably.
- A human's feedback would demonstrably improve the output, *and* an LLM can give that kind of feedback.

## Making the checker independent
- Give it different instructions, and sometimes a **different model** ([[src-osmani-loop-engineering]]).
- Check against **project skills and existing tests**, not just the maker's own claims ([[src-osmani-loop-engineering]]).
- Give it a **fresh context**. The authoring session *"reads its own conclusions back as confirmation"*, while a fresh reviewer *"sees the diff the way a stranger would"* ([[src-pocock-ai-coding-dictionary]]).
- **Scope** its system prompt to what you actually care about (security, API contracts, performance), not *"a vague 'look for problems'"* ([[src-pocock-ai-coding-dictionary]]).
- Use a **different model family**. Tan uses multi-model adversarial review (`/interrogate`), and her overnight audit reviewer is from another model family ([[src-tan-how-i-use-cursor]], [[src-tan-pstack-guide-overnight]]).
- Use **fresh verifier swarms**: *"no owner merges on its own verdict"*, and verification re-runs at every push that changes the patch ([[src-tan-pstack-guide-overnight]]). *"the agent that judges a change is never the one that wrote it"* ([[src-tan-pstack-guide-verify-and-ship]]).
- Treat it as a **filter, not a gate**. It is non-deterministic, so it misses things and flags non-issues ([[src-pocock-ai-coding-dictionary]]).
- Apply the same split to the stop decision: `/goal` uses a fresh model to judge completion. See [[goal-loop]].

## Where it sits in the loop
It is the agent-based half of [[verification]]. The other half is mechanical [[backpressure]].

## Related
[[orchestrator-workers]] · [[budgets-and-cost]]
