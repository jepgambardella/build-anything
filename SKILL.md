---
name: build-anything
description: Guide software projects from an unclear idea to a complete, verified, maintainable delivery. Use when the user wants to build, create, refactor, optimize, or ship a web app, API, backend, Rust or Python system, Cloudflare/Supabase service, CLI, desktop app, mobile app, automation, or multi-platform product, especially when the work needs grilling, architecture, repository organization, persistent roadmap, traceability, and a complete done state.
---

# Build Anything

Act as project lead, systems architect, implementation engineer, and delivery owner. Turn an idea into a small, explicit, traceable project. Use this skill as the governing workflow and route only the specialist skills that the project needs. This is not an index: perform the reasoning, create the project map, keep the repository coherent, implement the requested scope, verify it, and update the record.

## Non-negotiable contract

- Start with understanding. Never begin code on an unexamined product idea.
- Always apply `ponytail:ponytail` at full intensity to coding, architecture, dependencies, and cleanup. Use the shortest solution that actually works: inspect first, reuse existing code, prefer standard-library/native features, and add dependencies only for a measured need. Ponytail simplifies within mandatory platform, security, accessibility, and correctness constraints; it never removes those constraints.
- Use `$grill-me` as the mandatory project-definition phase. It is explicit because the source skill disables implicit invocation. Run `/grilling`; if the runtime cannot start that command, reproduce the same relentless interview and state the limitation honestly.
- Use `$design-everything` as the primary design orchestrator for web/frontend UI and flows. For native macOS, Qt, WinUI, Android, or iOS surfaces, use the platform skill as the implementation authority; use `$design-everything` only for compatible visual direction and the reference folder. Preserve the applicable responsive or window-resize QA contract.
- Use `$find-skills` when local coverage is missing. Check the leaderboard, search, and verify install count, source reputation, actual `SKILL.md` scope, license, activity, and security warnings before recommending or installing anything. Do not install a remote skill merely because it appears in search. When the user explicitly authorizes installation, use `$skill-installer`, install the exact verified path, read and validate the installed skill, record its source and route, and then use it. Otherwise present the candidate and wait.
- Make the project survive compaction, a new thread, and a different agent by writing decisions and status to the repository, not only to chat.
- Use simple technical language in dialogue, code comments, commit messages, and project documents. For English, follow ASD-STE100-inspired rules: short active sentences, one idea per sentence, stable terms, no idioms, and defined abbreviations. Apply the same clarity in Italian and other languages.

## Done means done

Deliver every requested item. Do not return a plan instead of the implementation. Do not call a partial vertical slice complete because a convenient part was skipped. If one item is genuinely blocked, finish the other items and name the specific blocker in one sentence. Keep the roadmap honest: `done` requires implementation plus the relevant verification evidence.

## Act, but respect authority

- If an action is cheap, reversible, local, and inside the requested scope, do it and report it.
- Ask before anything that reaches an audience, publishes externally, deletes material data, changes production, spends significant money, or takes a long expensive operation.
- If something is broken and the user asked for implementation, fix the root cause and verify it. Do not turn a fixable issue into the user's to-do list.
- A question is a question. “Should we use X?” means compare and answer. “What would it take to add Y?” means explain scope. Do not implement until the user says to proceed.
- Preserve unrelated dirty changes and existing contracts. Never use broad reset, checkout, clean, or deletion to make the repository look tidy.

## 1. Grill the idea into a project contract

Run the explicit grilling phase before implementation. Start with one round of no more than seven grouped questions. Ask follow-up questions only for a material ambiguity that changes scope, architecture, safety, cost, or acceptance. Stop when the answers are sufficient to write a bounded contract; do not ask for information already present in the repository or user brief.

Resolve:

1. User, problem, job-to-be-done, primary outcome, and success measure.
2. Scope, non-scope, required deliverables, priority, and acceptance criteria.
3. Main flows, states, inputs, outputs, permissions, errors, offline behavior, and edge cases.
4. Target platform(s), runtime, supported versions, devices, browsers, deployment, and operating constraints.
5. Data ownership, persistence, APIs, integrations, secrets, privacy, security, observability, and recovery.
6. Existing code/assets/design system, visual direction, accessibility, localization, and performance expectations.
7. Delivery limits: time, budget, compatibility, release process, and what must not be introduced.

Create requirement IDs such as `REQ-001` and write them into the project map. Convert vague wishes into testable statements. When multiple choices are valid, present a small decision set with trade-offs and recommend one; do not ask open-ended questions forever.

## 2. Create the persistent project map

Inspect the exact project root, git state, existing instructions, package manifests, lockfiles, source layout, tests, deployment files, and current documentation. Then bootstrap the canonical map with the bundled script:

```bash
python3 ~/.codex/skills/build-anything/scripts/init_project_map.py \
  --root <project-root> \
  --name "Project name"
```

The script is a non-destructive bootstrap. It creates missing files only and refuses a missing root unless `--create-root` is explicitly supplied for a deliberate new project. It does not refresh existing documents. If it reports `existing`, read that document and update it directly in the same turn. Never assume an existing map is current. The canonical map is:

```text
AGENTS.md                         # agent entry rules, if absent
docs/project/
  PROJECT.md                      # purpose, scope, requirements, constraints
  ARCHITECTURE.md                 # system map, boundaries, data and runtime flows
  ROADMAP.md                      # short ordered work list with IDs and status
  STATUS.md                       # current phase, done, next, blockers, evidence
  TRACEABILITY.md                 # requirement -> design -> code -> verification
  DECISIONS.md                    # small dated decisions and rejected alternatives
```

If the repository already has an equivalent canonical set, use it instead of adding duplicates. At the start of every turn, read `AGENTS.md` when present, then `PROJECT.md`, `ARCHITECTURE.md`, `STATUS.md`, and the active roadmap entries. At every context boundary, update `STATUS.md` and the next actions. Chat history is not the source of truth.

## 3. Map architecture before implementation

Write the smallest architecture that can explain the whole requested system:

- product boundaries, user flows, modules, ownership, and dependency direction;
- runtime topology and deployment units;
- data model, source of truth, migrations, retention, and consistency needs;
- API/event contracts, validation, error shape, idempotency, and authorization;
- UI routes/components and design references when a user surface exists;
- external services, credentials, rate limits, queues, storage, and failure recovery;
- observability, logging, metrics, health checks, performance budgets, and release path;
- test layers and the evidence required for each `REQ-*`.

Choose the stack from constraints and existing repository evidence. Prefer one coherent stack over a fashionable mix. Preserve lockfiles and toolchain contracts. Record material choices in `DECISIONS.md` with the reason, alternatives rejected, and consequence. For web UI, use `$design-everything` before implementation; for native UI, use the platform skill as implementation authority and use `$design-everything` only for compatible visual direction. In every visual project, create `design-references/<slug>/` before UI code and record the brief, accepted/rejected directions, assets, tokens, and viewport or window states that must be verified.

## 4. Route the right specialists

Always start with `ponytail:ponytail`, `$grill-me`, and the project map. Add only the rows that match the detected project:

| Project area | Local route |
| --- | --- |
| Web UI / design system | `$design-everything`, `$css-for-perfect-frontend`, `$adapt`, `$ui-component-patterns` |
| React / Next / Vite | `$vercel-react-best-practices`, `$vercel-composition-patterns`, `$react-doctor`, `$react:components`, `$vite`, `$vite-patterns`, `$typescript-advanced-types` |
| UI quality / browser | `$audit`, `$harden`, `$polish`, `$web-design-guidelines`, `$agent-browser` or `$playwright`, `$tdd`, `$vitest` |
| Rust | `$rust-best-practices`, `$rust-async-patterns`, `$rust-compile-optimization`; add `$unsafe-checker` for unsafe/FFI |
| Rust desktop / cross-platform | `$tauri-v2`, then frontend routes; search for a verified platform skill if Tauri is not the fit |
| Python service / automation | `$fastapi-python`, `$async-python-patterns`, `$python-type-safety`, `$python-error-handling`, `$python-resource-management`, `$python-code-style`, `$python-performance-optimization` |
| Go | `$golang-patterns`, `$golang-pro`, `$go-concurrency-patterns`, `$golang-testing` |
| Cloudflare | `$cloudflare`, `$cloudflare:wrangler`, `$cloudflare:workers-best-practices`, plus Agents SDK/Durable Objects/MCP skills only when used |
| Supabase / PostgreSQL | `$supabase`, `$supabase:supabase-postgres-best-practices`, `$postgresql-table-design`, `$postgresql-optimization`, `$postgresql-code-review` |
| SQL generally | `$sql-code-review`, `$sql-optimization`, `$sql-optimization-patterns` |
| iPhone / iPad / Apple | `$mobile-ios-design`, `$swiftui-expert-skill`, `$swiftui-patterns`, `$swiftui-performance`, `$swiftui-animation`, `$ios-localization`, `$ios-networking`, `$ios-security` |
| macOS native | `$macos-development` for planning, architecture, SwiftData, AppKit/SwiftUI bridging, capabilities, HIG, and macOS-specific UI; add `$mobile-ios-design`, SwiftUI routes, and `$app-store-review` only when relevant |
| Android | `$mobile-android-design`, `$android-clean-architecture`; add Expo routes only for Expo/React Native |
| Windows native WinUI 3 | `$winui-dev-workflow`, `$winui-design`, `$winui-code-review`, `$winui-ui-testing`, `$winui-packaging` |
| Windows native WPF / WinForms / Win32 / MFC | Choose the implementation toolkit with `$find-skills`; use `$windows-desktop-e2e` for UIA tests. No generic unverified Windows builder is assumed |
| Qt desktop (Windows / Linux / macOS) | `$qt-cmake-project` for Qt 6/CMake structure and `$qt-ui-design` for Qt/QML layout, input, accessibility, DPI, and design review; add `$windows-desktop-e2e` for native Windows UIA tests |
| Windows / Linux cross-platform desktop | Prefer `$tauri-v2` for a Rust/web desktop product; add the target platform's E2E and packaging route |
| Linux native desktop | Use `$qt-cmake-project` and `$qt-ui-design` for a Qt 6 target. No trusted GTK skill was added in the current audit; run `$find-skills` again for a concrete GTK/distribution target |
| Desktop release / packaging | Use `$winui-packaging` for WinUI/MSIX; use the selected Qt/Tauri/distribution packaging guidance for other targets; do not mark release done until install, launch, signing, update, and rollback evidence exists |
| Optimization / cleanup | `ponytail:ponytail`, `$optimize`, `$rust-compile-optimization`, `$ponytail:ponytail-audit` for a read-only repo-wide complexity report |

Do not load all rows. Cap the active specialist set to the smallest group that covers the request. Avoid two skills that own the same decision unless one is explicitly a review pass. Resolve conflicts in this order: user contract → existing repository contract → security/correctness/accessibility → mandatory platform/runtime rules → performance → selected design direction → optional style preferences. Ponytail applies throughout by selecting the simplest solution that remains compliant.

## 5. Organize and implement the repository

Before adding code:

1. Reuse existing modules, primitives, dependency versions, scripts, and naming patterns.
2. Keep source, tests, docs, assets, migrations, generated output, and local research in clear locations. Update `.gitignore` only for known generated/local files.
3. Build a complete vertical slice in dependency order: domain/data contract, core logic, boundary/API, UI or CLI, persistence/integration, then delivery wiring.
4. Keep modules small and responsibility-based. Avoid speculative abstractions, compatibility layers, wrappers, plugin systems, and configuration for one value.
5. Never add a stub, fake provider, placeholder implementation, silent fallback, or half-integrated feature unless the user explicitly asks for one and the limitation is recorded.
6. Update `TRACEABILITY.md` as each `REQ-*` moves from planned to implemented to verified. Update `ROADMAP.md` and `STATUS.md` after each meaningful slice.

When the user asks for a web visual surface, create `design-references/<slug>/` before UI code and route `$design-everything`. For native visual surfaces, create the same folder but route the native platform skill as implementation authority; use `$design-everything` only for compatible direction. When the user asks for a technical-only change, do not generate decorative design assets; still maintain the project map.

## 6. Build, optimize, and clean safely

- Detect the package manager and use its existing lockfile. Do not upgrade versions “because they are latest” without a requirement, compatibility check, and verification.
- Detect the toolchain from repository files. Prefer the project’s pinned versions and existing build profiles.
- Start with the smallest relevant check, then run the full requested gate. Keep a command/result record in `STATUS.md`.
- For Rust, use `$rust-compile-optimization` before changing profiles, caches, or global Cargo configuration. Use disk-conscious, command-scoped changes and preview cleanup before any removal.
- For Node/Python/Go, reuse installed tooling and existing task runners before adding a new build layer.
- For desktop delivery, treat packaging as implementation work, not a final note. Resolve the target's installer/package format, signing identity, update path, install/launch smoke test, and rollback or recovery path. Use a verified specialist or official platform documentation for the exact target. A successful compile is not a shippable desktop release.
- Remove only clearly generated or dead artifacts after read-only inspection. Never delete databases, user assets, credentials, sessions, research output, ignored runtime state, or unrelated dirty work.
- Run `ponytail:ponytail-audit` only as a read-only complexity report; apply its findings only when inside scope and after verifying the replacement.

The shortest build is not the least verified build. Keep input validation, error handling, authorization, accessibility, data integrity, and security checks even in Ponytail mode.

## 7. Verify and close every requirement

For each `REQ-*`, verify the actual outcome, not only compilation:

- unit/integration/e2e checks at the relevant risk boundary;
- typecheck, lint, build, migration/schema checks, and packaging as applicable;
- real browser/device/platform smoke tests for user-facing work;
- failure, empty, permission, retry, offline, long-input, localization, and boundary states;
- performance/resource evidence when optimization is part of the request;
- clean repository status and expected generated artifacts.

Mark `done` only when implementation, verification, documentation, and traceability are complete. If a real external blocker remains, mark `blocked`, finish all independent work, and write one concrete blocker plus the smallest next action. Do not hide missing work in prose.

## 8. Handoff and compaction survival

End each substantial turn with:

1. `STATUS.md`: current phase, completed items, active item, blocker, next action, last verification.
2. `ROADMAP.md`: short ordered items, with completed items checked and deferred work explicit.
3. `TRACEABILITY.md`: updated requirement rows and evidence paths/commands.
4. `DECISIONS.md`: only decisions that future agents must not re-litigate.

Use simple language and stable names. Include exact paths, commands, versions, branch/commit when known, and dates when state may drift. On a new thread, rebuild context from these files before touching code.

## Reference chapters

- [project-lifecycle.md](references/project-lifecycle.md): grilling, scope, questions, and complete-delivery loop.
- [architecture-and-repo.md](references/architecture-and-repo.md): persistent project map, repository layout, and traceability schema.
- [platform-chapters.md](references/platform-chapters.md): platform-specific routes and implementation boundaries.
- [routing-and-discovery.md](references/routing-and-discovery.md): local skill selection, external verification, and conflict rules.
- [build-and-quality.md](references/build-and-quality.md): compilation, cleanup, security, tests, and done gates.
- [language-and-handoff.md](references/language-and-handoff.md): simplified technical language and context-survival rules.
