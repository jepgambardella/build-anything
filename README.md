<div align="center">

# Build Anything

### Turn the idea into a finished, verified product.

**Build things. That's it.**

</div>

Build Anything is a project-lead skill for AI coding agents. It takes an unclear idea, asks the questions that matter, maps the architecture, selects the right specialist skills, organizes the repository, builds the requested scope, verifies it, and leaves a trace that survives the next thread.

It covers web apps, frontend, backend, Rust, Python, Cloudflare, Supabase, APIs, automations, macOS, iPhone, Android, Windows, Linux, Qt, WinUI, Tauri, packaging, and optimization. It routes specialist skills only when the project needs them.

## Self-contained by design

Build Anything ships the specialist skills it must use. The user does not need to install them separately. The controller reads the copies in `bundled-skills/`, records which ones were loaded, and leaves evidence of how each one was applied.

Included orchestration:

- [`grill-me`](bundled-skills/grill-me/SKILL.md) — mandatory `/grilling` interview before implementation.
- [`unlazy`](bundled-skills/unlazy/SKILL.md) — gates, runnable checks, evidence, Depth Tree, and report audit.
- [`ponytail`](bundled-skills/ponytail/SKILL.md) — simplest solution that actually works, without removing correctness or safety.
- [`find-skills`](bundled-skills/find-skills/SKILL.md), [`skill-installer`](bundled-skills/skill-installer/SKILL.md), and [`skill-creator`](bundled-skills/skill-creator/SKILL.md) — verified discovery, installation, and skill maintenance.

Included design spine:

- [`design-everything`](bundled-skills/design-everything/SKILL.md), [`frontend-design`](bundled-skills/frontend-design/SKILL.md), [`css-for-perfect-frontend`](bundled-skills/css-for-perfect-frontend/SKILL.md), [`adapt`](bundled-skills/adapt/SKILL.md), and [`ui-component-patterns`](bundled-skills/ui-component-patterns/SKILL.md).
- [`teach-impeccable`](bundled-skills/teach-impeccable/SKILL.md), [`image-taste-frontend`](bundled-skills/image-taste-frontend/SKILL.md), [`imagegen`](bundled-skills/imagegen/SKILL.md), [`ui-ux-pro-max`](bundled-skills/ui-ux-pro-max/SKILL.md), and the bundled style baselines: [`minimalist-ui`](bundled-skills/minimalist-ui/SKILL.md), [`industrial-brutalist-ui`](bundled-skills/industrial-brutalist-ui/SKILL.md), [`high-end-visual-design`](bundled-skills/high-end-visual-design/SKILL.md), [`design-taste-frontend`](bundled-skills/design-taste-frontend/SKILL.md), and [`stitch-design-taste`](bundled-skills/stitch-design-taste/SKILL.md).
- [`audit`](bundled-skills/audit/SKILL.md), [`critique`](bundled-skills/critique/SKILL.md), [`harden`](bundled-skills/harden/SKILL.md), [`polish`](bundled-skills/polish/SKILL.md), [`web-design-guidelines`](bundled-skills/web-design-guidelines/SKILL.md), [`arrange`](bundled-skills/arrange/SKILL.md), [`typeset`](bundled-skills/typeset/SKILL.md), [`normalize`](bundled-skills/normalize/SKILL.md), [`extract`](bundled-skills/extract/SKILL.md), [`user-oriented-frontend-and-design`](bundled-skills/user-oriented-frontend-and-design/SKILL.md), [`clarify`](bundled-skills/clarify/SKILL.md), and [`onboard`](bundled-skills/onboard/SKILL.md).

Included implementation routes cover React/Next/Vite, Rust, Python, Cloudflare, Supabase/PostgreSQL, SwiftUI/macOS/iOS, Android, WinUI, Qt, Tauri, browser testing, packaging, and desktop UI automation. See the complete [bundled skill catalog](references/bundled-skill-catalog.md).

## The rule

**Done means done.**

No slop. No vague hand-waving. No long language that hides missing work. No lazy stubs, fake data, silent fallbacks, or half-integrated features unless the user explicitly asks for them.

Use simple technical language. Keep the code small. Apply Ponytail: choose the simplest solution that actually works, then verify it.

### Anti-slop

Replace generic output with a clear decision, a real implementation, or a specific blocker.

### Anti-verbosity

Use the fewest words that make the decision, next action, and evidence unambiguous.

### Anti-laziness

Finish the requested scope. Do not hide missing work behind a plan, a stub, or a report.

## What it does

1. Grills the idea into a clear project contract.
2. Creates a persistent map for requirements, architecture, roadmap, status, decisions, and traceability.
3. Selects the smallest useful set of local specialist skills.
4. Builds the complete vertical slice in a clean repository.
5. Tests the real result, records evidence, and closes every requirement.

## Install

```bash
npx skills add jepgambardella/build-anything
```

Or install only the named skill:

```bash
npx skills add jepgambardella/build-anything --skill build-anything
```

## Use

Ask your agent to use `$build-anything` and describe what you want to build.

The skill starts with `$grill-me`, creates the project map before code, routes `$design-everything` for web visual work, uses native platform skills where required, and keeps `STATUS.md`, `ROADMAP.md`, `TRACEABILITY.md`, and `DECISIONS.md` current.

## License

MIT. See [LICENSE](LICENSE).

## Acknowledgements

Build Anything is an orchestration layer. It does not claim authorship of the specialist guidance bundled in this repository. We are grateful to the original authors and maintainers whose work makes this package useful:

- [AllThingsSmitty/css-protips](https://github.com/AllThingsSmitty/css-protips) for practical CSS techniques and responsive details.
- [Leonxlnx/unlazy](https://github.com/Leonxlnx/unlazy) for gate-first execution, evidence discipline, Depth Tree planning, and adversarial completion checks.
- [Vercel Agent Skills](https://github.com/vercel-labs/agent-skills) for strong React and Next.js engineering guidance.
- [The Qt Company R&D agent skills](https://github.com/TheQtCompanyRnD/agent-skills) for Qt and cross-platform desktop development guidance.
- [Microsoft WinUI agent skills](https://github.com/microsoft/win-dev-skills) for Windows app development, UI testing, and packaging guidance.
- [Apple platform skills](https://github.com/rshankras/claude-code-apple-skills) for macOS and Apple-platform development guidance.
- Every local skill author and maintainer whose design, frontend, platform, testing, quality, and workflow work is included in the bundle.

The complete provenance record is available in [references/source-notes.md](references/source-notes.md). Please follow each original project's license and attribution requirements when reusing its material.
