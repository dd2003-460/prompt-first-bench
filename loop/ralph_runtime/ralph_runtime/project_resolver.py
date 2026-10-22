"""Resolve a task to an existing workspace project or a new project path.

The resolver is intentionally deterministic and conservative.  It only
considers directories under ``<workspace>/projects`` that contain a RALPH or
legacy project marker, and it creates a new project when there is no clear
match instead of silently attaching a task to an unrelated project.
"""

from __future__ import annotations

import hashlib
import json
import os
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


IGNORED_DIRS = {
    ".git",
    ".hg",
    ".svn",
    ".venv",
    "__pycache__",
    "node_modules",
    "loop-artifacts",
}

PROJECT_FILES = (
    "loop-state.json",
    ".claude/ralph-loop.local.md",
    "tasks/TASKS.md",
    "loop/INDEX.md",
    "project.json",
    "CLAUDE.md",
)

COMMON_TERMS = {
    "a",
    "an",
    "and",
    "best",
    "find",
    "for",
    "help",
    "highest",
    "how",
    "i",
    "me",
    "need",
    "please",
    "research",
    "the",
    "to",
    "what",
    "with",
    "的",
    "了",
    "帮我",
    "需要",
    "调研",
    "最高",
    "性价比",
    "我需要",
    "请",
}

TERM_ALIASES = {
    "gpu": ("显卡", "图形卡", "hardware", "cuda", "nvidia", "amd"),
    "ai": ("人工智能", "agent", "llm", "模型"),
}


@dataclass(frozen=True)
class ProjectCandidate:
    root: Path
    score: int
    matched_terms: tuple[str, ...]
    has_state: bool
    has_legacy_state: bool


@dataclass(frozen=True)
class ProjectResolution:
    workspace: Path
    project: Path
    created: bool
    reason: str
    candidates: tuple[ProjectCandidate, ...] = ()


def _is_workspace(path: Path) -> bool:
    return (
        (path / "projects").is_dir()
        and (
            (path / "AGENTS.md").exists()
            or (path / "CLAUDE.md").exists()
            or (path / "agents-templates" / "RALPH-project" / "CLAUDE.md").exists()
        )
    )


def detect_workspace_root(start: str | Path | None = None, fallback: str | Path | None = None) -> Path:
    """Find the workspace that owns the current invocation.

    ``RALPH_WORKSPACE`` is an explicit override.  Otherwise the current
    directory and its parents are searched.  The source workspace is used as
    a fallback for the installed editable runtime, which lets a user invoke
    ``ralph run \"task\"`` from ``$HOME`` without losing the workspace root.
    """

    configured = os.environ.get("RALPH_WORKSPACE")
    if configured:
        configured_path = Path(configured).expanduser().resolve()
        if configured_path.exists() and configured_path.is_dir():
            return configured_path
        raise OSError(f"RALPH_WORKSPACE does not point to a directory: {configured_path}")

    current = Path(start or Path.cwd()).expanduser().resolve()
    for candidate in (current, *current.parents):
        if _is_workspace(candidate):
            return candidate

    if fallback is not None:
        fallback_path = Path(fallback).expanduser().resolve()
        if fallback_path.exists() and fallback_path.is_dir():
            return fallback_path
    return current


def _is_project_root(path: Path) -> bool:
    return any((path / marker).exists() for marker in PROJECT_FILES)


def iter_project_roots(workspace: str | Path) -> Iterable[Path]:
    """Yield marked projects below ``workspace/projects`` in stable order."""

    projects_root = Path(workspace).expanduser().resolve() / "projects"
    if not projects_root.is_dir():
        return

    for directory, subdirectories, _ in os.walk(projects_root):
        current = Path(directory)
        relative_parts = current.relative_to(projects_root).parts
        if len(relative_parts) > 4:
            subdirectories[:] = []
            continue
        subdirectories[:] = sorted(name for name in subdirectories if name not in IGNORED_DIRS)
        if relative_parts and _is_project_root(current):
            yield current


def _read_corpus(root: Path) -> tuple[str, str]:
    """Return searchable project text and the previous task description."""

    pieces = [root.name, str(root)]
    previous_task = ""
    for relative in PROJECT_FILES:
        path = root / relative
        if not path.is_file():
            continue
        try:
            text = path.read_text(encoding="utf-8", errors="ignore")[:32_000]
        except OSError:
            continue
        pieces.append(text)
        if relative == "loop-state.json":
            try:
                value = json.loads(text)
                task = value.get("task", {}) if isinstance(value, dict) else {}
                if isinstance(task, dict) and isinstance(task.get("description"), str):
                    previous_task = task["description"]
            except (json.JSONDecodeError, TypeError):
                pass
    return "\n".join(pieces).lower(), previous_task.lower()


def _terms(text: str) -> tuple[str, ...]:
    lowered = text.lower()
    terms: list[str] = []
    for token in re.findall(r"(?<![a-z0-9])[a-z][a-z0-9+._-]*", lowered):
        if token not in COMMON_TERMS and len(token) >= 2:
            terms.append(token)
    for run in re.findall(r"[\u4e00-\u9fff]{2,4}", lowered):
        if run not in COMMON_TERMS and len(run) <= 3:
            terms.append(run)
    return tuple(dict.fromkeys(terms))


def _count_term(text: str, term: str) -> int:
    if re.fullmatch(r"[a-z0-9+._-]+", term):
        return len(re.findall(rf"(?<![a-z0-9]){re.escape(term)}(?![a-z0-9])", text))
    return text.count(term)


def rank_projects(task: str, workspace: str | Path) -> tuple[ProjectCandidate, ...]:
    """Rank marked projects by task overlap without making a selection."""

    task_terms = _terms(task)
    ranked: list[ProjectCandidate] = []
    for root in iter_project_roots(workspace):
        corpus, previous_task = _read_corpus(root)
        path_text = root.name.lower()
        score = 0
        matched: list[str] = []
        for term in task_terms:
            path_hits = _count_term(path_text, term)
            path_hits += sum(_count_term(path_text, alias) for alias in TERM_ALIASES.get(term, ()))
            body_hits = min(_count_term(corpus, term), 5)
            if path_hits or body_hits:
                matched.append(term)
                score += path_hits * 8 + body_hits * 2
        if previous_task and any(term in previous_task for term in task_terms):
            score += 12
        if previous_task and previous_task.strip() == task.strip().lower():
            score += 24
        ranked.append(
            ProjectCandidate(
                root=root,
                score=score,
                matched_terms=tuple(matched),
                has_state=(root / "loop-state.json").exists(),
                has_legacy_state=(root / ".claude" / "ralph-loop.local.md").exists(),
            )
        )
    return tuple(sorted(ranked, key=lambda item: (-item.score, str(item.root))))


def _slug_for_task(task: str) -> str:
    lowered = task.lower()
    canonical: list[str] = []
    aliases = (
        (("gpu", "显卡", "图形卡", "cuda"), "gpu"),
        (("本地ai", "local ai", "人工智能"), "local-ai"),
        (("本地",), "local"),
        (("调研", "研究", "research"), "research"),
    )
    for needles, value in aliases:
        if any(needle in lowered for needle in needles):
            canonical.append(value)
    for token in _terms(task):
        if re.fullmatch(r"[a-z][a-z0-9-]{2,}", token) and token not in COMMON_TERMS:
            canonical.append(token)
    if not canonical:
        canonical.append("task")
    unique = list(dict.fromkeys(canonical))[:5]
    digest = hashlib.sha256(task.strip().encode("utf-8")).hexdigest()[:8]
    return re.sub(r"[^a-z0-9-]+", "-", "D1-" + "-".join(unique) + "-" + digest).strip("-")


def resolve_project(
    task: str,
    start: str | Path | None = None,
    fallback_workspace: str | Path | None = None,
) -> ProjectResolution:
    """Resolve a task to a current project or a deterministic new path."""

    workspace = detect_workspace_root(start=start, fallback=fallback_workspace)
    current = Path(start or Path.cwd()).expanduser().resolve()

    if current != workspace and _is_project_root(current):
        return ProjectResolution(workspace, current, False, "当前目录已经是一个 RALPH 项目")

    candidates = rank_projects(task, workspace)
    if candidates:
        top = candidates[0]
        second_score = candidates[1].score if len(candidates) > 1 else 0
        if top.score >= 8 and top.score - second_score >= 3:
            state_kind = "loop-state.json" if top.has_state else "旧版 loop 状态"
            return ProjectResolution(
                workspace,
                top.root,
                False,
                f"匹配到已有项目（{state_kind}；关键词: {', '.join(top.matched_terms[:6])}）",
                candidates,
            )

    project = workspace / "projects" / _slug_for_task(task)
    return ProjectResolution(
        workspace,
        project,
        True,
        "没有足够明确的已有项目匹配，将在 workspace/projects 下创建新项目",
        candidates,
    )
