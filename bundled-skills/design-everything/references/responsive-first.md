# Responsive-first implementation rules

Treat responsive behavior as a content and interaction contract. Do not target device names with a pile of overrides.

## Layout invariants

- Start at the narrowest usable width. Add `min-width` enhancements after the content and interaction order works on mobile.
- Use page-level media queries for shell changes and container queries for reusable components whose behavior depends on their own available width.
- Keep the document readable at 320 CSS px and at 200–400% text/viewport zoom. Avoid two-dimensional scrolling except for content that is inherently two-dimensional, such as a data table or map.
- Make every flex/grid child that must shrink eligible to shrink (`min-width: 0`, `minmax(0, 1fr)`). Bound prose with a readable measure; do not solve overflow by clipping the page.
- Prefer intrinsic sizing, `clamp()`, `min()`, `max()`, `minmax()`, `auto-fit`, and content-driven breakpoints over fixed device assumptions.
- Define a single shell contract: header, sidebar/drawer, main, inspector, and footer must have explicit ownership of scrolling and height.

## Shells, sidebars, and height

- Use `min-height: 100dvh` for app shells when dynamic viewport behavior matters; reserve `svh`/`lvh` for intentional small/large viewport semantics.
- Account for persistent header/sidebar dimensions instead of adding arbitrary top/left padding. Use safe-area insets where the platform requires them.
- On desktop, a sidebar may be sticky or fixed only when its scroll ownership, height, focus behavior, and escape path are clear. On narrow screens, collapse it to a drawer, bottom sheet, or accessible menu; do not leave a clipped fixed column.
- Never use `height: 100%` without a definite containing height. Prefer `min-height` for content regions unless a bounded scroll area is intentional.
- Keep one primary vertical scroll region. If a nested region must scroll, expose it as a deliberate surface with a visible affordance and keyboard/touch support.

## Text, grids, tables, and media

- Use `overflow-wrap: anywhere` or a controlled break strategy for untrusted IDs/URLs; use `text-overflow` only when truncation is acceptable and the full value remains available.
- Do not put critical copy in fixed-height boxes. Let headings wrap; reserve `line-clamp` for non-critical previews.
- Use grid tracks such as `minmax(0, 1fr)` and flex children with `min-width: 0`; audit every long-label and long-number path.
- For tables, choose intentionally: true horizontal scrolling with a labeled region, a column-priority/reflow layout, or a compact list/card representation. Never let the table make the whole page scroll sideways by accident.
- Give images and media an explicit aspect-ratio/frame policy, `object-fit`, loading strategy, alt treatment, and a narrow-screen crop that preserves the subject.

## Menus, popovers, and overlays

- Keep an overlay attached to its trigger and within the viewport. Prefer the component/library’s collision and placement logic; use CSS anchor positioning and `position-try` when supported, with a tested fallback.
- Choose top/bottom/left/right placement from available space; flip when needed. Do not cover the trigger’s target action or the focused element without a dismissal/reveal path.
- Manage focus, Escape, outside click, stacking contexts, and scroll locking. Verify the overlay on the last row, near each viewport edge, inside a scroll container, and with zoom.
- Do not use `z-index: 999999` as a substitute for understanding stacking contexts. Create a small semantic layer scale.

## Input and touch

- Keep controls large enough and separated enough for touch; follow WCAG 2.2 target-size and focus requirements.
- Do not rely on hover for essential information or actions. Gate hover-only polish with pointer/hover capability and provide keyboard/focus/touch equivalents.
- Keep form text at least 16px where mobile browser zoom behavior makes smaller inputs harmful; preserve visible labels, error association, and autocomplete semantics.
- Respect `prefers-reduced-motion`, pointer cancellation, `touch-action` needs, safe areas, and keyboard-visible states.

## Validation matrix

Check at least 320, 360, 390/430, 768, 1024, 1280/1440, and a wide viewport. Add landscape, short viewport height, 200% zoom, large text, long localized strings, dark mode, keyboard-only navigation, touch/pointer, loading/empty/error, and reduced-motion checks as relevant.

When a defect appears at one width, inspect the layout contract and neighboring widths. Fix the source constraint; do not accumulate a width-specific patch without a reason recorded in `qa/`.
