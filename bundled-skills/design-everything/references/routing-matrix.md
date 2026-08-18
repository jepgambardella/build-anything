# Skill routing matrix

Use this file after triage. The mother skill coordinates; the routed skill performs the specialized work. Load only the rows that apply.

## Local skill groups

### Always-consider for web UI

| Skill | Role | When to load | Guardrail |
| --- | --- | --- | --- |
| `$frontend-design` | Distinctive visual composition and art direction | New or visually important web UI | Match the brief and existing system; do not force an aesthetic |
| `$adapt` | Responsive behavior across screen classes | Any web layout or responsive change | Start mobile-first; use content-driven breakpoints |
| `$css-for-perfect-frontend` | CSS robustness, overflow, viewport, interaction, accessibility | Any CSS/layout/component implementation or audit | Treat its static audit as a gate, not a substitute for browser QA |
| `$ui-ux-pro-max` | Design-system candidates, palettes, typography, UX patterns | New direction, redesign, or unclear visual system | Select and adapt; do not blindly paste generated output |

### Structure, typography, and reuse

| Skill | Use for |
| --- | --- |
| `$arrange` | Layout hierarchy, grid/flex decisions, spacing rhythm, responsive regions |
| `$typeset` | Font pairing, text measure, type scale, wrapping, numeric alignment |
| `$normalize` | Aligning a new surface to an existing design system |
| `$extract` | Promoting repeated UI into reusable components/tokens |
| `$ui-component-patterns` | React/TypeScript component APIs, composition, hooks, accessibility |
| `$vercel-composition-patterns` | Compound components and scalable React composition |
| `$shadcn-ui` | Only repositories that actually use shadcn/ui |

### Visual directions — choose one baseline

| Direction | Route | Do not combine by default with |
| --- | --- | --- |
| Quiet editorial/minimal | `$minimalist-ui` | `$industrial-brutalist-ui`, high-density tactical rules |
| Swiss/industrial/brutalist | `$industrial-brutalist-ui` | `$minimalist-ui`, soft rounded SaaS defaults |
| High-agency/premium | `$design-taste-frontend` or `$high-end-visual-design` | A contradictory “quiet/minimal” baseline |
| Stitch-specific system | `$stitch-design-taste` | Unrelated token systems |

Use `$quieter`, `$bolder`, `$colorize`, `$distill`, `$make-interfaces-feel-better`, or `$uncodixfy` as modifiers/review lenses. They are not permission to discard requirements, accessibility, or an established brand.

### Imagery, motion, and content

| Need | Route |
| --- | --- |
| Image-led visual concept, moodboard, or art direction | `$image-taste-frontend`, then `$imagegen` when generation helps |
| Purposeful animation or interaction feedback | `$animate`; add `$delight` only for intentional moments |
| Plain-language copy, labels, and errors | `$user-oriented-frontend-and-design`, `$clarify` |
| Onboarding, empty states, progressive disclosure | `$onboard` |

### Hardening and delivery

| Need | Route |
| --- | --- |
| Edge cases, long text, i18n, errors, keyboard, reduced motion | `$harden` |
| Independent UX critique | `$critique` |
| Accessibility/performance/responsive audit | `$audit`, `$web-design-guidelines`, `$optimize` |
| Final visual cleanup | `$polish` |
| React/Next diagnostics | `$vercel-react-best-practices`, then `$react-doctor` after changes |
| Real browser interaction/screenshot evidence | `$agent-browser` or `$playwright` |

## Conditional setup and discovery

- `$teach-impeccable`: invoke when project design context is absent or stale. It is a project setup step, not a universal preamble.
- `$grill-me`: invoke only after the user explicitly asks for a grilling session; its own metadata disables implicit invocation.
- `$find-skills`: use only when local coverage is missing or the user asks to find/install another skill. Never install a remote skill without explicit permission.
- Native apps: route to `$mobile-ios-design`, `$mobile-android-design`, and the relevant SwiftUI/Compose skills instead of forcing web-specific CSS guidance.

## Precedence and conflict resolution

1. Explicit user brief and approved direction.
2. Existing repository design system, component library, content, and brand assets.
3. Accessibility, platform conventions, and browser standards.
4. Framework/runtime constraints and performance budgets.
5. Responsive behavior and content resilience.
6. The one selected visual direction.
7. Optional anti-generic or stylistic modifiers.

If two skills make incompatible absolute demands, keep the first applicable rule in this list and explain the trade-off. Do not average contradictory styles into a muddy result.
