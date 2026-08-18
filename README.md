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

- `grill-me` — mandatory `/grilling` interview before implementation.
- `unlazy` — gates, runnable checks, evidence, Depth Tree, and report audit.
- `ponytail` — simplest solution that actually works, without removing correctness or safety.
- `find-skills`, `skill-installer`, and `skill-creator` — verified discovery, installation, and skill maintenance.

Included design spine:

- `design-everything`, `frontend-design`, `css-for-perfect-frontend`, `adapt`, and `ui-component-patterns`.
- `teach-impeccable`, `image-taste-frontend`, `imagegen`, `ui-ux-pro-max`, and the bundled style baselines: `minimalist-ui`, `industrial-brutalist-ui`, `high-end-visual-design`, `design-taste-frontend`, and `stitch-design-taste`.
- `audit`, `critique`, `harden`, `polish`, `web-design-guidelines`, `arrange`, `typeset`, `normalize`, `extract`, `user-oriented-frontend-and-design`, `clarify`, and `onboard`.

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
