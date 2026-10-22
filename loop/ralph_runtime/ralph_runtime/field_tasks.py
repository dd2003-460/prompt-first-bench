"""Dynamic, non-blocking one-field task files for research stages."""

from __future__ import annotations

import hashlib
import json
import re
import os
import tempfile
from contextlib import contextmanager
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Mapping

from .result_artifacts import state_stage_artifact_dir
from .runtime_config import flow_only_mode


@contextmanager
def _dispatch_lock(root: str | Path):
    """Serialize field-agent reservations across concurrent Claude hooks."""

    lock_path = Path(root) / "loop-artifacts" / ".field-dispatch.lock"
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


def claim_field_task(
    root: str | Path,
    task_id: str,
    *,
    dispatch_name: str | None = None,
) -> tuple[dict[str, Any], dict[str, Any] | None]:
    """Atomically reserve one ready field before an Agent tool is launched.

    Claude can emit two sibling Agent PreToolUse hooks concurrently.  A plain
    read-modify-write lets both hooks observe the same ready snapshot and the
    later write erases the first reservation.  This transaction makes the
    task lifecycle itself the dispatch queue: each prompt claims its own task
    id, and a concurrent sibling cannot overwrite that claim.
    """

    from .state import load_state, save_state

    state_path = Path(root) / "loop-state.json"
    with _dispatch_lock(root):
        state = load_state(state_path)
        task: dict[str, Any] | None = None
        for item in state.get("field_tasks", []):
            if isinstance(item, dict) and str(item.get("id", "")) == str(task_id):
                task = dict(item)
                if str(item.get("status", "")) in {"ready", "pending"}:
                    item["status"] = "dispatching"
                    item["last_error"] = ""
                    item["web_failures"] = 0
                    item["web_attempts"] = 0
                    item["apply_count_at_dispatch"] = int(item.get("apply_count", 0) or 0)
                    # Read limits are per worker attempt, not a permanent
                    # penalty.  A stale worker may have consumed its three
                    # diagnostic reads without writing anything; the next
                    # bounded recovery worker must be allowed to read once
                    # and then perform the required Write/Edit -> apply.
                    item["field_read_count"] = 0
                    if dispatch_name:
                        item["dispatch_name"] = str(dispatch_name)
                    task = dict(item)
                    save_state(state_path, state)
                break
        return state, task


def increment_field_web_attempt(root: str | Path, task_id: str) -> tuple[dict[str, Any], int]:
    """Atomically count one external-tool attempt for a field task."""

    from .state import load_state, save_state

    state_path = Path(root) / "loop-state.json"
    with _dispatch_lock(root):
        state = load_state(state_path)
        attempts = 0
        for item in state.get("field_tasks", []):
            if isinstance(item, dict) and str(item.get("id", "")) == str(task_id):
                attempts = max(0, int(item.get("web_attempts", 0) or 0)) + 1
                item["web_attempts"] = attempts
                save_state(state_path, state)
                return state, attempts
        return state, attempts


def update_field_task_metadata_transaction(
    root: str | Path,
    task_id: str,
    **kwargs: Any,
) -> dict[str, Any]:
    """Merge lifecycle metadata into the newest state snapshot under lock."""

    from .state import load_state, save_state

    state_path = Path(root) / "loop-state.json"
    with _dispatch_lock(root):
        state = load_state(state_path)
        update_field_task_metadata(root, state, task_id, **kwargs)
        save_state(state_path, state)
        return state


def settle_field_agent_tool_response(
    root: str | Path,
    task_id: str,
    *,
    failed: bool,
    agent_alias: str | None = None,
) -> tuple[dict[str, Any], bool]:
    """Record a parent ``Agent`` tool response without reviving a finished child.

    Claude Code does not guarantee that ``PostToolUse(Agent)`` arrives before
    ``SubagentStop``.  A successful child can therefore be moved to
    ``deferred`` by its Stop hook and then immediately be written back to
    ``dispatched`` by the parent's late tool receipt.  Treat terminal lifecycle
    states as authoritative and only settle an *active* reservation here.

    The check and update deliberately share the field dispatch lock: a stale
    hook snapshot must never overwrite a newer Stop-hook transition.
    """

    from .state import load_state, save_state

    state_path = Path(root) / "loop-state.json"
    with _dispatch_lock(root):
        state = load_state(state_path)
        task = next(
            (
                item
                for item in state.get("field_tasks", [])
                if isinstance(item, dict) and str(item.get("id", "")) == str(task_id)
            ),
            None,
        )
        if task is None or str(task.get("status", "")) not in {"dispatching", "dispatched"}:
            return state, False
        if failed:
            update_field_task_metadata(
                root,
                state,
                task_id,
                status="ready",
                clear_agent_id=True,
                clear_agent_ids=True,
                last_error="Agent tool failed before a usable SubagentStop receipt",
            )
        else:
            update_field_task_metadata(
                root,
                state,
                task_id,
                status="dispatched",
                agent_alias=agent_alias,
            )
        save_state(state_path, state)
        return state, True


def bind_field_task(
    root: str | Path,
    agent_id: str,
    *,
    dispatch_name: str | None = None,
) -> tuple[dict[str, Any], dict[str, Any] | None]:
    """Atomically bind one SubagentStart identity to one unbound field.

    Candidate selection and the identity write must share the same lock.  If
    two SubagentStart hooks arrive together, selecting from two stale snapshots
    can otherwise bind both children to the first field.
    """

    from .state import load_state, save_state

    state_path = Path(root) / "loop-state.json"
    with _dispatch_lock(root):
        state = load_state(state_path)
        existing = field_task_by_agent(state, agent_id)
        if existing is not None:
            return state, existing
        candidates = [
            item for item in current_field_tasks(state, {"dispatching", "dispatched"})
            if not item.get("agent_id")
        ]
        if dispatch_name:
            named = [
                item for item in candidates
                if str(item.get("dispatch_name") or "").strip().lower()
                == str(dispatch_name).strip().lower()
            ]
            if named:
                candidates = named
        if not candidates:
            return state, None
        task = candidates[0]
        update_field_task_metadata(
            str(root),
            state,
            str(task["id"]),
            status="dispatched",
            agent_id=agent_id,
        )
        save_state(state_path, state)
        return state, field_task_by_agent(state, agent_id)


def rebind_field_task_to_path(
    root: str | Path,
    agent_id: str,
    target_path: str,
) -> tuple[dict[str, Any], dict[str, Any] | None]:
    """Use a worker's first task-file access to repair identity mismatches.

    Claude Code can deliver parallel SubagentStart identities in an order that
    does not match the prompts actually given to the children.  The task JSON
    path used by the child is an observable, unambiguous field identity.  This
    transaction makes that path authoritative and removes the same agent id
    from any sibling task it was incorrectly attached to.
    """

    from .state import load_state, save_state

    state_path = Path(root) / "loop-state.json"
    candidate_path = Path(str(target_path)).expanduser()
    if not candidate_path.is_absolute():
        candidate_path = Path(root) / candidate_path
    try:
        candidate_path = candidate_path.resolve()
    except OSError:
        return load_state(state_path), None
    with _dispatch_lock(root):
        state = load_state(state_path)
        target: dict[str, Any] | None = None
        for item in state.get("field_tasks", []):
            if not isinstance(item, dict):
                continue
            path = item.get("path")
            if not path:
                continue
            try:
                if (Path(root) / str(path)).resolve() == candidate_path:
                    target = item
                    break
            except OSError:
                continue
        if target is None:
            return state, None
        target_id = str(target.get("id", ""))
        changed = False
        for item in state.get("field_tasks", []):
            if not isinstance(item, dict):
                continue
            if str(item.get("id", "")) == target_id:
                continue
            aliases = item.get("agent_ids") if isinstance(item.get("agent_ids"), list) else []
            if item.get("agent_id") == agent_id:
                item.pop("agent_id", None)
                changed = True
            filtered = [value for value in aliases if str(value) != str(agent_id)]
            if filtered != aliases:
                item["agent_ids"] = filtered
                changed = True
        aliases = target.get("agent_ids") if isinstance(target.get("agent_ids"), list) else []
        aliases = [value for value in aliases if str(value) != str(agent_id)]
        target["agent_id"] = str(agent_id)
        if str(agent_id) not in {str(value) for value in aliases}:
            aliases.append(str(agent_id))
        target["agent_ids"] = aliases
        target["status"] = "dispatched"
        changed = True
        if changed:
            save_state(state_path, state)
            return state, dict(target)
        return state, dict(target)


def _safe_name(value: str) -> str:
    text = re.sub(r"[^A-Za-z0-9_.-]+", "-", value).strip("-")
    return text[:80] or "field"


def _task_id(stage_id: str, revision: str, concept: str) -> str:
    digest = hashlib.sha256(concept.encode("utf-8")).hexdigest()[:10]
    return f"{stage_id}-{revision}-field-{_safe_name(concept)}-{digest}"


def field_task_ref_from_prompt(prompt: Any) -> str | None:
    """Extract the controlled task-file reference from an Agent prompt.

    The marker is deliberately tiny and line-oriented so a Commander can
    dispatch a field without copying the whole stage contract into context.
    """

    if not isinstance(prompt, str):
        return None
    match = re.search(r"RALPH_FIELD_TASK=([^\s`]+)", prompt)
    return match.group(1).strip() if match else None


def field_task_by_ref(state: Mapping[str, Any], ref: str | None) -> dict[str, Any] | None:
    """Return one current field task by its relative task-file path."""

    if not ref:
        return None
    normalized = str(ref).replace("\\", "/").lstrip("./")
    tasks = state.get("field_tasks", [])
    if not isinstance(tasks, list):
        return None
    for task in tasks:
        if not isinstance(task, Mapping):
            continue
        path = str(task.get("path", "")).replace("\\", "/").lstrip("./")
        if path == normalized or path.endswith("/" + normalized):
            return dict(task)
    return None


def field_task_by_agent(state: Mapping[str, Any], agent_id: str | None) -> dict[str, Any] | None:
    if not agent_id:
        return None
    tasks = state.get("field_tasks", [])
    if not isinstance(tasks, list):
        return None
    for task in tasks:
        if not isinstance(task, Mapping):
            continue
        ids = [task.get("agent_id"), *(task.get("agent_ids", []) if isinstance(task.get("agent_ids"), list) else [])]
        if any(str(value) == str(agent_id) for value in ids if value):
            return dict(task)
    return None


def current_field_tasks(state: Mapping[str, Any], statuses: set[str] | None = None) -> list[dict[str, Any]]:
    tasks = state.get("field_tasks", [])
    if not isinstance(tasks, list):
        return []
    return [
        dict(task)
        for task in tasks
        if isinstance(task, Mapping)
        and (statuses is None or str(task.get("status", "")) in statuses)
    ]


def field_task_requires_agent(task: Mapping[str, Any]) -> bool:
    """Return whether a field is an external-fact task for a narrow Agent.

    ``pending`` is deliberately not synonymous with ``research_required``.
    Stage-01 semantic factors and default assumptions may be filled by the
    Commander incrementally; only fields explicitly marked
    ``research_required`` require an independent research worker.
    """

    return str(task.get("disposition", "")).strip().lower() == "research_required"


def update_field_task_metadata(
    root: str | Path,
    state: dict[str, Any],
    task_id: str,
    *,
    status: str | None = None,
    agent_id: str | None = None,
    agent_alias: str | None = None,
    clear_agent_id: bool = False,
    clear_agent_ids: bool = False,
    dispatch_name: str | None = None,
    last_error: str | None = None,
    web_failures: int | None = None,
    web_attempts: int | None = None,
    apply_count: int | None = None,
    apply_count_at_dispatch: int | None = None,
    last_applied_at: str | None = None,
    field_read_count: int | None = None,
    worker_pid: int | None = None,
) -> dict[str, Any]:
    """Persist lifecycle metadata without replacing an agent's field draft."""

    tasks = state.setdefault("field_tasks", [])
    if not isinstance(tasks, list):
        tasks = []
        state["field_tasks"] = tasks
    matched: dict[str, Any] | None = None
    for task in tasks:
        if isinstance(task, dict) and str(task.get("id", "")) == str(task_id):
            matched = task
            break
    if matched is None:
        return state
    if status is not None:
        matched["status"] = status
    if agent_id:
        value = str(agent_id)
        previous = matched.get("agent_id")
        aliases = list(matched.get("agent_ids", [])) if isinstance(matched.get("agent_ids"), list) else []
        for candidate in (previous, value):
            if candidate and str(candidate) not in {str(item) for item in aliases}:
                aliases.append(str(candidate))
        matched["agent_id"] = value
        matched["agent_ids"] = aliases
    elif agent_alias:
        aliases = list(matched.get("agent_ids", [])) if isinstance(matched.get("agent_ids"), list) else []
        value = str(agent_alias)
        if value not in {str(item) for item in aliases}:
            aliases.append(value)
        matched["agent_ids"] = aliases
    elif clear_agent_id:
        matched.pop("agent_id", None)
    if clear_agent_ids:
        matched.pop("agent_ids", None)
    if dispatch_name is not None:
        matched["dispatch_name"] = str(dispatch_name)
    if last_error is not None:
        matched["last_error"] = last_error
    if web_failures is not None:
        matched["web_failures"] = max(0, int(web_failures))
    if web_attempts is not None:
        matched["web_attempts"] = max(0, int(web_attempts))
    if apply_count is not None:
        matched["apply_count"] = max(0, int(apply_count))
    if apply_count_at_dispatch is not None:
        matched["apply_count_at_dispatch"] = max(0, int(apply_count_at_dispatch))
    if last_applied_at is not None:
        matched["last_applied_at"] = str(last_applied_at)
    if field_read_count is not None:
        matched["field_read_count"] = max(0, int(field_read_count))
    if worker_pid is not None:
        matched["worker_pid"] = max(0, int(worker_pid))
    matched["updated_at"] = datetime.now(timezone.utc).isoformat()

    path_value = matched.get("path")
    if path_value:
        path = Path(root) / str(path_value)
        try:
            raw = json.loads(path.read_text(encoding="utf-8"))
            if isinstance(raw, dict):
                for key in ("status", "agent_id", "agent_ids", "dispatch_name", "last_error", "web_failures", "web_attempts", "apply_count", "apply_count_at_dispatch", "last_applied_at", "field_read_count", "worker_pid", "updated_at"):
                    if key in matched:
                        raw[key] = matched[key]
                    elif key == "agent_id":
                        raw.pop(key, None)
                    elif key == "agent_ids":
                        raw.pop(key, None)
                _write_json_if_changed(path, raw)
        except (OSError, json.JSONDecodeError, ValueError):
            # The worker may be in the middle of writing its draft. State is
            # authoritative; the next field-apply/materialization reconciles
            # the task-file metadata.
            pass
    return state


def reopen_stale_field_tasks(
    root: str | Path,
    state: dict[str, Any],
    *,
    exclude_ids: set[str] | None = None,
) -> list[str]:
    """Reopen field agents left by a dead parent Claude context.

    A field Agent is owned by its parent Claude context.  If that context was
    killed by an API/memory error, Claude Code may not emit SubagentStop.  The
    next outer supervisor cycle is then the authoritative recovery boundary.
    """

    reopened: list[str] = []
    excluded = {str(item) for item in (exclude_ids or set())}
    for task in current_field_tasks(state, {"dispatching", "dispatched"}):
        task_id = str(task.get("id", ""))
        if not task_id or task_id in excluded:
            continue
        update_field_task_metadata(
            root,
            state,
            task_id,
            status="ready",
            clear_agent_id=True,
            clear_agent_ids=True,
            last_error="父 Claude 上下文已结束，未收到 SubagentStop；由 supervisor 重开",
            web_attempts=0,
            web_failures=0,
            field_read_count=0,
        )
        reopened.append(task_id)
    return reopened


def reconcile_applied_field_tasks(root: str | Path, state: dict[str, Any]) -> list[dict[str, str]]:
    """Recover field tasks whose child applied a draft but a late hook rewound them.

    This is narrower than generic stale-worker recovery: an ``apply_count``
    greater than the dispatch baseline is durable evidence that the child did
    useful work.  No process needs to be terminated and no draft is removed.
    It is therefore safe to run while the parent Commander still exists, and
    it repairs historical state produced before lifecycle event ordering was
    made transactional.
    """

    matrix = (
        (state.get("task_spec") or {}).get("attribute_matrix", [])
        if isinstance(state.get("task_spec"), Mapping)
        else []
    )
    fields_by_concept = {
        str(field.get("concept", "")): field
        for field in matrix
        if isinstance(field, Mapping)
    } if isinstance(matrix, list) else {}
    reconciled: list[dict[str, str]] = []
    for task in current_field_tasks(state, {"dispatching", "dispatched"}):
        task_id = str(task.get("id", ""))
        if not task_id:
            continue
        if int(task.get("apply_count", 0) or 0) <= int(task.get("apply_count_at_dispatch", 0) or 0):
            continue
        field = fields_by_concept.get(str(task.get("concept", "")), {})
        disposition = _normalized_disposition(field.get("disposition")) if isinstance(field, Mapping) else ""
        refs = field.get("evidence_refs") if isinstance(field, Mapping) else []
        complete = disposition in {"confirmed", "inferred", "assumed_default"} or (
            disposition == "research_required" and isinstance(refs, list) and bool(refs)
        )
        status = "completed" if complete else "ready"
        update_field_task_metadata(
            root,
            state,
            task_id,
            status=status,
            clear_agent_id=not complete,
            clear_agent_ids=not complete,
            field_read_count=0 if not complete else None,
            last_error=(
                "已提交字段被迟到的 Agent 回执错误标回 dispatched；保留结果并标记完成"
                if complete
                else "已提交不完整字段被迟到的 Agent 回执错误标回 dispatched；保留草稿并重新开放补证"
            ),
        )
        reconciled.append({"field_task_id": task_id, "status": status})
    return reconciled


def reopen_deferred_field_tasks(root: str | Path, state: dict[str, Any]) -> list[str]:
    """Reopen deferred fields fairly at a fresh supervisor boundary.

    A deferred field is a valid incremental draft, not a failed stage.  Do
    not reopen every deferred field while ready fields exist: doing so lets a
    temporarily unavailable web source repeatedly reclaim the only worker
    slot and starve unrelated concepts.  Once the ready queue is empty, open
    only the oldest deferred field; the next supervisor boundary can rotate
    to the next one if this attempt remains incomplete.
    """

    reopened: list[str] = []
    ready_exists = bool(current_field_tasks(state, {"ready", "pending"}))
    if ready_exists:
        return reopened
    deferred = current_field_tasks(state, {"deferred"})
    deferred.sort(key=lambda item: str(item.get("last_applied_at") or item.get("updated_at") or ""))
    for task in deferred[:1]:
        task_id = str(task.get("id", ""))
        if not task_id:
            continue
        update_field_task_metadata(
            root,
            state,
            task_id,
            status="ready",
            clear_agent_id=True,
            clear_agent_ids=True,
            last_error="上一轮已保存不完整字段；新 supervisor 上下文重新开放补证",
            web_attempts=0,
            web_failures=0,
        )
        reopened.append(task_id)
    return reopened


def _normalized_disposition(value: Any) -> str:
    # Migrate only historical aliases; the current protocol remains explicit.
    return {
        "research": "research_required",
        "research-needed": "research_required",
        "assume": "assumed_default",
        "inferred_default": "assumed_default",
    }.get(str(value), str(value))


def _write_json_if_changed(path: Path, value: Mapping[str, Any]) -> None:
    encoded = json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    if path.exists():
        try:
            if path.read_text(encoding="utf-8") == encoded:
                return
        except OSError:
            pass
    path.parent.mkdir(parents=True, exist_ok=True)
    # Hooks for sibling Agents can materialize the same task index at the
    # same time.  A fixed `.tmp` name lets one writer replace/delete another
    # writer's temporary file and produces a misleading FileNotFoundError.
    temporary_name: str | None = None
    try:
        with tempfile.NamedTemporaryFile(
            mode="w",
            encoding="utf-8",
            dir=path.parent,
            prefix=f".{path.name}.",
            suffix=".tmp",
            delete=False,
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


def _preserve_agent_draft(path: Path, generated: dict[str, Any]) -> dict[str, Any]:
    """Keep an agent's in-place draft when the task index is regenerated.

    Task files are deliberately usable as both a dispatch description and a
    small writable draft.  A later prompt render must not replace a partially
    completed draft with the original template, otherwise incremental work is
    silently lost before ``field-apply`` can validate it.
    """

    if not path.exists():
        return generated
    try:
        existing = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError, ValueError):
        return generated
    if not isinstance(existing, Mapping):
        return generated
    merged = dict(generated)
    # Lifecycle metadata belongs to loop-state.json.  Preserving it from an
    # older task-file copy can silently turn a live ``dispatched`` task back
    # into ``ready`` every time a Hook materializes the task index.  Only the
    # worker's editable draft is preserved here; runtime metadata is refreshed
    # from the generated/state value below.
    for key in ("field", "fields", "draft"):
        if key in existing:
            merged[key] = existing[key]
    return merged


def materialize_field_tasks(root: str | Path, state: dict[str, Any]) -> list[dict[str, Any]]:
    """Create one small task file per unresolved field.

    These are dispatch hints, not completion gates.  A task becomes complete
    when its concept is updated by ``field-apply``; no stale task can block
    StopHook or stage transitions.
    """

    root = Path(root)
    stage = state.get("stage", {}) if isinstance(state.get("stage"), Mapping) else {}
    stage_id = str(stage.get("id", "01"))
    revision = str(stage.get("revision", "r1"))
    flow_only = flow_only_mode(state)
    spec = state.get("task_spec", {}) if isinstance(state.get("task_spec"), Mapping) else {}
    matrix = spec.get("attribute_matrix", []) if isinstance(spec, Mapping) else []
    if not isinstance(matrix, list):
        matrix = []
    else:
        # Required-output task synthesis below is a materialization detail;
        # never append synthetic entries to the canonical task_spec list.
        matrix = list(matrix)

    # Stage 01's ``unknown`` output is the source of truth for stage 02.  A
    # stage transition can intentionally keep loop-state.json slim, while the
    # state loader may reattach the previous artifact for context.  Therefore
    # checking only ``not matrix`` is incorrect: a stage-01 matrix can be
    # present while stage 02 still has no research fields.  Detect actual
    # stage-02 research entries instead, then turn every prior unknown factor
    # into one bounded research field.
    stage02_research = [
        item for item in matrix
        if isinstance(item, Mapping)
        and (
            str(item.get("role", "")).strip() == "research_findings"
            or _normalized_disposition(item.get("disposition")) == "research_required"
            or str(item.get("concept", "")).strip().startswith("研究未知因素：")
        )
    ]
    if stage_id == "02" and not stage02_research:
        source_matrix = list(matrix)
        prior_path = root / "loop-artifacts" / "stages" / "01" / "r1" / "state.json"
        try:
            prior = json.loads(prior_path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError, ValueError):
            prior = {}
        prior_matrix = prior.get("attribute_matrix", []) if isinstance(prior, Mapping) else []
        if not isinstance(prior_matrix, list):
            prior_matrix = []
        unknowns = [
            item for item in prior_matrix
            if isinstance(item, Mapping)
            and (
                str(item.get("role", "")).strip() in {"unknown", "unknown_factors"}
                or str(item.get("concept", "")).strip().endswith("输出：unknown")
                or str(item.get("concept", "")).strip().lower() == "unknown"
            )
        ]
        # Prefer a recovered stage-01 matrix already attached to the current
        # state.  The artifact fallback is only needed when the slim state
        # contains no unknown entry at all.
        current_unknowns = [
            item for item in source_matrix
            if isinstance(item, Mapping)
            and (
                str(item.get("role", "")).strip() in {"unknown", "unknown_factors"}
                or str(item.get("concept", "")).strip().endswith("输出：unknown")
                or str(item.get("concept", "")).strip().lower() == "unknown"
            )
        ]
        if current_unknowns:
            unknowns = current_unknowns
        # Do not carry the stage-01 goal/known/unknown rows into stage 02;
        # stage 02's canonical matrix contains only its research leaves.
        matrix = []
        for item in unknowns:
            raw_attribute = str(item.get("attribute") or "未知因素").strip()
            # Keep the split deterministic and conservative.  If the model
            # supplied a list, each top-level factor becomes its own task;
            # otherwise the complete unknown statement remains one task.
            factors = [part.strip() for part in re.split(r"[；;、]\s*", raw_attribute) if part.strip()]
            if not factors:
                factors = [raw_attribute]
            for index, factor in enumerate(factors, 1):
                concept = f"研究未知因素：{factor[:96]}"
                matrix.append(
                    {
                        "concept": concept,
                        "role": "research_findings",
                        "attribute": f"验证并记录：{factor}",
                        "disposition": "research_required",
                        "evidence_refs": [],
                        "rationale": "由阶段 01 unknown 自动拆分；阶段 02 必须为每个因素取得可验证证据。",
                        "source_unknown": str(item.get("concept") or "阶段 01 输出：unknown"),
                        "factor_index": index,
                    }
                )
        if not matrix:
            matrix.append(
                {
                    "concept": "阶段 02 输出：research_findings",
                    "role": "research_findings",
                    "attribute": "对上一阶段未知因素进行独立调研并记录可验证来源",
                    "disposition": "research_required",
                    "evidence_refs": [],
                    "rationale": "阶段 02 的最小研究入口；待字段 Agent 补充证据。",
                }
            )
        state["task_spec"] = {
            "status": "research_pending",
            "attribute_matrix": matrix,
            "authoritative_inputs": [
                "loop-artifacts/stages/01/r1/state.json",
            ],
        }

    # Every stage may have required outputs before the model has created a
    # matrix entry for them.  Materialize each missing output as an ordinary
    # pending field task so incremental filling works at 01, cross-validation,
    # execution decomposition, and later stages alike.  The task file is only
    # a draft surface; field-apply remains the authority that adds the result
    # to the state matrix and validates it.
    required_roles = [str(item) for item in (stage.get("required_outputs") or []) if item]
    # Stage 02's required output is the research leaf matrix itself and is
    # synthesized above from stage 01 unknowns.  Do not duplicate the stage
    # 01 fixture's required roles when a legacy/test state changes only the
    # numeric id to ``02``; later stages do need their own missing output
    # fields (for example 02.5/cross_validation).
    if required_roles and stage_id not in {"02"}:
        existing_roles = {
            str(item.get("role"))
            for item in matrix
            if isinstance(item, Mapping) and item.get("role")
        }
        for role in required_roles:
            if role not in existing_roles:
                matrix.append(
                    {
                        "concept": f"阶段 01 输出：{role}",
                        "attribute": f"请填写 {role} 的正交因素分解",
                        "role": role,
                        "disposition": "pending",
                        "evidence_refs": [],
                        "rationale": "由运行时为缺失的 required output 生成的增量字段任务。",
                    }
                )

    # A plain sentence is not an execution DAG.  In the flow-only experiment
    # reopen a task_graph field that was filled without a structured payload so
    # the next bounded worker can repair it incrementally.  Real projects use
    # the same shape check when field-apply receives a task_graph payload; this
    # branch only prevents the test-mode auto-advance from accepting prose.
    if stage_id == "03" and flow_only:
        repaired_matrix: list[dict[str, Any]] = []
        for item in matrix:
            if not isinstance(item, Mapping):
                repaired_matrix.append(item)
                continue
            if str(item.get("role", "")) == "task_graph":
                graph_value = next(
                    (item.get(key) for key in ("task_graph", "graph", "value") if isinstance(item.get(key), Mapping)),
                    None,
                )
                if not isinstance(graph_value, Mapping) or not isinstance(graph_value.get("nodes"), list):
                    item = dict(item)
                    item["disposition"] = "pending"
                    item["rationale"] = (
                        str(item.get("rationale") or "")
                        + " 需要补充结构化 task_graph.nodes；普通文本不能作为 DAG 通过。"
                    ).strip()
            repaired_matrix.append(item)
        matrix = repaired_matrix
        state["task_spec"] = {**dict(spec), "attribute_matrix": matrix}

    directory = state_stage_artifact_dir(root, state) / "tasks"
    tasks: list[dict[str, Any]] = []
    prior_by_id = {
        str(item.get("id")): item
        for item in (state.get("field_tasks", []) if isinstance(state.get("field_tasks"), list) else [])
        if isinstance(item, Mapping) and item.get("id")
    }
    for field in matrix:
        if not isinstance(field, Mapping):
            continue
        disposition = _normalized_disposition(field.get("disposition"))
        if disposition not in {"research_required", "pending"}:
            continue
        if disposition == "research_required":
            refs = field.get("evidence_refs")
            if isinstance(refs, list) and refs:
                # Evidence turns a research_required leaf into a completed
                # field for the current stage gate; do not recreate its task.
                continue
        concept = str(field.get("concept") or field.get("attribute") or "").strip()
        if not concept:
            continue
        task_id = _task_id(stage_id, revision, concept)
        task = {
            "schema_version": 1,
            "type": "field_task",
            "id": task_id,
            "stage_id": stage_id,
            "revision": revision,
            "flow_only": flow_only,
            "status": "ready",
            "disposition": "research_required" if disposition == "research_required" else "pending",
            "concept": concept,
            "role": field.get("role", "unknown"),
            "attribute": field.get("attribute", ""),
            "field": {
                "concept": concept,
                "role": field.get("role", "unknown"),
                "attribute": field.get("attribute", ""),
                "disposition": "research_required" if disposition == "research_required" else "pending",
                "rationale": field.get("rationale", ""),
                "evidence_refs": field.get("evidence_refs", []),
            },
            "input_refs": [f"loop-artifacts/stages/{stage_id}/{revision}/fields.json"],
            "output_schema": {
                "concept": concept,
                "role": "string",
                "attribute": "string",
                "disposition": "confirmed|inferred|assumed_default|research_required",
                "rationale": "string",
                "evidence_refs": "array[string]",
                "confidence": "number 0..1",
            },
            "instruction": (
                f"只处理字段 `{concept}`，不要读取完整 loop-events.md。"
                "先在这个任务文件的 `field` 对象中增量填写；不要修改 loop-state.json。"
                "读取后立即提交，不要规划总报告；网页工具最多尝试两次，若没有有效结果就保存待补状态。"
                "字段可以多轮修改，已填内容必须保留。填写后优先运行 "
                f"`ralph field-apply . loop-artifacts/stages/{stage_id}/{revision}/tasks/{task_id}.json`，"
                "由 runtime 校验并原子合并；如果命令不可用，再把同一个单字段 JSON 返回给主 Agent。"
                + (
                    "flow-only 流程实验不调用网页工具、不伪造来源；完成后使用 disposition=inferred，"
                    "在 rationale 标明仅用于验证流程，evidence_refs 保持空数组。"
                    if flow_only
                    else "research_required 暂无证据时可以先保存为 research_required + 空 evidence_refs，"
                    "但必须在 rationale 标注待补证据，不得伪造来源。"
                )
                + "不需要 SendMessage、TaskGet 或其他协调工具；写完任务文件并运行 field-apply 后直接结束。"
            ),
        }
        path = directory / f"{task_id}.json"
        # State metadata is authoritative across Hook/materialization cycles;
        # the task file only carries the editable draft.  Without this merge,
        # regenerating the task index would reset a live dispatch to ready.
        prior = prior_by_id.get(task_id)
        if isinstance(prior, Mapping):
            for key in ("status", "agent_id", "agent_ids", "dispatch_name", "last_error", "web_failures", "web_attempts", "apply_count", "apply_count_at_dispatch", "last_applied_at", "field_read_count", "worker_pid", "updated_at"):
                if key in prior:
                    task[key] = prior[key]
        task = _preserve_agent_draft(path, task)
        _write_json_if_changed(path, task)
        task["path"] = str(path.relative_to(root))
        tasks.append(task)

    state["field_tasks"] = [
        {key: value for key, value in task.items() if key != "field"}
        for task in tasks
    ]
    return tasks
