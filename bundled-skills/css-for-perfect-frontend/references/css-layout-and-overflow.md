# CSS layout and overflow

Use these patterns as diagnostics and starting points, not as a universal stylesheet. Confirm the actual scroll contract and browser support in the project.

## Baseline

```css
*, *::before, *::after {
  box-sizing: border-box;
}

html {
  min-inline-size: 320px;
  color-scheme: light dark;
}

body {
  min-block-size: 100%;
  margin: 0;
  line-height: 1.5;
  overflow-wrap: break-word;
}

img, svg, video, canvas {
  display: block;
  max-inline-size: 100%;
}

button, input, select, textarea {
  font: inherit;
}
```

Do not copy `color-scheme` if the product does not support both themes. Keep reset rules compatible with the chosen component library.

## The common flex/grid failure

Flex and grid items have an automatic minimum size based on their content. A long URL, table, or unbreakable label can therefore make a supposedly fluid column wider than the viewport. Put the minimum-size fix on the item that must shrink, not randomly on the page:

```css
.page-body,
.toolbar-main,
.grid-cell {
  min-inline-size: 0;
}

.vertical-layout-child {
  min-block-size: 0;
}
```

For a page grid, prefer `minmax(0, 1fr)` for flexible tracks:

```css
.page {
  display: grid;
  grid-template-columns: minmax(14rem, 18rem) minmax(0, 1fr);
}
```

Use `repeat(auto-fit, minmax(16rem, 1fr))` for content that can genuinely reflow. Choose the minimum from the component's content, not from a device category.

## Scroll ownership

One axis should have one obvious owner. A typical app shell has a viewport-sized outer shell, a scrollable navigation region, and a scrollable main region. It must also make the children shrinkable:

```css
.shell {
  min-block-size: 100dvh;
  display: grid;
  grid-template-rows: auto minmax(0, 1fr);
}

.content-row {
  min-block-size: 0;
  display: grid;
  grid-template-columns: var(--nav-width) minmax(0, 1fr);
}

.nav,
.content {
  min-block-size: 0;
  min-inline-size: 0;
  overflow: auto;
}
```

Do not add `overflow: hidden` to `html`, `body`, or a broad wrapper merely to silence a scrollbar. It can hide content, break focus scrolling, and interfere with dialogs, popovers, and mobile gestures. If a nested scroller is intentional, use `overscroll-behavior: contain` only at that boundary and make the region discoverable and keyboard usable.

When a modal or drawer changes whether the page scrolls, `scrollbar-gutter: stable` can reserve space and prevent a horizontal layout jump. Verify it on platforms with overlay scrollbars, where the visual effect may be different. Do not use it as a substitute for deciding which element owns scrolling.

## Viewport and safe-area sizing

- `vh` can represent the large viewport and may be wrong while mobile browser UI is visible.
- `dvh` tracks the dynamic viewport and is useful for an active app surface.
- `svh` is the stable small viewport and can avoid content being hidden behind browser chrome.
- `lvh` is the large viewport and is appropriate only when that behavior is intentional.

Prefer `min-block-size: 100dvh` for full-height application regions that can grow. For a surface touching device edges:

```css
.edge-to-edge-panel {
  padding-block-end: max(1rem, env(safe-area-inset-bottom));
  padding-inline: max(1rem, env(safe-area-inset-left))
                  max(1rem, env(safe-area-inset-right));
}
```

## Text that survives real content

```css
.heading {
  max-inline-size: 24ch;
  text-wrap: balance;
}

.prose {
  max-inline-size: 70ch;
  text-wrap: pretty;
}

.identifier {
  overflow-wrap: anywhere;
}

.one-line-summary {
  min-inline-size: 0;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}
```

Use ellipsis only when truncation is part of the interaction and the full value is available via an accessible name, details view, or copy action. Do not use `break-all` for prose or apply `nowrap` to every UI label. `text-wrap: balance` is ideal for short headings but not a substitute for sensible width and copy.

## Tables and dense data

Keep the semantic table when the relationship between columns matters. Give horizontal scrolling to a named wrapper, not to the whole page:

```css
.table-region {
  max-inline-size: 100%;
  overflow-x: auto;
  overscroll-behavior-inline: contain;
}

.table-region table {
  inline-size: 100%;
  border-collapse: collapse;
}

.table-region th,
.table-region td {
  overflow-wrap: anywhere;
  vertical-align: top;
}
```

Use `table-layout: fixed` only when equal track behavior is appropriate and each cell has a wrapping/ellipsis policy. Otherwise allow content-driven columns or provide priority columns/stacked details on small screens. A table with two-dimensional meaning is an accepted exception to the “no horizontal scroll” rule; it still needs a visible, keyboard-usable scroll region.

For intentional carousels, keep the scroll local and make the affordance obvious:

```css
.carousel {
  display: flex;
  gap: var(--space-4);
  max-inline-size: 100%;
  overflow-x: auto;
  overscroll-behavior-inline: contain;
  scroll-snap-type: inline mandatory;
  touch-action: pan-x;
}

.carousel > * {
  flex: 0 0 min(18rem, 82vw);
  scroll-snap-align: start;
}
```

Do not put `touch-action: pan-x` on the whole page. Provide a non-gesture way to reach every item and check keyboard focus, reduced motion, and RTL behavior.

## Positioning and layering

Use a semantic z-index scale rather than arbitrary values:

```css
:root {
  --z-base: 0;
  --z-sticky: 10;
  --z-dropdown: 100;
  --z-backdrop: 200;
  --z-dialog: 300;
  --z-toast: 400;
  --z-tooltip: 500;
}
```

Before raising `z-index`, inspect stacking contexts created by `transform`, `opacity`, `filter`, `isolation`, and positioned ancestors. A higher number cannot escape the wrong stacking context. Avoid absolute layers that cover content or intercept pointer events unless they are a real overlay.
