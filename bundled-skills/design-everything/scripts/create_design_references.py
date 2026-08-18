#!/usr/bin/env python3
"""Create a non-destructive design reference workspace inside a project."""

from __future__ import annotations

import argparse
import re
from pathlib import Path


SLUG_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Create design-references/<slug> without overwriting existing files."
    )
    parser.add_argument("--root", required=True, help="Existing project root")
    parser.add_argument("--slug", required=True, help="Lowercase feature/page slug")
    parser.add_argument("--title", default=None, help="Human-readable title")
    return parser.parse_args()


def write_if_missing(path: Path, content: str) -> str:
    if path.exists():
        return "existing"
    path.write_text(content, encoding="utf-8")
    return "created"


def main() -> int:
    args = parse_args()
    root = Path(args.root).expanduser().resolve()
    if not root.is_dir():
        raise SystemExit(f"project root does not exist or is not a directory: {root}")
    if not SLUG_RE.fullmatch(args.slug):
        raise SystemExit("slug must use lowercase letters, digits, and single hyphens")

    title = args.title or args.slug.replace("-", " ").title()
    base = root / "design-references" / args.slug
    directories = [
        base / "directions",
        base / "selected",
        base / "tokens",
        base / "screenshots",
        base / "qa",
        base / "assets",
    ]
    for directory in directories:
        directory.mkdir(parents=True, exist_ok=True)

    files = {
        base / "README.md": f"""# {title} design references

Keep source references, approved direction, tokens, and viewport evidence for this UI here.
Do not replace an existing reference silently; record revisions in the relevant file.
""",
        base / "brief.md": """# {title} brief

- User/job: [fill]
- Primary action: [fill]
- In scope: [fill]
- Out of scope: [fill]
- Supported widths/devices: [fill]
- Accessibility/localization constraints: [fill]
""".format(title=title),
        base / "directions" / "README.md": """# Direction options

Store the compact A/B/C direction cards and mark the selected one with its date.
""",
        base / "selected" / "README.md": """# Selected references

Copy or export only approved visual references here. Record the source and usage rights in `brief.md` or a sidecar note.
""",
        base / "tokens" / "design-system.md": """# Approved design system

Record semantic colors, typography, spacing, radii, elevation, motion, and component decisions.
""",
        base / "screenshots" / "README.md": """# Screenshots

Use filenames such as `dashboard-390x844.png` and `dashboard-1440x900.png`.
""",
        base / "qa" / "README.md": """# Visual QA

Record viewport, browser/device, interaction path, result, and any known limitation.
""",
        base / "assets" / "README.md": """# Project-bound assets

Keep only assets used by the approved design. Preserve original filenames and source notes.
""",
    }
    for path, content in files.items():
        status = write_if_missing(path, content)
        print(f"{status}: {path}")

    print(f"reference workspace: {base}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
