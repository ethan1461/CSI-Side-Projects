"""Lint the CSI business brain.

Checks that the shared knowledge every agent depends on is wired up, current, and free
of facts the team has already corrected. Run from the repo root:

    python3 scripts/brain_lint.py            # human-readable report, exit 1 on errors
    python3 scripts/brain_lint.py --json     # machine-readable

Errors (exit 1):
  - a brain file without `as_of` in its frontmatter
  - an agent that is not wired to the brain (no index reference, or no Skill tool)
  - a known-stale phrase in live context (CLAUDE.md, agents, brain, skills)
Warnings (exit 0):
  - a brain file older than STALE_DAYS
  - a backtick path reference to something that does not exist yet
  - too many open proposals, or unmerged Project exports in the inbox

Stdlib only, so it runs anywhere the agents run.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass, field
from datetime import date
from pathlib import Path

STALE_DAYS = 60
MAX_OPEN_PROPOSALS = 10
BRAIN_INDEX = "context/brain/00-INDEX.md"

# Facts the team has corrected. Each entry: (regex, why it is wrong).
STALE_PATTERNS: list[tuple[str, str]] = [
    (r"\bfive[- ]gateways?\b", "CSI has 8 gateways (context/brain/company-facts.md)"),
    (r"\bfive U\.S\. gateways\b", "CSI has 8 gateways (context/brain/company-facts.md)"),
    (
        r"MIA,\s*JFK,\s*IAD,\s*IAH,\s*LAX(?![^\n]*\b(?:BOS|DFW|SFO)\b)",
        "5-gateway list; canonical list is JFK, IAD, MIA, BOS, DFW, IAH, LAX, SFO",
    ),
    (r"1,056\s*(?:→|->|to)\s*(?:Mar[^\n]*)?Jun[^\n]*904", "volume-decline framing disproved (CLAUDE.md §2)"),
    (r"[Cc]ustoms clearance for international inbound", "physical handling is export-only"),
]

# Where stale phrases matter. History (archive, reports, data) is allowed to be old.
LIVE_GLOBS = [
    "CLAUDE.md",
    ".claude/agents/*.md",
    ".claude/commands/*.md",
    ".claude/skills/**/*.md",
    "context/brain/**/*.md",
]
# Files allowed to *mention* stale phrases because they document the correction.
STALE_PHRASE_EXEMPT = {"scripts/brain_lint.py", "context/brain/changelog.md"}

# A line that names a stale fact in order to correct it is not itself stale.
CORRECTION_MARKERS = re.compile(r"disprov|contradict|earlier versions|not declining|stale|archived|do not cite", re.I)

# Gitignored by design (CLAUDE.md §7.2): present on Ethan's machine, never in a clone.
IGNORED_REF_PREFIXES = ("data/raw/",)

REF_RE = re.compile(r"`((?:context|reports|data|scripts|templates|\.claude)/[^`\s*<>]+)`")


@dataclass
class Report:
    errors: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)
    info: list[str] = field(default_factory=list)

    @property
    def ok(self) -> bool:
        return not self.errors


def frontmatter(text: str) -> dict[str, str]:
    """Return simple `key: value` pairs from a leading YAML frontmatter block."""
    if not text.startswith("---\n"):
        return {}
    end = text.find("\n---", 4)
    if end == -1:
        return {}
    out: dict[str, str] = {}
    for line in text[4:end].splitlines():
        if ":" in line and not line.startswith(" "):
            key, _, value = line.partition(":")
            out[key.strip()] = value.strip()
    return out


def brain_files(root: Path) -> list[Path]:
    brain = root / "context" / "brain"
    return sorted(
        p
        for p in brain.rglob("*.md")
        if "_proposals" not in p.parts and "_inbox" not in p.parts
    )


def check_brain_dates(root: Path, today: date, report: Report) -> None:
    for path in brain_files(root):
        rel = path.relative_to(root).as_posix()
        if rel == "context/brain/changelog.md":
            continue  # a log, dated per line
        as_of = frontmatter(path.read_text(encoding="utf-8")).get("as_of")
        if not as_of:
            report.errors.append(f"{rel}: no `as_of` in frontmatter")
            continue
        try:
            age = (today - date.fromisoformat(as_of)).days
        except ValueError:
            report.errors.append(f"{rel}: `as_of` is not YYYY-MM-DD ({as_of!r})")
            continue
        if age > STALE_DAYS:
            report.warnings.append(f"{rel}: as_of {as_of} is {age} days old — re-confirm or move to open-questions")


def check_agents(root: Path, report: Report) -> None:
    agents = sorted((root / ".claude" / "agents").glob("*.md"))
    if not agents:
        report.errors.append(".claude/agents/: no agent files found")
    for path in agents:
        rel = path.relative_to(root).as_posix()
        text = path.read_text(encoding="utf-8")
        fm = frontmatter(text)
        if not fm.get("name"):
            report.errors.append(f"{rel}: frontmatter has no `name`")
        tools = [t.strip() for t in fm.get("tools", "").split(",") if t.strip()]
        if tools and "Skill" not in tools:
            report.errors.append(f"{rel}: `tools` allowlist lacks Skill — this agent cannot use .claude/skills/")
        if BRAIN_INDEX not in text:
            report.errors.append(f"{rel}: never points to {BRAIN_INDEX}")
    report.info.append(f"agents checked: {len(agents)}")


def live_files(root: Path) -> list[Path]:
    seen: set[Path] = set()
    for pattern in LIVE_GLOBS:
        seen.update(p for p in root.glob(pattern) if p.is_file())
    return sorted(seen)


def check_stale_phrases(root: Path, report: Report) -> None:
    compiled = [(re.compile(rx), why) for rx, why in STALE_PATTERNS]
    for path in live_files(root):
        rel = path.relative_to(root).as_posix()
        if rel in STALE_PHRASE_EXEMPT:
            continue
        for lineno, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            if CORRECTION_MARKERS.search(line):
                continue
            for rx, why in compiled:
                if rx.search(line):
                    report.errors.append(f"{rel}:{lineno}: stale fact — {why}")


def check_references(root: Path, report: Report) -> None:
    for path in live_files(root):
        rel = path.relative_to(root).as_posix()
        for target in sorted(set(REF_RE.findall(path.read_text(encoding="utf-8")))):
            target = target.rstrip(".,;:)")
            if "YYYY" in target or "<" in target or "{" in target:
                continue  # a naming pattern, not a path
            if target.startswith(IGNORED_REF_PREFIXES):
                continue
            if not (root / target).exists():
                report.warnings.append(f"{rel}: references `{target}`, which does not exist yet")


def check_queues(root: Path, report: Report) -> None:
    brain = root / "context" / "brain"
    proposals = [p for p in (brain / "_proposals").glob("*.md") if p.name != "TEMPLATE.md"]
    inbox = [p for p in (brain / "_inbox").glob("*") if p.name != ".gitkeep"]
    report.info.append(f"open proposals: {len(proposals)}; unmerged inbox files: {len(inbox)}")
    if len(proposals) > MAX_OPEN_PROPOSALS:
        report.warnings.append(f"{len(proposals)} open proposals — the Monday review is not keeping up")
    if inbox:
        report.warnings.append(
            f"{len(inbox)} unmerged Project export(s) in _inbox — agents are working from an older company; run /brain-merge"
        )


def lint(root: Path, today: date | None = None) -> Report:
    report = Report()
    today = today or date.today()
    if not (root / BRAIN_INDEX).exists():
        report.errors.append(f"{BRAIN_INDEX} is missing")
        return report
    check_brain_dates(root, today, report)
    check_agents(root, report)
    check_stale_phrases(root, report)
    check_references(root, report)
    check_queues(root, report)
    return report


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parent.parent)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args(argv)

    report = lint(args.root)
    if args.json:
        print(json.dumps({"ok": report.ok, **report.__dict__}, indent=2))
    else:
        for label, items in (("ERROR", report.errors), ("WARN", report.warnings), ("INFO", report.info)):
            for item in items:
                print(f"{label:5} {item}")
        print("brain lint:", "PASS" if report.ok else f"FAIL ({len(report.errors)} error(s))")
    return 0 if report.ok else 1


if __name__ == "__main__":
    sys.exit(main())
