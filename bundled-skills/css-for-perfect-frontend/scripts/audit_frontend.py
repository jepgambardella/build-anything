#!/usr/bin/env python3
"""Small dependency-free static heuristic audit for frontend layout risks.

This is a triage tool, not a CSS parser or accessibility validator. It reports
file/line evidence and deliberately uses warnings instead of pretending that a
pattern is always wrong. Run it from a repository root or pass file paths.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter
from dataclasses import asdict, dataclass
from pathlib import Path


EXTENSIONS = {".css", ".scss", ".sass", ".less", ".html", ".jsx", ".tsx", ".vue", ".svelte"}
SKIP_PARTS = {".git", "node_modules", "dist", "build", ".next", "coverage", "vendor"}
MAX_BYTES = 1_500_000


@dataclass(frozen=True)
class Finding:
    severity: str
    rule: str
    path: str
    line: int | None
    message: str


def files_for(paths: list[str]) -> list[Path]:
    found: set[Path] = set()
    for raw in paths:
        path = Path(raw).resolve()
        candidates = path.rglob("*") if path.is_dir() else [path]
        for candidate in candidates:
            if not candidate.is_file() or candidate.suffix.lower() not in EXTENSIONS:
                continue
            if any(part in SKIP_PARTS for part in candidate.parts):
                continue
            try:
                if candidate.stat().st_size <= MAX_BYTES:
                    found.add(candidate)
            except OSError:
                continue
    return sorted(found)


def line_number(text: str, offset: int) -> int:
    return text.count("\n", 0, offset) + 1


def add_matches(findings: list[Finding], path: Path, text: str, pattern: str,
                severity: str, rule: str, message: str, flags: int = re.I) -> None:
    for match in re.finditer(pattern, text, flags):
        findings.append(Finding(severity, rule, str(path), line_number(text, match.start()), message))


def audit(path_list: list[str]) -> list[Finding]:
    files = files_for(path_list)
    findings: list[Finding] = []
    css_files: list[tuple[Path, str]] = []
    all_text: list[str] = []

    for path in files:
        try:
            text = path.read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError):
            continue
        all_text.append(text)
        if path.suffix.lower() in {".css", ".scss", ".sass", ".less"}:
            css_files.append((path, text))

        add_matches(
            findings, path, text, r"(?<![\w-])(?:height|min-height|block-size|min-block-size)\s*:\s*100vh\b",
            "high", "viewport-height", "Rigid 100vh sizing can be wrong with mobile browser chrome; review whether 100dvh/100svh or min-height is the intended contract.",
        )
        add_matches(
            findings, path, text, r"\boverflow(?:-[xy])?\s*:\s*hidden\b",
            "medium", "hidden-overflow", "Hidden overflow can mask a layout defect or clip focus/content; confirm that clipping is intentional and scoped.",
        )
        add_matches(
            findings, path, text, r"\bword-break\s*:\s*break-all\b",
            "high", "break-all", "break-all can make ordinary copy unreadable; prefer normal wrapping or overflow-wrap for long tokens.",
        )
        add_matches(
            findings, path, text, r"\btransition\s*:\s*all\b",
            "medium", "transition-all", "transition: all can animate layout and unexpected properties; enumerate cheap, intentional properties.",
        )
        add_matches(
            findings, path, text, r"\bz-index\s*:\s*(?:9{2,}|[1-9]\d{3,})\b",
            "medium", "arbitrary-z-index", "Very large z-index suggests stacking-context escalation; use a semantic scale and inspect the containing stacking context.",
        )
        add_matches(
            findings, path, text, r"\b(?:width|inline-size|min-width|min-inline-size)\s*:\s*\d{3,}px\b",
            "medium", "rigid-width", "Large fixed width may fail at narrow viewports; verify the component's intrinsic and responsive behavior.",
        )
        add_matches(
            findings, path, text, r"<br\s*/?>",
            "low", "manual-line-break", "Manual line breaks can make one viewport look right while breaking responsive or localized copy; verify that the break is semantic.",
        )
        add_matches(
            findings, path, text, r"\bwhite-space\s*:\s*nowrap\b",
            "medium", "nowrap", "nowrap can overflow labels, translated copy, and controls; confirm the content has a deliberate truncation or scroll strategy.",
        )
        add_matches(
            findings, path, text, r"\b(?:top|left|right|bottom)\s*:\s*\d{2,}px\b",
            "low", "hard-coded-position", "Hard-coded overlay coordinates can detach a menu or tooltip from its trigger after scroll or near viewport edges; inspect the positioning contract.",
        )
        add_matches(
            findings, path, text, r"\buser-select\s*:\s*none\b",
            "medium", "user-select-none", "user-select: none can block copying and text selection; scope it to non-text controls and verify touch behavior.",
        )
        add_matches(
            findings, path, text, r"\bcalc\(\s*\d+%\s*[-+]\s*[^)]*\)\b",
            "low", "percentage-math", "Percentage math often becomes brittle as gaps and content change; consider Grid minmax() or flex gap.",
        )
        add_matches(
            findings, path, text, r"!important\b",
            "low", "important", "!important may indicate specificity debt; verify whether a layer, scope, or token can express the intended precedence.",
        )

    combined = "\n".join(all_text)
    combined_css = "\n".join(text for _, text in css_files)

    html_files = [path for path in files if path.suffix.lower() in {".html", ".jsx", ".tsx", ".vue", ".svelte"}]
    if html_files and not re.search(r"<meta[^>]+name=[\"']viewport[\"']", combined, re.I):
        findings.append(Finding("high", "viewport-meta", "<markup-set>", None, "No viewport meta tag found; verify mobile layout is not rendered in a virtual desktop viewport."))
    if re.search(r"<div[^>]+(?:onclick|onkeydown|onkeyup|onkeypress)=|<span[^>]+(?:onclick|onkeydown|onkeyup|onkeypress)=", combined, re.I):
        findings.append(Finding("high", "nonsemantic-interactive", "<markup-set>", None, "A div/span appears to own an inline interaction; verify semantic button/link behavior, keyboard support, and accessible naming."))
    if re.search(r"<(?:div|span)\b[^>]*\b(?:role=[\"'](?:button|link|menuitem)|tabindex=)", combined, re.I):
        findings.append(Finding("medium", "custom-interactive", "<markup-set>", None, "A div/span appears to emulate an interactive element; prefer a native button/link or verify the complete keyboard, name, role, and state contract."))
    if re.search(r"<(?:button|a|input|select|textarea)\b", combined, re.I) and not re.search(r"aria-label=|<label\b|aria-labelledby=|>\s*[^<]+\s*</(?:button|a)>", combined, re.I):
        findings.append(Finding("medium", "accessible-name", "<markup-set>", None, "Interactive markup has no obvious accessible-name evidence; verify labels, visible text, or aria-labelledby/aria-label per control."))

    if css_files and not re.search(r"box-sizing\s*:\s*border-box", combined_css, re.I):
        findings.append(Finding("medium", "box-sizing", "<stylesheet-set>", None, "No border-box sizing rule found; inspect the reset and component library before adding one."))
    if css_files and not re.search(r"\@media\b|\@container\b", combined_css, re.I):
        findings.append(Finding("high", "responsive-rules", "<stylesheet-set>", None, "No media or container query found; verify that the UI still adapts to narrow and intermediate containers."))
    if css_files and not re.search(r":focus-visible\b|:focus\b", combined_css, re.I):
        findings.append(Finding("high", "focus-state", "<stylesheet-set>", None, "No focus or focus-visible styling found; keyboard users may not see the active control."))
    if css_files and re.search(r"\b(?:animation|transition)\s*:", combined_css, re.I) and not re.search(r"prefers-reduced-motion", combined_css, re.I):
        findings.append(Finding("medium", "reduced-motion", "<stylesheet-set>", None, "Motion is present without a reduced-motion branch; verify the project's motion accessibility policy."))
    if re.search(r"\b(?:table|<table\b)", combined, re.I) and not re.search(r"overflow-x\s*:\s*auto|overflow-inline\s*:\s*auto", combined_css, re.I):
        findings.append(Finding("medium", "table-overflow", "<stylesheet-set>", None, "A table was found without an obvious horizontal scroll wrapper; verify dense data at narrow widths."))
    if re.search(r"\b(?:input|select|textarea)\b", combined, re.I) and not re.search(r"(?:input|select|textarea)[^{]*\{[^}]*font-size\s*:", combined_css, re.I | re.S):
        findings.append(Finding("low", "form-font-size", "<stylesheet-set>", None, "Form controls have no obvious CSS font-size rule; check mobile browser zoom and the project's control primitives."))

    colors = Counter(re.findall(r"#[0-9a-f]{3,8}\b", combined_css, re.I))
    repeated = [value for value, count in colors.items() if count >= 8]
    if len(repeated) >= 4:
        findings.append(Finding("low", "color-tokens", "<stylesheet-set>", None, "Many repeated raw color literals were found; inspect whether semantic design tokens would reduce drift."))

    return sorted(findings, key=lambda item: (item.path, item.line or 0, item.rule))


def main() -> int:
    parser = argparse.ArgumentParser(description="Heuristic frontend CSS/layout audit")
    parser.add_argument("paths", nargs="*", default=["."], help="files or directories to inspect")
    parser.add_argument("--json", action="store_true", help="emit machine-readable JSON")
    args = parser.parse_args()
    findings = audit(args.paths)
    if args.json:
        print(json.dumps([asdict(item) for item in findings], indent=2))
    else:
        if not findings:
            print("PASS: no heuristic findings. Still run browser, keyboard, and visual checks.")
        else:
            print(f"{len(findings)} heuristic finding(s):")
            for item in findings:
                location = item.path if item.line is None else f"{item.path}:{item.line}"
                print(f"[{item.severity.upper()}] {item.rule} {location}\n  {item.message}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
