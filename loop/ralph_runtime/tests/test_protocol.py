import json

import pytest

from ralph_runtime.protocol import ProtocolError, parse_action, validate_action
from ralph_runtime.state import create_state


def test_parse_marked_action_and_validate():
    action = parse_action(
        """说明文字\n<RALPH_STAGE_RESULT>\n{\"action\":\"advance\",\"status\":\"passed\",\"stage_id\":\"01\",\"revision\":\"r1\",\"next_stage\":\"02\"}\n</RALPH_STAGE_RESULT>"""
    )
    validate_action(action, create_state("fixture"), enforce_contracts=False)
    assert action.action == "advance"


def test_parse_marked_action_with_nested_candidate_payload():
    action = parse_action(
        """<RALPH_STAGE_RESULT>
        {"action":"candidate","status":"candidate","stage_id":"exploration","revision":"r1",
         "payload":{"title":"new task","research_summary":"evidence","reason":"fit","scope":"bounded",
         "preference_brief":"prefer evidence","scanned_sources":["tasks/TASKS.md"]}}
        </RALPH_STAGE_RESULT>"""
    )
    assert action.payload["title"] == "new task"


def test_invalid_action_does_not_validate():
    with pytest.raises(ProtocolError):
        parse_action('{"action":"invent","status":"x","stage_id":"01","revision":"r1"}')


def test_stage_mismatch_is_rejected():
    action = parse_action('{"action":"advance","status":"passed","stage_id":"02","revision":"r1","next_stage":"03"}')
    with pytest.raises(ProtocolError):
        validate_action(action, create_state("fixture"))


def test_candidate_requires_payload():
    action = parse_action('{"action":"candidate","status":"candidate","stage_id":"01","revision":"r1"}')
    with pytest.raises(ProtocolError):
        validate_action(action, create_state("fixture"))


def test_stage_one_accepts_high_confidence_inferred_attribute():
    state = create_state("fixture")
    state["task_spec"]["attribute_matrix"] = [
        {
            "concept": "goal", "role": "objective", "attribute": "有证据的本地 GPU 推荐",
            "disposition": "confirmed", "rationale": "用户目标", "evidence_refs": ["user:task"],
        },
        {
            "concept": "known", "role": "known", "attribute": "个人开发者预算有限",
            "disposition": "inferred", "rationale": "由用户任务和项目环境共同推断", "evidence_refs": ["user:task"],
        },
        {
            "concept": "unknown", "role": "unknown", "attribute": "当前价格和兼容性",
            "disposition": "confirmed", "rationale": "明确记录为下一阶段待研究事实", "evidence_refs": [],
        },
    ]
    action = parse_action(json.dumps({
        "action": "advance",
        "status": "passed",
        "stage_id": "01",
        "revision": "r1",
        "next_stage": "02",
        "payload": {},
    }, ensure_ascii=False))
    validate_action(action, state)
