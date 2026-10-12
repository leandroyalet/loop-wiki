---
type: concept
branch: anatomy
tags: [loop-engineering, anatomy, verification, maker-checker]
sources: ["[[src-osmani-loop-engineering]]", "[[src-tns-loop-engineering]]", "[[src-huntley-ralph]]", "[[src-anthropic-building-effective-agents]]", "[[src-pocock-ai-coding-dictionary]]", "[[src-pocock-tdd-skill]]", "[[src-pocock-ralph-tips]]", "[[src-tan-loops-you-can-trust]]", "[[src-tan-pstack-guide-verify-and-ship]]", "[[src-tan-pstack-loop-principles]]"]
created: 2026-10-11
updated: 2026-10-12
status: solid
---
# Verification

**Verification** decides whether the loop's output is actually right, as opposed to merely produced. Osmani calls splitting the writer from the checker *"the most useful structural thing in a loop, by far"* ([[src-osmani-loop-engineering]]), and TNS calls the verifier *"the part that earns trust"* ([[src-tns-loop-engineering]]). Up: [[anatomy]].

## Where it sits in the loop
It comes after [[observation]] and before state is written and [[termination]] is decided.

## Verification is the limiting step
Tan applies Grove's *High Output Management*: a line is scheduled around its slowest step, and in agentic development that step is reproduction and verification, which wait on humans. *"Verification has become the limiting step, or long pole of software development"* ([[src-tan-loops-you-can-trust]]). *"Make the agent able to do it, and you stop being the bottleneck. Skip it, and running more agents only gets you more unchecked work to review"* ([[src-tan-pstack-guide-verify-and-ship]]). See [[earned-autonomy]] and [[verification-skill]].

## Proof, not claims
- **Prove it works.** Check the real artifact, not *"proxies, self-reports, or 'it compiles.'"* Script the check so a reviewer can re-run it ([[src-tan-pstack-loop-principles]]).
- **Match the check to the change.** A CLI change runs the command. A UI change walks the flow or diffs a frozen baseline. A parser change replays input. A perf change compares profiles. A storage change reads the value back ([[src-tan-pstack-guide-verify-and-ship]]).
- **Artifacts over explanations.** Ask for the failing→passing test, a before/after video, the trace. *"treat a confident reply without evidence as a red flag."* "Inconclusive" is an acceptable verdict ([[src-tan-pstack-guide-verify-and-ship]], [[src-tan-loops-you-can-trust]]).
- **Vet numbers** with a seven-question benchmark checklist before trusting a speedup ([[src-tan-pstack-guide-verify-and-ship]]).

## Three layers (Pocock's vocabulary)
| Layer | Nature | Catches | Cost |
|---|---|---|---|
| **Automated check** | deterministic, pass/fail: tests, types, lint, build, pre-commit | what can be asserted mechanically | cheap, and the agent self-corrects |
| **Automated review** | an agent judging another agent's work, *"often with a different model or system prompt"* | judgement-shaped issues: naming, missed edge cases | machine cost, non-deterministic |
| **Human review** | *"Reading the diff counts; reading the summary doesn't."* | everything else | expensive, and scales worst |

Source: [[src-pocock-ai-coding-dictionary]]. Treat automated review as *"a filter that raises the floor before a human looks, not a gate that replaces one."* It works because of **fresh context**: the authoring session *"reads its own conclusions back as confirmation"* ([[src-pocock-ai-coding-dictionary]]).

## Two families (Huntley, Osmani)
1. **Mechanical [[backpressure]]:** tests, type systems, static analyzers and security scanners that reject bad output. They are cheap and fast. *"the wheel has got to turn fast"* ([[src-huntley-ralph]]).
2. **A separate checker agent:** a second agent with different instructions, and sometimes a different model, because *"the model that wrote the code is way too nice grading its own homework"* ([[src-osmani-loop-engineering]]). This is the [[evaluator-optimizer]] pattern ([[src-anthropic-building-effective-agents]]).

pstack's Shipping playbook: *"the agent that judges a change is never the one that wrote it"*. One fresh agent verifies each PR live, and a reviewer from a different model family audits overnight decision logs ([[src-tan-pstack-guide-verify-and-ship]], [[src-tan-pstack-guide-overnight]]).

`/goal` applies the split to the stop condition itself: a fresh small model judges "done" after every turn ([[src-osmani-loop-engineering]]). See [[claude-code-goal]].

**Honest tests.** Only checks you can trust are useful. Vertical red-green TDD stops the model from writing tests of *"imagined behavior"* or rewriting tests to pass when context runs low ([[src-pocock-tdd-skill]]). Block commits unless everything passes: *"Ralph can't declare victory if the tests are red"* ([[src-pocock-ralph-tips]]).

## Limits
- *"'done' is a claim and not a proof."* Verification is still the human's job ([[src-osmani-loop-engineering]]). See [[operator-debts]].
- Models chase the reward signal. If the signal is "it compiles", you get placeholders ([[src-huntley-ralph]]). See [[failure-modes]].
- *"green checks mean the asserted properties hold, not that the code is right"* ([[src-pocock-ai-coding-dictionary]]).
- Automated tests check function. *"human review remains crucial"* for fit with broader requirements ([[src-anthropic-building-effective-agents]]).
- Checker sub-agents cost extra tokens, so *"spend them where a second opinion is worth paying for"* ([[src-osmani-loop-engineering]]). See [[budgets-and-cost]].

## Related
[[goal-spec]] · [[termination]] · [[human-in-the-loop]]
