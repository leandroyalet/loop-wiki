---
type: pattern
branch: patterns
tags: [loop-engineering, pattern, spec-evolution, convergence]
sources: ["[[src-ouroboros]]"]
created: 2026-10-19
updated: 2026-10-19
status: stub
---
# Evolutionary loop (spec ⇄ evaluation)

An **evolutionary loop** iterates on the *specification* as well as the code. Each generation runs against a fixed spec, is evaluated, and then the findings are used to write the **next** spec. The loop ends when the spec stops changing. [[ouroboros]]: *"Each cycle does not repeat — it evolves. The output of evaluation feeds back as input for the next generation"* ([[src-ouroboros]]). Up: [[patterns]].

## Where it sits in the loop
- **[[goal-spec]]:** frozen *within* a generation (*"Once a run starts, the Seed does not change within that run"*) and rewritten *between* generations.
- **[[verification]]:** each generation's evaluation result is the input to the next spec.
- **[[decision-step]]:** two engines. Wonder asks *"What do we still not know?"*, and Reflect asks *"How should the spec evolve?"*
- **[[termination]]:** convergence of the spec, not only success of the output.
- **[[context-and-state]]:** a *lineage* of generations in an event store, so each step can be stateless.

## Mechanics (Ouroboros)
All from [[src-ouroboros]]:
```
Gen 1:  Seed(O₁)              → Execute → Evaluate
Gen 2:  Wonder(O₁,E₁) → Reflect → Seed(O₂) → Execute → Evaluate
...until convergence or max_generations (30)
```
- **Gen 1** comes from a human interview. **Gen 2+** is *"fully autonomous — the Wonder and Reflect engines replace human input."*
- **Stop signals** (any one ends the loop, checked only after at least 2 generations):
  - ontology similarity ≥ 0.95
  - stagnation: similarity stays at or above the threshold for 3 generations
  - oscillation: generation N ≈ generation N−2
  - the cap of 30 generations
- **`ooo ralph`** runs the loop as a background job, and also stops on a QA pass, a regressing grade, cancellation or a time limit.
- **The two gates:** *"Ambiguity <= 0.2 — Do not build until you are clear"* and *"Similarity >= 0.95 — Do not stop evolving until you are stable."*

## How it differs from neighbours *(synthesis)*
| | [[goal-loop]] | [[ralph-loop]] (Huntley) | [[improvement-loops]] (`/ratchet`) | Evolutionary loop |
|---|---|---|---|---|
| Spec | fixed condition | fixed specs, evolving plan | fixed eval, evolving prompt | **evolving spec** |
| Stops when | the condition holds | never (a human stops it) | plateau or done | the spec converges (or QA passes) |
| Human role | writes the condition | watches | approves inputs, grader and plan | interviews for Gen 1, then optional |

## Contradictions & open questions
- **Autonomous spec change vs "never relax the goal".** Tan: *"the finish condition never quietly relaxes"* ([[src-tan-pstack-guide-overnight]]). omp: *"NEVER redefine success as a smaller … subset"* ([[src-omp]]). Here, Reflect rewrites the ACs by design. The safeguard is that a modified Seed or a reinterpreted goal triggers multi-model consensus, which can only withhold approval ([[src-ouroboros]]). Whether that is enough is untested.
- **Convergence ≠ correctness** *(synthesis)*. A stable ontology means the spec stopped changing, not that the result meets the user's need. The source's own *safe-but-wrong output* warning applies ([[src-ouroboros]]). See [[failure-modes]].
- It has a single source, and no field data.

## Related
[[patterns]] · [[goal-spec]] · [[termination]] · [[loop-pattern-comparison]]
