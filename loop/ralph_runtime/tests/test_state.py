from pathlib import Path

from ralph_runtime.protocol import parse_action
from ralph_runtime.state import (
    apply_action,
    create_state,
    load_state,
    reset_subagent_card,
    save_state,
    update_subagent_card,
)


def test_state_round_trip(tmp_path: Path):
    path = tmp_path / "loop-state.json"
    state = create_state("fixture")
    save_state(path, state)
    assert load_state(path) == state


def test_legacy_state_is_migrated():
    state = load_state(Path("/does/not/exist/loop-state.json"))
    assert state["schema_version"] == 4


def test_advance_preserves_full_next_node():
    state = create_state("fixture")
    action = parse_action('{"action":"advance","status":"passed","stage_id":"01","revision":"r1","next_stage":"02"}')
    updated = apply_action(state, action, enforce_contracts=False)
    assert updated["stage"]["name"] == "任务分解"
    assert updated["stage"]["required_outputs"]


def test_reset_subagent_card_clears_live_binding_and_dag_completion():
    state = create_state("fixture")
    card = next(iter(state["subagent_cards"].values()))
    completed = update_subagent_card(state, card["id"], "completed", agent_id="old-agent")

    recovered = reset_subagent_card(completed, card["id"])

    restored = recovered["subagent_cards"][card["id"]]
    assert restored["status"] == "pending"
    assert "agent_id" not in restored
    assert restored["last_agent_id"] == "old-agent"
    assert restored["recovery_count"] == 1
