---
name: css-for-perfect-frontend
description: Build, refactor, or audit production-quality frontend UI with resilient
  CSS, responsive layout, clean component structure, accessible interaction states,
  overflow-safe typography, and visual consistency with the existing design system
  or UI library. Use for HTML/CSS, Tailwind, CSS Modules, Sass, React/Next.js, Vue,
  Svelte, dashboards, sidebars, tables, forms, dropdowns, modals, responsive fixes,
  UI polish, and visual QA.
---

# CSS for Perfect Frontend

Treat frontend quality as a combination of three contracts: the visual language must stay coherent, the layout must survive real content and real viewports, and every interaction must remain usable with keyboard, touch, zoom, and reduced motion. Apply the workflow below whether building new UI or repairing an existing one.

## Operating rules

- Read the repository before writing CSS. Locate the app entry point, package manifest, global styles, theme/design tokens, component primitives, routing/layout shell, and the UI library already in use. Preserve its conventions.
- Use the project's existing colors, typefaces, spacing scale, radii, shadows, icon set, and component primitives before introducing anything new. Do not install or invent a library without checking the manifest and asking when installation changes scope.
- Separate structure from decoration. Use semantic HTML and normal document flow for structure; use absolute/fixed positioning only for overlays, anchored controls, or intentional decoration that cannot cover content.
- Prefer the simplest layout model that expresses the relationship: Flexbox for one-dimensional alignment, Grid for two-dimensional page/data structure, container queries for reusable components, and media queries for viewport or input changes.
- Prefer intrinsic and fluid sizing (`minmax()`, `clamp()`, `min()`, `max()`, `auto-fit`, `max-inline-size`) over guessed pixel widths. A fixed value is acceptable when it represents a real contract, such as a desktop sidebar or a toolbar control.
- Never hide a problem with `overflow: hidden`. First find the element that is too wide or too tall. Use clipping only when clipping is the intended product behavior.
- Treat a screenshot as evidence, not as a substitute for inspecting the DOM, computed layout, keyboard behavior, and real content.

## Workflow

### 1. Establish the contract

Before implementation or review, record:

- target pages/components and their one primary job;
- supported browsers, input methods, locales, light/dark themes, and reduced-motion behavior;
- minimum viewport and important zoom/reflow requirements;
- existing tokens, component library, icon library, CSS architecture, and naming conventions;
- which regions scroll: the document, a page body, a sidebar, a table, a panel, or a modal;
- states that must exist: loading, empty, error, long text, disabled, focus, hover, pressed, selected, expanded, validation, and permission variants.

If the request is an audit, stay read-only unless the user explicitly asks for fixes. If it is a build or fix, keep unrelated changes untouched.

### 2. Build the visual and CSS system first

Create or reuse semantic tokens for color, type, spacing, radius, elevation, motion, and z-index. Keep component rules close to the component and global rules narrow. Use logical properties (`margin-inline`, `padding-block`, `inset-inline-end`) when they do not conflict with an established project convention.

Use a small, intentional cascade. Prefer low-specificity selectors, component scopes, `:where()`/`:is()` where useful, and cascade layers when the project supports them. Avoid selector chains that require increasingly specific overrides. Keep one source of truth for each token.

Typography is part of layout: define a readable base line-height, a controlled measure for prose, a deliberate type scale, and tabular numerals for aligned data. Use `text-wrap: balance` for short headings and `text-wrap: pretty` selectively for longer editorial copy; do not insert manual `<br>` elements merely to make one viewport look right.

### 3. Construct the layout from outside in

Start with page shell, navigation, scroll regions, containers, and major tracks; only then style cards and controls. For a desktop application shell, a robust starting shape is:

```css
.app-shell {
  min-block-size: 100dvh;
  display: grid;
  grid-template-columns: var(--sidebar-size) minmax(0, 1fr);
}

.sidebar,
.main {
  min-block-size: 0;
  min-inline-size: 0;
}

.sidebar {
  block-size: 100dvh;
  overflow-y: auto;
  overscroll-behavior: contain;
}

.main {
  overflow: auto;
}
```

Adapt this to the app. Do not blindly force a nested-scroller architecture: choose one clear owner for each axis, document it, and verify that keyboard focus and mobile browser chrome remain usable. Use `min-width: 0`/`min-inline-size: 0` on flex/grid children that must shrink; use `min-height: 0`/`min-block-size: 0` on children inside constrained vertical layouts.

For sidebars, decide explicitly between normal flow, sticky, fixed, or a drawer. A desktop sidebar may have a fixed inline size and a viewport-relative block size (`100dvh`), but mobile should usually become a drawer or normal-flow navigation. Add safe-area padding where the UI can reach a device edge. Do not make a sidebar “fixed” in pixels just because its height looked right in one screenshot.

### 4. Make responsiveness content-driven

- Start from the narrow layout and add space, columns, or persistent navigation when the content needs it.
- Choose breakpoints where the composition fails, not because a framework has a familiar number. Test portrait and landscape.
- Use `@container` for components reused in different parent widths. Use `@media (hover: hover) and (pointer: fine)` for hover-only enhancements; touch must not depend on hover.
- Use `100dvh` for an actively sized app surface, `100svh` when the smallest stable viewport is safer, and `min-height` rather than a rigid height when content may grow. Use `env(safe-area-inset-*)` at device edges.
- Let controls wrap, stack, or change representation. Do not squeeze a desktop toolbar until labels overlap. Preserve the primary action and move secondary actions into a disclosure or menu.
- At minimum inspect 320/360/390px, 768px, 1024px, 1280px, and a wide desktop. Also test text zoom at 200% and the reflow condition around 320 CSS px.

### 5. Make overflow intentional

Use this order when content does not fit:

1. let the correct container grow or wrap;
2. remove accidental intrinsic minimums (`min-inline-size: 0`, `minmax(0, 1fr)`);
3. shorten or restructure content only when the product meaning allows it;
4. wrap long identifiers with `overflow-wrap: anywhere`;
5. use ellipsis only for a deliberate one-line summary with an accessible full value;
6. add a clearly signposted scroll region only when two-dimensional meaning or dense data requires it.

For every horizontal scroller, provide a label, keyboard focusability when it is a meaningful region, visible focus, and a mobile affordance. Tables may scroll horizontally when preserving the table is the best accessible representation; do not force every table into tiny unreadable cells. Consider a responsive alternative (priority columns, stacked rows, or a detail view) when the data does not require a two-dimensional table.

Never use `word-break: break-all` for ordinary copy. Do not apply `white-space: nowrap` to labels, navigation, buttons, or table cells without checking translations and long values. Use `overflow: clip` only when programmatic scrolling must also be impossible; `hidden` and `auto` have different behavior.

### 6. Build interaction geometry, not just appearance

Every interactive element needs a semantic control, an accessible name, a visible `:focus-visible` state, a disabled/pressed/selected state where relevant, and a pointer/touch target large enough for the context. Aim for a 44px target for primary touch controls; satisfy the applicable WCAG 2.2 target-size requirement and its exceptions rather than treating 44px as a universal CSS height.

For menus, tooltips, command palettes, and popovers:

- anchor the overlay to the trigger, keep it inside the viewport, and give it a max block size with its own scroll when content is long;
- prefer the native Popover API and CSS anchor positioning when the browser support target permits it;
- otherwise use the project's accessible primitive or a measured fallback, with explicit placement fallbacks above/below and start/end;
- never let a menu cover the trigger or the action the user is trying to choose without a clear reason;
- support keyboard navigation, Escape, outside-click behavior, focus return, and the correct `aria-expanded`/`aria-controls` state;
- do not make core actions hover-only. Tooltips must remain dismissible, hoverable, and persistent long enough to use.

For dialogs, prevent background interaction, keep focus inside while open, return focus to the invoker, and ensure the dialog itself can scroll without leaking scroll to the page. For drawers, make the close action reachable and do not obscure focused content at small widths.

For mobile browser edge cases, test real Safari/Chrome hardware rather than relying only on desktop emulation:

- keep tap feedback intentional; if `-webkit-tap-highlight-color` is changed, provide an equivalent pressed/focus state;
- apply `user-select: none` only to non-text controls such as icons or drag handles, never to readable content or form values;
- use `touch-action: manipulation` only on controls where it solves a proven gesture conflict, and use `pan-x`/`pan-y` on the corresponding carousel surface rather than disabling gestures globally;
- use `overscroll-behavior: none` only for a deliberately app-like root surface where pull-to-refresh or scroll chaining is a real conflict;
- use `scrollbar-gutter: stable` on a root or modal scroll owner when opening overlays would otherwise shift the layout, and verify overlay-scrollbar platforms;
- use `viewport-fit=cover` plus `env(safe-area-inset-*)` only when content intentionally reaches the device edge;
- set `theme-color` per supported color scheme when browser chrome should follow the UI, and keep it aligned with the actual surface color;
- use a horizontal carousel only when horizontal motion is part of the interaction, with `overflow-x: auto`, `scroll-snap-type`, visible affordance, and keyboard/assistive alternatives.

### 7. Polish without generic AI decoration

Make hierarchy visible through type, spacing, alignment, and restrained elevation before adding gradients, glass, glows, or motion. Use cards only for genuinely separate content or actions; do not nest rounded containers by default or repeat identical metric-card grids without a product reason. Respect the existing visual context instead of replacing it with a fashionable palette.

Keep motion purposeful and cheap: animate opacity and transforms where possible, avoid layout-thrashing properties, keep transitions brief, and provide a `prefers-reduced-motion: reduce` path. Do not add perpetual motion to ordinary navigation, tables, or dashboards just to make them feel “premium.”

### 8. Verify and report

Run the smallest relevant project checks: formatter, linter, typecheck, unit tests, build, and the project's browser/a11y checks. Discover them from `package.json`, workspace scripts, and repository docs; if no manifest or test setup exists, say so and perform the static/code review plus any available browser check. Run the bundled scanner for a fast static pass:

```bash
python3 <BUILD_ANYTHING_DIR>/bundled-skills/css-for-perfect-frontend/scripts/audit_frontend.py .
```

If a real browser is available, use the project's existing browser tooling or the `playwright`/`agent-browser` skill for screenshots and interaction checks. Inspect both code and rendered output. If no browser is available, mark rendered behavior, computed overflow, and screenshot checks as unverified rather than inferring them from CSS. Verify:

- no accidental document or nested horizontal overflow at tested widths;
- no clipped focus ring, fixed header, sidebar, toast, or popover hiding content;
- long labels, URLs, numbers, translated strings, empty states, errors, and dense tables;
- keyboard-only navigation, touch targets, Escape/close behavior, focus return, and scroll regions;
- light/dark/high-contrast behavior, contrast, reduced motion, text zoom, and safe areas;
- consistent tokens, component-library usage, naming, and absence of one-off overrides;
- screenshots at narrow, intermediate, and wide widths, with the visual diff explained rather than ignored.

Report findings with severity, exact location, user impact, evidence, and the smallest safe fix. Distinguish a real bug from a product decision (for example, an intentionally scrollable data table) and state what was not verified.

For each viewport/interaction check, record: viewport or device, input mode, action/state, expected result, observed result, evidence path (screenshot/log/DOM), and pass/fail/blocked. State the scanner's heuristic coverage and likely false positives separately from browser/a11y evidence.

## Reference routing

Load only the reference needed for the current task:

- [CSS layout and overflow](references/css-layout-and-overflow.md): shells, flex/grid sizing, viewport units, text, tables, and scroll ownership.
- [Interaction and component geometry](references/interaction-and-components.md): menus, popovers, dialogs, drawers, forms, focus, and touch.
- [Visual quality and accessibility](references/visual-quality-and-accessibility.md): tokens, typography, hierarchy, anti-patterns, states, and visual QA.
- [Source notes](references/source-notes.md): local skill synthesis and primary online documentation used for this skill.

Use the local `audit`, `adapt`, `arrange`, `frontend-design`, `harden`, `normalize`, `polish`, `typeset`, `ui-ux-pro-max`, `uncodixfy`, and `vercel-react-best-practices` skills as targeted companions when their full workflows are needed. This skill supplies the shared CSS/layout quality gate; it does not replace framework-specific testing or a human visual review.
