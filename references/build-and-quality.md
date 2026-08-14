# Build and quality gates

“Production-ready” is a set of evidence, not a tone.

## Build order

1. Parse/configure/typecheck the smallest changed unit.
2. Run focused unit/integration tests for the changed risk boundary.
3. Build the relevant package or target.
4. Run the full project gate required by the repository.
5. Run a real smoke path: browser, device, CLI, API, worker, desktop binary, or deployed preview as applicable.
6. Record commands and results in `docs/project/STATUS.md` and map them to `TRACEABILITY.md`.

Use existing package scripts and lockfiles. Do not silently change Node, Rust, Python, Go, Xcode, Android, or provider versions. If a version change is necessary, record the reason, affected contracts, and rollback/recovery path.

## Correctness gates

Check the relevant cases:

- happy path and invalid input;
- empty, loading, error, retry, timeout, and offline;
- authorization, permissions, secret boundaries, and unsafe input;
- idempotency, duplicate events, concurrency, migrations, and recovery;
- long content, localization, accessibility, keyboard/touch, and platform lifecycle;
- performance budgets and resource cleanup when requested.

## Safe cleanup

Inspect before cleanup. Identify exact targets. Preview size/scope. Remove only generated or demonstrably dead files within the request. Preserve credentials, cookies, databases, sessions, user assets, research output, ignored runtime state, and unrelated work. Never use a broad recursive delete to make a report look clean.

## No half measures

Do not mark a feature complete when a real provider, migration, UI state, permission path, test gate, packaging step, or documentation row is missing. If an external system blocks one part, complete the independent parts and mark the exact row blocked.

## Handoff evidence

The final status must name:

- changed paths and requirement IDs;
- commands run and results;
- actual platform/browser/device/provider checked;
- generated artifacts and where they live;
- remaining blocker, if any, in one concrete sentence;
- next roadmap item.
