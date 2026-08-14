<div align="center">

# Build Anything

### Turn the idea into a finished, verified product.

**Per fare cose, e basta.**

</div>

Build Anything is a project-lead skill for AI coding agents. It takes an unclear idea, asks the questions that matter, maps the architecture, selects the right specialist skills, organizes the repository, builds the requested scope, verifies it, and leaves a trace that survives the next thread.

It covers web apps, frontend, backend, Rust, Python, Cloudflare, Supabase, APIs, automations, macOS, iPhone, Android, Windows, Linux, Qt, WinUI, Tauri, packaging, and optimization. It routes specialist skills only when the project needs them.

## The rule

**Done means done.**

No slop. No vague hand-waving. No long language that hides missing work. No lazy stubs, fake data, silent fallbacks, or half-integrated features unless the user explicitly asks for them.

Use simple technical language. Keep the code small. Apply Ponytail: choose the simplest solution that actually works, then verify it.

### Anti-slop

Replace generic output with a clear decision, a real implementation, or a specific blocker.

### Anti-linguaggio lungo

Use the fewest words that make the decision, next action, and evidence unambiguous.

### Anti-prigrizia

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
