# Platform chapters

Select one primary chapter and add only cross-cutting skills that the project actually uses.

## Web application

Use `$design-everything` for visual/UI work, `$css-for-perfect-frontend` and `$adapt` for responsive behavior, and `$ui-component-patterns` for reusable components. Detect React/Next/Vite and then add only the matching performance, composition, type, and testing skills. Verify a real browser path when the work changes interaction or layout.

Check: routing, loading/error/empty states, keyboard/focus, touch, narrow widths, long data, localization, auth boundaries, caching, build, and deployment.

## Backend/API/service

Define API or event contracts before handlers. Select the language skill, database skill, auth/security guidance, and testing path. Verify validation at trust boundaries, authorization, idempotency, retries, timeouts, structured errors, migrations, observability, and a real smoke path.

Do not hide a missing integration behind a fake provider or a silent fallback. If a provider is unavailable, finish independent work and name the concrete blocker.

## Rust

Use `$rust-best-practices` for idioms, ownership, errors, clippy, API design, and tests. Add `$rust-async-patterns` for async/concurrency, `$unsafe-checker` for unsafe/FFI, and `$rust-compile-optimization` for build/cache/disk work. Prefer the smallest correct type and module structure. Measure before optimizing hot paths. Run focused checks before a broader cargo gate.

## Python

Use `$python-code-style`, `$python-type-safety`, `$python-error-handling`, and `$python-resource-management` as the base. Add `$async-python-patterns`, `$fastapi-python`, `$python-performance-optimization`, or `$python-design-patterns` only when the code uses those concerns. Keep environments and lockfiles consistent with the repository.

## Cloudflare

Use `$cloudflare`/`$cloudflare:wrangler` for provider configuration. Add Workers, Agents SDK, Durable Objects, MCP, or web-performance guidance only for the selected product. Verify bindings, environment separation, migrations, secrets, compatibility dates, local smoke, and the actual deployed/provider state when deployment is in scope.

## Supabase and PostgreSQL

Use `$supabase` for Supabase-specific workflows and `$supabase:supabase-postgres-best-practices` for database performance. Add `$postgresql-table-design`, `$postgresql-code-review`, or `$postgresql-optimization` for schema/query review. Keep migrations, RLS/auth boundaries, indexes, backups, and runtime schema evidence aligned.

## macOS, iPhone, and iPad

For native macOS work, start with `$macos-development` and load only its relevant module: `app-planner` is an optional platform checklist or explicit audit and must write into Build Anything's canonical map, not create a second project-document set; use `architecture-patterns` or `coding-best-practices` for structure, `swiftdata-architecture` for persistence, `appkit-swiftui-bridge` for hybrid UI, `macos-capabilities` for sandboxing/extensions/background work, and `ui-review-tahoe` for HIG/accessibility/UI review. Add `$mobile-ios-design` and the relevant SwiftUI/networking/localization/security skills only when the project also targets Apple mobile platforms. Use system controls and platform conventions before custom UI. Add `$app-store-review` before release-oriented work. Do not transfer web CSS assumptions to native layout, navigation, lifecycle, or input behavior.

## Android

Use `$mobile-android-design` and `$android-clean-architecture`; add Expo/Tailwind only for an Expo/React Native project. Verify Android back behavior, lifecycle, permissions, density, accessibility, offline/error states, and release configuration.

## Windows and Linux desktop

Use `$tauri-v2` for a Rust + web desktop product when it matches the constraints. Check native window behavior, filesystem permissions, update/signing/package requirements, offline operation, and platform-specific paths.

For native Windows applications, use the implementation guidance for the chosen toolkit and add `$windows-desktop-e2e` for WPF, WinForms, Win32/MFC, or Qt UI Automation tests. Give interactive controls stable Automation IDs, prefer condition-based waits over sleeps, isolate per-test user data, capture failure artifacts, and run the real suite on `windows-latest` or equivalent Windows hardware. Do not use this skill for web, Electron, WebView2, mobile, or unit-only tests.

For WinUI 3, use `$winui-dev-workflow` to scaffold/build/run, `$winui-design` before new XAML, `$winui-code-review` after a successful build, `$winui-ui-testing` for scripted UIA assertions and screenshots, and `$winui-packaging` for MSIX/signing/distribution. The Microsoft source is preview v0.x, so keep the installed tag pinned and verify the exact tool version. Its `winui-setup` path is user-invoked only; do not silently install or change Windows machine prerequisites.

For Qt 6 desktop work on Windows, Linux, or macOS, use `$qt-cmake-project` for CMake and target structure and `$qt-ui-design` for the visual and interaction contract. Load its `references/` files progressively: use `simple-project.md` for one target, `modular-architecture.md` for multiple targets, `qml-integration.md` for QML modules, `resources.md` for assets, `configure.md` for build configuration, and `common-mistakes.md` before final CMake output. Resolve packaging, signing, update, and install/launch verification separately for the chosen OS; the Qt skills do not by themselves prove a production installer.

For Linux, distinguish cross-platform packaging from native toolkit development. Tauri is the installed cross-platform route. Qt 6 now has a verified native route through `$qt-cmake-project` and `$qt-ui-design`. No trusted native GTK skill was added during the current audit; run `$find-skills` with the exact toolkit/distribution before choosing one. Verify window managers, filesystem conventions, accessibility, package format, signing/update model, and real hardware before marking Linux delivery complete.

## CLI, automation, and data tooling

Define command contracts, exit codes, config precedence, logs, dry-run behavior, idempotency, and safe handling of secrets. Prefer standard library/native tools. Test representative failure paths, not only the happy path.

## Cross-cutting release

Use `$tdd`, `$vitest`, `$playwright`, `$agent-browser`, `$requesting-code-review`, `$audit`, `$harden`, or `$web-design-guidelines` only when their evidence is relevant. Use `$optimize` after correctness and measurement exist. Use `$ponytail:ponytail-audit` as a read-only complexity report, not as permission for an unrequested rewrite.
