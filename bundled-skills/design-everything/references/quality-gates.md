# Quality gates

Scale verification to risk, but do not ship a new visual UI without evidence.

## Before implementation

- Confirm the user/job, primary action, scope, states, platform matrix, and selected direction.
- Confirm the project’s existing tokens, UI library, font/icon policy, and route/component ownership.
- Create `design-references/<slug>/` and record the direction and responsive invariants.

## During implementation

- Keep components semantic and composable; prefer existing primitives over parallel one-off systems.
- Check narrow layout first, then intermediate and wide widths. Verify text and data extremes before polishing.
- Keep keyboard/focus, touch, reduced motion, loading, empty, error, disabled, and permission states in the same pass as the happy path.
- Run the existing project commands for lint, typecheck, tests, and build at the appropriate point; do not invent commands when package scripts already define them.
- For React changes, use `$react-doctor` after implementation when the environment allows it; use `$vercel-react-best-practices` for performance-sensitive React/Next work.

## Minimum browser evidence

Capture at least one narrow and one wide screenshot, plus any state or overlay that drove the change. For high-risk UI capture the full matrix from `responsive-first.md`. Name captures by route, width, height, theme, and state.

Exercise:

- keyboard tab order and visible focus;
- menu/dropdown open near viewport edges and inside scroll containers;
- sidebar/drawer open/close, Escape, focus return, and scroll ownership;
- long labels, long numbers/URLs, localization, empty/error/loading;
- touch/pointer behavior without hover assumptions;
- zoom/text resize, dark mode, reduced motion, safe areas where relevant.

Use `$agent-browser` or `$playwright` for real interactions if available. A static screenshot is not proof that a popover, drawer, or keyboard path works.

## Static and project checks

When the repository is compatible, run the existing frontend audit script from `$css-for-perfect-frontend`:

```bash
python3 ~/.codex/skills/css-for-perfect-frontend/scripts/audit_frontend.py <project-root>
```

Treat findings as leads to inspect, not automatic proof of failure. Follow with the project’s lint/typecheck/test/build and, when possible, a real browser pass.

## Handoff report

State:

- files/components changed and why;
- selected direction and any deliberate deviations;
- viewport/device/browser matrix actually checked;
- commands and results;
- remaining limitations, untested browsers/devices, or known follow-up.

Never claim “perfect”, “fully responsive”, or “accessible” solely because a build passed.
