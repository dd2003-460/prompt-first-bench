from pathlib import Path
import sys

import pytest

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from ralph_runtime.state import update_subagent_card


@pytest.fixture(autouse=True)
def _isolate_ralph_global_config(tmp_path, monkeypatch):
    """Keep tests independent from a developer's real global browser login."""

    monkeypatch.setenv("XDG_CONFIG_HOME", str(tmp_path / "xdg-config"))


def complete_required_card(state, stage_id: str = "01"):
    state = dict(state)
    while True:
        pending = [
            card
            for card in state["subagent_cards"].values()
            if card["stage_id"] == stage_id
            and card["required_for_advance"]
            and card.get("status") != "completed"
        ]
        if not pending:
            break
        state = update_subagent_card(state, pending[0]["id"], "completed")
    return state


def gate_card_of(state, stage_id: str = "01"):
    return next(
        card
        for card in state["subagent_cards"].values()
        if card["stage_id"] == stage_id and card.get("is_stage_gate")
    )


def stage_review(stage_id: str, card_id: str):
    return {
        "reviewer_card_id": card_id,
        "context_mode": "bounded_artifacts",
        "verdict": "pass",
        "recommended_action": "advance",
        "checked_input_refs": [f"loop-artifacts/contracts/{stage_id}-r1-stage-input-package.json"],
        "checked_output_refs": ["RALPH_STAGE_RESULT.payload"],
        "checks": [
            {
                "criterion": "阶段契约已满足",
                "status": "pass",
                "evidence_refs": ["loop-artifacts/contracts/evidence.md"],
                "note": "独立门禁已核对。",
            }
        ],
        "blocking_findings": [],
        "summary": "独立门禁通过。",
    }


def stage_one_payload(card_id: str = "01-r1-requirements-auditor"):
    return {
        "stage_review": stage_review("01", card_id),
        "task_spec": {
            "semantic_map": {
                "background": ["本地 AI"],
                "decision_object": ["GPU"],
                "objective": ["性价比"],
                "comparison_set": ["候选 GPU"],
                "constraints": ["预算"],
                "deliverable": ["推荐报告"],
                "uncertainty": ["地区价格"],
            },
            "attribute_matrix": [
                {
                    "concept": "性价比",
                    "role": "objective",
                    "attribute": "性能/总成本",
                    "disposition": "research",
                    "rationale": "决定推荐排序",
                }
            ],
            "constraints": ["预算待确认"],
            "assumptions": [],
            "open_questions": [],
            "scenarios": [{"id": "S1", "name": "默认场景"}],
            "success_criteria": ["输出有证据的比较"],
            "requirements_audit": {
                "card_id": card_id,
                "artifact_ref": "loop-artifacts/audit.md",
                "summary": "已检查遗漏项",
            },
        }
    }
