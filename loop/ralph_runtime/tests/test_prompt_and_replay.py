import json

from ralph_runtime.prompt_renderer import PromptRenderer
from ralph_runtime.replay_runner import run_fixture
from ralph_runtime.state import create_state


def test_prompt_hash_is_stable():
    state = create_state("fixture")
    first = PromptRenderer().render(state)
    second = PromptRenderer().render(json.loads(json.dumps(state)))
    assert first.sha256 == second.sha256
    assert first.text == second.text
    assert '"next_stage": "02"' in first.text
    assert "不要只回复 READY" in first.text
    assert "不得使用精简版 JSON" in first.text
    assert '"payload": {' in first.text
    assert "payload.questions" in first.text


def test_invalid_output_has_repair_prompt_without_mutating_state():
    state = create_state("fixture")
    repair = PromptRenderer().repair_prompt(state, "missing next_stage")
    assert "missing next_stage" in repair.text
    assert "不要调用 Bash、cat、echo 或 ralph apply" in repair.text
    assert "RALPH_TASK_CARD=loop-artifacts/task-cards/01-r1-requirements-auditor.md" in repair.text
    assert state["last_action"] is None


def test_protocol_repair_preserves_attempted_advance_action():
    state = create_state("fixture")
    state["subagent_cards"] = {}
    repair = PromptRenderer().repair_prompt(
        state,
        "advance requires next_stage",
        raw_output='{"action":"advance","status":"passed","stage_id":"01","revision":"r1"}',
    )
    assert '"action": "advance"' in repair.text
    assert '"action": "blocked_human"' not in repair.text
    assert "RALPH_FEEDBACK[STAGE_RESULT_INVALID]" in repair.text


def test_protocol_repair_does_not_preserve_action_when_gate_blocks_advance():
    state = create_state("fixture")
    state["subagent_cards"] = {}
    repair = PromptRenderer().repair_prompt(
        state,
        "stage_review has blocking_findings; rollback or blocked_human is required",
        raw_output='{"action":"advance","status":"passed","stage_id":"01","revision":"r1"}',
    )
    assert "与状态机/门禁条件冲突" in repair.text
    assert "不要伪造 advance" in repair.text
    assert "不要复制旧 action 模板" in repair.text


def test_protocol_repair_with_pending_card_does_not_show_stage_action_template():
    state = create_state("fixture")
    repair = PromptRenderer().repair_prompt(state, "missing next_stage")
    assert "RALPH_TASK_CARD=loop-artifacts/task-cards/01-r1-requirements-auditor.md" in repair.text
    assert "下一次工具调用必须直接使用上方指定的 Agent" in repair.text
    assert "不要输出阶段结果" in repair.text


def test_compact_recovery_prompt_does_not_render_full_stage_payload():
    state = create_state("fixture")
    recovery = PromptRenderer().compact_recovery_prompt(
        state,
        reason="Prefill context too large for available memory",
        error_kind="memory_guard",
    )
    assert len(recovery.text) < 3000
    assert "loop-state.json" in recovery.text
    assert "Prefill context too large" in recovery.text
    assert "当前计划" not in recovery.text


def test_compact_recovery_prompt_starts_with_one_idempotent_field_action():
    state = create_state("fixture", task="先读取 brief.md，再完成质量审计")
    recovery = PromptRenderer().compact_recovery_prompt(state, reason="新会话")

    assert len(recovery.text) < 1500
    assert "RALPH 最小恢复" in recovery.text
    assert "下一次工具调用只执行 `ralph field-init .`" in recovery.text
    assert "advance.json 示例" not in recovery.text


def test_fresh_recovery_prompt_continues_instead_of_ending_session():
    state = create_state("fixture", task="继续当前阶段")
    state["subagent_cards"] = {
        "01-r1-auditor": {
            "id": "01-r1-auditor",
            "status": "pending",
            "card_ref": "loop-artifacts/task-cards/01-r1-auditor.md",
        }
    }
    recovery = PromptRenderer().compact_recovery_prompt(
        state,
        reason="旧会话中断",
        error_kind="runtime",
        fresh_session=True,
    )
    assert "这是一个新的 Commander 上下文" in recovery.text
    assert "builder 构造卡先于 gate 审计卡" in recovery.text
    assert "下一次工具调用必须直接使用 Agent" in recovery.text
    assert "RALPH_TASK_CARD=loop-artifacts/task-cards/01-r1-auditor.md" in recovery.text
    assert "不要读取 loop-state.json" in recovery.text
    assert "禁止用 Read/Grep/Glob 读取任何长文档" in recovery.text
    assert "当前会话应结束" not in recovery.text


def test_replay_advance_is_deterministic():
    fixture = {
        "state": create_state("fixture"),
        "agent_output": '{"action":"advance","status":"passed","stage_id":"01","revision":"r1","next_stage":"02","evidence":["fixture"]}',
    }
    first = run_fixture(fixture)
    second = run_fixture(fixture)
    assert first[1] == second[1]
    assert first[0] == second[0]
    assert first[0]["stage"]["id"] == "02"


def test_replay_blocked_then_skip():
    state = create_state("fixture")
    blocked = {
        "action": "blocked_human",
        "status": "blocked_human",
        "stage_id": "01",
        "revision": "r1",
        "message": "need human input",
    }
    from ralph_runtime.protocol import parse_action
    from ralph_runtime.state import apply_action

    state = apply_action(state, parse_action(blocked), enforce_contracts=False)
    assert state["status"] == "blocked_human"
    skipped = parse_action('{"action":"skip_blocked","status":"skipped","stage_id":"01","revision":"r1","next_stage":"02"}')
    state = apply_action(state, skipped, enforce_contracts=False)
    assert state["status"] == "running"
    assert state["stage"]["id"] == "02"
