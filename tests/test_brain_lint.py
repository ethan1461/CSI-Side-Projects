"""Tests for scripts/brain_lint.py. Run: python3 -m pytest tests/"""
from __future__ import annotations

import importlib.util
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
_spec = importlib.util.spec_from_file_location("brain_lint", ROOT / "scripts" / "brain_lint.py")
brain_lint = importlib.util.module_from_spec(_spec)
assert _spec.loader is not None
sys.modules["brain_lint"] = brain_lint  # dataclasses resolve types via sys.modules
_spec.loader.exec_module(brain_lint)

TODAY = date(2026, 11, 1)
GOOD_AGENT = (
    "---\nname: sales-lead\ntools: Read, Write, Skill\nmodel: sonnet\n---\n\n"
    "Read `context/brain/00-INDEX.md` first.\n"
)


def make_repo(tmp_path: Path, *, agent: str = GOOD_AGENT, facts_as_of: str = "2026-10-30") -> Path:
    brain = tmp_path / "context" / "brain"
    (brain / "_proposals").mkdir(parents=True)
    (brain / "_inbox").mkdir()
    (brain / "_inbox" / ".gitkeep").write_text("")
    (brain / "00-INDEX.md").write_text("---\nas_of: 2026-11-01\n---\n# Index\n")
    (brain / "company-facts.md").write_text(f"---\nas_of: {facts_as_of}\n---\n8 gateways.\n")
    (brain / "changelog.md").write_text("---\ntitle: log\n---\n- five gateways was wrong\n")
    agents = tmp_path / ".claude" / "agents"
    agents.mkdir(parents=True)
    (agents / "sales.md").write_text(agent)
    (tmp_path / "CLAUDE.md").write_text("# Rules\n")
    return tmp_path


def test_clean_repo_passes(tmp_path):
    report = brain_lint.lint(make_repo(tmp_path), TODAY)
    assert report.ok, report.errors
    assert not report.warnings


def test_agent_without_skill_tool_fails(tmp_path):
    agent = GOOD_AGENT.replace(", Skill", "")
    report = brain_lint.lint(make_repo(tmp_path, agent=agent), TODAY)
    assert any("lacks Skill" in e for e in report.errors)


def test_agent_not_pointing_at_brain_fails(tmp_path):
    agent = GOOD_AGENT.replace("context/brain/00-INDEX.md", "CLAUDE.md")
    report = brain_lint.lint(make_repo(tmp_path, agent=agent), TODAY)
    assert any("never points to" in e for e in report.errors)


def test_stale_gateway_phrase_fails_but_changelog_is_exempt(tmp_path):
    root = make_repo(tmp_path)
    (root / "CLAUDE.md").write_text("Gateways: MIA, JFK, IAD, IAH, LAX.\nfive-gateway routing\n")
    report = brain_lint.lint(root, TODAY)
    hits = [e for e in report.errors if "stale fact" in e]
    assert len(hits) == 2
    assert all(e.startswith("CLAUDE.md:") for e in hits)


def test_full_gateway_list_is_not_flagged(tmp_path):
    root = make_repo(tmp_path)
    (root / "CLAUDE.md").write_text("MIA, JFK, IAD, IAH, LAX, BOS, DFW, SFO\n")
    assert brain_lint.lint(root, TODAY).ok


def test_old_brain_file_warns(tmp_path):
    report = brain_lint.lint(make_repo(tmp_path, facts_as_of="2026-07-01"), TODAY)
    assert report.ok
    assert any("days old" in w for w in report.warnings)


def test_missing_as_of_fails(tmp_path):
    root = make_repo(tmp_path)
    (root / "context" / "brain" / "company-facts.md").write_text("# no frontmatter\n")
    report = brain_lint.lint(root, TODAY)
    assert any("no `as_of`" in e for e in report.errors)


def test_unmerged_inbox_warns(tmp_path):
    root = make_repo(tmp_path)
    (root / "context" / "brain" / "_inbox" / "2026-11-01-project-export.md").write_text("x")
    report = brain_lint.lint(root, TODAY)
    assert any("unmerged Project export" in w for w in report.warnings)


def test_missing_reference_warns_and_patterns_are_skipped(tmp_path):
    root = make_repo(tmp_path)
    (root / "CLAUDE.md").write_text("See `context/missing.md` and `reports/weekly/YYYY-WW-plan.md`.\n")
    report = brain_lint.lint(root, TODAY)
    refs = [w for w in report.warnings if "does not exist yet" in w]
    assert len(refs) == 1 and "context/missing.md" in refs[0]


def test_line_documenting_a_correction_is_not_flagged(tmp_path):
    root = make_repo(tmp_path)
    (root / "CLAUDE.md").write_text("The five-gateway list in older decks is stale; we have eight.\n")
    assert brain_lint.lint(root, TODAY).ok


def test_gitignored_raw_data_reference_is_not_a_warning(tmp_path):
    root = make_repo(tmp_path)
    (root / "CLAUDE.md").write_text("Source: `data/raw/export.csv`\n")
    assert not brain_lint.lint(root, TODAY).warnings
