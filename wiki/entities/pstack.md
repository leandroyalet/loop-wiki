---
type: entity
branch: entities
tags: [loop-engineering, product, pstack, skills]
sources: ["[[src-tan-how-i-use-cursor]]", "[[src-tan-pstack-guide-poteto-mode]]", "[[src-tan-pstack-guide-principles]]", "[[src-tan-pstack-guide-overnight]]", "[[src-tan-x-short-posts]]", "[[src-pocock-getting-started-with-ralph]]"]
created: 2026-10-12
updated: 2026-10-12
status: draft
---
# pstack

[[lauren-tan]]'s plugin of skills *"for rigorous engineering with agents"*. It lives in Cursor's official plugin repo (`cursor/plugins/pstack`, v0.15.21 when fetched) and is also available in Grok Bot ([[src-tan-x-short-posts]]). It grew out of *"turning every recurring failure mode into a skill"* ([[src-tan-loops-you-can-trust]]). Up: [[entities]].

## Shape
- **`/poteto-mode`:** a higher-order router that reads the principles, matches one of **23 playbooks**, copies its steps into a todo list, and calls the other skills as needed ([[src-tan-pstack-guide-poteto-mode]]).
- **24 principles**, each a skill. Agents must name the decision each principle changed ([[src-tan-pstack-guide-principles]]).
- **Workflow skills**, including `/how`, `/why`, `/architect`, `/arena`, `/interrogate`, `/tdd`, `/unslop`, `/swarm`, `/reflect`, `/figure-it-out`, `/show-me-your-work`, `/create-verification-skill`, `/maintain-verification-skill` and `/benchmark-checklist` ([[src-tan-how-i-use-cursor]], [[src-tan-pstack-guide-verify-and-ship]]).
- **Loop-relevant playbooks:** Autonomous run, Pause safely, Session pickup, Babysit, Shipping, Autopilot-full, Autopilot-stack, Orchestrate, Hillclimb ([[src-tan-pstack-guide-overnight]], [[src-tan-pstack-guide-poteto-mode]]).
- **Automation pack:** benny ([[src-tan-benny-automation]]).

## Where it fits
pstack is **what runs inside each iteration**: the rigor. Cursor's `/loop` and Automations provide the trigger and the repetition ([[src-tan-pstack-guide-overnight]]). Compare AI Hero's line: *"Ralph is the loop. Skills are what's inside"* ([[src-pocock-getting-started-with-ralph]]). See [[loop-primitives]].

## Related
[[cursor]] · [[verification-skill]] · [[build-the-lever]]
