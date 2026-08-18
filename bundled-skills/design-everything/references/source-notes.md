# Source notes

This coordinator combines the installed local skills with a small set of external standards and research. Use the links as reference material; do not treat community skill repositories as authoritative over the project brief, browser behavior, or accessibility standards.

## Local sources

- `~/.codex/skills/css-for-perfect-frontend/SKILL.md`: CSS/layout/overflow/interaction guardrails and static audit already installed for this user.
- `~/.agents/skills/adapt/SKILL.md`: mobile/tablet/desktop adaptation and content-driven breakpoint workflow.
- `~/.agents/skills/frontend-design/SKILL.md`: visual direction, hierarchy, typography, imagery, and deliberate motion.
- `~/.agents/skills/image-taste-frontend/SKILL.md` + `~/.codex/skills/.system/imagegen/SKILL.md`: image-led direction and generated visual references when appropriate.
- `~/.agents/skills/ui-ux-pro-max/SKILL.md`: searchable design-system and UX pattern guidance.
- `~/.agents/skills/teach-impeccable/SKILL.md`: durable project-specific design context setup.

## External references checked

- [Addy Osmani agent-skills — frontend-ui-engineering](https://github.com/addyosmani/agent-skills/blob/main/skills/frontend-ui-engineering/SKILL.md): production UI engineering, mobile-first examples, breakpoints, design-system/accessibility emphasis.
- [Wshobson agents catalogue](https://github.com/wshobson/agents/blob/main/docs/agent-skills.md): lists a dedicated responsive-design skill covering fluid layouts, Grid/Flexbox, and container queries; use as an ecosystem lead, not a dependency.
- [W3C WCAG 2.2](https://www.w3.org/TR/WCAG22/): reflow, focus, input modality, target size, contrast, motion, and full-page responsive conformance.
- [WAI Understanding Reflow](https://www.w3.org/WAI/WCAG22/Understanding/reflow): 320 CSS px reflow, zoom, and fixed/sticky content risks.
- [web.dev Container Queries](https://web.dev/learn/css/container-queries/): component behavior based on available container size rather than only viewport size.
- [MDN CSS Anchor Positioning](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Anchor_positioning): anchored overlays and `position-try` fallbacks for viewport-aware placement.
- [AllThingsSmitty css-protips](https://github.com/AllThingsSmitty/css-protips): practical CSS patterns, used as inspiration and filtered through current standards and project constraints.
- [skills.sh](https://skills.sh/): ecosystem discovery entry point for future skill searches; do not install without explicit user direction.

## Interpretation rule

The external sources support the principles in this skill; they do not justify blindly adding more dependencies or imposing a visual style. Verify browser support, project framework, and real interaction behavior before relying on a newer CSS feature.
