from ralph_runtime.protocol import parse_action
from ralph_runtime.state import apply_action, create_state


def test_exploration_can_create_marked_candidate_and_resume():
    state = apply_action(
        create_state("fixture"),
        parse_action('{"action":"explore","status":"exploring","stage_id":"01","revision":"r1"}'),
    )
    assert state["status"] == "exploration"
    candidate = parse_action(
        '{"action":"candidate","status":"candidate","stage_id":"exploration","revision":"r1",'
        '"payload":{"title":"candidate task","research_summary":"evidence","reason":"why",'
        '"scope":"只研究一个可验证问题","preference_brief":"偏好可复现、低风险的下一步",'
        '"scanned_sources":["tasks/TASKS.md"]}}'
    )
    state = apply_action(state, candidate)
    assert state["queue"]["candidates"][0]["status"] == "candidate"
    assert state["last_exploration"]["preference_brief"] == "偏好可复现、低风险的下一步"
    # Candidate creation is deliberately not task selection.  It must remain
    # in the queue until a later task-board selection or explicit approval.
    assert state["status"] == "exploration"
    assert not state.get("task_intake")


def test_candidate_without_research_is_rejected():
    from ralph_runtime.protocol import ProtocolError
    import pytest
    from ralph_runtime.state import create_state
    from ralph_runtime.protocol import validate_action

    with pytest.raises(ProtocolError):
        validate_action(
            parse_action('{"action":"candidate","status":"candidate","stage_id":"01","revision":"r1","payload":{"title":"incomplete"}}'),
            create_state("fixture"),
        )
