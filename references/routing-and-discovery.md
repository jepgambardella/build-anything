# Routing and skill discovery

Build Anything is an orchestrator. It should route, not create contradictory prompt piles.

## Local-first routing

Prefer the installed local skill that owns the concern:

- project definition: `$grill-me`, then this skill;
- web UI: `$design-everything`; native UI: the selected platform skill owns implementation and `$design-everything` is optional visual direction;
- minimal code and dependency choices: `$ponytail:ponytail`;
- project map: this skill and `init_project_map.py`;
- language/platform/backend/database chapters: see [platform-chapters.md](platform-chapters.md);
- missing capability: `$find-skills`;
- new or updated skill: `$skill-creator`.

Do not invoke two equivalent skills as simultaneous authorities. Use one implementation guide and one review guide when necessary. Keep the active set small enough to remember the decisions.

## Find-skills procedure

When local coverage is missing:

1. Check [skills.sh](https://skills.sh/) leaderboard first.
2. Search with specific terms using `npx skills find <query>`.
3. Prefer official or established sources and meaningful install counts.
4. Inspect the source repository, actual `SKILL.md`, scope, last activity, license, and security warnings. Read the installed file and any directly required references before routing it.
5. Reject a result that is too narrow, stale, duplicated locally, low-trust, or under-specified.
6. Present the candidate, evidence, install command, and trade-off. Install only after explicit user approval. When approval exists, use `$skill-installer`, check that the destination is not already present, install the exact path, validate it, and update this routing record.
7. Record reproducibility data for every installed external skill: source repository, exact path, ref/tag, commit SHA, installation date, local destination, validator result, and any local metadata-only normalization. Counts and stars must include their check date and source; they are not a substitute for a pinned ref.

## Candidates verified during creation

These are optional references, not automatic dependencies:

| Candidate | Evidence | Use |
| --- | --- | --- |
| `mattpocock/skills@improve-codebase-architecture` | High leaderboard visibility on skills.sh | Architecture review when local coverage is insufficient |
| `mindrally/skills@tauri-development` | About 1.1K installs in CLI search | Tauri-specific development if `$tauri-v2` is not enough |
| `apollographql/skills@rust-best-practices` | About 14.7K installs, established Apollo source | Alternative Rust review source; local `$rust-best-practices` already covers the default |
| `rshankras/claude-code-apple-skills@macos` (frontmatter name: `macos-development`) | About 1.3K installs; 600+ repository stars; MIT repository; macOS category with planner, architecture, SwiftData, AppKit, capabilities, and UI review modules | **Installed** at `~/.codex/skills/macos`; route for native macOS planning, implementation, and review. Audit: 2026-08-14, `main` at `9ffb83138209057875698dd11c1720c657c47a92` |
| `affaan-m/ECC@windows-desktop-e2e` | About 4.1K installs; MIT repository; large GitHub adoption; actual file covers WPF, WinForms, Win32/MFC, and Qt through pywinauto/UIA | **Installed** at `~/.codex/skills/windows-desktop-e2e`; route only for Windows native desktop E2E and testability. Audit: 2026-08-14, `main` at `c9de8f5b2b3a225bca9befa2b7700aa5e3a4d1b8` |
| `TheQtCompanyRnD/agent-skills@qt-cmake-project` | Official Qt AI skills repository; about 300 repository stars; exact skill uses Qt 6 CMake APIs and has explicit anti-LLM guardrails | **Installed** at `~/.codex/skills/qt-cmake-project`; route for Qt 6 project/build structure. Audit: 2026-08-14, `main` at `71d6c10da78b9a764468ae11c86ab3bc4ca4921f` |
| `TheQtCompanyRnD/agent-skills@qt-ui-design` | Official Qt AI skills repository; about 500 installs for the skill; covers Qt/QML layout, DPI, input, accessibility, localization, and design audit | **Installed** at `~/.codex/skills/qt-ui-design`; route for Qt UI decisions and review. Audit: 2026-08-14, `main` at `71d6c10da78b9a764468ae11c86ab3bc4ca4921f` |
| `microsoft/win-dev-skills@winui` | Microsoft repository, MIT, 381 stars, end-to-end WinUI 3/Windows App SDK workflow; preview v0.x with explicit pinning support; includes build, design, review, UI automation, and MSIX packaging | **Installed** at `~/.codex/skills/winui-*` from `v0.5.0`. Audit: 2026-08-14, SHA `455468c5c58f5c9fdc9c410dd32b3869d29a1bd9` |
| `glittercowboy/taches-cc-resources@create-plans` | Search result with a narrow planning scope | Optional planning reference; do not add if this skill already covers the need |

Treat install counts as time-sensitive evidence, not quality proof. Verify again before recommending a current install. Do not install low-count or low-trust candidates merely to fill a matrix.

### Candidates rejected in the platform audit

| Candidate | Reason |
| --- | --- |
| `mhagrelius/dotfiles@developing-gtk-apps` | About 110 installs and 2 repository stars. Too little evidence for a default native GTK route. |
| `nodnarbnitram/claude-code-extensions@tauri-v2` | High install count but a small repository and a duplicate of the installed local `$tauri-v2`; no added route justified the duplicate. |
| `openai/skills@winui-app` | Strong curated candidate, but it overlaps the pinned Microsoft WinUI set, which exposes separate build, design, review, testing, and packaging authorities. Avoid loading both. |

For native Linux GTK work, run a new targeted search when the toolkit and distribution are known. Qt is now covered by the pinned official Qt skills. Keep any new GTK candidate conditional until its source and scope pass the same checks.

## Conflict rules

1. User contract and explicit platform constraints.
2. Existing repository conventions and public contracts.
3. Security, correctness, data integrity, accessibility, and legal constraints.
4. The selected platform/framework skill and its mandatory platform constraints.
5. Ponytail simplicity and measured performance inside those constraints.
6. Optional style or workflow preferences.

If a specialist proposes a stub, compatibility layer, fallback, new dependency, or broad refactor, accept it only when the project contract requires it and record the reason.
