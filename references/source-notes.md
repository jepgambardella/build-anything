# Source notes

The mother skill is based first on the installed local skills and the user's project conventions. These external sources were checked for discovery and writing principles.

- [skills.sh leaderboard](https://skills.sh/): ecosystem discovery and install counts.
- [ASD-STE100 official site](https://www.asd-ste100.org/): controlled technical language, writing rules, dictionary, and Issue 9 reference.
- [ASD-STE100 official overview](https://www.asd-ste100.org/about_STE.html): purpose, clarity, stable terminology, and technical documentation scope.
- Local `ponytail:ponytail` instructions are authoritative for simplicity, reuse, standard-library/native-first decisions, and safe boundaries.
- [Vercel Agent Skills](https://github.com/vercel-labs/agent-skills): source family for established React/Next skill patterns; route only when the local equivalent is absent or the project uses it.
- [Apollo Rust best practices](https://github.com/apollographql/skills): external Rust candidate inspected through skills.sh; local `$rust-best-practices` remains the default.
- [Tauri development candidate](https://skills.sh/mindrally/skills/tauri-development): optional external candidate inspected through `find-skills`; do not install without approval.
- [Apple platform skills](https://github.com/rshankras/claude-code-apple-skills): source for the installed `skills/macos` skill, exposed locally as `macos-development`; used for native macOS planning, architecture, AppKit/SwiftUI, capabilities, and UI review.
- [Windows desktop E2E skill](https://github.com/affaan-m/ECC/blob/main/skills/windows-desktop-e2e/SKILL.md): source for the installed `windows-desktop-e2e` skill; used only for native Windows UI Automation testing and testability.
- [Official Qt agent skills](https://github.com/TheQtCompanyRnD/agent-skills): source for the installed `qt-cmake-project` and `qt-ui-design` skills; used for Qt 6/CMake structure and Qt/QML UI quality on Windows, Linux, and macOS. The local copy keeps the body intact and moves source-only frontmatter fields into `metadata` for the Codex validator.
- Local normalization record: on 2026-08-14, source-only frontmatter fields in the macOS modules and Qt skills were moved under `metadata`; instruction bodies were not changed. All selected parent/module entrypoints pass the local validator.
- [Microsoft WinUI agent skills](https://github.com/microsoft/win-dev-skills/tree/v0.5.0/plugins/winui/skills): source for the installed WinUI workflow, design, code review, UI testing, and packaging skills. Pinned to tag `v0.5.0` / commit `455468c5c58f5c9fdc9c410dd32b3869d29a1bd9` on 2026-08-14. The repository labels v0.x as preview, so Build Anything must keep the pin and verify Windows tools before use.
- [GTK app candidate](https://www.skills.sh/mhagrelius/dotfiles/developing-gtk-apps): rejected during the audit because the source had too little adoption and repository evidence for a default production route.
- [Alternative Tauri candidate](https://www.skills.sh/nodnarbnitram/claude-code-extensions/tauri-v2): rejected because it duplicated the installed local `$tauri-v2` route without enough additional value.

These links are references, not permission to add dependencies, update versions, or impose a framework. Validate current source state before installing or using an external skill.
