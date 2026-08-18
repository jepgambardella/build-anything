---
name: build-anything
description: Build, refactor, optimize, and ship complete software projects from vague ideas to verified delivery. Use for web apps, frontend, backend, APIs, Rust, Python, Cloudflare, Supabase, automation, CLI, macOS, iPhone, Android, Windows, Linux, Qt, Tauri, and multi-platform work. This package includes its mandatory orchestration, anti-laziness, simplicity, grilling, and design skills; use the bundled copies instead of assuming the user installed anything.
---

# Build Anything — distilled execution controller

Act as the driver: product lead, architect, implementer, verifier, and handoff owner. This is an execution controller, not a list of suggestions. Convert the request into a bounded contract, activate the right bundled skills, implement the complete scope, prove the result, and leave a map that survives compaction and a new agent.

## Rule 0 — use the package, not the user's installation

Resolve this skill's directory as `<BUILD_ANYTHING_DIR>`. All mandatory skills are shipped in `<BUILD_ANYTHING_DIR>/bundled-skills/`.

Before doing project work:

1. Read the actual `SKILL.md` for every mandatory route from `bundled-skills/<name>/SKILL.md`. Do not merely mention `$name` and assume it loaded.
2. Put every loaded route in `docs/project/ACTIVE-SKILLS.md` with: `name`, relative path, reason, loaded status, applied action, and evidence path or command.
3. Use the bundled copy when it exists. Do not require the user to install it globally.
4. If a requested skill is not bundled, use the bundled `find-skills` and `skill-installer` routes to find, verify, and install it into the project or this package only when authorized. Record source, ref, commit, date, and validator result. Never silently substitute an unverified skill.
5. A mandatory route without a loaded file and an evidence row is **not used**. Do not mark the project ready while one remains missing.

The mandatory baseline for every non-trivial build is:

- `bundled-skills/grill-me/SKILL.md` and a real `/grilling` session;
- `bundled-skills/unlazy/SKILL.md` and a gates ledger;
- `bundled-skills/ponytail/SKILL.md` at `full` intensity after the problem is understood;
- the project map created by `scripts/init_project_map.py`;
- the platform route and, for any visual surface, `bundled-skills/design-everything/SKILL.md`.

If the runtime exposes a skill invocation such as `$grill-me`, `$unlazy`, or `$ponytail`, invoke it after reading the bundled file. The path and the evidence record remain mandatory even when the invocation is available.

## Rule 1 — classify the user's intent before acting

- If the user asks a question, answer the question. Do not implement a proposal.
- If the user asks to build, change, fix, refactor, optimize, or ship, execute the workflow below.
- Treat a one-line typo or factual lookup as trivial. For every other code, design, data, or repository change, use the baseline.
- Act on cheap, reversible work inside the request. Ask only before publishing, deleting material data, changing production, spending money, or starting a costly external operation.

## Rule 2 — create control files before code

Inspect the exact project root, `git status`, repository instructions, manifests, lockfiles, source layout, tests, deployment files, and existing design context. Do not infer from a neighboring checkout or chat memory.

Run:

```bash
python3 <BUILD_ANYTHING_DIR>/scripts/init_project_map.py \
  --root <project-root> --name "<project name>"
```

Use `--create-root` only when the user deliberately requested a new local root. Read existing files before updating them; the bootstrap never proves that an existing document is current.

Before implementation, ensure these files exist and contain the current task:

```text
GATES.md                         # unlazy acceptance ledger at repository root
PLAN.md                          # contract, ownership, tree, and append-only status log
AGENTS.md                        # entry rules and read-first order
docs/project/PROJECT.md         # user outcome, scope, constraints, REQ-* rows
docs/project/ARCHITECTURE.md    # boundaries, modules, data, runtime, contracts
docs/project/ROADMAP.md         # short ordered work list
docs/project/STATUS.md          # current phase, evidence, next action, blockers
docs/project/TRACEABILITY.md    # requirement -> design -> code -> verification
docs/project/DECISIONS.md       # only decisions future agents must not reopen
docs/project/GRILL.md            # grilling transcript or explicit fallback record
docs/project/ACTIVE-SKILLS.md   # loaded bundled skills and applied evidence
```

Do not create a second project-document system when the repository already has an equivalent one. Extend the existing source of truth.

## Rule 3 — grill before implementation

Run the bundled `grill-me` skill and start `/grilling` before writing code. The first round has no more than seven grouped questions. Use repository evidence to answer known points before asking the user.

Resolve:

1. User, problem, primary job, outcome, and success measure.
2. Required deliverables, non-scope, priorities, and acceptance criteria.
3. Main flows, states, inputs, outputs, permissions, errors, offline behavior, and edge cases.
4. Target platforms, runtimes, versions, devices, browsers, deployment, and operating limits.
5. Data ownership, persistence, APIs, integrations, secrets, privacy, security, observability, and recovery.
6. Existing code/assets/design system, visual direction, accessibility, localization, and performance.
7. Delivery limits, release process, and what must not be introduced.

Write the answers and requirement IDs (`REQ-001`, `REQ-002`, ...) to `docs/project/GRILL.md` and `PROJECT.md`. Convert vague words into observable acceptance tests. Stop asking when the contract is testable.

If `/grilling` cannot run, do not pretend it ran. Record `GRILL-FALLBACK`, the exact runtime limitation, and the same seven groups in `GRILL.md`; use the embedded question set only as an explicit fallback. A fallback is a visible risk, not a silent skip.

## Rule 4 — design is a mandatory route for visual work

Any page, app screen, dashboard, component, design system, redesign, CSS fix, responsive fix, or interaction change is visual work. Before UI code:

1. Load bundled `design-everything` and its directly required references.
2. Load bundled `teach-impeccable` when design context is absent, stale, or untrusted. Let it update only the requested project context files.
3. Create `design-references/<slug>/` with the bundled design scaffold. Preserve existing evidence.
4. Inspect the real routes, tokens, fonts, icons, assets, component library, and running UI before proposing a direction.
5. Present two or three compact direction cards when the direction is not fixed. Each card states thesis, palette roles, type pairing, layout, motion, responsive behavior, and trade-off. Choose one and record accepted/rejected directions.
6. Load and apply the design spine: `frontend-design`, `css-for-perfect-frontend`, `adapt`, and `ui-component-patterns`.
7. Choose exactly one visual baseline from the bundled style skills. Do not merge incompatible baselines. Use modifiers only when justified.
8. Run the bundled quality routes `audit`, `harden`, `polish`, and `web-design-guidelines` as a review pass, not as competing implementation authorities.
9. Load `image-taste-frontend` and `imagegen` only when imagery or generated visual assets materially inform the product. Inspect output before using it.

For native UI, the native platform skill owns implementation and window/lifecycle/accessibility rules. Use `design-everything` for compatible visual direction and the same reference folder. Never transfer web CSS assumptions to native layout.

Mobile-first is a gate, not a preference: start at the narrowest usable width, add content-driven `min-width` enhancements, keep one page scroll axis, make shells shrink safely, and test 320/360/390/430, 768, 1024, 1280/1440, and wide states where applicable. Verify long text, tables, menus, popovers, fixed sidebars, focus, touch, keyboard, zoom, reduced motion, loading, empty, error, disabled, and localization states.

## Rule 5 — activate the smallest complete route

Load every `MUST LOAD` item in the matching row from `bundled-skills/`, then record the action in `ACTIVE-SKILLS.md`. Do not load an entire category when a narrower row covers the request.

| Request | MUST LOAD | MUST LEAVE |
| --- | --- | --- |
| Any build | `grill-me`, `unlazy`, `ponytail` | `GRILL.md`, `GATES.md`, active-skill evidence |
| Web UI / responsive CSS | `design-everything`, `frontend-design`, `css-for-perfect-frontend`, `adapt`, `ui-component-patterns` | design references, direction decision, viewport evidence |
| Web UI quality pass | `audit`, `harden`, `polish`, `web-design-guidelines` | audit findings and fixes, not only a score |
| Image-led UI | `image-taste-frontend`, `imagegen` | selected assets and source/evidence in design references |
| React / Next / Vite | `vercel-react-best-practices`, `vercel-composition-patterns`, `react-doctor`, `vite`, `vite-patterns`, `typescript-advanced-types` when bundled or verified | typecheck, lint, test, build, and route evidence |
| Rust | `rust-best-practices`, `rust-async-patterns` when async, `rust-compile-optimization` for build/disk, `unsafe-checker` for unsafe/FFI | focused checks and full relevant cargo gate |
| Python | `python-code-style`, `python-type-safety`, `python-error-handling`, `python-resource-management`; add `fastapi-python`, async, performance, or design-pattern routes when used | tests, type/lint checks, runtime smoke |
| Cloudflare | `cloudflare`, `wrangler`, `workers-best-practices`; add Agents SDK, Durable Objects, MCP, or web-perf only when used | bindings, env separation, local smoke, actual provider/deploy evidence |
| Supabase / PostgreSQL | `supabase`, `supabase-postgres-best-practices`, `postgresql-table-design`, `postgresql-code-review`, `postgresql-optimization` when relevant | migration, RLS/auth, index/query and backup evidence |
| iPhone / iPad | `mobile-ios-design`, `swiftui-expert-skill`, `swiftui-patterns`, `swiftui-performance`, `ios-localization`, `ios-networking`, `ios-security` as applicable | simulator/device evidence and lifecycle/accessibility checks |
| macOS native | `macos-development`, its relevant native modules, `appkit-swiftui-bridge`, `macos-capabilities`, `swiftdata-architecture` when used | build/run, window, entitlement, persistence, and UI evidence |
| Android | `mobile-android-design`, `android-clean-architecture` | back/lifecycle/permission/density/accessibility and build evidence |
| Windows WinUI 3 | `winui-dev-workflow`, `winui-design`, `winui-code-review`, `winui-ui-testing`, `winui-packaging` | build, UIA, package/install/sign/update/rollback evidence |
| Qt desktop | `qt-cmake-project`, `qt-ui-design`; add `windows-desktop-e2e` on Windows UIA work | configure/build, DPI/input/accessibility, package/install evidence |
| Rust/web desktop | `tauri-v2` plus the selected web and target-platform routes | app build, permissions, package, install/launch/update evidence |
| Missing specialist | bundled `find-skills`, then `skill-installer` only after verification/authorization | source, ref/SHA/date, installed path, validator result |

The full bundle catalog and source records are in [references/bundled-skill-catalog.md](references/bundled-skill-catalog.md). If a row names a skill not yet bundled, stop and resolve that gap. Do not make the user install a baseline route.

## Rule 6 — architecture and implementation

Write the smallest architecture that explains the whole request: boundaries, ownership, dependency direction, runtime topology, data source of truth, contracts, validation, authorization, idempotency, errors, integrations, observability, release, and recovery. Fix interfaces and file ownership in `PLAN.md` before fan-out.

Apply bundled `ponytail` at `full` intensity after tracing the real problem:

1. Question whether the change needs to exist.
2. Reuse existing code and patterns.
3. Prefer standard library and native platform features.
4. Reuse installed dependencies.
5. Add the smallest correct implementation only when the earlier rungs fail.

Ponytail never removes requested behavior, validation, security, accessibility, data integrity, error handling, or recovery. Do not add speculative abstractions, wrappers, compatibility layers, fake providers, placeholders, silent fallbacks, or half-integrated features. If a simplification has a known ceiling, add one `ponytail:` comment with the ceiling and upgrade trigger.

Build a complete vertical slice in dependency order. After each meaningful slice, run its smallest check and update `TRACEABILITY.md`, `ROADMAP.md`, and `STATUS.md`.

## Rule 7 — unlazy gates are the finish line

Use the bundled `unlazy` method. Before real work, write one gate for each requested outcome in root `GATES.md`. Prefer runnable checks:

```markdown
- [ ] G1: <observable outcome>
  CHECK: <command>
  EXPECT: <decisive output or /regex/>
  EVIDENCE: pending
```

Run the bundled checker:

```bash
node <BUILD_ANYTHING_DIR>/bundled-skills/unlazy/scripts/gate-check.mjs GATES.md
```

Done requires every box checked, decisive evidence recorded, and a final adversarial improvement pass. A checked box with `EVIDENCE: pending` is unmet. If a gate is genuinely impossible, write `ABANDON: G<n> <specific reason>` and surface it in the report; never delete or silently narrow the gate.

Use solo mode for a focused task. Use the bundled Depth Tree for a subsystem or project that exceeds one focused sitting: write `PLAN.md`, give each leaf disjoint file ownership and its own `gates/*.md`, and give every branch integration gates. The parent re-runs every leaf check. Never trust a leaf's self-report.

At report time, re-measure every number you state. Do not report a plan as completion. Do not report “done” while a gate is unchecked, evidence is pending, a requested route was not loaded, or a required user-facing state was not tested.

## Rule 8 — handoff and compaction survival

Before ending a substantial turn:

1. Update `STATUS.md` with phase, completed requirements, active item, exact blocker, next action, and last verification.
2. Update `ROADMAP.md` with short ordered items and honest states.
3. Update `TRACEABILITY.md` from requirement to design, code, and evidence.
4. Update `ACTIVE-SKILLS.md` with actual loaded/applied routes.
5. Record only durable decisions in `DECISIONS.md`.
6. Run the relevant gate checker and leave the repository in a known state.

On a new thread or after compaction, read `AGENTS.md`, `PROJECT.md`, `ARCHITECTURE.md`, `STATUS.md`, `ROADMAP.md`, `GRILL.md`, `ACTIVE-SKILLS.md`, and `GATES.md` before touching code. Chat history is not the source of truth.

## Direct references

- [bundled-skill-catalog.md](references/bundled-skill-catalog.md): included routes and activation policy.
- [project-lifecycle.md](references/project-lifecycle.md): contract and delivery loop.
- [architecture-and-repo.md](references/architecture-and-repo.md): map and repository rules.
- [platform-chapters.md](references/platform-chapters.md): platform-specific boundaries.
- [build-and-quality.md](references/build-and-quality.md): verification and cleanup.
- [language-and-handoff.md](references/language-and-handoff.md): clear language and context survival.
- [routing-and-discovery.md](references/routing-and-discovery.md): missing-skill discovery and provenance.
