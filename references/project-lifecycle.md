# Project lifecycle

Use this chapter for every new build or major change. Keep the loop short for a small fix, but do not skip understanding, tracking, or verification.

## Grill protocol

Read `bundled-skills/grill-me/SKILL.md`, invoke the bundled `grill-me` skill,
and start a real `/grilling` session. The goal is not to produce a long
specification. The goal is to remove ambiguity that would change the
architecture, cost, safety, user outcome, or delivery order. Record the
session in `docs/project/GRILL.md`; a name in chat is not activation evidence.

Use a first round of no more than seven grouped questions. Ask follow-ups only when an unanswered point changes scope, architecture, safety, cost, or acceptance. Ask about:

1. The user and the problem.
2. The smallest successful outcome.
3. Required and forbidden behavior.
4. Data, integrations, permissions, security, and failure states.
5. Platform, runtime, deployment, budget, and version constraints.
6. Design, accessibility, localization, performance, and operations.
7. Acceptance evidence and what “done” means.

Use the repository to answer questions before asking the user. Ask for a choice only when different answers create materially different work. Offer a recommended option with a short reason. Stop grilling when the project contract is testable.

Before implementation, read the bundled `unlazy` and `ponytail` entrypoints,
create `GATES.md`, and record all three baseline routes in
`docs/project/ACTIVE-SKILLS.md`. If `/grilling` is unavailable, record the
exact `GRILL-FALLBACK` reason before using the embedded question set.

## Contract format

Write a compact contract in `docs/project/PROJECT.md`:

```text
Goal: one user outcome.
Users: who acts and why.
In scope: numbered deliverables.
Out of scope: explicit exclusions.
Constraints: platform, data, security, performance, budget.
Acceptance: observable conditions for each REQ-*.
```

Convert vague terms into observable behavior. “Fast” becomes a measured budget. “Secure” becomes authentication, authorization, validation, secret handling, and an abuse boundary. “Production-ready” becomes build, test, deploy, monitoring, rollback/recovery, and documentation evidence.

## Work loop

For each roadmap item:

1. Read the project map and inspect the actual code path.
2. State the smallest implementation slice and its risks.
3. Implement the complete slice with existing conventions.
4. Run the smallest relevant check immediately.
5. Run the broader gate when the slice is complete.
6. Update traceability, status, and the roadmap.

Do not let a plan become a substitute for implementation. Do not silently expand scope because a specialist skill suggests a nice-to-have.

## Question semantics

When the user asks “Should we use X?”, compare X with the current approach and answer. When the user asks “What would it take to add Y?”, explain scope, risks, and plan. Wait for authorization before implementing a proposal. A build request is different: within its scope, act on cheap reversible work and report it after completion.
