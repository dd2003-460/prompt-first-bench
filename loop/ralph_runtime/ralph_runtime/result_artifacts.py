"""Stage-scoped result artifacts and mechanical validation helpers."""

from __future__ import annotations

import re
from pathlib import Path
from typing import Any, Mapping


def _safe_component(value: Any, fallback: str) -> str:
    text = re.sub(r"[^A-Za-z0-9._-]+", "-", str(value or "")).strip("-")
    return text or fallback


def stage_artifact_dir(root: str | Path, stage_id: Any, revision: Any) -> Path:
    """Return the canonical writable artifact directory for one stage attempt."""

    return (
        Path(root)
        / "loop-artifacts"
        / "stages"
        / _safe_component(stage_id, "unknown-stage")
        / _safe_component(revision, "r1")
    )


def state_stage_artifact_dir(root: str | Path, state: Mapping[str, Any]) -> Path:
    stage = state.get("stage", {})
    stage = stage if isinstance(stage, Mapping) else {}
    return stage_artifact_dir(root, stage.get("id"), stage.get("revision"))


def resolve_result_artifact(root: str | Path, reference: str | Path) -> Path:
    """Resolve a result reference and keep it inside loop-artifacts/stages."""

    project_root = Path(root).resolve()
    candidate = Path(reference).expanduser()
    if not candidate.is_absolute():
        candidate = project_root / candidate
    resolved = candidate.resolve()
    allowed_root = (project_root / "loop-artifacts" / "stages").resolve()
    if resolved != allowed_root and allowed_root not in resolved.parents:
        raise ValueError("result artifact 必须位于 loop-artifacts/stages/ 下")
    return resolved
