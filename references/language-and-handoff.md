# Language and handoff rules

Use language that a technically capable user can scan quickly and a new agent can execute without guessing.

## Simplified technical language

- Use short active sentences.
- Put one action or fact in each sentence.
- Use one stable term for one concept. Define an abbreviation on first use.
- Prefer concrete verbs: `read`, `check`, `create`, `run`, `verify`, `record`.
- Avoid idioms, filler, vague praise, and hidden assumptions.
- Separate fact, decision, risk, blocker, and next action.
- Preserve domain terms when precision needs them. Add a short explanation, not a weaker synonym.
- In Italian, use Italian Technical Simplified style. In English, use ASD-STE100-inspired clarity. This is a clarity policy, not a claim of full standard compliance.

## Persistent status format

Keep `STATUS.md` short enough to read in one minute:

```text
Phase: implementation
Last updated: 2026-08-14 18:30 Europe/Rome
Done: REQ-001, REQ-002
Current: REQ-003 — exact next action
Blocked: none
Verification: command -> result
Next: smallest unblocked action
```

Keep the long reasoning in `ARCHITECTURE.md` or `DECISIONS.md`, not in a status diary.

## New-thread protocol

When starting after compaction or in a new thread:

1. Read `AGENTS.md`.
2. Read `PROJECT.md`, `ARCHITECTURE.md`, `STATUS.md`, and active roadmap rows.
3. Inspect `git status` and the exact files named by the current task.
4. Continue from the recorded current item. Do not restart planning or invent a second source of truth.
5. Update the map before ending the turn if decisions or state changed.

Use exact paths, commands, versions, and dates when they affect reproducibility. State uncertainty and unverified external state explicitly.
