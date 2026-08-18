# Bundled skill catalog

Build Anything is self-contained for its baseline workflow. The folders in
`../bundled-skills/` are the copies that the controller must read and use.
They are not decorative references and they are not a request for the user to
install more skills.

The current package contains the complete bundled set, including the
orchestration core, design system, frontend quality, language, backend,
database, cloud, Apple, Android, Windows, Qt, Tauri, testing, and release
routes. Each bundled `SKILL.md` passes the local skill validator.

## Mandatory execution core

| Folder | Role | Required evidence |
| --- | --- | --- |
| `grill-me` | Explicit `/grilling` interview | `docs/project/GRILL.md` transcript or visible fallback |
| `unlazy` | Gates, evidence, Depth Tree, report audit | `GATES.md` checked by the bundled `gate-check.mjs` |
| `ponytail` | Full-intensity simplicity and anti-overengineering | `ACTIVE-SKILLS.md` plus simplification decisions |
| `find-skills` | Discovery when a route is missing | search and source verification record |
| `skill-installer` | Install a verified missing route | source/ref/SHA/date/path/validator record |
| `skill-creator` | Create or update a skill when requested | validated skill directory and evidence |

## Mandatory visual spine

Load these for a visual web or frontend task, in this order:

1. `design-everything` — design director and route coordinator;
2. `teach-impeccable` — only when project design context is missing or stale;
3. `frontend-design` — intentional visual direction;
4. `css-for-perfect-frontend` — responsive CSS and layout correctness;
5. `adapt` — narrow-to-wide adaptation and responsive fixes;
6. `ui-component-patterns` — component contracts and reuse;
7. one style baseline, not several competing authorities;
8. `audit`, `harden`, `polish`, and `web-design-guidelines` — review and repair.

The style baselines shipped here are `minimalist-ui`,
`industrial-brutalist-ui`, `high-end-visual-design`, `design-taste-frontend`,
and `stitch-design-taste`. Choose one. The modifiers are `distill`, `quieter`,
`bolder`, `colorize`, `overdrive`, `animate`, and `delight`.

Use `image-taste-frontend` and `imagegen` only when imagery is part of the
approved direction. Keep selected assets and rejected alternatives in
`design-references/<slug>/`.

## Platform routes

Platform skills are bundled when present in this package. The controller must
load only the row that matches the project:

| Area | Bundled route |
| --- | --- |
| React / Next / Vite | `vercel-react-best-practices`, `vercel-composition-patterns`, `react-doctor`, `vite`, `vite-patterns`, `typescript-advanced-types` |
| Rust | `rust-best-practices`, `rust-async-patterns`, `rust-compile-optimization`, `unsafe-checker` |
| Python | `python-code-style`, `python-type-safety`, `python-error-handling`, `python-resource-management`, `fastapi-python`, `async-python-patterns`, `python-performance-optimization`, `python-design-patterns` |
| Cloudflare | `cloudflare`, `wrangler`, `workers-best-practices`, `agents-sdk`, `durable-objects`, `building-mcp-server-on-cloudflare`, `web-perf` |
| Supabase / PostgreSQL | `supabase`, `supabase-postgres-best-practices`, `postgresql-table-design`, `postgresql-code-review`, `postgresql-optimization` |
| Apple | `macos-development`, `appkit-swiftui-bridge`, `macos-capabilities`, `swiftdata-architecture`, `mobile-ios-design`, `swiftui-expert-skill`, `swiftui-patterns`, `swiftui-performance`, `swiftui-animation`, `ios-localization`, `ios-networking`, `ios-security` |
| Android | `mobile-android-design`, `android-clean-architecture` |
| Windows WinUI | `winui-dev-workflow`, `winui-design`, `winui-code-review`, `winui-ui-testing`, `winui-packaging` |
| Qt desktop | `qt-cmake-project`, `qt-ui-design`, `windows-desktop-e2e` when Windows UIA applies |
| Rust/web desktop | `tauri-v2` plus the selected web and target-platform routes |

Cross-cutting routes also shipped in the bundle include `playwright`,
`agent-browser`, `tdd`, `vitest`, `shadcn-ui`, `react-components`,
`requesting-code-review`, and the platform-specific packaging and debug
modules. Load them only when their evidence is relevant.

If a listed route is absent from the package, treat that as a packaging bug:
use the bundled discovery and installer routes, fix the bundle, validate it,
and record the source. Do not tell the end user to install a baseline route.
