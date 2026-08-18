---
name: teach-impeccable
description: One-time setup that gathers design context for your project and saves
  it to your AI config file. Run once to establish persistent design guidelines.
metadata:
  source_user-invocable: true
---

Gather and persist **design + operational AI context** for this project, then keep both aligned for all future sessions.

## Step 1: Explore the Codebase Deeply

Before asking questions, scan what is already knowable:

- `README`, `docs/`, runbooks, and roadmap files
- app/runtime config (`package.json`, `wrangler.jsonc`, env docs)
- iOS files (`ios/Project.yml`, `Core/UI/*`, feature screens, typography/colors)
- existing brand assets (icons, fonts, launch assets)
- current AI governance files (`agents.md`, `.impeccable.md`, `.github/copilot-instructions.md`)

Also classify the project type:
- native iOS / SwiftUI
- backend Cloudflare
- web companion or not

Capture what is clear vs unclear.

## Step 2: Ask Only Missing UX Questions

Ask only what cannot be reliably inferred.

### Users & Product Intent
- Who are the primary users?
- What core job are they trying to get done?
- What emotional tone should UX create?

### Brand & Visual Boundaries
- Brand in 3 words
- Positive references and what to emulate
- Anti-references and what to avoid

### Accessibility & Inclusion
- Required accessibility baseline and known constraints
- Reduced motion / color blindness / readability constraints

Skip any question already answered by code/docs/project history.

## Step 3: Update `.impeccable.md` (`## Design Context`)

Synthesize findings into:

```markdown
## Design Context

### Users
...

### Brand Personality
...

### Aesthetic Direction
...

### Design Principles
...
```

If the file exists, update in place; do not duplicate sections.

## Step 4: Update `agents.md` with Operational Skill Policy

Create or refresh a section that defines **mandatory skill routing**:

1. Scan globally installed skills from:
   - `~/.agents/skills`
   - `~/.codex/plugins/cache/**/skills/*`
2. Select only skills useful for this project stack.
3. Write a condition matrix in `agents.md`:
   - `condition -> mandatory skill(s)`
4. Include:
   - core mandatory skills for this project
   - per-domain triggers (SwiftUI UI, performance, networking, security, Cloudflare deploy, App Store readiness)
   - explicit exclusions (skills not to use for this project unless explicitly requested)

Rule: avoid vague statements like "use best skill"; always name exact skill identifiers.

## Step 5: Optional Sync to Copilot Instructions

Ask whether to mirror `## Design Context` (and optionally the skill policy summary) into `.github/copilot-instructions.md`.
If yes, append or update in place.

## Completion Output

When done, provide:
- files updated
- final design principles
- final "mandatory skill policy" summary used to govern future work
