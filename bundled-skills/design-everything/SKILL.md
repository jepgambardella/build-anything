---
name: design-everything
description: Orchestrate production-quality frontend and product UI work from discovery
  through visual direction, mobile-first responsive implementation, accessibility,
  component architecture, and evidence-based QA. Use for new interfaces, redesigns,
  design-system work, responsive fixes, visual polish, UI audits, or any request where
  the result must feel deliberate rather than AI-generated.
---

# Design Everything

Act as the design director, UX analyst, responsive CSS specialist, and frontend implementation coordinator. Treat this skill as a router: select a small compatible set of installed skills, apply them in an explicit order, and reconcile conflicts before changing code. Do not load every design skill at once.

## Operating contract

- Preserve the user's product intent, existing brand, established component library, and repository conventions before introducing taste.
- Treat visual quality, interaction quality, responsive behavior, accessibility, maintainability, and verification as one deliverable.
- Do not begin a new visual direction from a generic dashboard template, arbitrary gradients, invented icons, or unexamined defaults.
- For an existing project, inspect the real code, tokens, routes, assets, and running UI before proposing a replacement.
- For a known bug with an unambiguous target, keep the process short; do not force a design workshop.
- Record decisions and screenshots in a project-local `design-references/<slug>/` folder on every design/frontend task. Use the bundled scaffold script described in [reference-workspace.md](references/reference-workspace.md).

## 1. Triage the request

Classify the work before routing skills:

| Class | Typical request | First route |
| --- | --- | --- |
| New visual UI | page, app, dashboard, landing, prototype | `frontend-design`, `ui-ux-pro-max`, `adapt`, `css-for-perfect-frontend` |
| Existing redesign | “make it professional”, restyle, modernization | `redesign-existing-projects`, `critique`, `normalize`, `adapt`, `polish` |
| Responsive/CSS defect | overflow, bad wrapping, sidebar, dropdown, viewport bug | `css-for-perfect-frontend`, `adapt`, `harden`, then browser QA |
| Component/system work | reusable components, API, tokens, composition | `ui-component-patterns`, `normalize`, `extract`; add library-specific skill only when detected |
| Visual direction | palette, type, imagery, moodboard | `ui-ux-pro-max`, `frontend-design`, `image-taste-frontend`, optionally `imagegen` |
| Content/flow | copy, empty states, onboarding, errors | `user-oriented-frontend-and-design`, `clarify`, `onboard`, `harden` |
| Final review | “audit”, “polish”, “ship-ready” | `audit`, `critique`, `harden`, `polish`, `web-design-guidelines` |
| React/Next implementation | React components, app routes, performance | `ui-component-patterns`; add `vercel-composition-patterns`, `vercel-react-best-practices`, and `react-doctor` when applicable |
| Native mobile | SwiftUI/iOS or Compose/Android | route to the corresponding native mobile skill; do not apply web CSS rules blindly |

Use at most one primary visual direction and a focused set of implementation/audit skills. Load a reference only when its condition is met. See [routing-matrix.md](references/routing-matrix.md).

## 2. Inspect before asking

Read only enough of the project to avoid asking questions whose answers are already present:

1. Find the project root, `package.json`/build files, entry routes, and existing component/style directories.
2. Inspect design tokens, CSS variables, typography, icon system, theme modes, and installed UI library.
3. Check `AGENTS.md`, `agents.md`, `.impeccable.md`, README guidance, and existing visual references.
4. Run or inspect the relevant page if a browser/screenshot path exists; collect the current failure, not just a description.
5. Identify the content density, data states, required interactions, and likely narrowest usable width.

Do not overwrite an established system because a local skill has a stronger aesthetic opinion. Existing project evidence outranks stylistic defaults.

## 3. Run a bounded design interview

Ask only questions still unanswered. Use one focused round of 3–7 questions, then continue; ask another round only when a material decision remains blocked. If the user already supplied a complete brief, skip questions and summarize the inferred contract for confirmation.

Resolve these dimensions:

- user, job-to-be-done, primary action, and success signal;
- pages/states in scope, content density, and data edge cases;
- brand references, forbidden patterns, existing library, and accessibility constraints;
- platforms, supported browsers, target widths, touch/keyboard expectations, and localization;
- imagery/source assets, motion appetite, light/dark modes, and delivery constraints.

Present 2–3 compact direction cards before implementation when the direction is not already fixed. Each card must state: name, one-sentence thesis, palette roles, type pairing, layout character, interaction/motion posture, responsive behavior, and one trade-off. Prefer “A/B/C + modify” over open-ended taste questions. Never present a palette or font choice without explaining hierarchy and readability.

Use `$grill-me` only when the user explicitly asks for a grilling session: that skill is intentionally not implicit. Otherwise apply the bounded interview above.

## 4. Define the direction and reference workspace

After the user selects or corrects a direction:

1. Create `design-references/<slug>/` using `scripts/create_design_references.py`; preserve existing files and never replace a folder silently.
2. Save the brief, rejected/accepted direction cards, selected screenshots or image references, token decisions, and viewport QA evidence there. See [reference-workspace.md](references/reference-workspace.md).
3. For a new visual build, invoke `$image-taste-frontend` and `$imagegen` when imagery or a visual concept materially informs the UI. Inspect generated output before implementation and copy/move only the chosen project-bound assets into the reference folder. Do not generate decorative images merely to fill a folder for a technical bug fix.
4. Use `$teach-impeccable` when the project lacks a trustworthy design context or its context is stale. Let it inspect the repository and update project-level `.impeccable.md`/`agents.md` only within the requested project scope. Do not run it blindly inside this skill package or ask questions already answered.
5. If useful, use `$ui-ux-pro-max` to generate 2–3 candidate design systems and persist only the selected, project-compatible result. Do not let a generated recommendation override an existing brand or component contract.

Do not implement until the visual/interaction contract is clear, except for a narrowly scoped repair where the expected behavior is already specified.

## 5. Route the smallest compatible skill set

For web UI, the default technical spine is `$frontend-design` + `$adapt` + `$css-for-perfect-frontend`. Add specialists by need:

- **Structure and tokens:** `$arrange`, `$typeset`, `$normalize`, `$extract`.
- **Components and React:** `$ui-component-patterns`; `$shadcn-ui` only if the repository uses shadcn; `$vercel-composition-patterns` for compound/composable React APIs; `$vercel-react-best-practices` and `$react-doctor` for React/Next performance and post-change diagnostics.
- **Visual language:** choose exactly one baseline among `$minimalist-ui`, `$industrial-brutalist-ui`, `$design-taste-frontend`, `$high-end-visual-design`, `$stitch-design-taste`, or another explicitly selected direction. Use `$quieter`, `$bolder`, `$colorize`, or `$distill` as modifiers, not competing baselines.
- **Imagery and motion:** `$image-taste-frontend`/`$imagegen` for image-led work; `$animate` only when motion improves hierarchy or feedback; `$delight` only for intentional product moments.
- **Content and states:** `$user-oriented-frontend-and-design`, `$clarify`, `$onboard`, `$harden`.
- **Quality:** `$audit`, `$critique`, `$harden`, `$polish`, `$web-design-guidelines`, and `$optimize` as justified by risk. Use `$agent-browser` or `$playwright` when a real browser is available for interaction and screenshot verification.
- **Discovery:** `$find-skills` only when local coverage is missing or the user asks to search/install. Do not install an external skill automatically.

The external `frontend-ui-engineering` reference from Addy Osmani is useful for its production UI, mobile-first, WCAG, and breakpoint discipline; treat it as supplemental guidance, not a dependency. Keep the local `adapt` + `css-for-perfect-frontend` spine as the authoritative local workflow.

Resolve conflicts in this order: explicit user brief → existing project/design-system contract → accessibility and platform standards → framework/library constraints → responsive behavior → selected visual direction → anti-generic heuristics. When two aesthetic skills disagree, ask the user to choose or follow the selected direction; do not merge incompatible rule sets.

## 6. Implement mobile-first and component-first

Apply the rules in [responsive-first.md](references/responsive-first.md):

- design the narrow layout first, then add `min-width` enhancements driven by content rather than device names;
- keep one page-level scroll axis unless a two-dimensional surface is genuinely the content (for example, a data table);
- make fixed/sticky shell regions explicit, viewport-aware, and safe-area-aware; ensure main content has a real min/max contract and can shrink (`min-width: 0` where needed);
- make sidebars collapse, become a drawer, or become a documented secondary scroll region; never let a “fixed” desktop sidebar become a clipped mobile column;
- make menus, popovers, tooltips, and dropdowns choose a safe placement, flip when space is insufficient, remain connected to their trigger, and not cover the action that opened them;
- protect text with `minmax(0, 1fr)`, `overflow-wrap: anywhere`, sensible line lengths, truncation only when content remains discoverable, and table-specific narrow-screen behavior;
- define states before styling: loading, empty, error, disabled, focus-visible, hover only where hover exists, pressed, validation, long content, localization, and reduced motion;
- preserve the selected tokens/components; do not create one-off magic numbers or a second style system without a documented reason.

## 7. Verify the result, not just the code

Run the proportionate gates in [quality-gates.md](references/quality-gates.md). At minimum:

1. Check the app at 320/360/390/430, 768, 1024, 1280/1440, and a wide viewport; include landscape where relevant.
2. Test keyboard, visible focus, touch/pointer, zoom/text resize, long labels, empty/error/loading states, dark mode if supported, and reduced motion.
3. Capture representative screenshots into `design-references/<slug>/screenshots/` and compare them with the approved direction.
4. Run the project’s existing lint/typecheck/test/build commands and the static frontend audit when applicable.
5. Fix the root layout or component contract, not a sequence of viewport-specific patches. Re-check adjacent widths after each structural fix.

Report what was changed, what was verified, the viewport/device matrix, and any unverified browser or real-device limitation. Do not call a UI “perfect” when a screenshot, interaction, or build gate is still missing.

## Reference map

- [routing-matrix.md](references/routing-matrix.md): local skill selection, precedence, and incompatibilities.
- [interview-and-direction.md](references/interview-and-direction.md): question loop and direction-card format.
- [reference-workspace.md](references/reference-workspace.md): mandatory visual evidence folder and image workflow.
- [responsive-first.md](references/responsive-first.md): layout, CSS, interaction, and viewport guardrails.
- [quality-gates.md](references/quality-gates.md): implementation and QA checklist.
- [source-notes.md](references/source-notes.md): external standards and research used to shape this coordinator.
