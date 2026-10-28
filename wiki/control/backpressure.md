---
type: concept
branch: control
tags: [loop-engineering, control, verification, tests]
sources: ["[[src-huntley-ralph]]", "[[src-pocock-ralph-tips]]", "[[src-pocock-feedback-loops-typescript]]", "[[src-pocock-tdd-skill]]", "[[src-pocock-ai-coding-dictionary]]", "[[src-agentos-docs]]", "[[src-omp]]", "[[src-ouroboros]]"]
created: 2026-10-11
updated: 2026-10-19
status: draft
---
# Backpressure

**Backpressure** is any mechanical check wired into the loop to *reject* invalid generations. Huntley names it as phase two of Ralph: *"As code generation is easy now, what is hard is ensuring that Ralph has generated the right thing"* ([[src-huntley-ralph]]). Up: [[control]].

## Where it sits in the loop
It is the mechanical half of [[verification]]. The checker-agent half is [[evaluator-optimizer]].

## Sources of backpressure
From [[src-huntley-ralph]]:
- Tests, *just for the unit that changed*, after each change.
- **Type systems.** Rust gives strong backpressure but compiles slowly. *"It's the speed of the wheel turning that matters, balanced against the axis of correctness."*
- Static analysers and type checkers, which are essential for dynamically typed languages. Without them you get *"a bonfire of outcomes"*.
- Security scanners, or *"anything"* else that can reject output.

## Pocock's feedback-loop stack
From [[src-pocock-ralph-tips]] and [[src-pocock-feedback-loops-typescript]]:
- TypeScript types (*"essentially free feedback for your AI"*)
- unit tests (Vitest)
- Playwright MCP for UI
- ESLint and Prettier through lint-staged
- **Husky pre-commit hooks** that run all of them

*"The best setup blocks commits unless everything passes. Ralph can't declare victory if the tests are red."* *"AI agents don't get frustrated by repetition"*, so a failing hook just makes the agent try again.

## Real services over mocks
[[agentos]]: *"Test through real services, not mocks. No unit tests. Integration tests via MCP against the running engine"* ([[src-agentos-docs]]). This is close to Tan's *prove it works on the real artifact* ([[src-tan-pstack-loop-principles]]), and further from Pocock's fast unit-test stack. Its commit-time `evaluate_commit` is a scored LLM review (pass at 90) against the principles docs. Under this wiki's definition that is automated *review*, not backpressure. See [[verification]].

## Gates on the stream and at publication (omp)
From [[src-omp]]:
- **Stale-edit rejection.** Hashline edits reference per-line content hashes. If the file changed since the last read, *"the anchors diverge — we reject the patch before it corrupts anything."*
- **Stream rules (TTSR).** A regex or AST rule matching mid-output *"aborts the stream mid-token, injects the rule … and retries from the same point."* This is backpressure applied before the action lands.
- **Publication gates.** robomp's `gh_open_pr` runs `bun run fix`, `bun check` and the repo's full `bun run test` (1 h budget). On failure, *"no PR is created"*. `skip_checks` is allowed only for verified pre-existing breakage on the default branch, and is recorded.
- **Exit codes as the loop gate.** `/loop --until '<cmd>'` lets a test command decide whether the loop goes again.

## Design notes
- **Make the mechanical stage the only one that can say yes.** In Ouroboros, only the executed Stage 1 checks can grant acceptance, and the LLM stages can only withhold. Its open issue #2562 shows the next weak point: the detector can record *"commands that cannot fail (e.g. `pytest --version`)"* as evidence ([[src-ouroboros]]). *(synthesis)* A check that can't fail is no backpressure at all.
- **Speed matters.** Slow backpressure means fewer iterations ([[src-huntley-ralph]]).
- **Don't parallelise validation.** Ralph uses only one subagent for build and test, because fanning out validation creates *"bad form back pressure"* ([[src-huntley-ralph]]). See [[orchestrator-workers]].
- **Backpressure can be gamed.** If "compiles" is the only signal, models produce placeholders. See [[failure-modes]]. Tests written in bulk *"test imagined behavior"*, and a model low on context may rewrite a test to pass it. Vertical TDD keeps tests honest ([[src-pocock-tdd-skill]]).
- **Determinism is the point.** *"A flaky test is a broken check"*, and it poisons the self-correction loop ([[src-pocock-ai-coding-dictionary]]).
- **Explain the tests.** Write down *why* each test matters, so future iterations can decide whether to keep, change or fix it ([[src-huntley-ralph]]).

## Contradictions & open questions
- **Terminology.** Pocock's dictionary says: *"Avoid: 'feedback loop' / 'backpressure' — both lump checks together with review"*. It prefers **automated check** ([[src-pocock-ai-coding-dictionary]]). Yet his own earlier articles say "feedback loops" ([[src-pocock-ralph-tips]]). This wiki keeps "backpressure" (Huntley's term) to mean **deterministic checks only**, matching Pocock's "automated check". See [[verification]].

## Related
[[verification]] · [[ralph-loop]] · [[agent-experience]]
