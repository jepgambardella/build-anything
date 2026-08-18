# Source notes

This skill is a synthesis, not a replacement for the standards. Re-open the primary sources when a browser-support or conformance decision matters.

## Local skill inputs

- `frontend-design`: subject-specific visual direction, typography, deliberate hierarchy, restraint, and self-critique.
- `adapt`: content-driven adaptation across mobile/tablet/desktop, input methods, orientation, and real-device verification.
- `arrange`: spacing systems, Flexbox versus Grid, intrinsic responsive grids, named areas, rhythm, and semantic z-index scales.
- `audit`: accessibility, theming, responsive, performance, and anti-pattern audit structure.
- `harden`: text overflow, i18n, error/empty states, edge cases, reduced motion, and visual regression checks.
- `normalize`: alignment with existing design tokens and component conventions.
- `polish` and `typeset`: final spacing, focus, interaction, typography, line length, and zoom checks.
- `ui-ux-pro-max`: touch, contrast, responsive, motion, charts, and pre-delivery checklists.
- `uncodixfy`: restraint against generic AI UI patterns and excessive decoration.
- `vercel-react-best-practices`: optional React/Next.js performance pass after layout correctness.

## Primary online sources

- [CSS Protips](https://github.com/AllThingsSmitty/css-protips): reset/box sizing, focus, aspect ratio, tables, specificity, `rem`/`em`, form font size, and logical margins. Some tips are historical or context-specific; validate browser support and accessibility before adopting them.
- [MDN: CSS values and units](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units) and [MDN: length units](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length): viewport units including `svh`, `lvh`, and `dvh`.
- [web.dev: container queries](https://web.dev/learn/css/container-queries/): component responsiveness based on the containing block rather than only the viewport.
- [MDN: Grid layout](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Grid_layout/Basic_concepts) and [MDN: responsive auto-fit grids](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/CSS_layout/Grids): `minmax()` and intrinsic tracks.
- [web.dev: overflow](https://web.dev/learn/css/overflow/): intentional clipping, scroll regions, keyboard access, scroll chaining, and `overscroll-behavior`.
- [MDN: overscroll behavior](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overscroll-behavior) and [MDN: scrollbar gutter](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scrollbar-gutter): containment and stable scrollbar space.
- [web.dev: typography](https://web.dev/learn/css/typography/): `text-wrap`, `overflow-wrap`, and text overflow behavior.
- [MDN: Popover API](https://developer.mozilla.org/en-US/docs/Web/API/Popover_API/Using) and [MDN: CSS anchor positioning](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Anchor_positioning/Using): anchored overlays and placement fallbacks. Check compatibility before relying on newer features.
- [WAI-ARIA APG: disclosure](https://www.w3.org/WAI/ARIA/apg/patterns/disclosure/): button, expanded state, and keyboard behavior for show/hide controls.
- [WCAG 2.2](https://www.w3.org/TR/WCAG22/), especially [Reflow](https://www.w3.org/WAI/WCAG22/Understanding/reflow), focus visibility/obscuration, contrast, text spacing, hover/focus content, motion, and target size.
