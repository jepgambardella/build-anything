#!/usr/bin/env python3
"""Validate the self-contained Build Anything skill bundle."""

from __future__ import annotations

import argparse
from pathlib import Path
import re


BASELINE = {
    "grill-me",
    "unlazy",
    "ponytail",
    "design-everything",
    "frontend-design",
    "css-for-perfect-frontend",
    "adapt",
    "ui-component-patterns",
    "find-skills",
    "skill-installer",
}
FORBIDDEN_PATTERNS = (
    re.compile(r"/Users/[^/\s]+/\.codex/"),
    re.compile(r"gho_"),
    re.compile(r"github_pat_"),
    re.compile(r"BEGIN PRIVATE KEY"),
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--root",
        default=Path(__file__).resolve().parents[1],
        type=Path,
        help="Build Anything skill directory",
    )
    return parser.parse_args()


def main() -> int:
    root = parse_args().root.expanduser().resolve()
    bundle = root / "bundled-skills"
    if not (root / "SKILL.md").is_file():
        raise SystemExit(f"missing root SKILL.md: {root}")
    if not bundle.is_dir():
        raise SystemExit(f"missing bundled-skills directory: {bundle}")

    skill_dirs = sorted(path for path in bundle.iterdir() if path.is_dir())
    names = {path.name for path in skill_dirs}
    missing = sorted(BASELINE - names)
    if missing:
        raise SystemExit(f"missing mandatory bundled skills: {', '.join(missing)}")

    missing_entrypoints = sorted(
        path.name for path in skill_dirs if not (path / "SKILL.md").is_file()
    )
    if missing_entrypoints:
        raise SystemExit(
            "bundled directories without SKILL.md: " + ", ".join(missing_entrypoints)
        )

    scanned_files = [root / "SKILL.md"]
    for skill_dir in skill_dirs:
        scanned_files.extend(skill_dir.rglob("*"))
    for path in scanned_files:
        if not path.is_file() or path.suffix in {".pyc", ".DS_Store"}:
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        for pattern in FORBIDDEN_PATTERNS:
            if pattern.search(text):
                raise SystemExit(
                    f"forbidden local/secrets marker {pattern.pattern!r}: {path}"
                )

    print(f"bundle valid: {len(skill_dirs)} skills")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
