---
type: concept
branch: anatomy
tags: [loop-engineering, anatomy, verification, maker-checker]
sources: ["[[src-osmani-loop-engineering]]", "[[src-tns-loop-engineering]]", "[[src-huntley-ralph]]", "[[src-anthropic-building-effective-agents]]", "[[src-pocock-ai-coding-dictionary]]", "[[src-pocock-tdd-skill]]", "[[src-pocock-ralph-tips]]", "[[src-tan-loops-you-can-trust]]", "[[src-tan-pstack-guide-verify-and-ship]]", "[[src-tan-pstack-loop-principles]]", "[[src-inside-pstack-report]]", "[[src-openprose]]", "[[src-omp]]", "[[src-ouroboros]]", "[[src-osmani-claude-code-code-review]]", "[[src-anthropic-fold-subagents]]"]
created: 2026-10-11
updated: 2026-10-27
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
- **Say how far up the evidence ladder you got:** *"1 You said so. 2 You pointed at the line. 3 You showed the bad case can't happen. 4 You ran it. 5 You reproduced it in the running app."* Label every claim *measured*, *inferred* or *guess* ([[src-inside-pstack-report]]).
- **A gap is never a pass.** A worker result missing its SHAs or method is a gap, not a pass. The three verdicts are VERIFIED / NOT VERIFIED / INCONCLUSIVE ([[src-inside-pstack-report]]).
- **A result is a claim.** OpenProse's result convention says *"A result is a claim supported by evidence, not independent proof"*, and *"Completing a response or making a correct observation alone does not establish fulfillment."* An evaluation reports its own outcome separately from its findings about the subject, so a *fulfilled* evaluation can still find *unmet* requirements ([[src-openprose]]).
- **Check every citation.** Before claiming fulfillment, check each claim against the passage it cites. *"never reconstruct positions from memory"*, and *"'Not completed' does not establish 'in progress'"* ([[src-openprose]]).
- **Scope the check to the claim.** omp's goal audit: *"A narrow check (one file passes its unit test) does not prove a broad claim (feature works end-to-end)"*, and *"Uncertainty = not achieved."* Inspect the current state, and *"NEVER rely on earlier-session memory"* ([[src-omp]]).
- **Test the grader before trusting it.** `/ratchet` runs pre-flight checks: an oracle should score ~100% and a null answer ~0%, a judge must fail an empty string or a confident answer to the wrong question, and the same output graded twice must get the same grade. Decisions are made on a frozen **held-out split** whose transcripts are never written ([[src-omp]]). See [[improvement-loops]].
- **Models may withhold, never grant.** In Ouroboros, *"Model judgment may clarify, construct checks, and withhold approval. It cannot grant acceptance; acceptance comes from executed verification."* Only the mechanical stage (lint/build/test/coverage, no LLM) can approve. LLM scoring and multi-model votes can only block, and if no check ran the result is `unverified`, not passed ([[src-ouroboros]]).
- **Execution is not evaluation.** *"Completion is not approval. Task failure is not semantic drift."* Keep worker task states (`completed`/`failed`) separate from AC verdicts (`pass`/`fail`/`not_evaluated`), and *"partial verifier coverage cannot approve a run"* ([[src-ouroboros]]).
- **Hide the answer key.** Ouroboros never shows workers the harness's `verify_command` or `output_assertion`, and retry hints use only sanitized output. *"Hidden grading is a correctness boundary, not a tuning option"* ([[src-ouroboros]]). omp's `/ratchet` gets the same effect with a held-out test split ([[src-omp]]).
- **Name the evidence failure.** `FABRICATION_SUSPECTED` means there is no transcript evidence at all. `EVIDENCE_FORM_MISMATCH` means real work exists but its form can't prove the claim, so retry with a proof form that fits ([[src-ouroboros]]).
- **Show, don't say.** The Claude Code team asks Claude for something runnable (tests, the build, a screenshot compared with the design): *"Instead of saying the task is done, we ask it to show us the result."* A subagent then reviews the diff in fresh context. [[boris-cherny]] estimates that a verification process improves Claude's output **2–3×** (as reported in [[src-osmani-claude-code-code-review]]).
- **Ask what check fits the risk.** *"did someone read the code?"* is an imprecise stand-in for *"what could go wrong with this change, and what check - automated or human - is the right one to catch it?"* ([[src-osmani-claude-code-code-review]]). See [[layered-code-review]].
- **Suspect easy passes.** *"When something passes too easily, suspect the observation method before the system"* ([[src-inside-pstack-report]]).
- **Verdicts expire.** The Claude Code team's human approvals are good for one commit, and an untrusted new commit needs re-approval ([[src-osmani-claude-code-code-review]]). A verdict covers one patch. pstack re-checks with `git patch-id` *"because a chain rebase moves every PR to a new SHA without failing any check"*, and its ledger voids a verdict when the head SHA changes ([[src-inside-pstack-report]]). *(synthesis)* This is verification state treated as [[idempotency|derived from what exists]], not from what was once checked.

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

**Layers, not one gate.** The Claude Code team stacks six imperfect layers (pre-PR verification, AI review, security review, CI, risk-tiered human approval, merge queue and flags) over fast rollback: *"Each layer catches some bugs while missing others"* ([[src-osmani-claude-code-code-review]]). See [[layered-code-review]] and [[rollback-and-recovery]].

pstack's Shipping playbook: *"the agent that judges a change is never the one that wrote it"*. One fresh agent verifies each PR live, and a reviewer from a different model family audits overnight decision logs ([[src-tan-pstack-guide-verify-and-ship]], [[src-tan-pstack-guide-overnight]]).

`/goal` applies the split to the stop condition itself: a fresh small model judges "done" after every turn ([[src-osmani-loop-engineering]]). See [[claude-code-goal]].

**Honest tests.** Only checks you can trust are useful. Vertical red-green TDD stops the model from writing tests of *"imagined behavior"* or rewriting tests to pass when context runs low ([[src-pocock-tdd-skill]]). Block commits unless everything passes: *"Ralph can't declare victory if the tests are red"* ([[src-pocock-ralph-tips]]).

## Evals for the agent itself (Anthropic)
Changing the *architecture* of an agent needs its own verification. Anthropic's recipe ([[src-anthropic-fold-subagents]]):
- One **end-to-end task-completion eval** owned by a central team, plus small sets each team ships with its skills. *"Even a set of 10 golden examples is enough to start."*
- Grade the final message against a rubric, then add routing accuracy (orchestrator) or right-skill/right-tool checks (single loop).
- **Read the flips, not the total.** Cover every agent chain that runs together in production and every rule that must not break, and run each task more than once, because a break may show up in one run of two.
- Where systems are hard to replay, timestamp important events so they can be replayed later as targeted evals.

See [[folding-subagents]]. *(synthesis)* This parallels the Claude Code team scoring its reviewer daily against past incidents ([[src-osmani-claude-code-code-review]]).

## Limits
- *"'done' is a claim and not a proof."* Verification is still the human's job ([[src-osmani-loop-engineering]]). See [[operator-debts]].
- Models chase the reward signal. If the signal is "it compiles", you get placeholders ([[src-huntley-ralph]]). See [[failure-modes]].
- *"green checks mean the asserted properties hold, not that the code is right"* ([[src-pocock-ai-coding-dictionary]]).
- Automated tests check function. *"human review remains crucial"* for fit with broader requirements ([[src-anthropic-building-effective-agents]]).
- **Should the doer see the grader?** Pocock and Tan want the agent to run the checks itself ([[src-pocock-ralph-tips]], [[src-tan-pstack-guide-verify-and-ship]]). Ouroboros hides the harness's grader from it, so it can't be gamed ([[src-ouroboros]]). *(synthesis)* The two combine: the agent's own checks act as backpressure, and the harness keeps a held-out gate. See [[open-questions]].
- Checker sub-agents cost extra tokens, so *"spend them where a second opinion is worth paying for"* ([[src-osmani-loop-engineering]]). See [[budgets-and-cost]].

## Related
[[goal-spec]] · [[termination]] · [[human-in-the-loop]]
