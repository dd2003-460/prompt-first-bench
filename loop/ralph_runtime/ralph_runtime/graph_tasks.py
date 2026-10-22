"""Materialize validated execution-DAG nodes as small incremental task files."""

from __future__ import annotations

import json
import os
import re
import tempfile
from contextlib import contextmanager
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Mapping

from .dag import validate_plan
from .result_artifacts import state_stage_artifact_dir


def _resolve_artifacts_root(root: str | Path) -> Path:
    """Return the real loop-artifacts root, handling sibling layout."""
    candidate = (Path(root).resolve() / "loop-artifacts").resolve()
    if candidate.is_dir():
        return candidate
    sibling = Path(root).resolve().parent / "loop-artifacts"
    if sibling.is_dir():
        return sibling.resolve()
    return candidate  # let callers fail with a natural error


def sibling_artifact_dir(root: Path) -> Path:
    """Return the sibling loop-artifacts root (workspace root)."""
    return (root.parent / "loop-artifacts").resolve()


@contextmanager
def _graph_apply_lock(root: str | Path):
    artifacts_root = _resolve_artifacts_root(root)
    lock_path = artifacts_root / ".graph-apply.lock"
    lock_path.parent.mkdir(parents=True, exist_ok=True)
    handle = lock_path.open("a+", encoding="utf-8")
    try:
        try:
            import fcntl
            fcntl.flock(handle.fileno(), fcntl.LOCK_EX)
        except (ImportError, OSError):
            pass
        yield
    finally:
        try:
            import fcntl
            fcntl.flock(handle.fileno(), fcntl.LOCK_UN)
        except (ImportError, OSError):
            pass
        handle.close()


def _safe(value: Any) -> str:
    return re.sub(r"[^A-Za-z0-9_.-]+", "-", str(value)).strip("-")[:80] or "node"


def _write(path: Path, payload: Mapping[str, Any]) -> None:
    encoded = json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    if path.exists():
        try:
            if path.read_text(encoding="utf-8") == encoded:
                return
        except OSError:
            pass
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary_name: str | None = None
    try:
        with tempfile.NamedTemporaryFile(
            mode="w", encoding="utf-8", dir=path.parent,
            prefix=f".{path.name}.", suffix=".tmp", delete=False,
        ) as handle:
            handle.write(encoded)
            handle.flush()
            os.fsync(handle.fileno())
            temporary_name = handle.name
        os.replace(temporary_name, path)
        temporary_name = None
    finally:
        if temporary_name:
            try:
                os.unlink(temporary_name)
            except FileNotFoundError:
                pass


def _preserve(path: Path, generated: dict[str, Any]) -> dict[str, Any]:
    if not path.exists():
        return generated
    try:
        existing = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError, ValueError):
        return generated
    if not isinstance(existing, Mapping):
        return generated
    merged = dict(generated)
    # Status is derived from the current plan's completed set and dependency
    # closure.  Preserving a stale ``blocked``/``ready`` value would hide a
    # newly opened Join after a sibling node completes.
    for key in ("output", "evidence", "last_error", "updated_at"):
        if key in existing:
            merged[key] = existing[key]
    return merged


def _declared_artifacts_exist(root: Path, node: Mapping[str, Any]) -> tuple[list[str], list[str]]:
    """Return safe, declared output paths and any that a worker did not write.

    ``graph-apply`` is the completion boundary.  Accepting an inline `output`
    while every path in ``writes`` is absent lets a model mark a report task
    complete without producing the report.  Resolve each declared path under
    the project root so an absolute path or ``..`` cannot be smuggled through
    the execution record.

    Handles dual layout: ``loop-artifacts/`` may be nested inside ``root`` or
    at ``root.parent/loop-artifacts/`` (sibling layout).
    """

    declared = node.get("writes", [])
    if not isinstance(declared, list) or not declared:
        return [], ["<node declares no writes>"]
    safe: list[str] = []
    missing: list[str] = []
    sibling_artifacts = root.parent / "loop-artifacts"
    for raw in declared:
        if not isinstance(raw, str) or not raw.strip():
            missing.append(str(raw))
            continue
        candidate = (root / raw).resolve()
        if root not in candidate.parents:
            missing.append(raw)
            continue
        relative = str(candidate.relative_to(root))
        safe.append(relative)
        # Check nested layout first, then sibling layout
        exists = candidate.is_file() and candidate.stat().st_size > 0
        if not exists and sibling_artifacts.is_dir():
            # raw is typically "loop-artifacts/..." — strip that prefix to
            # get the path under the sibling loop-artifacts root.
            sibling_rel = raw
            for prefix in ("loop-artifacts/", "loop-artifacts"):
                if sibling_rel.startswith(prefix + "/") or sibling_rel == prefix:
                    sibling_rel = sibling_rel[len(prefix):].lstrip("/")
                    break
            if sibling_rel:
                sibling_candidate = (sibling_artifacts / sibling_rel).resolve()
                exists = sibling_candidate.is_file() and sibling_candidate.stat().st_size > 0
        if not exists:
            missing.append(relative)
    return safe, missing


def materialize_graph_tasks(root: str | Path, state: dict[str, Any]) -> list[dict[str, Any]]:
    """Create one task file per plan node without changing the plan itself."""

    root = Path(root)
    plan = state.get("plan")
    if not isinstance(plan, Mapping) or not isinstance(plan.get("nodes"), list) or not plan.get("nodes"):
        state["graph_tasks"] = []
        return []
    report = validate_plan(plan, strict=True)
    completed = {str(item) for item in plan.get("completed", [])}
    stage = state.get("stage", {}) if isinstance(state.get("stage"), Mapping) else {}
    stage_id = str(stage.get("id", "03"))
    revision = str(stage.get("revision", "r1"))
    directory = state_stage_artifact_dir(root, state) / "tasks"
    tasks: list[dict[str, Any]] = []
    for raw in plan["nodes"]:
        if not isinstance(raw, Mapping):
            continue
        node_id = str(raw.get("id"))
        deps = [str(value) for value in raw.get("depends_on", [])]
        ready = node_id not in completed and all(dep in completed for dep in deps)
        task_id = f"{stage_id}-{revision}-node-{_safe(node_id)}"
        task = {
            "schema_version": 1,
            "type": "graph_task",
            "id": task_id,
            "node_id": node_id,
            "stage_id": stage_id,
            "revision": revision,
            "status": "completed" if node_id in completed else ("ready" if ready else "blocked"),
            "parent_id": raw.get("parent_id"),
            "depends_on": deps,
            "execution_mode": raw.get("execution_mode", "serial"),
            "parallel_group_id": raw.get("parallel_group_id"),
            "orthogonal_key": raw.get("orthogonal_key"),
            "input_refs": list(raw.get("input_refs", [])),
            "output_schema": raw.get("output_schema", {}),
            "preconditions": list(raw.get("preconditions", [])),
            "postconditions": list(raw.get("postconditions", [])),
            "writes": list(raw.get("writes", [])),
            "instruction": (
                f"只执行 DAG 节点 `{node_id}`。先确认 depends_on 已完成；"
                "只写 writes 声明的路径，完成后把 output/evidence 增量写回本任务文件。"
                "不要修改 loop-state.json；阶段推进由 Commander 使用 ralph apply 完成。"
            ),
        }
        path = directory / f"{task_id}.json"
        task = _preserve(path, task)
        _write(path, task)
        task["path"] = str(path.relative_to(root))
        tasks.append(task)
    state["graph_tasks"] = tasks
    state.setdefault("plan", {})["ready"] = list(report.ready)
    return tasks


def apply_graph_task(root: str | Path, task_file: str | Path) -> dict[str, Any]:
    """Validate and atomically complete one execution-DAG node.

    A worker owns only its graph-task JSON.  This command is the sole write
    path that can add a node to ``plan.completed``; it verifies the current
    plan, dependency completion, and a non-empty result before rebuilding the
    durable ready/blocked/Join view.
    """

    from .events import append_observation
    from .state import load_state, save_state

    root = Path(root).expanduser().resolve()
    path = Path(task_file).expanduser()
    if not path.is_absolute():
        path = root / path
    path = path.resolve()
    state = load_state(root / "loop-state.json")
    allowed_dir = state_stage_artifact_dir(root, state).resolve()
    # Handle layout where loop-artifacts/ is at workspace root (sibling to
    # the project directory) rather than nested inside it.  If the expected
    # allowed_dir does not exist, try the same relative path under a
    # sibling loop-artifacts/.
    if not allowed_dir.is_dir():
        sibling_artifacts = root.parent / "loop-artifacts"
        if sibling_artifacts.is_dir():
            try:
                rel = allowed_dir.relative_to(root)
                sibling_allowed = (sibling_artifacts / rel).resolve()
            except ValueError:
                sibling_allowed = sibling_artifacts.resolve() / allowed_dir.parts[1]
            if sibling_allowed.is_dir():
                allowed_dir = sibling_allowed
    # Broader safety check: task must be under loop-artifacts/stages/ in
    # either the nested or sibling layout.
    nested_stages = (root / "loop-artifacts" / "stages").resolve()
    sibling_stages = (root.parent / "loop-artifacts" / "stages").resolve()
    if allowed_dir not in path.parents:
        if nested_stages not in path.parents and sibling_stages not in path.parents:
            raise ValueError(f"DAG 节点文件必须位于当前阶段目录：{allowed_dir.relative_to(root)}")
    try:
        raw = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise ValueError(f"DAG 节点 JSON 语法错误：第 {exc.lineno} 行、第 {exc.colno} 列：{exc.msg}") from exc
    if not isinstance(raw, Mapping) or raw.get("type") != "graph_task":
        raise ValueError("DAG 节点文件必须是 type=graph_task 对象")
    node_id = str(raw.get("node_id") or "").strip()
    if not node_id:
        raise ValueError("DAG 节点缺少 node_id")
    plan = state.get("plan")
    if not isinstance(plan, dict):
        raise ValueError("当前没有可执行 plan；先用 field-apply 提交 task_graph")
    report = validate_plan(plan, strict=True)
    nodes = {str(node.get("id")): node for node in plan.get("nodes", []) if isinstance(node, Mapping)}
    node = nodes.get(node_id)
    if node is None:
        raise ValueError(f"DAG 节点不存在：{node_id}")
    completed = {str(item) for item in plan.get("completed", [])}
    if node_id in completed:
        return {"ok": True, "node_id": node_id, "status": "completed", "already_completed": True}
    dependencies = [str(item) for item in node.get("depends_on", [])]
    missing = [item for item in dependencies if item not in completed]
    if missing:
        raise ValueError(f"节点 {node_id} 仍有未完成依赖：{', '.join(missing)}")
    output = raw.get("output")
    evidence = raw.get("evidence", [])
    if output in (None, "", {}, []) and not evidence:
        raise ValueError(f"节点 {node_id} 缺少 output 或 evidence；允许多轮填写后再运行 graph-apply")
    artifact_refs, missing_artifacts = _declared_artifacts_exist(root, node)
    if missing_artifacts:
        raise ValueError(
            f"节点 {node_id} 还没有写出声明的交付文件：{', '.join(missing_artifacts)}。"
            "先只写 node.writes 中的项目内相对路径，再运行 graph-apply；"
            "任务 JSON 里的 output 不能替代实际交付文件。"
        )
    with _graph_apply_lock(root):
        # Reload inside the lock so two parallel workers cannot lose each
        # other's completed node.
        state = load_state(root / "loop-state.json")
        plan = state.get("plan")
        if not isinstance(plan, dict):
            raise ValueError("当前没有可执行 plan")
        completed = {str(item) for item in plan.get("completed", [])}
        if node_id not in completed:
            completed.add(node_id)
            plan["completed"] = sorted(completed)
            plan.setdefault("task_results", {})[node_id] = {
                "output": output,
                "evidence": evidence,
                "artifact_refs": artifact_refs,
                "updated_at": datetime.now(timezone.utc).isoformat(),
            }
            materialize_graph_tasks(root, state)
            save_state(root / "loop-state.json", state)
        raw = dict(raw)
        raw["status"] = "completed"
        raw["updated_at"] = datetime.now(timezone.utc).isoformat()
        _write(path, raw)
    live = load_state(root / "loop-state.json")
    ready = list(live.get("plan", {}).get("ready", [])) if isinstance(live.get("plan"), Mapping) else []
    append_observation(
        root / "loop-events.md",
        "graph_task_increment_applied",
        {"node_id": node_id, "status": "completed", "ready_nodes": ready},
    )
    return {"ok": True, "node_id": node_id, "status": "completed", "ready_nodes": ready}
