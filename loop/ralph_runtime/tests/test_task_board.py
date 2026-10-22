import json
from pathlib import Path

import pytest

from ralph_runtime.cli import task_next
from ralph_runtime.events import apply_and_record, read_events, replay_events
from ralph_runtime.nodes import DEFAULT_GRAPH
from ralph_runtime.state import create_state, save_state, update_subagent_card
from ralph_runtime.task_board import TaskBoardError, claim_task_reference, parse_task_board, select_next_task


BOARD = """# TASKS

| ID | 任务 | 状态 | 优先级 | 依赖 | 说明 |
|---|---|---|---|---|---|
| F1 | 建立研究基线 | 📋 就绪 | P1 | — | first |
| F2 | 设计验证 | ⏳ 待办 | P1 | 依赖 F1 | second |
| F3 | 被阻塞 | 人类阻塞 | P0 | — | human |
"""


def test_task_board_selects_ready_and_respects_dependencies(tmp_path: Path):
    tasks = tmp_path / "tasks" / "TASKS.md"
    tasks.parent.mkdir()
    tasks.write_text(BOARD, encoding="utf-8")

    selected = select_next_task(tmp_path)
    assert selected is not None
    assert selected.task_id == "F1"
    assert selected.selection()["source"] == "task_board"

    with pytest.raises(TaskBoardError, match="next eligible"):
        claim_task_reference(tmp_path, "F2", claimant="fixture")

    claimed = claim_task_reference(tmp_path, "F1", claimant="fixture")
    assert claimed["claim_status"] == "claimed"
    text = tasks.read_text(encoding="utf-8")
    assert "RALPH:fixture" in text
    assert select_next_task(tmp_path) is None


def test_task_board_parses_checkbox_items():
    items = parse_task_board("- [ ] L1: 编译基线 P1\n- [x] L2: 完成修复 P1\n")
    assert [(item.task_id, item.status) for item in items] == [("L1", "pending"), ("L2", "completed")]


def test_task_next_is_read_only_and_returns_selection(tmp_path: Path):
    tasks = tmp_path / "tasks" / "TASKS.md"
    tasks.parent.mkdir()
    tasks.write_text(BOARD, encoding="utf-8")
    before = tasks.read_text(encoding="utf-8")

    result = task_next(tmp_path)

    assert result["ready"] is True
    assert result["selection"]["task_id"] == "F1"
    assert tasks.read_text(encoding="utf-8") == before


def _exploration_action() -> dict:
    return {
        "action": "advance",
        "status": "passed",
        "stage_id": "exploration",
        "revision": "r1",
        "next_stage": "01",
        "payload": {
            "stage_review": {
                "reviewer_card_id": "exploration-r1-exploration-auditor",
                "context_mode": "bounded_artifacts",
                "verdict": "pass",
                "recommended_action": "advance",
                "checked_input_refs": ["loop-artifacts/contracts/exploration-r1-stage-input-package.json"],
                "checked_output_refs": ["loop-artifacts/contracts/exploration-r1-submission-template.json"],
                "checks": [
                    {
                        "criterion": "任务板优先级和依赖已审计",
                        "status": "pass",
                        "evidence_refs": ["tasks/TASKS.md"],
                        "note": "F1 ready",
                    }
                ],
                "blocking_findings": [],
                "summary": "探索门禁通过",
            },
            "exploration": {
                "preference_brief": "优先完成已有研究基线",
                "scanned_sources": ["tasks/TASKS.md"],
                "selection_mode": "task_board",
                "selected_task": {
                    "task_id": "F1",
                    "title": "建立研究基线",
                    "source": "task_board",
                    "source_path": "tasks/TASKS.md",
                    "priority": "P1",
                    "reason": "ready 且没有未完成依赖",
                },
                "candidate_tasks": [],
            },
        },
    }


def test_valid_exploration_selection_claims_board_and_restarts_task(tmp_path: Path):
    tasks = tmp_path / "tasks" / "TASKS.md"
    tasks.parent.mkdir()
    tasks.write_text(BOARD, encoding="utf-8")
    state_path = tmp_path / "loop-state.json"
    event_path = tmp_path / "loop-events.md"
    state = create_state("fixture", task="旧任务")
    node = DEFAULT_GRAPH.get("exploration")
    state["stage"] = {"id": node.id, "revision": "r1", **node.to_dict()}
    gate = next(iter(state["subagent_cards"].values()))
    # The stage cards need to be regenerated after manually moving the fixture.
    from ralph_runtime.contracts import ensure_stage_cards

    state = ensure_stage_cards(state)
    gate = state["subagent_cards"]["exploration-r1-exploration-auditor"]
    state = update_subagent_card(state, gate["id"], "completed")
    save_state(state_path, state)

    updated = apply_and_record(state_path, event_path, _exploration_action())

    assert updated["stage"]["id"] == "01"
    assert updated["task"]["description"] == "建立研究基线"
    assert updated["task_intake"]["board_status"] == "claimed"
    assert "RALPH:fixture" in tasks.read_text(encoding="utf-8")
    assert "task_board_claimed" in event_path.read_text(encoding="utf-8")

    replay_initial = create_state("fixture", task="旧任务")
    replay_initial["stage"] = {"id": "exploration", "revision": "r1", **DEFAULT_GRAPH.get("exploration").to_dict()}
    replayed = replay_events(replay_initial, read_events(event_path))
    assert replayed["stage"]["id"] == updated["stage"]["id"]
    assert replayed["task"]["description"] == updated["task"]["description"]
    assert replayed["task_intake"]["board_status"] == "claimed"
