# Interview and direction protocol

Use this protocol for a new UI or a redesign. Keep it lightweight when the user has already answered the questions.

## Inspect first

Before asking, inspect the project for:

- routes, screenshots, existing UI, design tokens, and component-library usage;
- copy/content shape, data states, permissions, and primary flows;
- target platforms, browser support, localization, and accessibility requirements;
- brand assets, forbidden patterns, reference URLs, and existing `.impeccable.md`/`agents.md`.

Ask only what inspection cannot establish.

## One focused question round

Ask up to seven short questions, preferably 3–5:

1. Who is using this, what job are they completing, and what is the primary action?
2. Which pages/states are in scope, and what content/data must be visible above the fold?
3. Which existing brand, UI library, screenshot, or product should the result respect?
4. Which visual directions are welcome or forbidden? Is the product calm, dense, editorial, tactile, technical, playful, or something else?
5. Which devices, widths, input modes, browsers, and localization constraints matter?
6. What must happen when content is long, missing, loading, invalid, offline, or permission-restricted?
7. Are there performance, motion, dark-mode, asset, or delivery constraints?

If the request is underspecified but low risk, infer sensible defaults and list them instead of blocking. If an answer changes the architecture or visual direction, ask before implementation.

## Direction cards

Show 2–3 candidates only when needed. Use this compact shape:

```text
A — [name]
Thesis: [one sentence about the user's experience]
Palette: [surface / text / border / accent / semantic states]
Type: [display / body / numeric or UI role]
Layout: [grid, density, whitespace, image treatment]
Interaction: [focus, hover/pointer, motion, feedback]
Responsive: [what collapses, reorders, scrolls, or becomes a drawer]
Trade-off: [what this direction sacrifices]
```

Make options meaningfully different, not three shades of the same generic SaaS dashboard. Include one safe direction and one distinctive direction when the brief allows it. Ask the user to choose, modify, or reject; record the result in `design-references/<slug>/directions/`.

## Teach-impeccable handoff

Use `$teach-impeccable` after the interview when the repository needs a durable design context. Let it inspect the actual codebase and write project-level context only if the requested implementation scope permits it. Confirm that the resulting `.impeccable.md`/`agents.md` records:

- visual principles and anti-patterns;
- semantic tokens and component ownership;
- responsive classes and shell geometry;
- typography and content rules;
- accessibility, motion, and QA expectations.

Do not use it to replace a missing product decision. The mother skill still owns the direction contract and must keep it in the reference workspace.
