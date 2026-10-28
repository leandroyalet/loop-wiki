---
type: concept
branch: anatomy
tags: [loop-engineering, anatomy, specification]
sources: ["[[src-huntley-ralph]]", "[[src-osmani-loop-engineering]]", "[[src-anthropic-building-effective-agents]]", "[[src-pocock-ralph-tips]]", "[[src-pocock-triage-skill]]", "[[src-pocock-seven-phases]]", "[[src-tan-pstack-guide-overnight]]", "[[src-tan-pstack-guide-poteto-mode]]", "[[src-tan-pstack-guide-verify-and-ship]]", "[[src-agentos-docs]]", "[[src-openprose]]", "[[src-omp]]", "[[src-ouroboros]]"]
created: 2026-10-11
updated: 2026-10-19
status: draft
---
# Goal spec (definition of done)

The **goal spec** is the written statement of what the loop is trying to achieve and how anyone can tell it has succeeded. Osmani frames a loop as *"a recursive goal where you define a purpose and the AI iterates until complete"* ([[src-osmani-loop-engineering]]). Up: [[anatomy]].

## Where it sits in the loop
[[context-and-state]] loads the spec every iteration. [[verification]] checks against it, and [[termination]] reads the result.

## Forms it takes
- **Spec files.** Ralph's specs are written through a long conversation with the agent before any building starts, *"one per file, in the specifications folder"*, and loaded every loop ([[src-huntley-ralph]]).
- **A verifiable stop condition.** `/goal "all tests in test/auth pass and lint is clean"` ([[src-osmani-loop-engineering]]). See [[claude-code-goal]].
- **A prioritised plan.** Ralph's `fix_plan.md` is the running to-do list that the loop maintains and the human *"watch[es] like a hawk"* ([[src-huntley-ralph]]).
- **A PRD that describes the end state.** *"The PRD describes the end state, not the journey"* ([[src-pocock-seven-phases]]). Pocock structures items as JSON with `passes: false`, an idea taken from Anthropic's long-running-harness article. Ralph flips each item to `true`, so the PRD is *"both scope definition and progress tracker"*. It can be edited mid-flight: reset `passes`, or add items ([[src-pocock-ralph-tips]]).
- **Agent briefs on tickets.** These are *durable* rather than precise: types, signatures and behaviours, never file paths or line numbers ([[src-pocock-triage-skill]]). See [[backlog-triage]].
- **Clear success criteria** are what make agents worthwhile in the first place ([[src-anthropic-building-effective-agents]]).
- **Composable contracts.** [[openprose]] writes the goal as Markdown requirements at a versioned address, and adopts reusable conventions by linking to them: *"You set goals instead of prescribing steps."* A procedure *"may be supplied or chosen, and replaced while preserving requirements."* Requirements are kept apart from inputs, since the supplied notes are *"task data, not instructions"*. Conflicting adopted documents need *"an authorized resolution; adding documents does not decide precedence"* ([[src-openprose]]).
- **A standing invariant.** An OpenProse *responsibility* states *"what should stay true"* rather than what to finish. Its `### Maintains` postconditions are the goal, and they are compiled to validators ([[src-openprose]]). See [[reconciler-loop]].
- **An interviewed objective with five fixed fields.** omp's `/guided-goal` asks one question at a time (≤6 questions) until five things are pinned down: binary success criteria, a verification method, an attempt cap, boundaries with a denylist, and stop/escalation conditions. The result is written as `## Objective / Success criteria / Verification / Boundaries / Stop conditions`. It rejects *"uncapped iteration ('until CI is green', 'keep going until it works')"* and *"self-graded success without verification command"* ([[src-omp]]).
- **A scored, graded spec file.** [[ouroboros]] interviews until its **ambiguity score** is ≤ 0.2. The score is 1 − the weighted clarity of goal (40%), constraints (30%) and success criteria (30%), and *"A low score can still hide wrong content."* It then writes a YAML **Seed** with `goal`, `constraints`, `acceptance_criteria`, `ontology_schema`, `evaluation_principles` and `exit_conditions`. Non-goals and assumptions go to a separate **Ledger**. Seeds are graded A/B/C, and only grade A runs unattended ([[src-ouroboros]]). See [[evolutionary-loop]].

## A predicate, not a duration
*"a duration is not a finish condition. 'work on this for 4 hours' gives the agent nothing to check … Give /loop a predicate that can pass or fail"* ([[src-tan-pstack-guide-overnight]]). The done check *"must be able to pass or fail. 'Make it better' and 'work on it for an hour' aren't checks"* ([[src-tan-pstack-guide-poteto-mode]]). Example: *"done means zero old callers, all parser fixtures pass, old api deleted."* State it up front, and ask for the **proof** you want to see ([[src-tan-pstack-guide-verify-and-ship]]). See [[overnight-contract]]. omp's version is *"NEVER redefine success as a smaller, easier, or already-completed subset,"* and its goal can't be dropped and replaced by the agent ([[src-omp]]).

**Restate before acting.** For noisy reports, the first step is a plain-English restatement with *"don't change any code yet"*, so a misreading costs one message instead of one wrong fix. Hold back your own theory of the cause, because it narrows the search ([[src-tan-pstack-guide-poteto-mode]]).

## Fence the scope, and gate the spec
[[agentos]]'s problem definition (`pain.md`) must do five things:
- name the pain in one sentence
- list the affected personas
- cite evidence as `file:line` and exact errors
- state the forward-looking pain
- say honestly what is still unknown

Its **"Explicit non-problems"** section is *"the single most load-bearing section — it's what keeps the solution from overreaching."* The opposite error is named too: *"Pre-shrinking the problem to make the solution feel smaller is the single most common failure mode."* An adversarial evaluator must **pass the spec** before any proposal is written. It *"rejects vague pain, solutioneering, and overscoped problems"* ([[src-agentos-docs]]). *(synthesis)* This is verification applied to the goal itself, before the loop starts.

## Specify against shortcuts
*"the vaguer the task, the greater the risk. Ralph might loop forever … Or it might take shortcuts, declaring victory."* For example, Ralph skipped "internal" commands and marked them as excluded from coverage. The fix is to specify the **files to include**, the **stop condition**, and the **edge cases** ([[src-pocock-ralph-tips]]). See [[failure-modes]].

## Why it matters
Bad specs produce confidently wrong loops. Huntley lost about a month because his lexer spec defined one keyword twice for opposing cases: *"it's easy to blame the tools instead of the operator"* ([[src-huntley-ralph]]). An agent *"will fill any hole in your intent with a confident guess"* (intent debt, [[src-osmani-loop-engineering]]). See [[operator-debts]]. Ouroboros: *"Most AI coding fails at the **input**, not the output. The bottleneck is not AI capability — it is human clarity"* ([[src-ouroboros]]).

## Contradictions & open questions
- How precise must a goal be? `/goal` wants a machine-checkable condition. Ralph trusts the model to *"choose the most important thing"* from a fuzzy plan. These two ends of the spectrum are compared in [[loop-pattern-comparison]].

## Related
[[verification]] · [[termination]] · [[writing-a-loop-prompt]]
