# Interaction and component geometry

Treat a component as a state machine with geometry. A visually correct resting state is not a finished component.

## Shared control contract

Every custom control must have:

- semantic HTML or a correct role/name/state mapping;
- a visible keyboard focus indicator, preferably `:focus-visible`;
- hover, focus, pressed, selected, disabled, loading, and error states where applicable;
- a pointer target large enough to use without precision;
- a label that remains usable when text is translated or enlarged;
- no dependence on hover for essential information or actions.

```css
:where(button, a, input, select, textarea, [tabindex]):focus-visible {
  outline: 2px solid var(--focus-ring);
  outline-offset: 3px;
}
```

Do not remove outlines without replacing them with a contrast-checked indicator. Avoid changing layout on hover/focus: prefer color, border, shadow, and opacity rather than transforms that move the hit target.

## Dropdowns, menus, and popovers

The default position must be safe, but the component must also handle the trigger near every viewport edge. Use the native Popover API and anchor positioning when the support target allows it:

```css
[popover] {
  inset: auto;
  margin: 0;
  max-inline-size: min(22rem, calc(100vw - 2 * var(--page-gutter)));
  max-block-size: min(32rem, calc(100dvh - 2 * var(--page-gutter)));
  overflow: auto;
  position-area: bottom span-inline;
  position-try-fallbacks: flip-block, flip-inline;
}
```

This is progressive enhancement: verify support and retain the project's accessible fallback. The fallback must still anchor the popup to the trigger, choose above/below and start/end placement based on available space, and keep the popup inside the viewport. Do not position a menu with a hard-coded `top` that happens to work at one scroll offset.

Behavior checklist:

- trigger exposes `aria-expanded` and `aria-controls` when using a custom disclosure;
- Enter/Space opens the control, Escape closes it, and focus returns to the trigger;
- menu items have the expected keyboard behavior for the chosen pattern;
- outside click does not accidentally submit or activate an unrelated action;
- hover/focus content can be dismissed, hovered, and kept visible long enough to use;
- the popup cannot cover the trigger's active area or the selected action without an intentional modal relationship.

For a simple show/hide section, use a real button and `aria-expanded`; do not turn a `div` into a button through CSS alone.

## Dialogs and drawers

Prefer the platform dialog or the project's tested dialog primitive. While open:

- keep focus inside the modal interaction;
- provide an obvious close control and Escape behavior;
- prevent background interaction without trapping the user in an unscrollable surface;
- give the dialog body its own `overflow: auto` only when its height is constrained;
- return focus to the invoker;
- check focused elements at small widths and at 200% zoom so fixed chrome does not obscure them.

On mobile, a drawer or bottom sheet can be a better representation than a tiny desktop dropdown. It must still expose the same information architecture and be dismissible.

## Forms

- Put visible labels above controls unless a tested component pattern says otherwise.
- Keep input text at least 16 CSS px on mobile to avoid unwanted browser zoom; do not shrink controls to fit a dense grid.
- Keep label, hint, error, and control associations semantic. Errors must not be conveyed only by color.
- Let a form become one column when labels or validation messages would collide.
- Check long labels, right-to-left text, browser autofill, invalid values, disabled states, and keyboard traversal.

## Touch, hover, and motion

Use `@media (hover: hover) and (pointer: fine)` for enhancements such as hover previews. Make the base action work on touch and keyboard. Use `touch-action` only to document an intentional gesture surface; never disable scrolling across a broad page without a product reason.

On touch devices, a fast tap needs immediate visual feedback but must not create accidental selection or browser gesture conflicts. Scope `user-select: none` to controls whose text is not content, and scope `touch-action` to the gesture surface. A global reset such as `* { user-select: none }` is a usability and accessibility bug.

Prefer transitions on `opacity`, `transform`, `color`, and `background-color`; avoid animating `width`, `height`, `top`, `left`, or large layout trees. Keep motion short and provide:

```css
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    scroll-behavior: auto !important;
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
  }
}
```

Use the project's established accessibility policy if it has a more precise reduced-motion implementation.
