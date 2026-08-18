# Visual quality and accessibility

Use this reference for the pass that turns “technically works” into a coherent, professional interface. It combines the local frontend skills into a compact decision guide.

## Preserve context

Before choosing a color, font, radius, shadow, icon, or animation, inspect what the project already uses. If a UI library is present, use its primitives and override its tokens rather than rebuilding near-duplicates. If a design source or screenshot exists, identify its layout grid, alignment anchors, spacing rhythm, type hierarchy, and interaction assumptions. Do not copy a screenshot's accidental pixel values into a generalized component.

Avoid common AI-generated tells unless the brief explicitly asks for them: repeated rounded cards, floating glass shells, random gradients, glow-heavy dark mode, generic metric grids, decorative labels, excessive pills/badges, unmotivated asymmetry, fake data, and motion on every element. Distinctiveness should come from the product's subject and hierarchy, not from adding effects.

## Tokens and hierarchy

Use semantic tokens, for example:

```css
:root {
  --surface-page: #f8fafc;
  --surface-panel: #ffffff;
  --text-primary: #172033;
  --text-secondary: #526078;
  --border-subtle: #d8dee9;
  --accent: #2457d6;
  --focus-ring: #2457d6;
  --space-1: 0.25rem;
  --space-2: 0.5rem;
  --space-3: 0.75rem;
  --space-4: 1rem;
  --space-6: 1.5rem;
  --space-8: 2rem;
}
```

The values must come from the actual project. Keep spacing consistent but not monotonous: tight for related items, larger for separate groups. Use `gap` for sibling layout. Prefer hierarchy through type, alignment, and space before adding containers or shadows. Never use low-contrast text as decoration.

## Typography

- Use the chosen type system and real weights; do not silently substitute a random web font.
- Keep body copy readable and control prose measure, usually around 45–75 characters per line depending on the product.
- Use `font-variant-numeric: tabular-nums` for data that must align and `font-feature-settings` only when the project needs it.
- Test headings with long localized strings and `text-wrap: balance`; test body copy with enlarged text and `text-wrap: pretty` only where performance permits.
- Do not solve wrapping with manual line breaks that fail at other widths.

## Accessibility floor

Check against WCAG 2.2 and the project's target conformance:

- normal text contrast at least 4.5:1, large text at least 3:1;
- meaningful non-text controls/states at least 3:1 against adjacent colors where the criterion applies;
- keyboard focus visible and not hidden by sticky/fixed UI;
- content reflows without loss of information or two-dimensional scrolling at the applicable narrow/zoomed viewport, except content whose meaning requires two dimensions (such as a data table);
- text can be resized to 200% without loss of content or functionality;
- color is not the only signal for status, errors, or selection;
- motion, flashing, hover content, target size, and pointer cancellation follow the applicable WCAG criteria;
- semantic landmarks, headings, names, labels, and status messages survive visual restyling.

The practical target for primary touch controls is 44px, but do not distort a compact desktop UI without considering the input method and the WCAG exceptions.

## States and content matrix

Render or reason through at least:

| Dimension | Test content/state |
| --- | --- |
| length | short label, long label, unbroken URL/token, large number |
| data | zero rows, one row, many rows, missing value, error value |
| interaction | hover, keyboard focus, pressed, selected, disabled, loading |
| viewport | narrow portrait, narrow landscape, tablet, desktop, wide desktop |
| user setting | 200% text zoom, reduced motion, dark/light, forced colors if supported |
| language | longer translation, accents, RTL if in scope |

## Visual QA pass

Use a screenshot at representative widths, then ask:

1. Can the primary task be identified in two seconds?
2. Do alignment anchors, spacing rhythm, and component boundaries remain consistent?
3. Is any text cramped, orphaned, clipped, or oddly wrapped?
4. Do controls look actionable without relying on color or hover?
5. Is the page too card-heavy, too decorative, or too sparse for its content density?
6. Does responsive behavior preserve priority rather than merely stacking everything?
7. Does every visible overlay have a reason, a close path, a focus path, and viewport-safe geometry?

Fix the root layout or token problem before adding one-off offsets. Record intentional exceptions so a later “cleanup” does not remove required product behavior.

