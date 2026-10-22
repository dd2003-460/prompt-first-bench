import json

from ralph_runtime.events import append_observation, read_events
from ralph_runtime.hooks import (
    handle_hook,
    handle_pretooluse,
    handle_stop,
    handle_subagentstop,
    run_hook,
)
from ralph_runtime.state import create_state, load_state, save_state, update_subagent_card
from conftest import complete_required_card, stage_one_payload


def test_pretooluse_shadow_allows_but_records(tmp_path):
    save_state(tmp_path / "loop-state.json", create_state("fixture"))
    result = handle_pretooluse(
        {"cwd": str(tmp_path), "tool_name": "Edit", "tool_input": {"file_path": "code.py"}, "ralph_role": "commander"},
        mode="shadow",
    )
    assert result["hookSpecificOutput"]["permissionDecision"] == "allow"
    assert "loop-events.md" in {path.name for path in tmp_path.iterdir()}


def test_pretooluse_enforce_denies_commander_edit(tmp_path):
    save_state(tmp_path / "loop-state.json", create_state("fixture"))
    result = handle_pretooluse(
        {"cwd": str(tmp_path), "tool_name": "Edit", "tool_input": {"file_path": "code.py"}, "ralph_role": "commander"},
        mode="enforce",
    )
    assert result["hookSpecificOutput"]["permissionDecision"] == "deny"
    assert "不要用 Agent 绕过" in result["hookSpecificOutput"]["permissionDecisionReason"]


def test_pretooluse_enforce_denies_commander_full_event_log_read(tmp_path):
    save_state(tmp_path / "loop-state.json", create_state("fixture"))
    result = handle_pretooluse(
        {
            "cwd": str(tmp_path),
            "tool_name": "Read",
            "tool_input": {"file_path": "loop-events.md"},
            "ralph_role": "commander",
        },
        mode="enforce",
    )
    assert result["hookSpecificOutput"]["permissionDecision"] == "deny"
    reason = result["hookSpecificOutput"]["permissionDecisionReason"]
    assert "ralph events . --tail 20" in reason
    assert "blocked_human" in reason


def test_worker_bash_denial_explains_read_only_gate_output(tmp_path):
    state = create_state("fixture")
    card = next(iter(state["subagent_cards"].values()))
    state = update_subagent_card(state, card["id"], "dispatched", agent_id="agent-worker")
    save_state(tmp_path / "loop-state.json", state)
    result = handle_pretooluse(
        {
            "cwd": str(tmp_path),
            "tool_name": "Bash",
            "tool_input": {"command": "python inspect.py"},
            "ralph_role": "worker",
            "agent_id": "agent-worker",
        },
        mode="enforce",
    )
    assert result["hookSpecificOutput"]["permissionDecision"] == "deny"
    reason = result["hookSpecificOutput"]["permissionDecisionReason"]
    assert "只读审计卡" in reason
    assert "RALPH_GATE_REVIEW" in reason


def test_posttooluse_records_bounded_tool_response(tmp_path):
    save_state(tmp_path / "loop-state.json", create_state("fixture"))
    handle_hook(
        "posttooluse",
        {
            "cwd": str(tmp_path),
            "tool_name": "Read",
            "tool_response": {
                "status": "completed",
                "output": "x" * 10000,
                "unbounded_payload": "y" * 10000,
            },
        },
        mode="enforce",
    )
    event = read_events(tmp_path / "loop-events.md")[-1]
    response = event["observation"]["tool_response"]
    assert len(response["output"]) <= 700
    assert "unbounded_payload" not in response


def test_stop_shadow_does_not_block(tmp_path):
    save_state(tmp_path / "loop-state.json", create_state("fixture"))
    result = handle_stop({"cwd": str(tmp_path)}, mode="shadow")
    assert "decision" not in result
    assert "systemMessage" in result


def test_stop_inline_blocks_and_continues_in_the_same_context(tmp_path):
    save_state(tmp_path / "loop-state.json", create_state("fixture"))
    result = handle_stop(
        {
            "cwd": str(tmp_path),
            "last_assistant_message": "我刚完成诊断，下一步准备运行验证。",
        },
        mode="hybrid",
        stop_policy="inline",
    )

    assert result["decision"] == "block"
    assert "RALPH 同上下文继续" in result["reason"]
    assert "我刚完成诊断" in result["reason"]
    assert any(event["type"] == "inline_stop_intercepted" for event in read_events(tmp_path / "loop-events.md"))


def test_run_hook_inline_stop_does_not_emit_fresh_context_marker(tmp_path):
    save_state(tmp_path / "loop-state.json", create_state("fixture"))
    result = json.loads(
        run_hook(
            "stop",
            json.dumps({"cwd": str(tmp_path), "last_assistant_message": "继续验证"}),
            mode="hybrid",
            stop_policy="inline",
        )
    )

    assert result["decision"] == "block"
    assert not any(event["type"] == "ralph_stop_handled" for event in read_events(tmp_path / "loop-events.md"))


def test_inline_stop_repeated_output_switches_strategy_without_new_context(tmp_path):
    save_state(tmp_path / "loop-state.json", create_state("fixture"))
    payload = {
        "cwd": str(tmp_path),
        "last_assistant_message": '{"action":"advance","status":"passed","stage_id":"01","revision":"r1"}',
    }

    results = [handle_stop(payload, mode="hybrid", stop_policy="inline") for _ in range(3)]

    assert all(result["decision"] == "block" for result in results)
    assert "策略切换" in results[-1]["reason"]
    events = read_events(tmp_path / "loop-events.md")
    assert sum(event["type"] == "inline_stop_intercepted" for event in events) == 3
    assert not any(event["type"] == "ralph_stop_handled" for event in events)


def test_stop_enforce_blocks_running_state_but_guard_allows(tmp_path):
    save_state(tmp_path / "loop-state.json", create_state("fixture"))
    blocked = handle_stop({"cwd": str(tmp_path)}, mode="enforce")
    assert blocked["decision"] == "block"
    allowed = handle_stop({"cwd": str(tmp_path), "stop_hook_active": True}, mode="enforce")
    assert allowed == {}


def test_stop_allows_commander_turn_to_end_while_subagent_is_dispatched(tmp_path):
    state = create_state("fixture")
    card = next(iter(state["subagent_cards"].values()))
    state = update_subagent_card(state, card["id"], "dispatched", agent_id="agent-running")
    save_state(tmp_path / "loop-state.json", state)

    result = handle_stop({"cwd": str(tmp_path)}, mode="enforce")

    assert "decision" not in result
    assert "SubagentStop" in result["systemMessage"]
    assert load_state(tmp_path / "loop-state.json")["subagent_cards"][card["id"]]["status"] == "dispatched"
    assert any(
        event["type"] == "stop_allowed_waiting_for_subagent"
        for event in read_events(tmp_path / "loop-events.md")
    )


def test_stop_hook_reentry_does_not_parse_stale_commander_output_while_card_runs(tmp_path):
    state = create_state("fixture")
    card = next(iter(state["subagent_cards"].values()))
    state = update_subagent_card(state, card["id"], "dispatched", agent_id="agent-running")
    save_state(tmp_path / "loop-state.json", state)

    result = handle_stop(
        {
            "cwd": str(tmp_path),
            "stop_hook_active": True,
            "last_assistant_message": '{"action":"advance","status":"passed"}',
        },
        mode="enforce",
    )

    assert result == {}
    assert load_state(tmp_path / "loop-state.json")["subagent_cards"][card["id"]]["status"] == "dispatched"
    events = read_events(tmp_path / "loop-events.md")
    assert any(event["type"] == "stop_allowed_waiting_for_subagent" for event in events)
    assert not any(event["type"] == "stage_result_rejected" for event in events)


def test_stop_runtime_memory_error_preserves_state_and_allows_new_context(tmp_path):
    initial = create_state("fixture")
    save_state(tmp_path / "loop-state.json", initial)
    result = handle_stop(
        {
            "cwd": str(tmp_path),
            "stop_reason": "error",
            "last_assistant_message": (
                "API Error: oMLX prefill memory guard rejected this prompt: "
                "Prefill context too large for available memory"
            ),
        },
        mode="enforce",
    )
    assert "decision" not in result
    assert "RALPH_FEEDBACK[RUNTIME_INTERRUPTION]" in result["systemMessage"]
    assert "ralph resume" in result["systemMessage"]
    assert load_state(tmp_path / "loop-state.json") == initial
    events = read_events(tmp_path / "loop-events.md")
    interruption = [event for event in events if event["type"] == "runtime_interrupted"]
    assert len(interruption) == 1
    assert interruption[0]["observation"]["kind"] == "memory_guard"


def test_stop_continuation_uses_bounded_recovery_prompt(tmp_path):
    save_state(tmp_path / "loop-state.json", create_state("fixture"))
    result = handle_stop({"cwd": str(tmp_path)}, mode="enforce")
    assert result["decision"] == "block"
    assert len(result["reason"]) < 5000
    assert "loop-state.json" in result["reason"]


def test_compaction_hooks_record_start_and_bounded_summary(tmp_path):
    save_state(tmp_path / "loop-state.json", create_state("fixture"))
    assert handle_hook(
        "precompact",
        {"cwd": str(tmp_path), "trigger": "auto", "session_id": "s1"},
        mode="enforce",
    ) == {}
    long_summary = "compact summary " * 500
    assert handle_hook(
        "postcompact",
        {"cwd": str(tmp_path), "trigger": "auto", "session_id": "s1", "compact_summary": long_summary},
        mode="enforce",
    ) == {}

    events = read_events(tmp_path / "loop-events.md")
    started = [event for event in events if event["type"] == "context_compaction_started"]
    completed = [event for event in events if event["type"] == "context_compaction_completed"]
    assert len(started) == 1
    assert len(completed) == 1
    assert completed[0]["observation"]["summary_characters"] <= 2400
    assert completed[0].get("output_excerpt", "")


def test_stop_auto_applies_valid_agent_result(tmp_path):
    save_state(tmp_path / "loop-state.json", complete_required_card(create_state("fixture")))
    output = '<RALPH_STAGE_RESULT>' + json.dumps({
        "action": "advance", "status": "passed", "stage_id": "01", "revision": "r1", "next_stage": "02",
        "evidence": ["verified"], "payload": stage_one_payload(),
    }, ensure_ascii=False) + '</RALPH_STAGE_RESULT>'
    result = handle_stop(
        {"cwd": str(tmp_path), "last_assistant_message": output},
        mode="enforce",
    )
    assert result["decision"] == "block"
    assert load_state(tmp_path / "loop-state.json")["stage"]["id"] == "02"
    assert any(event["type"] == "stage_advanced" for event in read_events(tmp_path / "loop-events.md"))


def test_stop_auto_applies_blocked_human_and_allows_session_to_end(tmp_path):
    save_state(tmp_path / "loop-state.json", create_state("fixture"))
    output = '<RALPH_STAGE_RESULT>' + json.dumps({
        "action": "blocked_human",
        "status": "blocked_human",
        "stage_id": "01",
        "revision": "r1",
        "message": "需要人类澄清",
        "payload": {
            "questions": [{
                "question": "并行任务具体是什么？",
                "why_it_matters": "会改变资源预算",
                "recommended_option": "默认一个本地模型服务",
            }],
        },
    }, ensure_ascii=False) + '</RALPH_STAGE_RESULT>'

    result = handle_stop(
        {"cwd": str(tmp_path), "last_assistant_message": output},
        mode="enforce",
    )

    assert result == {}
    state = load_state(tmp_path / "loop-state.json")
    assert state["status"] == "blocked_human"
    assert any(event["type"] == "stop_allowed_after_apply" for event in read_events(tmp_path / "loop-events.md"))


def test_stop_allows_existing_human_block_without_new_action(tmp_path):
    state = create_state("fixture")
    state["status"] = "blocked_human"
    save_state(tmp_path / "loop-state.json", state)

    result = handle_stop({"cwd": str(tmp_path)}, mode="enforce")

    assert result == {}
    assert any(
        event["type"] == "stop_allowed_human_block_waiting"
        for event in read_events(tmp_path / "loop-events.md")
    )


def test_stop_rejects_invalid_result_without_mutating_state(tmp_path):
    save_state(tmp_path / "loop-state.json", create_state("fixture"))
    output = '{"action":"advance","status":"passed","stage_id":"01","revision":"r1"}'
    result = handle_stop(
        {"cwd": str(tmp_path), "last_assistant_message": output},
        mode="enforce",
    )
    assert result["decision"] == "block"
    assert "next_stage" in result["reason"]
    assert load_state(tmp_path / "loop-state.json")["stage"]["id"] == "01"
    assert any(event["type"] == "stage_result_rejected" for event in read_events(tmp_path / "loop-events.md"))


def test_stop_hook_active_invalid_result_blocks_to_force_repair(tmp_path):
    save_state(tmp_path / "loop-state.json", create_state("fixture"))
    output = '{"action":"advance","status":"passed","stage_id":"01","revision":"r1"}'
    result = handle_stop(
        {"cwd": str(tmp_path), "last_assistant_message": output, "stop_hook_active": True},
        mode="enforce",
    )
    # The Stop hook must block the session end so the model repairs the
    # malformed result in the same context instead of idling and waiting for
    # the outer supervisor to relaunch a fresh context.
    assert result["decision"] == "block"
    events = read_events(tmp_path / "loop-events.md")
    assert any(event["type"] == "stage_result_repair_prompted" for event in events)
    assert any(
        event["type"] == "stop_hook_guarded"
        and event.get("observation", {}).get("reason") == "invalid_result_after_stop_hook"
        for event in events
    )


def test_stop_exhausts_same_context_repair_budget_for_outer_supervisor(tmp_path):
    initial = create_state("fixture")
    save_state(tmp_path / "loop-state.json", initial)
    append_observation(
        tmp_path / "loop-events.md",
        "supervisor_cycle_started",
        {"cycle": 1, "stage": "01", "revision": "r1"},
    )

    results = []
    for index in range(3):
        results.append(
            handle_stop(
                {
                    "cwd": str(tmp_path),
                    "last_assistant_message": (
                        '{"action":"advance","status":"passed",'
                        f'"stage_id":"01","revision":"r1","attempt":{index}'
                        '}'
                    ),
                },
                mode="enforce",
            )
        )

    assert results[0]["decision"] == "block"
    assert results[1]["decision"] == "block"
    assert "decision" not in results[2]
    assert "REPAIR_BUDGET_EXHAUSTED" in results[2]["systemMessage"]
    assert load_state(tmp_path / "loop-state.json") == initial
    assert any(
        event["type"] == "stage_result_repair_exhausted"
        for event in read_events(tmp_path / "loop-events.md")
    )


def test_stop_does_not_apply_same_output_twice(tmp_path):
    save_state(tmp_path / "loop-state.json", complete_required_card(create_state("fixture")))
    output = json.dumps({
        "action": "advance", "status": "passed", "stage_id": "01", "revision": "r1", "next_stage": "02",
        "payload": stage_one_payload(),
    }, ensure_ascii=False)
    handle_stop({"cwd": str(tmp_path), "last_assistant_message": output}, mode="enforce")
    second = handle_stop(
        {"cwd": str(tmp_path), "last_assistant_message": output, "stop_hook_active": True},
        mode="enforce",
    )
    # A duplicate (no-progress) stop must NOT idle the loop; the Stop hook
    # blocks and points the Commander at the next concrete action.
    assert second.get("decision") == "block"
    events = read_events(tmp_path / "loop-events.md")
    assert sum(event["type"] == "stage_advanced" for event in events) == 1


def test_subagentstop_blocks_builder_without_slice_when_stop_hook_active(tmp_path):
    state = create_state("fixture")
    card = {
        "id": "01-r1-builder-task_spec-context",
        "stage_id": "01",
        "revision": "r1",
        "task_id": None,
        "is_stage_gate": False,
        "status": "dispatched",
        "agent_id": "builder-agent",
        "slice_roles": ["background", "decision_object", "objective"],
        "input_refs": ["loop-artifacts/stages/01/r1/task_spec.partial.context.json"],
        "allowed_tools": ["Write", "Edit"],
    }
    state["subagent_cards"] = {card["id"]: card}
    save_state(tmp_path / "loop-state.json", state)
    result = handle_subagentstop(
        {"cwd": str(tmp_path), "agent_id": "builder-agent", "stop_hook_active": True},
        mode="enforce",
    )
    assert result.get("decision") == "block"
    assert load_state(tmp_path / "loop-state.json")["subagent_cards"][card["id"]]["status"] == "pending"


def test_subagentstop_reverts_hollow_completion_marked_by_model(tmp_path):
    state = create_state("fixture")
    card = {
        "id": "01-r1-builder-task_spec-context",
        "stage_id": "01",
        "revision": "r1",
        "task_id": None,
        "is_stage_gate": False,
        "status": "completed",
        "agent_id": "builder-agent",
        "slice_roles": ["background", "decision_object", "objective"],
        "input_refs": ["loop-artifacts/stages/01/r1/task_spec.partial.context.json"],
        "allowed_tools": ["Write", "Edit"],
    }
    state["subagent_cards"] = {card["id"]: card}
    save_state(tmp_path / "loop-state.json", state)
    skeleton = (
        tmp_path / "loop-artifacts/stages/01/r1/task_spec.json"
    )
    skeleton.parent.mkdir(parents=True, exist_ok=True)
    from ralph_runtime.contracts import stage_submission_template

    skeleton.write_text(
        json.dumps(stage_submission_template(state)["payload"]["task_spec"], ensure_ascii=False, indent=2)
        + "\n",
        encoding="utf-8",
    )
    result = handle_subagentstop(
        {"cwd": str(tmp_path), "agent_id": "builder-agent", "stop_hook_active": True},
        mode="enforce",
    )
    assert result.get("decision") == "block"
    reverted = load_state(tmp_path / "loop-state.json")["subagent_cards"][card["id"]]
    assert reverted["status"] == "pending"
    assert reverted["agent_id"] is None


def test_subagentstop_blocks_invalid_gate_review_when_stop_hook_active(tmp_path):
    state = create_state("fixture")
    card = {
        "id": "01-r1-requirements-auditor",
        "stage_id": "01",
        "revision": "r1",
        "task_id": None,
        "is_stage_gate": True,
        "status": "dispatched",
        "agent_id": "gate-agent",
        "input_refs": [],
        "output_schema": {
            "required": ["verdict"],
            "verdict_values": ["pass", "rollback"],
            "check_status_values": ["pass", "fail"],
        },
    }
    state["subagent_cards"] = {card["id"]: card}
    save_state(tmp_path / "loop-state.json", state)
    result = handle_subagentstop(
        {
            "cwd": str(tmp_path),
            "agent_id": "gate-agent",
            "stop_hook_active": True,
            "last_assistant_message": "no gate review marker here",
        },
        mode="enforce",
    )
    assert result.get("decision") == "block"
    assert load_state(tmp_path / "loop-state.json")["subagent_cards"][card["id"]]["status"] == "dispatched"
