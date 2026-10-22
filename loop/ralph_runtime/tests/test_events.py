import json
from pathlib import Path

from ralph_runtime.events import append_observation, apply_and_record, read_events, replay_events
from ralph_runtime.state import create_state, save_state
from conftest import complete_required_card, stage_one_payload


def test_markdown_event_round_trip(tmp_path: Path):
    state_path = tmp_path / "loop-state.json"
    event_path = tmp_path / "loop-events.md"
    state = complete_required_card(create_state("fixture"))
    save_state(state_path, state)
    raw = json.dumps({
        "action": "advance", "status": "passed", "stage_id": "01", "revision": "r1", "next_stage": "02",
        "payload": stage_one_payload(),
    }, ensure_ascii=False)
    updated = apply_and_record(state_path, event_path, raw, raw_output="stage output")
    events = read_events(event_path)
    assert len(events) == 1
    assert events[0]["type"] == "stage_advanced"
    assert events[0]["output_excerpt"] == "stage output"
    assert events[0]["output_sha256"]
    assert (tmp_path / events[0]["full_output_ref"]).read_text(encoding="utf-8") == "stage output"
    replayed = replay_events(create_state("fixture"), events)
    assert replayed["stage"]["id"] == updated["stage"]["id"] == "02"
    assert replayed["last_event_id"] == events[0]["event_id"]


def test_replay_restores_task_and_task_card_lifecycle_from_observations(tmp_path: Path):
    event_path = tmp_path / "loop-events.md"
    card_id = "01-r1-requirements-auditor"
    append_observation(event_path, "session_started", {"task": "调研金融时间序列"})
    append_observation(event_path, "human_input_received", {"stage": "01"}, output="资产为美股日频")
    append_observation(
        event_path,
        "pretooluse_observed",
        {"tool_name": "Agent", "decision": "allow", "task_card_id": card_id},
    )
    append_observation(
        event_path,
        "subagent_card_bound",
        {"task_card_id": card_id, "agent_id": "agent-old"},
    )
    append_observation(
        event_path,
        "subagent_card_completed",
        {"task_card_id": card_id, "status": "completed"},
    )
    append_observation(
        event_path,
        "subagent_card_recovered",
        {"task_card_id": card_id, "prior_agent_id": "agent-old", "reason": "invalid receipt"},
    )

    replayed = replay_events(create_state("fixture"), read_events(event_path))
    card = replayed["subagent_cards"][card_id]

    assert replayed["task"]["description"] == "调研金融时间序列"
    assert replayed["task_spec"]["authoritative_inputs"][-1]["text"] == "资产为美股日频"
    assert card["status"] == "pending"
    assert card["last_agent_id"] == "agent-old"
    assert card["recovery_count"] == 1
