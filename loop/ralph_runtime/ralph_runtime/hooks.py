"""Claude Code Hook adapters with shadow and enforce modes."""

from __future__ import annotations

import json
import hashlib
import os
import re
import time
from pathlib import Path
from typing import Any, Mapping

from .contracts import (
    card_by_ref,
    materialize_contract_documents,
    merge_task_spec_partials,
    SEMANTIC_ROLES,
    factor_groups,
    stage_submission_template,
    task_card_marker,
)
from .events import append_observation, apply_and_record, read_events
from .feedback import feedback_context, gate_feedback, render_feedback, tool_feedback
from .result_artifacts import state_stage_artifact_dir
from .runtime_config import (
    STOP_POLICIES,
    effective_tool_decision,
    field_mode_enabled,
    max_field_web_attempts,
    max_parallel_fields,
)
from .field_tasks import (
    claim_field_task,
    bind_field_task,
    current_field_tasks,
    field_task_by_agent,
    field_task_by_ref,
    field_task_ref_from_prompt,
    field_task_requires_agent,
    increment_field_web_attempt,
    update_field_task_metadata,
    update_field_task_metadata_transaction,
    rebind_field_task_to_path,
    settle_field_agent_tool_response,
    materialize_field_tasks,
)


# A Stop Hook repair is useful only while the current Claude context is still
# making a bounded attempt to comply.  In inline mode the budget switches the
# prompt from syntax repair to strategy revision; it must not discard the
# context merely because a model emitted malformed XML several times.
MAX_PROTOCOL_REPAIRS_PER_CONTEXT = 3
from .prompt_renderer import PromptRenderer
from .protocol import parse_action
from .stage_policy import decide_tool
from .state import load_state, record_human_input, save_state, update_subagent_card
from .web_llm import web_llm_crosscheck_enabled


def _find_project_root(payload: Mapping[str, Any]) -> Path | None:
    raw_cwd = payload.get("cwd") or payload.get("workspace") or os.getcwd()
    current = Path(str(raw_cwd)).expanduser().resolve()
    for candidate in (current, *current.parents):
        if (candidate / "loop-state.json").exists():
            return candidate
    return None


def _tool_input(payload: Mapping[str, Any]) -> Mapping[str, Any]:
    value = payload.get("tool_input", {})
    return value if isinstance(value, Mapping) else {}


def _target_path(tool_input: Mapping[str, Any]) -> str | None:
    for key in ("file_path", "path", "target_path"):
        if tool_input.get(key):
            return str(tool_input[key])
    return None


def _command(tool_input: Mapping[str, Any]) -> str | None:
    value = tool_input.get("command")
    return str(value) if value else None


def _resolved_target(root: Path, target: str | None) -> Path | None:
    if not target:
        return None
    candidate = Path(target).expanduser()
    if not candidate.is_absolute():
        candidate = root / candidate
    return candidate.resolve()


def _commander_event_log_error(
    root: Path,
    role: str,
    tool_name: str,
    tool_input: Mapping[str, Any],
) -> str | None:
    """Prevent an unbounded transcript read of the append-only event journal."""

    if role != "commander" or tool_name != "Read":
        return None
    target = _resolved_target(root, _target_path(tool_input))
    if target != (root / "loop-events.md").resolve():
        return None
    return render_feedback(
        "EVENT_LOG_LOOP",
        detected="Commander 正在读取完整 loop-events.md；这会把旧工具输出重新注入上下文并放大 KV cache。",
        correction="停止当前 Read；事件日志是诊断摘要，不是工作输入。",
        next_action=(
            "需要诊断时只运行一次 `ralph events . --tail 20`；若字段任务正在运行，"
            "直接等待 field-apply 或字段生命周期回执。"
        ),
        forbidden="继续 Read/cat/tail 循环、重复派发字段 Agent，或把运行中字段误标为 blocked_human。",
    )


def _agent_card_error(state: Mapping[str, Any], tool_input: Mapping[str, Any]) -> tuple[dict[str, Any] | None, str | None]:
    reference = task_card_marker(tool_input)
    if reference is None:
        # Phase 1 relaxation: do NOT hard-block an Agent call that lacks the
        # RALPH_TASK_CARD marker.  A missing marker simply means the call is
        # unbound (run as a generic agent); the previous fatal block is what
        # trapped weak models in an endless recombobulating loop.
        return None, None
    card = card_by_ref(state, reference)
    if card is None:
        return None, f"Agent 任务卡未获批准：{reference}"
    stage = state.get("stage", {})
    if str(card.get("stage_id")) != str(stage.get("id")) or str(card.get("revision")) != str(stage.get("revision")):
        return None, f"任务卡 {card.get('id')} 不属于当前阶段"
    status = str(card.get("status", "pending"))
    if status == "completed":
        return None, tool_feedback(
            "DUPLICATE_DISPATCH",
            detected=f"任务卡 `{card.get('id')}` 已完成，当前 Agent 调用是重复派发。",
            correction="复用已有 gate receipt 和 artifact，不重新启动同一任务。",
            next_action="读取已完成回执并直接整理阶段提交；若回执缺失，报告运行时问题，不要重派。",
            forbidden="再次调用 Agent、创建任务卡、Write/Edit 或把内部等待伪装成 blocked_human。",
        )
    if status == "failed":
        return None, tool_feedback(
            "FAILED_CARD_RECOVERY",
            detected=f"任务卡 `{card.get('id')}` 已失败。",
            correction="先检查失败 artifact 和当前阶段条件，再决定回滚或重新分解。",
            next_action="停止重复派发；输出 rollback/repair_prompt，或等待人类重新授权新的计划修订。",
            forbidden="用同一任务卡无限重试、伪造 completed 或跳过失败原因。",
        )
    if status == "dispatched":
        if card.get("agent_id"):
            return None, render_feedback(
                "DUPLICATE_DISPATCH",
                detected=f"任务卡 `{card.get('id')}` 已绑定子代理 `{card.get('agent_id')}`，重复 Agent 调用被拒绝。",
                correction="把 dispatched 视为内部运行中状态，不是人类阻塞。",
                next_action=(
                    "不要再调用工具；等待 SubagentStop。需要诊断时最多运行一次 "
                    "`ralph events . --tail 20`，回执到达后再决定是否 advance。"
                ),
                forbidden="再次 Agent、创建/Write 任务卡、AskUserQuestion 或标记 blocked_human。",
            )
        return None, render_feedback(
            "DISPATCH_BINDING_WAIT",
            detected=f"任务卡 `{card.get('id')}` 已派发，正在等待 SubagentStart 绑定。",
            correction="生命周期事件尚未完成，当前不能证明任务失败或完成。",
            next_action="停止当前工具调用，等待 SubagentStart/SubagentStop 后再处理。",
            forbidden="不要再次调用 Agent、创建/Write 任务卡或标记 blocked_human。",
        )
    waiting = _unbound_dispatched_cards(state)
    if waiting:
        waiting_ids = ", ".join(str(item.get("id", "?")) for item in waiting)
        return None, render_feedback(
            "DISPATCH_ORDER",
            detected=f"已有未绑定的 dispatched 任务卡：{waiting_ids}。",
            correction="先完成已有生命周期绑定，再处理新的 Agent。",
            next_action="等待 SubagentStart；不要派发并行的未绑定卡。",
            forbidden="重复 Agent、手动写 agent_id 或跳过生命周期。",
        )
    return card, None


def _save_card_status(root: Path, state: Mapping[str, Any], card_id: str, status: str, agent_id: str | None = None) -> dict[str, Any]:
    updated = update_subagent_card(state, card_id, status, agent_id=agent_id)
    save_state(root / "loop-state.json", updated)
    materialize_contract_documents(root, updated)
    return updated


def _response_mapping(payload: Mapping[str, Any]) -> Mapping[str, Any]:
    response = payload.get("tool_response", {})
    return response if isinstance(response, Mapping) else {}


def _tool_failure(payload: Mapping[str, Any]) -> tuple[bool, str]:
    """Detect failed/blocked external tools without copying their full output.

    Search providers often return a successful HTTP wrapper whose result is an
    error page or a 403.  Treating that as useful evidence is worse than a
    bounded fallback: it makes a local Agent retry the same dead endpoint
    indefinitely.  This helper intentionally only returns a short diagnostic.
    """

    raw = payload.get("tool_response")
    values: list[Any]
    if isinstance(raw, list):
        values = raw
    else:
        values = [raw]
    for value in values:
        if not isinstance(value, Mapping):
            continue
        status = str(value.get("status", "")).lower()
        code = value.get("code")
        text = " ".join(
            str(value.get(key, ""))
            for key in ("error", "stderr", "message", "result", "content", "codeText")
            if value.get(key) is not None
        )
        # Some WebSearch providers return HTTP-200-shaped envelopes even when
        # no search was performed.  ``searchCount=0`` with a one-line
        # conversational placeholder or a serialized tool call is not
        # evidence and must enter the bounded fallback path instead of making
        # the field Agent retry forever.
        results = value.get("results")
        search_count = value.get("searchCount")
        placeholder = isinstance(results, list) and all(
            isinstance(item, str)
            and (
                "i'll search" in item.lower()
                or "<tool_call>" in item.lower()
                or "<|im_start|>" in item.lower()
                or '"query"' in item.lower()
                or "no results" in item.lower()
            )
            for item in results
        )
        empty_search = (
            isinstance(search_count, int)
            and search_count <= 0
            and isinstance(results, list)
            and (not results or placeholder)
        )
        failed = (
            value.get("success") is False
            or value.get("is_error") is True
            or value.get("isError") is True
            or status in {"failed", "error", "cancelled"}
            or (isinstance(code, int) and code >= 400)
            or bool(re.search(r"(?:HTTP\s*)?(?:4\d\d|5\d\d)\b|forbidden|no response from model|search error|fetch failed", text, re.I))
            or empty_search
        )
        if failed:
            return True, _bounded_hook_text(text or value, 700)
    return False, ""


def _agent_response_status(response: Mapping[str, Any]) -> str:
    # An unstructured tool response is not proof that a subagent finished.
    # Keep the card pending completion until SubagentStop rather than allowing
    # a false stage advance.
    if not response:
        return "dispatched"
    raw_status = str(response.get("status", "")).lower()
    if response.get("success") is False or raw_status in {"failed", "error", "cancelled"}:
        return "failed"
    if bool(response.get("isAsync")) or raw_status in {"async_launched", "running", "pending"}:
        return "dispatched"
    return "completed"


def _agent_id(payload: Mapping[str, Any]) -> str | None:
    response = _response_mapping(payload)
    sources: list[Any] = [response, payload]
    raw_response = payload.get("tool_response")
    if isinstance(raw_response, list):
        sources.extend(raw_response)
    for source in sources:
        if not isinstance(source, Mapping):
            continue
        for key in ("agent_id", "agentId", "subagent_id", "subagentId"):
            value = source.get(key)
            if value:
                return str(value)
        # Claude Code sometimes returns the asynchronous Agent receipt as a
        # text content block instead of a JSON object.
        text = source.get("text") or source.get("content")
        if isinstance(text, str):
            match = re.search(r"agent_id:\s*([^\s]+)", text)
            if match:
                return match.group(1)
    # Claude Code documents the direct agent_id on SubagentStart/Stop.  Some
    # tool hook payloads instead expose the child transcript path; it has the
    # stable `agent-<id>.jsonl` form, so use it as a compatibility fallback.
    for key in ("agent_transcript_path", "transcript_path"):
        value = payload.get(key)
        if not value:
            continue
        name = Path(str(value)).name
        if name.startswith("agent-") and name.endswith(".jsonl"):
            candidate = name[len("agent-") : -len(".jsonl")]
            if candidate:
                return candidate
    # Supervisor-launched top-level workers do not receive Claude's
    # SubagentStart payload.  Their launcher supplies this durable identity so
    # the same Hook field/web guards apply to them as to nested workers.
    environment_agent_id = os.environ.get("RALPH_AGENT_ID", "").strip()
    if environment_agent_id:
        return environment_agent_id
    return None


def _field_task_from_agent_input(state: Mapping[str, Any], tool_input: Mapping[str, Any]) -> dict[str, Any] | None:
    prompt = tool_input.get("prompt") or tool_input.get("instructions") or tool_input.get("input")
    ref = field_task_ref_from_prompt(prompt)
    return field_task_by_ref(state, ref)


def _field_task_from_path(
    root: Path,
    state: Mapping[str, Any],
    target: str | None,
) -> dict[str, Any] | None:
    """Resolve a tool path against the project root and find its field task.

    Do not call ``Path.resolve()`` on a relative tool path before joining the
    project root.  Hook processes inherit the workspace's cwd, which may be
    different from the project being supervised; doing so was the source of
    a cross-project ``relative_to`` crash in the worker hook.
    """

    resolved = _resolved_target(root, target)
    if resolved is None:
        return None
    for task in current_field_tasks(state):
        path = task.get("path")
        if not path:
            continue
        try:
            if (root / str(path)).resolve() == resolved:
                return dict(task)
        except OSError:
            continue
    return None


def _field_task_path_hint(root: Path, state: Mapping[str, Any], target: str | None) -> str | None:
    """Return the canonical JSON task path for a field-task read.

    This is used for both a hallucinated ``.js`` sibling and a valid ``.json``
    task path: Commander should dispatch the field Agent, not read the
    worker's input into its own context.
    """

    if not target:
        return None
    candidate = Path(str(target)).expanduser()
    if not candidate.is_absolute():
        candidate = root / candidate
    if candidate.suffix == ".js":
        json_candidate = candidate.with_suffix(".json")
    elif candidate.suffix == ".json":
        json_candidate = candidate
    else:
        return None
    for task in current_field_tasks(state):
        path = task.get("path")
        if not path:
            continue
        try:
            if (root / str(path)).resolve() == json_candidate.resolve():
                return str(path)
        except OSError:
            continue
        if candidate.suffix == ".js" and Path(str(path)).stem == candidate.stem:
            return str(path)
    return None


def _card_for_agent(state: Mapping[str, Any], agent_id: str | None) -> dict[str, Any] | None:
    if not agent_id:
        return None
    cards = state.get("subagent_cards", {})
    if not isinstance(cards, Mapping):
        return None
    for card in cards.values():
        if isinstance(card, Mapping) and str(card.get("agent_id", "")) == agent_id:
            return dict(card)
    return None


def _unbound_dispatched_cards(state: Mapping[str, Any]) -> list[dict[str, Any]]:
    stage = state.get("stage", {})
    stage_id = str(stage.get("id", ""))
    revision = str(stage.get("revision", ""))
    cards = state.get("subagent_cards", {})
    if not isinstance(cards, Mapping):
        return []
    return [
        dict(card)
        for card in cards.values()
        if isinstance(card, Mapping)
        and str(card.get("status", "")) == "dispatched"
        and not card.get("agent_id")
        and str(card.get("stage_id", "")) == stage_id
        and str(card.get("revision", "")) == revision
    ]


def _current_dispatched_cards(state: Mapping[str, Any]) -> list[dict[str, Any]]:
    """Return cards still running in the current stage/revision."""

    stage = state.get("stage", {})
    stage_id = str(stage.get("id", ""))
    revision = str(stage.get("revision", ""))
    cards = state.get("subagent_cards", {})
    if not isinstance(cards, Mapping):
        return []
    return [
        dict(card)
        for card in cards.values()
        if isinstance(card, Mapping)
        and str(card.get("status", "")) == "dispatched"
        and str(card.get("stage_id", "")) == stage_id
        and str(card.get("revision", "")) == revision
    ]


def _slice_owner_card(root: Path, state: Mapping[str, Any], target: str | None) -> dict[str, Any] | None:
    """Find the current-stage card whose slice input_refs contains `target`.

    Used so a builder/gate worker may Write/Edit its slice even when the
    agent_id binding is stale (the model rewrites loop-state.json with its own
    placeholder id after the subagent has already started).
    """

    if not target:
        return None
    candidate = Path(target).expanduser()
    if not candidate.is_absolute():
        candidate = root / candidate
    try:
        candidate = candidate.resolve()
    except OSError:
        return None
    stage = state.get("stage", {})
    stage_id = str(stage.get("id", ""))
    revision = str(stage.get("revision", "r1"))
    for card in (state.get("subagent_cards", {}) or {}).values():
        if not isinstance(card, Mapping):
            continue
        if str(card.get("stage_id", "")) != stage_id or str(card.get("revision", "")) != revision:
            continue
        if str(card.get("status", "")) in ("completed", "failed"):
            continue
        for ref in card.get("input_refs", []) or []:
            try:
                if (root / str(ref)).resolve() == candidate:
                    return dict(card)
            except OSError:
                continue
    return None


def _bind_waiting_card(root: Path, state: Mapping[str, Any], agent_id: str) -> tuple[dict[str, Any] | None, str | None]:
    existing = _card_for_agent(state, agent_id)
    if existing is not None:
        return existing, None
    stage = state.get("stage", {})
    stage_id = str(stage.get("id", ""))
    revision = str(stage.get("revision", "r1"))
    dispatched = [
        card
        for card in (state.get("subagent_cards", {}) or {}).values()
        if isinstance(card, Mapping)
        and str(card.get("stage_id", "")) == stage_id
        and str(card.get("revision", "")) == revision
        and card.get("status") == "dispatched"
    ]
    if len(dispatched) == 1:
        card = dispatched[0]
        updated = _save_card_status(root, state, str(card["id"]), "dispatched", agent_id=agent_id)
        return _card_for_agent(updated, agent_id), None
    if not dispatched:
        return None, "no_dispatched_card"
    ids = ", ".join(str(card.get("id", "?")) for card in dispatched)
    return None, f"ambiguous_dispatched_cards:{ids}"


def _card_tool_error(root: Path, card: Mapping[str, Any], tool_name: str, tool_input: Mapping[str, Any]) -> str | None:
    allowed_tools = {str(value) for value in card.get("allowed_tools", [])}
    if tool_name not in allowed_tools:
        if tool_name == "Bash":
            return tool_feedback(
                "WORKER_GATE_SCOPE",
                detected=f"只读审计卡 `{card.get('id')}` 尝试使用 Bash。",
                correction="门禁只需要读取任务卡列出的 document_refs，不能执行项目命令。",
                next_action="用 Read/Glob/Grep 完成边界内审计，然后直接返回完整 `<RALPH_GATE_REVIEW>` JSON。",
                forbidden="Bash、Write、Edit、修改文件、读取 loop-state.json 或开始外部调研。",
            )
        return tool_feedback(
            "WORKER_TOOL_SCOPE",
            detected=f"任务卡 `{card.get('id')}` 不允许使用 {tool_name}。",
            correction=f"只使用任务卡白名单：{', '.join(sorted(allowed_tools)) or '无'}。",
            next_action="继续当前边界内工作，完成后返回任务卡要求的结构化结果。",
            forbidden="用其他工具绕过白名单或扩大 document_refs。",
        )

    target = _target_path(tool_input)
    if tool_name == "Read" and target:
        candidate = Path(target).expanduser()
        if not candidate.is_absolute():
            candidate = root / candidate
        candidate = candidate.resolve()
        allowed_refs = [str(card.get("card_ref", "")), *[str(ref) for ref in card.get("document_refs", [])]]
        allowed_paths = {(root / ref).resolve() for ref in allowed_refs if ref}
        if candidate not in allowed_paths:
            return tool_feedback(
                "WORKER_READ_SCOPE",
                detected=f"任务卡 `{card.get('id')}` 尝试读取 document_refs 之外的文件。",
                correction="门禁上下文必须保持有界，只读取任务卡和明确列出的输入包/契约/模板。",
                next_action="停止该 Read，改读允许的 document_refs；读完后直接输出门禁回执。",
                forbidden="读取完整 loop-events.md、loop-state.json、其他阶段 artifact 或项目业务文件。",
            )

    if tool_name in {"Glob", "Grep"}:
        if not target:
            return tool_feedback(
                "WORKER_SEARCH_SCOPE",
                detected=f"任务卡 `{card.get('id')}` 的 {tool_name} 没有限定搜索路径。",
                correction="搜索必须限制在任务卡允许的 loop-artifacts/范围内。",
                next_action=f"为 {tool_name} 指定一个明确的 loop-artifacts/目标，或停止搜索并提交回执。",
                forbidden="无界搜索项目根目录或读取完整历史日志。",
            )
        candidate = Path(target).expanduser()
        if not candidate.is_absolute():
            candidate = root / candidate
        candidate = candidate.resolve()
        artifact_root = (root / "loop-artifacts").resolve()
        if candidate != artifact_root and artifact_root not in candidate.parents:
            return tool_feedback(
                "WORKER_SEARCH_SCOPE",
                detected=f"任务卡 `{card.get('id')}` 的 {tool_name} 超出了 loop-artifacts/。",
                correction="把搜索范围收回任务卡允许的 artifact 目录。",
                next_action=f"只搜索 `{artifact_root}` 下的指定输入，完成后直接提交门禁回执。",
                forbidden="搜索业务目录、全量 loop-events.md 或其他任务的文件。",
            )
    return None


def _record(root: Path, event_type: str, payload: Mapping[str, Any], output: str | None = None) -> None:
    append_observation(root / "loop-events.md", event_type, payload, output=output)


def _output_digest(output: str) -> str:
    return hashlib.sha256(output.encode("utf-8")).hexdigest()


def _output_was_applied(root: Path, digest: str) -> bool:
    for event in read_events(root / "loop-events.md"):
        if event.get("output_sha256") == digest:
            return True
        observation = event.get("observation")
        if isinstance(observation, Mapping) and observation.get("output_sha256") == digest:
            return True
    return False


def _consecutive_protocol_rejections(root: Path) -> int:
    """Count invalid stage results since the latest supervisor cycle.

    The supervisor writes ``supervisor_cycle_started`` before launching each
    fresh Claude process.  Treating that event as a boundary prevents a bad
    previous context from consuming the new context's repair budget.
    """

    count = 0
    for event in reversed(read_events(root / "loop-events.md")):
        event_type = str(event.get("type", ""))
        if event_type == "stage_result_rejected":
            count += 1
            continue
        if event_type == "supervisor_cycle_started":
            break
        # A successfully applied state action also starts a new semantic
        # attempt, even if the supervisor has not yet launched a new process.
        if event_type in {
            "stage_advanced",
            "stage_rollback",
            "task_spec_clarified",
            "blocked_human",
            "blocked_task_skipped",
            "exploration_started",
            "action_recorded",
        }:
            break
    return count


def _invalid_output_artifact(root: Path, digest: str, output: str) -> str:
    try:
        state = load_state(root / "loop-state.json")
        artifact_dir = state_stage_artifact_dir(root, state)
    except (OSError, ValueError, KeyError, TypeError):
        artifact_dir = root / "loop-artifacts" / "stages" / "unknown-stage" / "r1"
    artifact_dir.mkdir(parents=True, exist_ok=True)
    artifact_path = artifact_dir / f"{digest}.invalid-agent-output.md"
    if not artifact_path.exists():
        artifact_path.write_text(output, encoding="utf-8")
    return str(artifact_path.relative_to(root))


def _apply_agent_result(root: Path, output: str) -> dict[str, Any]:
    """Parse, validate, persist and journal one final Agent result.

    The output digest makes Stop Hook retries idempotent. A repeated Stop event
    cannot apply the same action twice.
    """

    digest = _output_digest(output)
    if _output_was_applied(root, digest):
        return {"status": "duplicate", "output_sha256": digest}
    try:
        action = parse_action(output)
        state = apply_and_record(
            root / "loop-state.json",
            root / "loop-events.md",
            action.to_dict(),
            raw_output=output,
        )
        return {
            "status": "applied",
            "action": action.to_dict(),
            "state": state,
            "output_sha256": digest,
        }
    except Exception as exc:  # Hook failures must become Agent-visible repair feedback.
        artifact_ref = _invalid_output_artifact(root, digest, output)
        _record(
            root,
            "stage_result_rejected",
            {
                "error": str(exc),
                "output_sha256": digest,
                "artifact_ref": artifact_ref,
            },
            output=output,
        )
        return {
            "status": "rejected",
            "error": str(exc),
            "artifact_ref": artifact_ref,
            "output_sha256": digest,
        }


def _stop_response(reason: str, mode: str, stop_policy: str = "fresh") -> dict[str, Any]:
    if stop_policy == "inline":
        return {
            "decision": "block",
            "reason": reason[:12000],
            "systemMessage": "RALPH inline continuation: keep the current Claude context and continue from durable state.",
        }
    if mode in {"shadow", "hybrid"}:
        # Stop only supports a blocking decision.  Hybrid deliberately lets a
        # malformed draft end the turn; the outer supervisor can start a short
        # recovery context instead of trapping a local model in a repair loop.
        label = "shadow" if mode == "shadow" else "hybrid"
        return {"systemMessage": f"RALPH {label}：" + reason}
    return {"decision": "block", "reason": reason[:12000]}


def _inline_stop_repeat_count(root: Path, output_digest: str) -> int:
    """Count consecutive identical inline Stops without a tool/state event.

    The official Ralph Loop plugin uses an output hash to avoid feeding an
    identical answer back forever.  Here the hash does not terminate work: it
    upgrades the next prompt to a strategy-revision instruction while keeping
    the same Claude context alive.
    """

    count = 0
    progress_events = {
        "posttooluse_observed",
        "field_increment_applied",
        "stage_advanced",
        "stage_rollback",
        "task_spec_clarified",
        "action_recorded",
        "human_input_received",
    }
    for event in reversed(read_events(root / "loop-events.md")):
        event_type = str(event.get("type", ""))
        if event_type == "inline_stop_intercepted":
            observation = event.get("observation")
            previous = observation.get("output_sha256") if isinstance(observation, Mapping) else None
            if previous == output_digest:
                count += 1
                continue
            break
        if event_type in progress_events:
            break
    return count


def _inline_stop_response(
    root: Path,
    state: Mapping[str, Any],
    *,
    reason: str,
    output: str | None,
    event_reason: str,
) -> dict[str, Any]:
    """Block Stop and feed a bounded, state-aware prompt into this context."""

    visible_output = _bounded_hook_text(output, 2400)
    output_digest = _output_digest(visible_output) if visible_output else ""
    repeated = _inline_stop_repeat_count(root, output_digest) if output_digest else 0
    stage = state.get("stage") if isinstance(state.get("stage"), Mapping) else {}
    _record(
        root,
        "inline_stop_intercepted",
        {
            "stage": stage.get("id"),
            "revision": stage.get("revision"),
            "reason": event_reason,
            "output_sha256": output_digest or None,
            "identical_stop_count": repeated + 1 if output_digest else 0,
            "state_preserved": True,
            "recovery": "same_claude_context",
        },
    )
    repeat_instruction = ""
    if repeated + 1 >= MAX_PROTOCOL_REPAIRS_PER_CONTEXT:
        repeat_instruction = (
            "\n\n## 策略切换（禁止重复上一轮）\n"
            f"你已经在没有工具/状态进展的情况下给出相同输出 {repeated + 1} 次。"
            "不要再次解释或重发同一结果；先检查当前阶段状态和最近错误，"
            "再执行一个与上一轮不同的最小诊断、修复或验证动作。"
        )
    prior_output = ""
    if visible_output:
        prior_output = (
            "\n\n## 上一轮可见输出（仅用于继续，不要照抄）\n"
            "<RALPH_LAST_OUTPUT>\n"
            + visible_output
            + "\n</RALPH_LAST_OUTPUT>\n"
        )
    continuation = (
        "# RALPH 同上下文继续\n"
        "Stop 已被拦截：不要退出、不要从头规划，也不要假装完成。"
        "保留当前 Claude 上下文；先检查持久化状态和已产生的文件，再做一个具体动作。"
        "若本轮已有可验证进展，先运行对应的 `ralph field-apply`、`ralph graph-apply` 或 "
        "`ralph apply` 记录状态；不要直接编辑 `loop-state.json`。\n\n"
        + reason
        + prior_output
        + repeat_instruction
    )
    return _stop_response(continuation, mode="enforce", stop_policy="inline")


def _field_command_hint(
    stage: Mapping[str, Any] | None = None,
    state: Mapping[str, Any] | None = None,
) -> str:
    stage = stage if isinstance(stage, Mapping) else {}
    stage_id = str(stage.get("id", "01"))
    revision = str(stage.get("revision", "r1"))
    draft = f"loop-artifacts/stages/{stage_id}/{revision}/fields.json"
    advance = f"loop-artifacts/stages/{stage_id}/{revision}/advance.json"
    hint = (
        "RALPH 当前阶段命令提示（Hook 每次工具调用都会重复注入）：只修改当前阶段草稿，不要直接修改 loop-state.json。"
        f"若草稿不存在先运行 `ralph field-init .`；把新增/修改字段写入 `{draft}`，格式为 `{{\"fields\":[{{\"concept\":\"...\","
        "\"role\":\"...\",\"attribute\":\"...\",\"disposition\":\"pending|confirmed|"
        "assumed_default|research_required\",\"rationale\":\"...\",\"evidence_refs\":[]}}]}}`，"
        f"然后运行 `ralph field-apply . {draft}`（校验 + 增量合并 + 原子保存）。语法错误、空字段或缺字段时只修复命令输出列出的项目；空的 pending 字段可以保留，已通过字段保留不重写。"
        f"DAG 节点先写自己 node.writes 声明的实际非空文件，再更新自己的 task JSON 并运行 `ralph graph-apply . <节点文件>`（校验依赖 + 交付文件 + 更新 ready/Join）。"
        f"全部字段和节点通过后，写 `{advance}` 并运行 `ralph apply . {advance}`（最终校验 + 状态转换 + 事件记录）。"
        "候选/探索任务用 `ralph task-next .`；诊断只用 `ralph status .`（或 `ralph field-status .`）、"
        "`ralph events . --tail 20`、`ralph validate .` 或 `ralph render . <file>`；"
        "上下文中断后用 `ralph resume .`，不要重复读取完整 loop-events.md。"
    )
    if stage_id == "exploration":
        hint += (
            " 探索是尾节点而非终止：先运行 `ralph task-next .`；人类阻塞任务直接跳过。"
            "候选必须带研究摘要/理由/范围并标记 `status=candidate`，用 `candidate` 动作写入 queue，"
            "不要用未获批准的 candidate selected_task 提交 `advance`；只有选中 tasks/TASKS.md 的 ready/pending 任务才用 `selection_mode=task_board` 返回 01。"
        )
    tasks = state.get("field_tasks", []) if isinstance(state, Mapping) else []
    if tasks:
        ready = [
            item for item in tasks
            if isinstance(item, Mapping) and str(item.get("status", "")) in {"ready", "pending"}
        ]
        active = [
            item for item in tasks
            if isinstance(item, Mapping) and str(item.get("status", "")) in {"dispatching", "dispatched"}
        ]
        deferred = [
            item for item in tasks
            if isinstance(item, Mapping) and str(item.get("status", "")) == "deferred"
        ]
        hint += f" 当前共有 {len(tasks)} 个字段任务，本轮最多处理 {max_parallel_fields()} 个 ready 字段；"
        hint += "当前批次完成后再处理下一批。"
        if active:
            hint += " 正在运行（禁止重复派发）：" + "、".join(
                f"{item.get('concept')}[{item.get('status')}]"
                for item in active[:max_parallel_fields()]
            ) + "。"
        hint += " 当前批次："
        hint += "；".join(
            f"{item.get('concept')}→{item.get('path')}"
            for item in ready[:max_parallel_fields()]
            if isinstance(item, Mapping) and item.get("concept") and item.get("path")
        )
        if len(ready) > max_parallel_fields():
            hint += f"；其余 {len(ready) - max_parallel_fields()} 个 ready 字段稍后处理"
        if deferred:
            hint += f"；另有 {len(deferred)} 个不完整字段将在下一次 supervisor 上下文重新开放"
        hint += "。对 disposition=research_required 的字段，当前阶段必须逐项调用 Agent；"
        hint += "prompt 第一行使用 `RALPH_FIELD_TASK=<path>`，每个 Agent 只处理一个字段，"
        hint += "优先把结果写回该任务文件的 field 对象并运行 `ralph field-apply . <任务文件>`；若命令报错，只按错误提示增量修复同一文件并重试。"
    graph_tasks = state.get("graph_tasks", []) if isinstance(state, Mapping) else []
    if graph_tasks:
        hint += (
            " 当前已有执行 DAG 节点：子代理先写自己 node.writes 声明的实际非空文件，再修改自己的 graph task JSON，"
            "完成后运行 `ralph graph-apply . <节点文件>`；runtime 会校验 depends_on 与交付文件、"
            "原子更新 plan.completed 并重新计算 ready/blocked/Join。不要直接修改 plan 或 loop-state.json。"
        )
    return hint


def _dispatch_first_repetitions(root: Path) -> int:
    """Count repeated field-dispatch gate attempts in the current cycle.

    Hybrid mode intentionally gives the model one soft correction.  A weak
    local model can otherwise keep reading the same files forever because the
    internal decision is denied but the effective permission is still allow.
    After two repetitions the gate becomes a real deny for that tool call.
    """

    count = 0
    for event in reversed(read_events(root / "loop-events.md")):
        event_type = str(event.get("type", ""))
        if event_type == "supervisor_cycle_started":
            break
        if event_type != "pretooluse_observed":
            continue
        observation = event.get("observation")
        if not isinstance(observation, Mapping):
            continue
        reason = str(observation.get("reason", ""))
        if "RALPH_FEEDBACK[FIELD_DISPATCH_FIRST]" in reason:
            count += 1
    return count


def _escalate_dispatch_first_feedback(root: Path, reason: str) -> str:
    if "RALPH_FEEDBACK[FIELD_DISPATCH_FIRST]" not in reason:
        return reason
    if _dispatch_first_repetitions(root) < 2:
        return reason
    return reason.replace(
        "RALPH_FEEDBACK[FIELD_DISPATCH_FIRST]",
        "RALPH_FEEDBACK[FIELD_DISPATCH_FIRST_ESCALATED]",
        1,
    )


def _bounded_hook_text(value: Any, limit: int = 6000) -> str:
    """Extract a small diagnostic slice without copying a transcript."""

    if value is None or isinstance(value, bool):
        return ""
    if isinstance(value, (Mapping, list, tuple)):
        try:
            value = json.dumps(value, ensure_ascii=False, sort_keys=True)
        except (TypeError, ValueError):
            value = str(value)
    text = str(value).replace("\x00", " ").strip()
    if len(text) <= limit:
        return text
    half = max(1, (limit - 80) // 2)
    return text[:half] + "\n[… 中间诊断内容已截断 …]\n" + text[-half:]


def _bounded_tool_response(value: Any) -> dict[str, Any] | str:
    """Keep PostToolUse diagnostics useful without copying tool transcripts."""

    if not isinstance(value, Mapping):
        return _bounded_hook_text(value, 1600)

    # These fields are useful for lifecycle diagnosis.  Large result bodies
    # are represented by short excerpts; unknown fields are represented only
    # by their names so a tool cannot silently grow loop-events.md.
    scalar_keys = (
        "status",
        "success",
        "isAsync",
        "agent_id",
        "agentId",
        "subagent_id",
        "subagentId",
        "stop_reason",
        "error",
        "error_message",
        "message",
    )
    text_keys = ("output", "content", "stdout", "stderr", "text", "result")
    bounded: dict[str, Any] = {}
    for key in scalar_keys:
        if key in value:
            item = value[key]
            bounded[key] = _bounded_hook_text(item, 320) if isinstance(item, (Mapping, list, tuple)) else item
    for key in text_keys:
        if key in value:
            bounded[key] = _bounded_hook_text(value[key], 700)
    if not bounded:
        bounded["keys"] = [str(key) for key in list(value.keys())[:32]]
    return bounded


def _runtime_signal_text(payload: Mapping[str, Any]) -> str:
    """Collect only Hook error fields; never serialize the full Hook payload."""

    fields = (
        "error",
        "error_message",
        "stop_reason",
        "reason",
        "message",
        "last_assistant_message",
    )
    chunks: list[str] = []
    for key in fields:
        value = _bounded_hook_text(payload.get(key))
        if value:
            chunks.append(f"{key}: {value}")
    response = _response_mapping(payload)
    for key in ("error", "error_message", "status", "message", "stop_reason"):
        value = _bounded_hook_text(response.get(key))
        if value:
            chunks.append(f"tool_response.{key}: {value}")
    return "\n".join(chunks)


def _classify_runtime_interruption(payload: Mapping[str, Any]) -> tuple[str, str] | None:
    """Recognize infrastructure failures before trying to parse stage output.

    These failures are not Agent decisions. Treating them as malformed
    RALPH_STAGE_RESULT would create a repair loop and may append another full
    prompt to an already memory-pressure transcript.
    """

    signal = _runtime_signal_text(payload)
    lowered = signal.lower()
    memory_patterns = (
        "prefill context too large",
        "prefill memory guard",
        "memory guard rejected",
        "prefill safety cap",
        "available memory",
        "out of memory",
        "outofmemory",
        "oom",
        "内存不足",
        "显存不足",
    )
    connection_patterns = (
        "econnreset",
        "connection to the api was lost",
        "connection reset",
        "connection refused",
        "broken pipe",
        "network error",
    )
    timeout_patterns = ("timed out", "timeout", "deadline exceeded", "超时")
    api_patterns = ("api error", "request failed", "http 4", "http 5")
    stall_patterns = (
        "stalled mid-stream",
        "response stalled",
        "stream interrupted",
        "generation stalled",
        "incomplete response",
        "stream was interrupted",
        "connection closed before",
    )
    if any(pattern in lowered for pattern in memory_patterns):
        kind = "memory_guard"
    elif any(pattern in lowered for pattern in connection_patterns):
        kind = "connection"
    elif any(pattern in lowered for pattern in timeout_patterns):
        kind = "timeout"
    elif any(pattern in lowered for pattern in stall_patterns):
        kind = "stall"
    elif any(pattern in lowered for pattern in api_patterns):
        kind = "api_error"
    else:
        stop_reason = str(payload.get("stop_reason", "")).lower()
        if payload.get("error") or stop_reason in {"error", "failed", "cancelled", "aborted"}:
            kind = "runtime"
        else:
            return None
    return kind, _bounded_hook_text(signal, 1600)


def _runtime_stop_message(state: Mapping[str, Any], kind: str, excerpt: str) -> str:
    stage = state.get("stage", {})
    stage_id = str(stage.get("id", "?")) if isinstance(stage, Mapping) else "?"
    revision = str(stage.get("revision", "?")) if isinstance(stage, Mapping) else "?"
    labels = {
        "memory_guard": "oMLX 上下文/内存保护",
        "connection": "模型连接中断",
        "timeout": "模型请求超时",
        "stall": "模型响应中断（stalled mid-stream）",
        "api_error": "模型 API 错误",
        "runtime": "运行时错误",
    }
    label = labels.get(kind, kind)
    detail = _bounded_hook_text(excerpt, 700)
    return render_feedback(
        "RUNTIME_INTERRUPTION",
        detected=(
            f"{label}；当前阶段 {stage_id}-{revision} 未推进。"
            f"错误摘要：{detail or 'Hook 未收到可解析的错误正文'}"
        ),
        correction="保留 loop-state.json 原状，不把基础设施错误当成协议错误或阶段失败。",
        next_action="允许当前会话安全结束；下一次使用 `ralph resume <项目路径>` 建立短上下文。",
        forbidden="在原会话重复发送完整历史、重复派发同一任务或进入字段修复循环。",
    )


def _record_runtime_interruption(
    root: Path,
    state: Mapping[str, Any],
    payload: Mapping[str, Any],
    kind: str,
    excerpt: str,
) -> None:
    stage = state.get("stage", {})
    stage_id = stage.get("id") if isinstance(stage, Mapping) else None
    revision = stage.get("revision") if isinstance(stage, Mapping) else None
    _record(
        root,
        "runtime_interrupted",
        {
            "stage": stage_id,
            "revision": revision,
            "kind": kind,
            "stop_reason": _bounded_hook_text(payload.get("stop_reason"), 120),
            "state_preserved": True,
            "recovery": "allow_stop_then_ralph_resume",
        },
        output=excerpt,
    )


def handle_pretooluse(payload: Mapping[str, Any], mode: str = "hybrid") -> dict[str, Any]:
    root = _find_project_root(payload)
    if root is None:
        return {"decision": "allow", "reason": "no loop-state.json found"}
    state = load_state(root / "loop-state.json")
    if field_mode_enabled():
        # Materialization is normally already persisted by the supervisor.
        # Avoid writing an unchanged snapshot on every concurrent PreToolUse:
        # that stale write could erase a sibling Agent's reservation before
        # claim_field_task acquires its transaction lock.
        before = repr(state.get("field_tasks"))
        materialize_field_tasks(root, state)
        if repr(state.get("field_tasks")) != before:
            save_state(root / "loop-state.json", state)
    tool_name = str(payload.get("tool_name", ""))
    tool_input = _tool_input(payload)
    agent_id = _agent_id(payload)
    bound_card = None if field_mode_enabled() else _card_for_agent(state, agent_id)
    slice_owner_bind = False
    if not field_mode_enabled() and bound_card is None and tool_name in {"Write", "Edit"}:
        owner = _slice_owner_card(root, state, _target_path(tool_input))
        if owner is not None:
            bound_card = owner
            slice_owner_bind = True
    # Field-mode workers intentionally have no legacy task-card binding.  A
    # Claude subagent still carries an agent_id, so use that identity to keep
    # the Commander-only dispatch gate from blocking the worker's own Read,
    # WebSearch, Write, and field-apply steps.
    role = (
        "worker"
        if bound_card is not None or (field_mode_enabled() and bool(agent_id))
        else str(payload.get("ralph_role") or os.environ.get("RALPH_ROLE", "commander"))
    )
    # Commander must never read long documents or subagent-only artifacts. A
    # single large Read (e.g. the stage-input-package embeds the whole
    # task_spec and is ~18K tokens) can blow the 60k context window in one
    # turn, before auto-compact (which only runs between turns) can act. The
    # Commander only dispatches subagents; the subagents read the docs.
    _commander_read_denied = False
    _commander_read_reason = None
    if role == "commander" and tool_name == "Read" and field_mode_enabled():
        canonical_task = _field_task_path_hint(root, state, _target_path(tool_input))
        if canonical_task:
            attempted_task = _field_task_from_path(root, state, canonical_task)
            requires_agent = bool(attempted_task and field_task_requires_agent(attempted_task))
            stage = state.get("stage", {}) if isinstance(state, Mapping) else {}
            stage_id = str(stage.get("id", "01"))
            revision = str(stage.get("revision", "r1"))
            fields_path = f"loop-artifacts/stages/{stage_id}/{revision}/fields.json"
            next_action = (
                "不要读取任务文件来构造总报告；下一次工具调用仍必须是带 RALPH_FIELD_TASK 标记的 Agent。"
                if requires_agent
                else (
                    f"不要读取结构字段任务卡；直接 Write/Edit 当前阶段草稿 `{fields_path}`，"
                    f"然后运行 `ralph field-apply . {fields_path}`。"
                )
            )
            _commander_read_denied = True
            _commander_read_reason = tool_feedback(
                "FIELD_TASK_PATH_CORRECTION",
                detected=(
                    f"Commander 尝试直接读取字段任务文件 `{_target_path(tool_input)}`。"
                    if str(_target_path(tool_input)).endswith(".json")
                    else f"任务文件路径使用了不存在的扩展名：`{_target_path(tool_input)}`。"
                ),
                correction=(
                    f"字段任务文件是受控输入；正确路径为 `{canonical_task}`，但 Commander 不需要读取它。"
                    if str(_target_path(tool_input)).endswith(".json")
                    else f"字段任务文件是 JSON，不是 JavaScript；正确路径为 `{canonical_task}`。"
                ),
                next_action=next_action,
                forbidden="创建 `.js` 副本、读取多个任务文件或绕过 field-apply。",
            )
    if role == "commander" and tool_name in {"Read", "Grep", "Glob"}:
        _tgt = _target_path(tool_input)
        if _tgt:
            _resolved = _resolved_target(root, _tgt)
            _rp = str(_resolved)
            if _rp.endswith("loop-state.json"):
                pass  # minimal state read still allowed
            elif any(
                seg in _rp
                for seg in (
                    "/loop-artifacts/contracts/",
                    "/loop-artifacts/task-cards/",
                    "/loop-artifacts/gate-reviews/",
                )
            ):
                _commander_read_denied = True
                _commander_read_reason = tool_feedback(
                    "COMMANDER_DOC_READ",
                    detected=f"Commander 尝试读取受限阶段文档 `{_tgt}`。",
                    correction="字段任务文件已经包含单字段输入；不要读取完整契约、门禁回执或历史阶段文档。",
                    next_action="直接按当前字段任务提示派发 Agent，或读取有限事件摘要。",
                    forbidden="用 Read/Grep/Glob 读取完整契约、gate review 或历史阶段文档。",
                )
            else:
                try:
                    if _resolved.exists() and _resolved.stat().st_size > 25000:
                        _commander_read_denied = True
                        _commander_read_reason = tool_feedback(
                            "COMMANDER_LONG_READ",
                            detected=f"Commander 尝试读取约 {_resolved.stat().st_size // 1024}KB 的长文档 `{_tgt}`。",
                            correction="Commander 上下文窗口只有 60k，长文档会一次性撑爆它。",
                            next_action="直接派发当前 ready 字段；长文档由字段 Agent 读取。",
                            forbidden="用 Read/Grep/Glob 读取超过 ~25KB 的文件。",
                        )
                except OSError:
                    pass
    if _commander_read_denied:
        decision_value = "deny"
        decision_reason = _commander_read_reason
    else:
        decision = decide_tool(
            state,
            role,
            tool_name,
            target_path=_target_path(tool_input),
            command=_command(tool_input),
        )
        decision_value = decision.decision
        decision_reason = decision.reason
    card_id: str | None = str(bound_card["id"]) if bound_card is not None else None
    event_log_error = _commander_event_log_error(root, role, tool_name, tool_input)
    if event_log_error:
        decision_value = "deny"
        decision_reason = event_log_error
    if bound_card is not None and not slice_owner_bind:
        card_error = _card_tool_error(root, bound_card, tool_name, tool_input)
        if card_error:
            decision_value = "deny"
            decision_reason = card_error

    # Keep the first correction soft in hybrid mode, but make an unchanged
    # repeated Read/Bash/etc. converge to a hard denial.  This prevents the
    # exact read-loop observed with local models while preserving a forgiving
    # first attempt for normal Commander diagnostics.
    decision_reason = _escalate_dispatch_first_feedback(root, decision_reason)

    field_task = _field_task_from_agent_input(state, tool_input) if field_mode_enabled() and tool_name == "Agent" else None
    owned_field_task = field_task_by_agent(state, agent_id) if field_mode_enabled() else None
    # A child task path is authoritative.  Rebind before applying the write
    # guard: SubagentStart can arrive with a stale/swapped identity, so the
    # first Read/Edit of the actual task file must repair ownership rather than
    # being rejected as an apparent cross-task write.
    if field_mode_enabled() and role == "worker" and agent_id and _target_path(tool_input):
        path_task = _field_task_from_path(root, state, _target_path(tool_input))
        if path_task is not None and (owned_field_task is None or owned_field_task.get("id") != path_task.get("id")):
            state, rebound = rebind_field_task_to_path(root, agent_id, str(path_task.get("path", "")))
            if rebound is not None:
                owned_field_task = rebound
                _record(
                    root,
                    "field_task_rebound_from_worker_path",
                    {
                        "agent_id": agent_id,
                        "field_task_id": rebound.get("id"),
                        "path": rebound.get("path"),
                        "reason": "worker task path is authoritative after parallel identity mismatch",
                    },
                )
    worker_path_error: str | None = None
    if (
        field_mode_enabled()
        and role == "worker"
        and owned_field_task is not None
        and tool_name in {"Write", "Edit"}
        and _target_path(tool_input)
    ):
        expected = _resolved_target(root, str(owned_field_task.get("path", "")))
        actual = _resolved_target(root, _target_path(tool_input))
        if expected is not None and actual != expected:
            worker_path_error = tool_feedback(
                "FIELD_TASK_PATH_CORRECTION",
                detected=f"worker 尝试修改不属于自己的字段文件 `{_target_path(tool_input)}`。",
                correction=f"当前 worker 只能修改自己的 task JSON：`{owned_field_task.get('path')}`。",
                next_action=(
                    f"立即 Write/Edit `{owned_field_task.get('path')}` 的 `field` 对象，"
                    f"然后运行 `ralph field-apply . {owned_field_task.get('path')}`。"
                ),
                forbidden="修改 fields.json、loop-state.json、其他字段任务或项目业务文件。",
            )
    if worker_path_error:
        decision_value = "deny"
        decision_reason = worker_path_error
    if (
        field_mode_enabled()
        and role == "worker"
        and tool_name == "Read"
        and owned_field_task is not None
        and int(owned_field_task.get("field_read_count", 0) or 0) >= 1
    ):
        decision_value = "deny"
        decision_reason = tool_feedback(
            "FIELD_WRITE_AFTER_READ",
            detected=f"字段任务 `{owned_field_task.get('id')}` 已经读取自己的 task JSON，仍再次请求 Read。",
            correction="字段 worker 读取一次即可；当前内容已经足够进行增量填写。",
            next_action=(
                f"立即用 Write/Edit 修改 `{owned_field_task.get('path')}` 的 field 对象，"
                f"然后运行 `ralph field-apply . {owned_field_task.get('path')}`。"
            ),
            forbidden="重复 Read/Grep/Glob、读取其他任务或只输出自然语言而不提交字段。",
        )
    if (
        field_mode_enabled()
        and role == "worker"
        and tool_name in {"WebSearch", "WebFetch"}
        and owned_field_task is not None
        and int(owned_field_task.get("web_failures", 0) or 0) >= 2
    ):
        decision_value = "deny"
        stage_id = str((state.get("stage") or {}).get("id") or "") if isinstance(state, Mapping) else ""
        if stage_id == "02" and web_llm_crosscheck_enabled(root):
            next_action = (
                f"先运行 `ralph web-llm-check . {owned_field_task.get('path')}`，向已授权网页 LLM 询问具体可复核来源线索；"
                "回执只是线索，随后必须验证实际 HTTPS 页面。若仍没有具体页面，再把研究结论增量写回 "
                f"`{owned_field_task.get('path')}`：保留 disposition=research_required、evidence_refs=[]，"
                "在 rationale 写明失败原因，然后运行 `ralph field-apply . <任务文件>`。"
            )
        else:
            next_action = (
                f"直接把研究结论增量写回 `{owned_field_task.get('path')}`："
                "保留 disposition=research_required、evidence_refs=[]，在 rationale 写明失败原因，"
                "然后运行 `ralph field-apply . <任务文件>`。"
            )
        decision_reason = tool_feedback(
            "FIELD_WEB_FAILURE_LOOP",
            detected=(
                f"字段 `{owned_field_task.get('concept', '')}` 的外部搜索已连续失败 "
                f"{owned_field_task.get('web_failures')} 次。"
            ),
            correction="停止重复搜索；外部证据源当前不可用，不得把错误页当作证据。",
            next_action=next_action,
            forbidden="继续调用 WebSearch/WebFetch、伪造 URL、自然语言结束而不写入任务文件。",
        )
    if (
        field_mode_enabled()
        and role == "worker"
        and tool_name in {"WebSearch", "WebFetch"}
        and owned_field_task is not None
        and decision_value == "allow"
    ):
        max_attempts = max_field_web_attempts()
        attempts = int(owned_field_task.get("web_attempts", 0) or 0)
        if attempts >= max_attempts:
            decision_value = "deny"
            decision_reason = tool_feedback(
                "FIELD_WEB_ATTEMPT_LIMIT",
                detected=(
                    f"字段 `{owned_field_task.get('concept', '')}` 已达到网页工具尝试上限 "
                    f"({attempts}/{max_attempts})。"
                ),
                correction="不要等待挂起的网页请求，也不要再次搜索；直接提交当前字段的可验证草稿或待补状态。",
                next_action=(
                    f"增量写回 `{owned_field_task.get('path')}`：保留 disposition=research_required、"
                    "evidence_refs=[]，在 rationale 说明外部工具不可用，然后运行 `ralph field-apply . <任务文件>`。"
                ),
                forbidden="继续调用 WebSearch/WebFetch、伪造来源或只返回自然语言而不提交字段文件。",
            )
        else:
            state, attempts = increment_field_web_attempt(root, str(owned_field_task["id"]))
            # Keep the in-hook lookup in sync for the subsequent failure
            # handling and event path.
            owned_field_task["web_attempts"] = attempts
    auto_bound_field_path: str | None = None
    if field_mode_enabled() and role == "commander" and tool_name == "Agent" and decision_value == "allow":
        ready_research = [
            item for item in current_field_tasks(state, {"ready", "pending"})
            if field_task_requires_agent(item)
        ]
        if field_task is not None and not field_task_requires_agent(field_task):
            decision_value = "deny"
            decision_reason = tool_feedback(
                "FIELD_AGENT_NOT_NEEDED",
                detected=f"字段 `{field_task.get('concept', '')}` 是 `{field_task.get('disposition', 'pending')}` 结构字段，不是 research_required。",
                correction="pending/assumed_default 字段由 Commander 直接增量填写；只有 research_required 字段才派独立 Agent。",
                next_action="直接 Write/Edit 当前阶段 fields.json（不改 loop-state.json），然后运行 `ralph field-apply . <fields.json>`；若确实需要外部事实，先把该字段标记为 research_required。",
                forbidden="为结构化填空字段派无边界 Agent，或让未绑定 Agent 改写项目文件。",
            )
        if ready_research and field_task is None:
            first = ready_research[0]
            if mode == "hybrid":
                # Some local Claude-compatible frontends put the child task in
                # ``description`` and silently drop the prompt's first line.
                # Do not turn that formatting omission into a dead loop: the
                # queue itself is authoritative, so reserve exactly the first
                # ready field and let SubagentStart bind the child.  The narrow
                # one-field boundary and field-apply gate remain unchanged.
                field_task = dict(first)
                auto_bound_field_path = str(first.get("path", ""))
                decision_reason = tool_feedback(
                    "FIELD_TASK_MARKER_AUTOFILLED",
                    detected="Agent prompt 缺少 RALPH_FIELD_TASK 标记，但当前只有受控的 ready 字段队列。",
                    correction=f"runtime 已自动绑定一个字段：`{auto_bound_field_path}`。",
                    next_action="子代理只处理这个字段，读取任务文件、增量填写 field，并运行 `ralph field-apply`。",
                    forbidden="不要把多个字段合并到一个 Agent，不要直接修改 loop-state.json。",
                )
            else:
                decision_value = "deny"
                decision_reason = tool_feedback(
                    "FIELD_TASK_MARKER_REQUIRED",
                    detected="当前阶段存在未派发的 research_required 字段，但 Agent prompt 没有绑定有效字段任务。",
                    correction=f"只派发一个字段；prompt 第一行必须是 `RALPH_FIELD_TASK={first.get('path', '<task-file>')}`。",
                    next_action="把该字段交给一个窄 Agent；不要派发无边界的总研究 Agent。",
                    forbidden="省略 RALPH_FIELD_TASK、把多个字段合并到一个 Agent 或自行生成总研究报告。",
                )
        elif not ready_research and field_task is None:
            decision_value = "deny"
            decision_reason = tool_feedback(
                "FIELD_AGENT_NOT_NEEDED",
                detected="当前没有 ready/pending 的 research_required 字段任务。",
                correction="本轮应由 Commander 直接增量填写结构字段，不需要启动无边界 Agent。",
                next_action="写入当前阶段的 fields.json 后运行 `ralph field-apply . <fields.json>`；填写完成后按提示运行 `ralph apply`。",
                forbidden="没有 research_required 字段时派发未绑定 Agent，或把结构分解交给旧 task-card/auditor 协议。",
            )
        elif field_task and str(field_task.get("status", "")) in {"dispatching", "dispatched"}:
            decision_value = "deny"
            decision_reason = tool_feedback(
                "FIELD_TASK_DUPLICATE",
                detected=f"字段任务 `{field_task.get('id')}` 已处于 {field_task.get('status')} 生命周期状态。",
                correction="保留已有子代理，不要重复派发同一字段；等待 SubagentStop 或 field-apply。",
                next_action="继续当前批次的其他 ready 字段，或等待子代理完成。",
                forbidden="重复 Agent、复制任务文件或把运行中任务标记 blocked_human。",
            )

    if tool_name == "Agent" and decision_value == "allow":
        if field_mode_enabled():
            # There is no legacy card gate.  A research_required field still
            # requires one narrow Agent dispatch, while pending/default fields
            # may be filled by Commander incrementally.
            if "FIELD_TASK_MARKER_AUTOFILLED" not in decision_reason:
                decision_reason = "field mode: narrow Agent allowed; one Agent per research field"
            if field_task is not None:
                # Reserve by task id under a file lock.  Two sibling Agent
                # hooks may arrive concurrently; saving the pre-hook snapshot
                # here would let the second call erase the first reservation.
                dispatch_name = tool_input.get("name") or tool_input.get("description")
                state, claimed = claim_field_task(
                    root,
                    str(field_task["id"]),
                    dispatch_name=str(dispatch_name) if dispatch_name else None,
                )
                if claimed is None:
                    decision_value = "deny"
                    decision_reason = tool_feedback(
                        "FIELD_TASK_CLAIM_LOST",
                        detected=f"字段任务 `{field_task.get('id')}` 已被其他生命周期事件占用。",
                        correction="保留已有字段 Agent，不重复派发同一字段。",
                        next_action="等待 SubagentStop；如果任务失败，由 supervisor 重新打开该字段。",
                        forbidden="重复调用 Agent、覆盖其他字段或把内部运行状态标记为 blocked_human。",
                    )
        else:
            card, card_error = _agent_card_error(state, tool_input)
            if card_error:
                decision_value = "deny"
                decision_reason = card_error
            elif card is not None:
                card_id = str(card["id"])
                decision_reason = f"approved task card {card_id}"
                if card.get("status") == "pending":
                    state = _save_card_status(root, state, card_id, "dispatched")
            else:
                decision_reason = "untracked Agent allowed in hybrid field workflow"
    _record(
        root,
        "pretooluse_observed",
        {
            "tool_name": tool_name,
            "role": role,
            "mode": mode,
            "decision": decision_value,
            "reason": decision_reason,
            "task_card_id": card_id,
            "agent_id": agent_id,
            "target_path": _target_path(tool_input),
            "command": _bounded_hook_text(_command(tool_input), 700) if tool_name == "Bash" else None,
        },
    )
    effective = effective_tool_decision(decision_value, decision_reason, mode)
    response: dict[str, Any] = {
        "hookSpecificOutput": {
            "hookEventName": "PreToolUse",
            "permissionDecision": effective,
            "permissionDecisionReason": f"{decision_reason} (mode={mode})",
        }
    }
    if field_mode_enabled() and role == "commander":
        response["hookSpecificOutput"]["additionalContext"] = _field_command_hint(
            state.get("stage") if isinstance(state, Mapping) else None,
            state,
        )
        if auto_bound_field_path:
            response["hookSpecificOutput"]["additionalContext"] += (
                f"\n本次 Agent 已由 runtime 自动绑定字段任务 `{auto_bound_field_path}`；"
                "不要重新派发该字段，子代理完成后等待 field-apply 回执。"
            )
    elif field_mode_enabled() and role == "worker":
        response["hookSpecificOutput"]["additionalContext"] = (
            "RALPH 字段 Agent 命令提示：只修改自己的 task JSON 的 field 对象；"
            "JSON 草稿可多轮填写。每次修改后运行 `ralph field-apply . <自己的任务文件>`；"
            "语法或字段错误只修复命令列出的项目并重试，已通过字段保留；"
            "如果是 DAG 节点，改用 `ralph graph-apply . <自己的节点文件>`。"
            "不要修改 loop-state.json；外部工具失败时不伪造来源，写入 research_required、"
            "空 evidence_refs 和 rationale 后仍运行 field-apply。"
        )
    return response


def handle_posttooluse(payload: Mapping[str, Any], mode: str = "hybrid") -> dict[str, Any]:
    root = _find_project_root(payload)
    if root is not None:
        tool_name = str(payload.get("tool_name", ""))
        tool_input = _tool_input(payload)
        state = load_state(root / "loop-state.json")
        if field_mode_enabled():
            materialize_field_tasks(root, state)
        owned_field_task = field_task_by_agent(state, _agent_id(payload)) if field_mode_enabled() else None
        card_id: str | None = None
        card_status: str | None = None
        if tool_name == "Agent":
            if field_mode_enabled():
                field_task = _field_task_from_agent_input(state, tool_input)
                raw_response = payload.get("tool_response")
                response_map = _response_mapping(payload)
                failed = (
                    isinstance(response_map, Mapping)
                    and (response_map.get("success") is False or str(response_map.get("status", "")).lower() in {"failed", "error", "cancelled"})
                )
                if field_task is not None:
                    state, _settled = settle_field_agent_tool_response(
                        root,
                        str(field_task["id"]),
                        failed=failed,
                        # The asynchronous child identity is authoritative at
                        # SubagentStart.  This is only an alias for an active
                        # reservation, and must not revive a task that its
                        # SubagentStop hook has already deferred/completed.
                        agent_alias=None if failed else _agent_id(payload),
                    )
            card = None if field_mode_enabled() else card_by_ref(state, task_card_marker(tool_input))
            if card is not None:
                card_id = str(card["id"])
                card_status = _agent_response_status(_response_mapping(payload))
                # A foreground Agent response is not sufficient proof that a
                # gate fulfilled its required receipt.  SubagentStop gives us
                # the final message, which is where the tagged gate JSON is
                # validated before the card may become completed.
                if card.get("is_stage_gate") and card_status == "completed":
                    card_status = "dispatched"
                _save_card_status(root, state, card_id, card_status, agent_id=_agent_id(payload))
        _record(
            root,
            "posttooluse_observed",
            {
                "tool_name": tool_name,
                "mode": mode,
                "tool_response": _bounded_tool_response(payload.get("tool_response")),
                "task_card_id": card_id,
                "task_card_status": card_status,
                "agent_id": _agent_id(payload),
            },
        )
        # A command/file write is allowed to be incremental, but a failed
        # command must produce an actionable repair prompt immediately.  This
        # keeps a weak local model from treating stderr as a stage failure or
        # silently continuing with an unapplied draft.
        response_map = _response_mapping(payload)
        external_failed, external_detail = _tool_failure(payload)
        if (
            field_mode_enabled()
            and owned_field_task is not None
            and tool_name in {"WebSearch", "WebFetch"}
            and not external_failed
            and int(owned_field_task.get("web_failures", 0) or 0) > 0
        ):
            # The fuse counts consecutive failures, not a lifetime total.
            # A real source result restores the field's retry budget.
            state = update_field_task_metadata_transaction(
                root,
                str(owned_field_task["id"]),
                web_failures=0,
                web_attempts=0,
                last_error="",
            )
        if (
            field_mode_enabled()
            and owned_field_task is not None
            and tool_name in {"WebSearch", "WebFetch"}
            and external_failed
        ):
            failures = int(owned_field_task.get("web_failures", 0) or 0) + 1
            state = update_field_task_metadata_transaction(
                root,
                str(owned_field_task["id"]),
                web_failures=failures,
                last_error=external_detail or "外部搜索工具失败",
            )
            _record(
                root,
                "field_external_tool_failed",
                {
                    "field_task_id": owned_field_task.get("id"),
                    "concept": owned_field_task.get("concept"),
                    "tool_name": tool_name,
                    "failure_count": failures,
                    "detail": external_detail,
                },
            )
            return {
                "hookSpecificOutput": {
                    "hookEventName": "PostToolUse",
                    "additionalContext": (
                        f"RALPH 外部工具 `{tool_name}` 失败（第 {failures} 次）：{external_detail}\n"
                        + (
                            "不要继续重复搜索。现在把该字段写回任务文件，保留 "
                            "disposition=research_required 和空 evidence_refs，并在 rationale 说明来源不可用，"
                            "然后运行 `ralph field-apply . <任务文件>`。"
                            if failures >= 2
                            else "可换一个权威来源重试一次；若再次失败，必须按字段降级规则写回任务文件。"
                        )
                    ),
                }
            }
        if (
            field_mode_enabled()
            and owned_field_task is not None
            and tool_name in {"WebSearch", "WebFetch"}
            and not external_failed
        ):
            # A successful search is evidence input, not permission to keep
            # searching indefinitely.  Push small local models out of the
            # tool loop and into the incremental Write -> field-apply step.
            return {
                "hookSpecificOutput": {
                    "hookEventName": "PostToolUse",
                    "additionalContext": (
                        "RALPH 外部证据工具已返回结果。下一次工具调用必须是 Write 或 Edit 自己的任务 JSON，"
                        "把可验证结论和来源写入当前 field 的 attribute/rationale/evidence_refs；"
                        "不要再次搜索、不要读取其他文件。写入后立即运行同一个 `ralph field-apply`；"
                        "若结果不足以确认，保留 disposition=research_required 并在 rationale 标注待补证据。"
                    ),
                }
            }
        failed = (
            response_map.get("success") is False
            or response_map.get("is_error") is True
            or response_map.get("isError") is True
            or str(response_map.get("status", "")).lower() in {"failed", "error", "cancelled"}
            or response_map.get("exit_code") not in (None, 0)
        )
        if field_mode_enabled() and failed and tool_name in {"Bash", "Write", "Edit"}:
            detail = _bounded_hook_text(
                response_map.get("stderr") or response_map.get("error") or response_map.get("message") or response_map,
                900,
            )
            return {
                "hookSpecificOutput": {
                    "hookEventName": "PostToolUse",
                    "additionalContext": (
                        "RALPH 增量命令未通过；状态尚未因本次失败而改变。"
                        f"错误摘要：{detail}\n"
                        "只修复错误指出的 JSON 语法或缺失字段，保留已通过字段，"
                        "然后重新运行同一个 `ralph field-apply . <字段文件>`；"
                        "不要直接修改 loop-state.json，也不要重做其他字段。"
                    ),
                }
            }
        if field_mode_enabled() and owned_field_task is not None and tool_name == "Read":
            task_path = str(owned_field_task.get("path") or "自己的字段任务文件")
            update_field_task_metadata_transaction(
                root,
                str(owned_field_task.get("id")),
                field_read_count=int(owned_field_task.get("field_read_count", 0) or 0) + 1,
            )
            return {
                "hookSpecificOutput": {
                    "hookEventName": "PostToolUse",
                    "additionalContext": (
                        "RALPH 字段增量硬顺序提示：你已经读取了自己的任务文件。"
                        f"下一次工具调用必须是 Write 或 Edit `{task_path}` 的 `field` 对象，"
                        "只填写/修复当前 concept；不要再次 Read、Grep、Glob、规划总报告或读取其他文件。"
                        f"写入后立即运行 `ralph field-apply . {task_path}`；若命令报错，只按报错列出的字段增量修复并重试。"
                    ),
                }
            }
    return {}


def handle_subagentstart(payload: Mapping[str, Any], mode: str = "hybrid") -> dict[str, Any]:
    """Bind a newly spawned subagent to one current field task."""

    root = _find_project_root(payload)
    if root is None:
        return {}
    agent_id = _agent_id(payload)
    if not agent_id:
        _record(root, "subagentstart_observed", {"mode": mode, "reason": "missing_agent_id"})
        return {}
    state = load_state(root / "loop-state.json")
    if field_mode_enabled():
        materialize_field_tasks(root, state)
    if field_mode_enabled():
        task = field_task_by_agent(state, agent_id)
        if task is None:
            candidates = [
                item for item in current_field_tasks(state, {"dispatching", "dispatched"})
                if not item.get("agent_id")
            ]
            # Claude exposes the child name as ``agent_type`` on
            # SubagentStart.  Preserve the parent Agent's requested name at
            # reservation time so parallel starts bind by identity, not by
            # timing/order.  Order-based fallback remains for integrations
            # that do not expose agent_type.
            agent_type = str(payload.get("agent_type") or "").strip().lower()
            if agent_type:
                named = [
                    item for item in candidates
                    if str(item.get("dispatch_name") or "").strip().lower() == agent_type
                ]
                if named:
                    candidates = named
            if candidates:
                # Claude may emit two SubagentStart events in an order that
                # differs from the parent tool responses.  The dispatch queue
                # is still the authoritative binding order; waiting for a
                # unique candidate leaves parallel fields unbound forever.
                # PostToolUse/SubagentStop add aliases when Claude exposes a
                # second identifier for the same child.
                # Re-select and bind under the dispatch lock; the local
                # candidate list may already be stale when sibling hooks race.
                requested_name = str(candidates[0].get("dispatch_name") or "")
                state, task = bind_field_task(root, agent_id, dispatch_name=requested_name)
        if task is not None:
            context = (
                f"RALPH 字段 Agent 已绑定任务 `{task.get('id')}`，只处理概念 `{task.get('concept')}`。"
                f"先读取 `{task.get('path')}`，把结果增量写入该文件的 field 对象；"
                "不要修改 loop-state.json、其他字段或完整事件日志。"
                f"填写后必须运行 `ralph field-apply . {task.get('path')}`；命令返回字段问题时只修复列出的项目并重试。"
            )
            _record(
                root,
                "field_task_bound",
                {"mode": mode, "agent_id": agent_id, "field_task_id": task.get("id"), "path": task.get("path")},
            )
            return {
                "hookSpecificOutput": {
                    "hookEventName": "SubagentStart",
                    "additionalContext": context,
                }
            }
    # The historical task-card protocol is deliberately not a fallback.  A
    # SubagentStart without a field binding is observable but unowned; letting
    # it run would make a later natural-language result look like completion.
    _record(
        root,
        "subagentstart_unbound",
        {
            "mode": mode,
            "agent_id": agent_id,
            "agent_type": payload.get("agent_type"),
            "reason": "no current field task binding",
        },
    )
    return {"systemMessage": "RALPH：该子代理没有绑定当前字段任务；不要写入项目或提交结果。"}


def _parse_gate_review(output: str) -> tuple[dict[str, Any] | None, str | None]:
    marker = "<RALPH_GATE_REVIEW>"
    if marker not in output:
        return None, f"缺少 {marker} 标记"
    content = output.split(marker, 1)[1].lstrip()
    if content.startswith("```"):
        parts = content.split("\n", 1)
        content = parts[1] if len(parts) == 2 else ""
    start = content.find("{")
    if start < 0:
        return None, "门禁回执中没有 JSON 对象"
    try:
        parsed, _ = json.JSONDecoder().raw_decode(content[start:])
    except json.JSONDecodeError as exc:
        return None, f"门禁回执 JSON 无法解析：{exc.msg}"
    if not isinstance(parsed, Mapping):
        return None, "门禁回执必须是 JSON 对象"
    return dict(parsed), None


def _gate_review_error(card: Mapping[str, Any], review: Mapping[str, Any]) -> str | None:
    schema = card.get("output_schema", {})
    required = schema.get("required", []) if isinstance(schema, Mapping) else []
    missing = [str(key) for key in required if key not in review or review.get(key) in (None, "")]
    if missing:
        return "门禁回执缺少字段：" + ", ".join(missing)
    if str(review.get("reviewer_card_id", "")) != str(card.get("id", "")):
        return "门禁回执 reviewer_card_id 与绑定任务卡不一致"
    allowed_verdicts = schema.get("verdict_values", []) if isinstance(schema, Mapping) else []
    if allowed_verdicts and review.get("verdict") not in allowed_verdicts:
        return "门禁回执 verdict 不在允许值中"
    checks = review.get("checks")
    if not isinstance(checks, list) or not checks:
        return "门禁回执 checks 必须是非空列表"
    allowed_check_status = schema.get("check_status_values", []) if isinstance(schema, Mapping) else []
    for index, check in enumerate(checks):
        if not isinstance(check, Mapping):
            return f"门禁回执 checks[{index}] 必须是对象"
        if allowed_check_status and check.get("status") not in allowed_check_status:
            return f"门禁回执 checks[{index}].status 不在允许值中"
    return None


def _gate_receipt_format(card: Mapping[str, Any]) -> str:
    """Return a small fill-in skeleton for a rejected gate receipt."""

    schema = card.get("output_schema", {})
    schema = schema if isinstance(schema, Mapping) else {}
    verdicts = schema.get("verdict_values", ["pass", "rollback", "blocked_human"])
    statuses = schema.get("check_status_values", ["pass", "fail", "uncertain"])
    required = schema.get("required", [])
    example = {
        "reviewer_card_id": str(card.get("id", "<card-id>")),
        "verdict": "pass",
        "recommended_action": "advance",
        "checked_input_refs": ["<document-ref>"],
        "checked_output_refs": [],
        "checks": [
            {
                "criterion": "填写一项实际审计标准",
                "status": "pass",
                "evidence_refs": [],
                "note": "说明检查结果，不要只写通过。",
            }
        ],
        "blocking_findings": [],
        "summary": "用已有审计结果填写简短总结。",
    }
    return (
        "必须包含字段："
        + ", ".join(str(item) for item in required)
        + f"；verdict 只能是 {list(verdicts)}；checks.status 只能是 {list(statuses)}。"
        "下面是填写骨架，尖括号内容必须替换，不能原样提交：\n"
        "<RALPH_GATE_REVIEW>\n"
        + json.dumps(example, ensure_ascii=False, indent=2)
        + "\n</RALPH_GATE_REVIEW>"
    )


def _write_gate_review_artifact(root: Path, card_id: str, review: Mapping[str, Any]) -> str:
    digest = _output_digest(json.dumps(review, ensure_ascii=False, sort_keys=True))
    artifact_dir = root / "loop-artifacts" / "gate-reviews"
    artifact_dir.mkdir(parents=True, exist_ok=True)
    safe_card_id = card_id.replace("/", "_")
    artifact_path = artifact_dir / f"{safe_card_id}-{digest}.json"
    if not artifact_path.exists():
        artifact_path.write_text(json.dumps(review, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return str(artifact_path.relative_to(root))


def _slice_still_skeleton(root: Path, slice_ref: str, state: Mapping[str, Any]) -> bool:
    """True when the builder's slice is byte-identical to the prefilled skeleton.

    The runtime pre-writes an editable skeleton so the builder only has to Edit
    fields.  A builder that merely returns the JSON as text leaves the file
    untouched; that must be blocked, not accepted as "written".
    """

    path = root / slice_ref
    try:
        current = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return False
    task_id = Path(slice_ref).stem
    skeleton = _skeleton_for_slice(state, slice_ref, task_id)
    if skeleton is None:
        return False
    return current == skeleton


def _skeleton_for_slice(state: Mapping[str, Any], slice_ref: str, task_id: str) -> Any | None:
    """Reconstruct the prefilled skeleton for a slice, at the slice's own stage/revision.

    The skeleton is ``payload[task_id]`` of the submission template.  It must be
    built for the *slice's* stage and revision (encoded in its path), not the
    current ``state`` revision — otherwise a revision bump makes a freshly
    generated skeleton differ from the on-disk one and the unfilled check
    false-negatives.
    """

    parts = Path(slice_ref).parts
    try:
        idx = parts.index("stages")
        stage_id = str(parts[idx + 1])
        revision = str(parts[idx + 2])
    except (ValueError, IndexError):
        stage_id = str(state.get("stage", {}).get("id", ""))
        revision = str(state.get("stage", {}).get("revision", "r1"))
    if not stage_id:
        return None
    rebuilt = dict(state)
    rebuilt["stage"] = {**state.get("stage", {}), "id": stage_id, "revision": revision}
    try:
        payload = stage_submission_template(rebuilt).get("payload", {})
    except Exception:
        return None
    return payload.get(task_id)


def _slice_missing_roles(
    root: Path, slice_ref: str, state: Mapping[str, Any], roles: list[str] | None = None
) -> list[str]:
    """Semantic roles still empty in a task_spec slice (drives incremental fill).

    When ``roles`` is given (a field-group builder), only those roles are
    checked against the partial file.  Otherwise all ``SEMANTIC_ROLES`` are
    checked (canonical slice).  Returns the still-empty roles.
    """

    task_id = Path(slice_ref).stem
    if not task_id.startswith("task_spec"):
        return []
    roles_to_check = list(roles) if roles else list(SEMANTIC_ROLES)
    try:
        current = json.loads((root / slice_ref).read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return list(roles_to_check)
    if not isinstance(current, Mapping):
        return list(roles_to_check)
    semantic_map = current.get("semantic_map", {})
    filled_roles = set()
    if isinstance(semantic_map, Mapping):
        for role in roles_to_check:
            value = semantic_map.get(role)
            if isinstance(value, list) and value:
                filled_roles.add(role)
            elif isinstance(value, str) and value.strip():
                filled_roles.add(role)
    matrix = current.get("attribute_matrix", [])
    if isinstance(matrix, list):
        for entry in matrix:
            if isinstance(entry, Mapping) and entry.get("role") in roles_to_check:
                filled_roles.add(entry["role"])
    return [role for role in roles_to_check if role not in filled_roles]


def _revert_card_to_pending(root: Path, card_id: str) -> None:
    """Undo a hollow completion so the Commander must actually re-run the card."""

    state = load_state(root / "loop-state.json")
    if field_mode_enabled():
        materialize_field_tasks(root, state)
    card = state.get("subagent_cards", {}).get(str(card_id))
    if not isinstance(card, Mapping):
        return
    card = dict(card)
    card["status"] = "pending"
    card["agent_id"] = None
    card.pop("completed_at", None)
    card["gate_verdict"] = None
    card["gate_review_ref"] = None
    state.setdefault("subagent_cards", {})[str(card_id)] = card
    save_state(root / "loop-state.json", state)
    materialize_contract_documents(root, state)


def handle_subagentstop(payload: Mapping[str, Any], mode: str = "hybrid") -> dict[str, Any]:
    """Close asynchronous task cards when Claude Code reports a subagent stop."""

    root = _find_project_root(payload)
    if root is None:
        return {}
    agent_id = _agent_id(payload)
    if not agent_id:
        _record(root, "subagentstop_observed", {"mode": mode, "reason": "missing_agent_id"})
        return {}
    state = load_state(root / "loop-state.json")
    if field_mode_enabled():
        materialize_field_tasks(root, state)
    if field_mode_enabled():
        field_task = field_task_by_agent(state, agent_id)
        if field_task is not None:
            concept = str(field_task.get("concept", ""))
            matrix = (state.get("task_spec", {}) or {}).get("attribute_matrix", [])
            current = next(
                (item for item in matrix if isinstance(item, Mapping) and str(item.get("concept", "")) == concept),
                None,
            ) if isinstance(matrix, list) else None
            stop_reason = str(payload.get("stop_reason", "")).lower()
            failed = bool(payload.get("error")) or stop_reason in {"error", "failed", "cancelled", "aborted"}
            disposition = str(current.get("disposition", "")) if isinstance(current, Mapping) else ""
            complete = disposition in {"confirmed", "inferred", "assumed_default"}
            apply_count = int(field_task.get("apply_count", 0) or 0)
            apply_baseline = int(field_task.get("apply_count_at_dispatch", 0) or 0)
            applied_this_run = apply_count > apply_baseline
            if failed or (not complete and not applied_this_run):
                state = update_field_task_metadata_transaction(
                    root,
                    str(field_task["id"]),
                    status="ready",
                    last_error=("子代理异常退出" if failed else "子代理结束前未通过 field-apply"),
                )
                _record(
                    root,
                    "field_task_reopened",
                    {
                        "mode": mode,
                        "agent_id": agent_id,
                        "field_task_id": field_task.get("id"),
                        "concept": concept,
                        "reason": "failed" if failed else "field_not_applied",
                    },
                )
                return {
                    "systemMessage": (
                        f"RALPH 字段任务 `{field_task.get('id')}` 尚未形成可接受字段，已恢复 ready；"
                        "不要把自然语言回执当成完成。下次由 Commander 重新派发该单字段 Agent，"
                        "并让它写任务文件后运行 field-apply。"
                    )
                }
            # An incomplete but successfully applied draft is still a valid
            # field attempt.  Defer it until the next supervisor context so
            # the Commander can process other ready fields without an
            # immediate same-context retry loop.  It is not terminal: the
            # stage gate still needs the missing evidence.
            state = update_field_task_metadata_transaction(
                root,
                str(field_task["id"]),
                status="deferred",
            )
            _record(
                root,
                "field_task_deferred",
                {
                    "mode": mode,
                    "agent_id": agent_id,
                    "field_task_id": field_task.get("id"),
                    "concept": concept,
                    "reason": "incomplete draft applied; retry at next supervisor context",
                },
            )
            return {}
    # Field-centric mode has no card/auditor fallback.  A lifecycle event
    # without a current field binding is recorded only; it cannot mutate state.
    _record(
        root,
        "subagentstop_unbound",
        {"mode": mode, "agent_id": agent_id, "reason": "no current field task binding"},
    )
    return {}


def handle_userpromptsubmit(payload: Mapping[str, Any], mode: str = "hybrid") -> dict[str, Any]:
    """Persist every human clarification as canonical task input before Claude sees it."""

    root = _find_project_root(payload)
    if root is None:
        return {}
    text = payload.get("prompt") or payload.get("user_prompt") or ""
    if not isinstance(text, str) or not text.strip():
        return {}
    state = load_state(root / "loop-state.json")
    updated = record_human_input(state, text)
    # Claude Code sends Hook-injected recovery text through the same event as
    # an actual human message.  The state helper returns an unchanged copy for
    # such generated prompts; do not write a misleading human-input event or
    # regenerate contracts in that case.
    if updated == state:
        return {}
    save_state(root / "loop-state.json", updated)
    materialize_contract_documents(root, updated)
    _record(
        root,
        "human_input_received",
        {"mode": mode, "stage": updated.get("stage", {}).get("id"), "characters": len(text.strip())},
        output=text.strip(),
    )
    return {}


def handle_precompact(payload: Mapping[str, Any], mode: str = "hybrid") -> dict[str, Any]:
    """Record a compaction attempt without ever blocking it.

    PreCompact is deliberately observational. Blocking compaction while the
    local backend is under memory pressure would remove the recovery path we
    are trying to protect.
    """

    root = _find_project_root(payload)
    if root is None:
        return {}
    _record(
        root,
        "context_compaction_started",
        {
            "mode": mode,
            "trigger": _bounded_hook_text(payload.get("trigger"), 80) or "unknown",
            "session_id": _bounded_hook_text(payload.get("session_id"), 160),
            "custom_instructions_characters": len(_bounded_hook_text(payload.get("custom_instructions"))),
        },
    )
    return {}


def handle_postcompact(payload: Mapping[str, Any], mode: str = "hybrid") -> dict[str, Any]:
    """Record completion and a bounded excerpt of Claude's compact summary."""

    root = _find_project_root(payload)
    if root is None:
        return {}
    summary = _bounded_hook_text(payload.get("compact_summary"), 2400)
    _record(
        root,
        "context_compaction_completed",
        {
            "mode": mode,
            "trigger": _bounded_hook_text(payload.get("trigger"), 80) or "unknown",
            "session_id": _bounded_hook_text(payload.get("session_id"), 160),
            "summary_characters": len(summary),
            "summary_recorded": bool(summary),
        },
        output=summary or None,
    )
    return {}


def handle_stop(
    payload: Mapping[str, Any],
    mode: str = "hybrid",
    auto_apply: bool = True,
    stop_policy: str = "fresh",
) -> dict[str, Any]:
    if stop_policy not in STOP_POLICIES:
        stop_policy = "fresh"
    root = _find_project_root(payload)
    if root is None:
        return {}
    state = load_state(root / "loop-state.json")
    if field_mode_enabled():
        materialize_field_tasks(root, state)
        save_state(root / "loop-state.json", state)
    if state.get("status") in {"completed", "stopped"}:
        return {}
    if state.get("status") == "blocked_human":
        output = payload.get("last_assistant_message")
        if not isinstance(output, str) or "<RALPH_STAGE_RESULT>" not in output:
            _record(
                root,
                "stop_allowed_human_block_waiting",
                {
                    "stage": state.get("stage", {}).get("id"),
                    "revision": state.get("stage", {}).get("revision"),
                    "state_preserved": True,
                },
            )
            return {}

    stop_hook_active = bool(payload.get("stop_hook_active"))
    inline_stop = stop_policy == "inline"

    # Infrastructure failures must be handled before parsing the final Agent
    # message. In particular, an oMLX prefill rejection can arrive as text in
    # last_assistant_message; treating it as an invalid stage action would
    # generate a repair prompt and make the next request even larger.
    runtime = _classify_runtime_interruption(payload)
    if runtime is not None:
        kind, excerpt = runtime
        _record_runtime_interruption(root, state, payload, kind, excerpt)
        if stop_hook_active:
            _record(
                root,
                "stop_hook_guarded",
                {"reason": "runtime_interruption_already_guarded", "kind": kind},
            )
            return {}
        # No decision=block here: the only safe recovery from a rejected
        # prefill is a new, shorter context. The persisted state remains at
        # the same stage and can be resumed explicitly.
        return {"systemMessage": _runtime_stop_message(state, kind, excerpt)[:3000]}

    # A Commander is allowed to finish its current turn while a field worker
    # is still running.  The outer supervisor owns recovery if Claude exits
    # without a SubagentStop event; hybrid mode must not trap a weak local
    # model in a StopHook/read loop just because a durable task is dispatched.
    output = payload.get("last_assistant_message")
    candidate_action = None
    if auto_apply and isinstance(output, str) and output.strip():
        # Peek only at the action name for diagnostics.  The old task-card
        # exception is no longer part of the active protocol.
        try:
            candidate_action = parse_action(output)
        except Exception:
            candidate_action = None

    waiting_field_tasks = current_field_tasks(state, {"dispatching", "dispatched"})
    if waiting_field_tasks and not stop_hook_active:
        task_ids = [str(task.get("id", "?")) for task in waiting_field_tasks]
        _record(
            root,
            "stop_blocked_waiting_for_field_agents",
            {
                "field_task_ids": task_ids,
                "state_preserved": True,
                "advance_allowed": False,
                "recovery": "wait_for_subagent_stop_then_field_apply",
            },
        )
        reason = (
            "RALPH 字段 Agent 仍标记为运行中（"
            + ", ".join(task_ids)
            + "）。hybrid 模式允许本轮结束；supervisor 会检查是否有真实进程，"
            "并在没有 field-apply/SubagentStop 时自动重开任务。不要把它们标记为完成或 blocked_human。"
        )
        if inline_stop:
            return _inline_stop_response(
                root,
                state,
                reason=(
                    "字段 Agent 仍在运行。不要重派、不要改写任务状态；"
                    "等待 SubagentStop 回执，或检查它已写入的单字段草稿后运行 field-apply。"
                ),
                output=output if isinstance(output, str) else None,
                event_reason="waiting_for_field_agents",
            )
        if mode == "enforce":
            return {"decision": "block", "reason": reason}
        return {"systemMessage": "RALPH hybrid：" + reason}
    if waiting_field_tasks and stop_hook_active:
        _record(
            root,
            "stop_blocked_waiting_for_field_agents",
            {
                "field_task_ids": [str(task.get("id", "?")) for task in waiting_field_tasks],
                "state_preserved": True,
                "stop_hook_active": True,
            },
        )
        if inline_stop:
            return _inline_stop_response(
                root,
                state,
                reason="字段 Agent 尚未完成；继续等待 SubagentStop，不要启动新的上下文或重复派发。",
                output=output if isinstance(output, str) else None,
                event_reason="waiting_for_field_agents_reentry",
            )
        if mode == "enforce":
            return {
                "decision": "block",
                "reason": "字段 Agent 尚未完成；继续等待 SubagentStop，不要启动新的上下文。",
            }
        return {
            "systemMessage": (
                "RALPH hybrid：字段 Agent 尚未完成；允许本轮结束，supervisor 将从任务文件恢复。"
            )
        }

    result: dict[str, Any] | None = None
    if auto_apply and isinstance(output, str) and output.strip():
        result = _apply_agent_result(root, output)
        if result["status"] == "duplicate":
            _record(
                root,
                "stop_hook_guarded",
                {"reason": "duplicate_agent_output", "output_sha256": result["output_sha256"]},
            )
            # Never allow an idle stop on a no-progress duplicate: keep the
            # Commander in the loop and point it at the next concrete action.
            duplicate_reason = (
                "该结构化阶段结果已经应用过（重复输出），状态已保存且未改变。请勿重复提交；"
                "直接按当前阶段继续唯一允许的下一个动作：若有 ready 字段就派发它，"
                "否则修复草稿或输出 advance / clarify。"
            )
            if inline_stop:
                return _inline_stop_response(
                    root,
                    state,
                    reason=duplicate_reason,
                    output=output,
                    event_reason="duplicate_agent_output",
                )
            return _stop_response(duplicate_reason, mode, stop_policy)
        if result["status"] == "applied":
            state = load_state(root / "loop-state.json")
            action = result["action"]
            if state.get("status") in {"completed", "stopped"}:
                return {}
            # A human block is a terminal result for this Commander turn. Do
            # not return decision=block here: that would make Claude continue
            # the same context after the state was already persisted, often
            # producing an unnecessary ToolSearch/read loop. The question
            # bundle is already in the applied action and event log; allow
            # the session to stop and let the next human reply resume it.
            if state.get("status") == "blocked_human":
                _record(
                    root,
                    "stop_allowed_after_apply",
                    {
                        "action": action["action"],
                        "stage": state.get("stage", {}).get("id"),
                        "status": "blocked_human",
                        "state_preserved": True,
                    },
                )
                return {}
            prompt = PromptRenderer().compact_recovery_prompt(
                state,
                reason=f"已自动应用动作 {action['action']}",
                error_kind="continuation",
                action_hint="读取新的当前阶段后继续；不要复制完整计划，不要重做已完成阶段。",
            ).text
            reason = (
                f"RALPH 已自动应用动作 `{action['action']}`，状态已保存。"
                "请继续执行新的当前阶段：\n"
                + prompt
            )
            if inline_stop:
                return _inline_stop_response(
                    root,
                    state,
                    reason=reason,
                    output=output,
                    event_reason="action_applied",
                )
            if stop_hook_active:
                _record(
                    root,
                    "stop_hook_guarded",
                    {"reason": "stop_hook_active_after_new_action", "output_sha256": result["output_sha256"]},
                )
                return {"systemMessage": reason[:12000]}
            _record(
                root,
                "stop_intercepted_after_apply",
                {"action": action["action"], "stage": state.get("stage", {}).get("id")},
            )
            return _stop_response(reason, mode, stop_policy)

        # Invalid output is not allowed to alter state. Give the Agent a
        # generated repair prompt; enforce mode turns it into a real block.
        state = load_state(root / "loop-state.json")
        repair = PromptRenderer().repair_prompt(
            state,
            result["error"],
            raw_output=output,
        ).text
        reason = (
            "RALPH_STAGE_RESULT 未通过字段或状态校验：\n"
            + repair
            + "\n本次原始结果已保存为阶段工件："
            + str(result["artifact_ref"])
            + "\n需要机械复核时只运行：ralph validate . --result "
            + str(result["artifact_ref"])
        )
        _record(
            root,
            "stage_result_repair_prompted",
            {"error": result["error"], "artifact_ref": result["artifact_ref"]},
        )
        repair_count = _consecutive_protocol_rejections(root)
        if repair_count >= MAX_PROTOCOL_REPAIRS_PER_CONTEXT:
            if inline_stop:
                strategy_reason = (
                    "同一上下文已连续输出无效阶段结果。不要继续修补 XML/JSON 格式，也不要退出重开；"
                    "先停止输出 RALPH_STAGE_RESULT，检查当前阶段、任务文件和上一次校验错误，"
                    "然后执行一个能产生新证据的工具动作。\n\n"
                    + repair
                )
                return _inline_stop_response(
                    root,
                    state,
                    reason=strategy_reason,
                    output=output,
                    event_reason="protocol_strategy_revision",
                )
            # Returning only a systemMessage deliberately allows Claude to
            # stop.  The durable state is unchanged; the outer supervisor
            # observes the exit and starts a fresh context with a compact
            # prompt.  This is the escape hatch for a same-context XML/JSON
            # repair loop.
            _record(
                root,
                "stage_result_repair_exhausted",
                {
                    "repair_count": repair_count,
                    "max_repairs": MAX_PROTOCOL_REPAIRS_PER_CONTEXT,
                    "recovery": "outer_ralph_loop_fresh_context",
                    "state_preserved": True,
                },
            )
            return {
                "systemMessage": render_feedback(
                    "REPAIR_BUDGET_EXHAUSTED",
                    detected=(
                        f"当前 Claude 上下文已连续 {repair_count} 次输出无效阶段结果。"
                    ),
                    correction=(
                        "结束当前上下文；RALPH 外层监督器会读取持久化状态并启动新的短上下文。"
                    ),
                    next_action="不要继续输出 XML、半截 JSON、自然语言或重复读取历史日志。",
                    forbidden="修改 loop-state.json、伪造已通过、继续同一格式修复循环。",
                )[:3000]
            }
        if stop_hook_active and not inline_stop:
            _record(
                root,
                "stop_hook_guarded",
                {"reason": "invalid_result_after_stop_hook", "output_sha256": result["output_sha256"]},
            )
            # Block the stop so the model is forced to fix the malformed
            # RALPH_STAGE_RESULT in the same context (the repair prompt is in
            # `reason`). Returning only a systemMessage would let Claude Code
            # end the turn and idle; the outer loop would then relaunch a fresh
            # context instead of repairing inline. The repair budget escape
            # hatch above still allows a stop once MAX_PROTOCOL_REPAIRS_PER_CONTEXT
            # is reached.
            return _stop_response(reason, mode, stop_policy)
        if inline_stop:
            return _inline_stop_response(
                root,
                state,
                reason=reason,
                output=output,
                event_reason="invalid_stage_result",
            )
        return _stop_response(reason, mode, stop_policy)

    if stop_hook_active and not inline_stop:
        _record(root, "stop_hook_guarded", {"reason": "stop_hook_active"})
        return {}

    prompt = PromptRenderer().compact_recovery_prompt(
        state,
        reason="Stop Hook 收到停止信号，但没有收到可应用的结构化阶段动作。",
        error_kind="continuation",
    ).text
    reason = (
        render_feedback(
            "STOP_WITHOUT_ACTION",
            detected="Stop Hook 没有收到可应用的 RALPH_STAGE_RESULT，也没有可确认的阶段完成动作。",
            correction="不要把普通总结、READY 或空消息当成阶段完成。",
            next_action="按下面的短恢复指令执行当前阶段唯一允许的动作。",
            forbidden="重做历史、完整读取 loop-events.md、直接修改状态或重复派发。",
        )
        + "\n"
        + prompt
    )
    _record(root, "stop_intercepted", {"status": state.get("status"), "stage": state.get("stage", {}).get("id")})
    if inline_stop:
        return _inline_stop_response(
            root,
            state,
            reason=reason,
            output=output if isinstance(output, str) else None,
            event_reason="stop_without_action",
        )
    return _stop_response(reason, mode, stop_policy)


def handle_hook(
    event: str,
    payload: Mapping[str, Any],
    mode: str = "hybrid",
    auto_apply: bool = True,
    stop_policy: str = "fresh",
) -> dict[str, Any]:
    if event == "pretooluse":
        return handle_pretooluse(payload, mode)
    if event == "posttooluse":
        return handle_posttooluse(payload, mode)
    if event == "subagentstart":
        return handle_subagentstart(payload, mode)
    if event == "subagentstop":
        return handle_subagentstop(payload, mode)
    if event == "userpromptsubmit":
        return handle_userpromptsubmit(payload, mode)
    if event == "precompact":
        return handle_precompact(payload, mode)
    if event == "postcompact":
        return handle_postcompact(payload, mode)
    if event == "stop":
        return handle_stop(payload, mode, auto_apply=auto_apply, stop_policy=stop_policy)
    raise ValueError(f"unsupported Hook event: {event}")


def run_hook(
    event: str,
    payload_text: str,
    mode: str = "hybrid",
    auto_apply: bool = True,
    stop_policy: str = "fresh",
) -> str:
    payload = json.loads(payload_text or "{}")
    result = handle_hook(event, payload, mode, auto_apply=auto_apply, stop_policy=stop_policy)
    if event == "stop":
        # Canonical turn-completion marker. Claude idles at the interactive
        # prompt after a Stop and never exits on its own, so the outer
        # `ralph loop` supervisor watches for this marker and relaunches the
        # next fresh context immediately. A blocked Stop must not emit this
        # marker: field Agents belong to the current Claude context and would
        # otherwise be killed before SubagentStop arrives.
        root = _find_project_root(payload)
        if root is not None and result.get("decision") != "block":
            _record(
                root,
                "ralph_stop_handled",
                {"mode": mode, "auto_apply": auto_apply, "stop_policy": stop_policy},
            )
    return json.dumps(result, ensure_ascii=False)
