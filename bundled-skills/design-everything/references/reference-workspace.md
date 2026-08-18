# Reference workspace contract

Every design/frontend task gets a project-local evidence folder:

```text
<project-root>/design-references/<feature-slug>/
├── README.md
├── brief.md
├── directions/       # A/B/C cards, rejected and approved directions
├── selected/         # approved visual references and selected generated images
├── tokens/           # semantic design-system decisions
├── screenshots/      # implementation captures by viewport/state
├── qa/               # interaction and visual verification notes
└── assets/           # project-bound copies of approved assets only
```

Create it with the bundled, non-destructive helper:

```bash
python3 ~/.codex/skills/design-everything/scripts/create_design_references.py \
  --root <project-root> \
  --slug <feature-slug> \
  --title "Human readable feature name"
```

The helper creates missing files and directories only. Preserve an existing folder, do not use a broad delete, and record revisions rather than silently replacing references.

## What to save

- `brief.md`: user/job, scope, platform matrix, content states, constraints.
- `directions/`: compact options and the decision rationale.
- `selected/`: source screenshots, approved moodboards, or generated design references. Add a source/rights note for external assets.
- `tokens/design-system.md`: palette roles, typography roles, spacing, radii, elevation, motion, component choices, and responsive invariants.
- `screenshots/`: named captures such as `orders-390x844-light.png`, `orders-1440x900-dark.png`, and important states.
- `qa/`: viewport, browser/device, input method, action path, expected/actual result, and known limitation.

## Image workflow

For image-led work, use `$image-taste-frontend` to establish image direction and `$imagegen` to create visual references when generation is appropriate. Generate only after the brief and candidate direction are understood. Inspect generated images, reject weak or generic options, and store only approved project-bound assets in `selected/` or `assets/`.

For a CSS repair, component refactor, or audit, do not invent decorative images. Still create the folder and capture the current/after UI screenshots or record why a screenshot could not be obtained.

The visual reference is a contract, not a replacement for the running UI: compare the implementation against it while preserving readable content, accessible controls, and real product behavior.
