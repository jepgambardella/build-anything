#!/usr/bin/env python3
"""Bootstrap the minimal persistent project map without overwriting user files."""

from __future__ import annotations

import argparse
import re
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Bootstrap AGENTS.md and docs/project/*.md when they are missing."
    )
    parser.add_argument("--root", required=True, help="Existing project root")
    parser.add_argument(
        "--create-root",
        action="store_true",
        help="Create --root when starting a deliberately new project",
    )
    parser.add_argument("--name", required=True, help="Human-readable project name")
    return parser.parse_args()


def safe_slug(name: str) -> str:
    value = re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")
    return value or "project"


def write_if_missing(path: Path, content: str) -> str:
    if path.exists():
        return "existing"
    path.write_text(content, encoding="utf-8")
    return "created"


def main() -> int:
    args = parse_args()
    root = Path(args.root).expanduser().resolve()
    if root.exists() and not root.is_dir():
        raise SystemExit(f"error: project root is not a directory: {root}")
    if not root.exists():
        if not args.create_root:
            raise SystemExit(
                f"error: project root does not exist: {root}; "
                "use --create-root only for a deliberate new project"
            )
        root.mkdir(parents=True, exist_ok=False)
    project_dir = root / "docs" / "project"
    project_dir.mkdir(parents=True, exist_ok=True)
    slug = safe_slug(args.name)

    files = {
        root / "AGENTS.md": """# Project agent rules

Read these files before changing code:

1. `docs/project/PROJECT.md`
2. `docs/project/ARCHITECTURE.md`
3. `docs/project/STATUS.md`
4. the active items in `docs/project/ROADMAP.md`
5. `docs/project/TRACEABILITY.md` and `docs/project/DECISIONS.md` when relevant

Keep the implementation simple. Preserve unrelated work. Update status and traceability after each meaningful change. Do not mark an item done without verification evidence.
""",
        project_dir / "PROJECT.md": f"""# {args.name}

Project slug: `{slug}`
Status: discovery
Owner: [fill]
Last updated: [YYYY-MM-DD]

## Goal

[One clear sentence describing the user outcome.]

## Users and primary job

[Who uses the system and what they must complete.]

## Scope

- In scope: [fill]
- Out of scope: [fill]

## Requirements

- `REQ-001` — [testable requirement]

## Constraints

- Platform/runtime: [fill]
- Security/privacy: [fill]
- Performance/reliability: [fill]
- Localization/accessibility: [fill]

## Source of truth

Architecture: `ARCHITECTURE.md`
Work order: `ROADMAP.md`
Current state: `STATUS.md`
Requirement evidence: `TRACEABILITY.md`
Decisions: `DECISIONS.md`
""",
        project_dir / "ARCHITECTURE.md": f"""# {args.name} architecture

## System boundary

[What this project owns. What it does not own.]

## Runtime topology

```text
[client] -> [API/service] -> [storage/external systems]
```

## Modules and ownership

| Module | Responsibility | Depends on | Evidence |
| --- | --- | --- | --- |
| [name] | [one responsibility] | [name] | [path/test] |

## Data and contracts

- Source of truth: [fill]
- Main entities: [fill]
- API/events: [fill]
- Validation/auth/idempotency: [fill]
- Migration/retention policy: [fill]

## Delivery and operations

- Build: [command]
- Deploy: [command or provider]
- Health/metrics/logs: [fill]
- Recovery path: [fill]

## Architecture rules

- [short rule]
""",
        project_dir / "ROADMAP.md": f"""# {args.name} roadmap

Legend: `[ ] planned` · `[~] in progress` · `[x] done` · `[!] blocked` · `[-] deferred`

## Order

- [ ] `REQ-001` — [first deliverable]
- [ ] `REQ-002` — [second deliverable]

## Dependency notes

- [Item] depends on [item] because [reason].

Keep items short. Link each item to `TRACEABILITY.md` and the relevant section of `ARCHITECTURE.md`.
""",
        project_dir / "STATUS.md": f"""# {args.name} status

Last updated: [YYYY-MM-DD HH:MM timezone]
Phase: discovery
Branch/commit: [fill]

## Done

- [none yet]

## Current

- [one active item]

## Next

- [one smallest next action]

## Blockers

- None.

## Verification

- Command: [not run]
- Result: [not run]

## Context note

Write enough exact path/command/version detail for a new agent to continue without chat history.
""",
        project_dir / "TRACEABILITY.md": f"""# {args.name} traceability

Keep one row per requirement. Replace placeholders with exact paths, commands, screenshots, or release evidence.

| ID | Requirement | Design/architecture | Implementation | Verification | Status |
| --- | --- | --- | --- | --- | --- |
| `REQ-001` | [testable statement] | [section/path] | [file/module] | [command/evidence] | planned |
""",
        project_dir / "DECISIONS.md": f"""# {args.name} decisions

Record only decisions that affect future work. Do not turn this into a diary.

## DEC-001 — [decision title]

- Date: [YYYY-MM-DD]
- Status: proposed | accepted | superseded
- Decision: [one clear sentence]
- Why: [constraint or evidence]
- Rejected: [alternative and reason]
- Consequence: [what future work must follow]
""",
    }

    for path, content in files.items():
        status = write_if_missing(path, content)
        if status == "existing":
            print(f"existing (read and update manually): {path}")
        else:
            print(f"{status}: {path}")
    print(f"project map: {project_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
