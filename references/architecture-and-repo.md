# Architecture and repository map

The repository is part of the product. Keep it understandable to a new agent and a human maintainer.

## Read-first order

1. Exact project root and `git status`.
2. `AGENTS.md` and existing project instructions.
3. `docs/project/PROJECT.md`.
4. `docs/project/ARCHITECTURE.md`.
5. `docs/project/STATUS.md` and active `ROADMAP.md` items.
6. `docs/project/GRILL.md`, `docs/project/ACTIVE-SKILLS.md`, and `GATES.md`.
7. Manifests, lockfiles, toolchain files, entry points, tests, deployment files, and current generated state.

Preserve unrelated work. Never infer production behavior from a neighboring checkout, stale artifact, or an old chat note.

## Required map fields

### Project

- goal, users, primary flow, scope, non-scope;
- requirement IDs and acceptance conditions;
- platform/runtime/deployment constraints;
- data ownership, privacy, security, performance, and support boundaries.

### Architecture

- system boundary and runtime topology;
- modules and dependency direction;
- data entities, source of truth, migrations, retention, and consistency;
- API/event contracts, validation, authorization, idempotency, errors;
- external services, secrets, queues, storage, limits, failure/recovery;
- build, deploy, health, metrics, logs, and release evidence.

### Traceability

Keep one row per requirement:

| ID | Requirement | Design/architecture | Code/artifact | Verification | Status |
| --- | --- | --- | --- | --- | --- |
| `REQ-001` | observable behavior | section/path | exact file/module | command/screenshot/smoke | planned |

Use `planned`, `in_progress`, `implemented`, `verified`, `blocked`, or `deferred`. `implemented` is not `done`; only `verified` can close a requirement.

Every requirement must have a gate or a concrete manual evidence line. A
checked requirement without evidence is not verified.

## Repository organization

Use the existing structure when it is coherent. Otherwise keep a small predictable layout:

```text
src/ or app/       production source
tests/              tests that match risk boundaries
docs/project/       persistent project map
docs/               user/technical documentation when needed
scripts/            repeatable project commands
assets/             source assets owned by the project
public/             web-served assets when the framework uses it
deploy/             infrastructure/deployment only when needed
GATES.md            unlazy acceptance ledger
PLAN.md             contract and tree when the task is large
```

Do not create folders “for later”. Do not commit build output, credentials, local databases, sessions, or generated research unless the project contract requires them. Use `.gitignore` for confirmed generated/local paths.

## Decisions

Record a decision only if a future agent might wrongly revisit it. Include date, decision, reason, rejected alternative, and consequence. Keep decisions short. Prefer a simple decision over an abstract framework that hides the reason.

## Repository lifecycle

- If the requested project root does not exist, create exactly the requested local path with the map script's explicit `--create-root` flag. Do not guess a production or remote location. If the path may be a typo, stop and resolve it before creating it.
- Initialize git only when the build request includes repository creation or the project workflow requires it; never publish a remote without permission.
- Do not use destructive cleanup to hide a dirty worktree.
- When cleaning, identify exact generated/dead targets, preview the result, and preserve user data and unrelated artifacts.
