"""Append-only Markdown event journal for RALPH."""

from __future__ import annotations

import hashlib
import json
import re
import uuid
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable, Mapping

from .contracts import materialize_contract_documents
from .protocol import ActionResult, parse_action
from .result_artifacts import stage_artifact_dir
from .task_board import TaskBoardError, claim_task_reference
from .state import (
    apply_action,
    load_state,
    record_human_input,
    reset_subagent_card,
    save_state,
    set_task,
    update_subagent_card,
)


EVENT_START = "<!-- RALPH_EVENT"
EVENT_END = "RALPH_EVENT -->"
EVENT_BLOCK_RE = re.compile(
    r"<!--\s*RALPH_EVENT\s*\n(?P<meta>\{.*?\})\s*\nRALPH_EVENT\s*-->\s*",
    flags=re.DOTALL,
)


def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def event_type(action: str) -> str:
    return {
        "advance": "stage_advanced",
        "rollback": "stage_rollback",
        "blocked_human": "blocked_human",
        "skip_blocked": "blocked_task_skipped",
        "candidate": "candidate_created",
        "explore": "exploration_started",
        "dispatch": "task_dispatched",
        "join": "parallel_joined",
        "clarify": "task_spec_clarified",
        "repair_prompt": "prompt_repair_requested",
    }.get(action, "action_recorded")


def output_excerpt(output: str | None, limit: int = 4000) -> str:
    if not output:
        return ""
    clean = output.replace(EVENT_START, "<!-- RALPH_EVENT_REMOVED").replace(EVENT_END, "RALPH_EVENT_REMOVED -->")
    if len(clean) <= limit:
        return clean
    return clean[:limit] + "\n\n[… output excerpt truncated …]"


def _hash_state(state: Mapping[str, Any]) -> str:
    encoded = json.dumps(state, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(encoded.encode("utf-8")).hexdigest()


def build_event(
    action: ActionResult,
    before: Mapping[str, Any],
    after: Mapping[str, Any],
    raw_output: str | None = None,
    validation: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    return {
        "event_id": str(uuid.uuid4()),
        "type": event_type(action.action),
        "timestamp": now_iso(),
        "stage": action.stage_id,
        "revision": action.revision,
        "action": action.to_dict(),
        "state_before_sha256": _hash_state(before),
        "state_after_sha256": _hash_state(after),
        "validation": dict(validation or {"status": "passed"}),
        "output_excerpt": output_excerpt(raw_output),
        "output_sha256": hashlib.sha256(raw_output.encode("utf-8")).hexdigest() if raw_output else None,
    }


def append_event(
    path: str | Path,
    event: Mapping[str, Any],
    agent_output: str | None = None,
    validation: str | None = None,
    artifacts: Iterable[str] = (),
) -> None:
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    action = event.get("action", {})
    stage = action.get("stage_id", event.get("stage", "?")) if isinstance(action, Mapping) else event.get("stage", "?")
    revision = action.get("revision", event.get("revision", "?")) if isinstance(action, Mapping) else event.get("revision", "?")
    event_copy = dict(event)
    if agent_output is not None:
        event_copy["output_excerpt"] = output_excerpt(agent_output)
    event_copy["artifact_refs"] = list(artifacts)
    metadata = json.dumps(event_copy, ensure_ascii=False, sort_keys=True, indent=2)
    output = event_copy.get("output_excerpt", "")
    validation_text = validation or json.dumps(event_copy.get("validation", {}), ensure_ascii=False, sort_keys=True)
    artifact_text = "\n".join(f"- {item}" for item in event_copy["artifact_refs"]) or "- none"
    block = (
        f"## {stage}-{revision} | {event_copy.get('type', 'event')}\n\n"
        f"{EVENT_START}\n{metadata}\n{EVENT_END}\n\n"
        "### Agent 输出摘录\n\n"
        f"{output}\n\n"
        "### 验证结果\n\n"
        f"{validation_text}\n\n"
        "### 文件和证据\n\n"
        f"{artifact_text}\n\n"
    )
    with path.open("a", encoding="utf-8") as handle:
        handle.write(block)


def read_events(path: str | Path) -> list[dict[str, Any]]:
    path = Path(path)
    if not path.exists():
        return []
    events: list[dict[str, Any]] = []
    for match in EVENT_BLOCK_RE.finditer(path.read_text(encoding="utf-8")):
        try:
            value = json.loads(match.group("meta"))
        except json.JSONDecodeError as exc:
            raise ValueError(f"invalid RALPH event metadata in {path}: {exc}") from exc
        if not isinstance(value, dict) or "event_id" not in value:
            raise ValueError(f"RALPH event metadata missing event_id in {path}")
        events.append(value)
    return events


def _replay_observation(state: Mapping[str, Any], event: Mapping[str, Any]) -> dict[str, Any]:
    """Apply the state-bearing subset of an append-only observation event.

    Hook events are deliberately more verbose than state transitions.  Most
    are diagnostic only, but a small subset records exactly the lifecycle
    mutations made by the controller.  Replaying those restores the current
    task and task-card truth, rather than merely the numbered workflow stage.
    """

    observation = event.get("observation")
    if not isinstance(observation, Mapping):
        return dict(state)
    event_type = str(event.get("type", ""))
    updated = dict(state)

    if event_type == "session_started":
        task = observation.get("task")
        current = updated.get("task", {})
        current_text = current.get("description") if isinstance(current, Mapping) else ""
        if isinstance(task, str) and task.strip() and task != current_text:
            return set_task(updated, task)
        return updated

    if event_type == "human_input_received":
        text = event.get("output_excerpt")
        if isinstance(text, str) and text.strip():
            return record_human_input(updated, text)
        return updated

    if event_type == "task_board_claimed":
        intake = updated.get("task_intake")
        if isinstance(intake, Mapping):
            intake_copy = dict(intake)
            intake_copy["board_status"] = "claimed"
            updated["task_intake"] = intake_copy
        return updated

    card_id = observation.get("task_card_id")
    if not isinstance(card_id, str) or not card_id:
        return updated
    cards = updated.get("subagent_cards", {})
    if not isinstance(cards, Mapping) or card_id not in cards:
        # A malformed or historical observation must not make replay fail.
        return updated
    agent_id = observation.get("agent_id")
    agent_id = str(agent_id) if agent_id else None

    if event_type == "pretooluse_observed":
        if observation.get("tool_name") == "Agent" and observation.get("decision") == "allow":
            return update_subagent_card(updated, card_id, "dispatched")
        return updated

    if event_type == "posttooluse_observed":
        status = observation.get("task_card_status")
        if status in {"pending", "dispatched", "completed", "failed"}:
            return update_subagent_card(updated, card_id, str(status), agent_id=agent_id)
        return updated

    if event_type in {"subagent_card_bound", "subagent_card_bound_on_stop"}:
        return update_subagent_card(updated, card_id, "dispatched", agent_id=agent_id)

    if event_type == "subagent_card_completed":
        return update_subagent_card(updated, card_id, "completed", agent_id=agent_id)

    if event_type == "subagent_card_failed":
        return update_subagent_card(updated, card_id, "failed", agent_id=agent_id)

    if event_type == "subagent_card_reconciled":
        outcome = str(observation.get("outcome", ""))
        if outcome == "completed":
            reconciled = update_subagent_card(updated, card_id, "completed", agent_id=agent_id)
            card = reconciled.get("subagent_cards", {}).get(card_id)
            if isinstance(card, dict):
                if observation.get("gate_review_ref"):
                    card["gate_review_ref"] = observation.get("gate_review_ref")
                if observation.get("gate_verdict"):
                    card["gate_verdict"] = observation.get("gate_verdict")
                card["reconciled_from"] = "dispatched"
            return reconciled
        if outcome == "pending":
            try:
                return reset_subagent_card(updated, card_id, allow_dispatched=True)
            except (KeyError, ValueError):
                return updated
        return updated

    if event_type == "subagent_card_recovered":
        try:
            prior_agent_id = observation.get("prior_agent_id")
            if prior_agent_id:
                current_status = str(cards[card_id].get("status", "completed"))
                if current_status in {"completed", "failed"}:
                    updated = update_subagent_card(
                        updated,
                        card_id,
                        current_status,
                        agent_id=str(prior_agent_id),
                    )
            return reset_subagent_card(updated, card_id)
        except (KeyError, ValueError):
            return updated
    return updated


def replay_events(initial_state: Mapping[str, Any], events: Iterable[Mapping[str, Any]]) -> dict[str, Any]:
    state = dict(initial_state)
    for event in events:
        raw_action = event.get("action")
        if isinstance(raw_action, Mapping):
            state = apply_action(state, parse_action(raw_action), enforce_contracts=False)
            state["last_event_id"] = event.get("event_id")
            continue
        state = _replay_observation(state, event)
    return state


def apply_and_record(
    state_path: str | Path,
    event_path: str | Path,
    raw_action: str | Mapping[str, Any],
    raw_output: str | None = None,
) -> dict[str, Any]:
    before = load_state(state_path)
    action = parse_action(raw_action)
    after = apply_action(before, action)
    project_root = Path(state_path).parent
    board_claim: dict[str, Any] | None = None
    intake = after.get("task_intake")
    if (
        action.action == "advance"
        and str(before.get("stage", {}).get("id", "")) == "exploration"
        and isinstance(intake, Mapping)
        and str(intake.get("source", "")) == "task_board"
    ):
        try:
            board_claim = claim_task_reference(
                project_root,
                str(intake.get("task_id", "")),
                str(intake.get("source_path", "tasks/TASKS.md")),
                claimant=str(before.get("project_id", "ralph")),
            )
        except TaskBoardError:
            # The board must be claimed before loop-state.json is persisted.
            # A failed claim therefore leaves the state transition unapplied.
            raise
        claimed_intake = dict(intake)
        claimed_intake["board_status"] = "claimed"
        after["task_intake"] = claimed_intake
    materialized = materialize_contract_documents(project_root, after)
    event = build_event(action, before, after, raw_output=raw_output)
    artifact_refs = list(action.artifact_refs) + materialized
    if raw_output:
        artifact_dir = stage_artifact_dir(project_root, action.stage_id, action.revision)
        artifact_dir.mkdir(parents=True, exist_ok=True)
        artifact_path = artifact_dir / f"{event['event_id']}.agent-output.md"
        artifact_path.write_text(raw_output, encoding="utf-8")
        artifact_refs.append(str(artifact_path.relative_to(Path(state_path).parent)))
        event["full_output_ref"] = artifact_refs[-1]
    append_event(event_path, event, agent_output=raw_output, artifacts=artifact_refs)
    if board_claim is not None:
        append_observation(
            event_path,
            "task_board_claimed",
            {
                "stage": "exploration",
                "revision": action.revision,
                "task_id": board_claim.get("task_id"),
                "source_path": board_claim.get("source_path"),
                "claim_status": board_claim.get("claim_status"),
                "claimant": board_claim.get("claimant"),
            },
        )
    after["last_event_id"] = event["event_id"]
    save_state(state_path, after)
    return after


def append_observation(
    path: str | Path,
    observation_type: str,
    payload: Mapping[str, Any],
    output: str | None = None,
    artifacts: Iterable[str] = (),
) -> dict[str, Any]:
    event = {
        "event_id": str(uuid.uuid4()),
        "type": observation_type,
        "timestamp": now_iso(),
        "observation": dict(payload),
    }
    if payload.get("stage") is not None:
        event["stage"] = payload["stage"]
    if payload.get("revision") is not None:
        event["revision"] = payload["revision"]
    append_event(path, event, agent_output=output, artifacts=artifacts)
    return event
