import json
from pathlib import Path

import ralph_runtime.cli as cli
from ralph_runtime.contracts import materialize_contract_documents
from ralph_runtime.events import append_observation
from ralph_runtime.prompt_renderer import PromptRenderer
from ralph_runtime.state import create_state, load_state, save_state, update_subagent_card
from ralph_runtime.cli import reconcile_stale_cards
from conftest import complete_required_card, gate_card_of, stage_one_payload


def test_prepare_project_creates_scaffold_and_persists_task(tmp_path: Path):
    project = tmp_path / "new-project"
    root, settings, is_new, created = cli.prepare_project(
        project,
        task="实现一个 CSV 统计工具",
        mode="shadow",
        record_session=True,
    )

    assert root == project.resolve()
    assert settings == root / ".claude" / "settings.ralph.json"
    assert is_new is True
    assert (root / "loop-state.json").exists()
    assert (root / "loop-events.md").exists()
    assert (root / "CLAUDE.md").exists()
    assert settings.exists()
    assert str(root / "CLAUDE.md") in created

    state = load_state(root / "loop-state.json")
    assert state["task"]["description"] == "实现一个 CSV 统计工具"
    assert "实现一个 CSV 统计工具" in PromptRenderer().render(state).text
    assert "session_started" in (root / "loop-events.md").read_text(encoding="utf-8")


def test_prepare_project_installs_inline_stop_hook_by_default(tmp_path: Path):
    project = tmp_path / "inline-stop-project"
    _, settings, _, _ = cli.prepare_project(project, task="测试同上下文继续")

    config = json.loads(settings.read_text(encoding="utf-8"))
    command = config["hooks"]["Stop"][0]["hooks"][0]["command"]
    assert "--stop-policy inline" in command


def test_validate_result_artifact_checks_then_atomically_applies(tmp_path: Path):
    project = tmp_path / "artifact-project"
    project.mkdir()
    state = complete_required_card(create_state("artifact-project"))
    save_state(project / "loop-state.json", state)
    (project / "loop-events.md").touch()
    artifact = project / "loop-artifacts" / "stages" / "01" / "r1" / "submission.json"
    artifact.parent.mkdir(parents=True)
    raw = json.dumps(
        {
            "action": "advance",
            "status": "passed",
            "stage_id": "01",
            "revision": "r1",
            "next_stage": "02",
            "payload": stage_one_payload(),
        },
        ensure_ascii=False,
    )
    artifact.write_text(raw, encoding="utf-8")

    checked = cli.validate_result_artifact(project, "loop-artifacts/stages/01/r1/submission.json")
    assert checked["valid"] is True
    assert checked["applied"] is False
    assert load_state(project / "loop-state.json")["stage"]["id"] == "01"

    applied = cli.validate_result_artifact(
        project,
        "loop-artifacts/stages/01/r1/submission.json",
        apply=True,
    )
    assert applied["applied"] is True
    assert load_state(project / "loop-state.json")["stage"]["id"] == "02"


def test_prepare_existing_project_preserves_canonical_task_and_records_new_input(tmp_path: Path):
    project = tmp_path / "existing-project"
    cli.prepare_project(project, task="第一项任务")
    state_path = project / "loop-state.json"
    state = load_state(state_path)
    state["stage"]["id"] = "03"
    state["status"] = "running"
    state["task_spec"]["attribute_matrix"] = [{
        "concept": "已通过字段",
        "role": "known",
        "attribute": "保留这个结果",
        "disposition": "confirmed",
        "evidence_refs": [],
    }]
    state_path.write_text(json.dumps(state, ensure_ascii=False), encoding="utf-8")

    _, _, is_new, _ = cli.prepare_project(project, task="第二项任务")
    updated = load_state(state_path)
    assert is_new is False
    assert updated["stage"]["id"] == "03"
    assert updated["task"]["description"] == "第一项任务"
    assert updated["task_spec"]["attribute_matrix"][0]["concept"] == "已通过字段"
    assert any(
        item.get("source") == "ralph loop" and item.get("text") == "第二项任务"
        for item in updated["task_spec"]["authoritative_inputs"]
    )
    assert "task_update_preserved_as_input" in (project / "loop-events.md").read_text(encoding="utf-8")


def test_prepare_empty_initialized_project_adopts_first_explicit_task(tmp_path: Path):
    project = tmp_path / "empty-initialized-project"
    cli.prepare_project(project)

    _, _, is_new, _ = cli.prepare_project(project, task="flow_only：完成离线流程测试")
    updated = load_state(project / "loop-state.json")

    assert is_new is False
    assert updated["task"] == {
        "description": "flow_only：完成离线流程测试",
        "source": "ralph loop",
    }
    assert updated["task_spec"]["authoritative_inputs"][0]["kind"] == "initial_task"
    assert updated["task_spec"]["authoritative_inputs"][0]["source"] == "ralph loop"
    assert updated["task_spec"]["authoritative_inputs"][0]["text"] == "flow_only：完成离线流程测试"
    events = (project / "loop-events.md").read_text(encoding="utf-8")
    assert "empty_task_adopted" in events
    assert "task_update_preserved_as_input" not in events


def test_events_tail_returns_bounded_summaries(tmp_path: Path):
    project = tmp_path / "event-project"
    cli.prepare_project(project, task="测试事件摘要")
    for index in range(5):
        append_observation(
            project / "loop-events.md",
            "posttooluse_observed",
            {
                "tool_name": "Read",
                "decision": "allow",
                "reason": "z" * 5000,
            },
            output="x" * 10000,
        )

    result = cli.events_tail(project, limit=2)
    assert result["total_events"] == 5  # five observations; this setup does not record a session
    assert result["returned_events"] == 2
    assert len(json.dumps(result, ensure_ascii=False)) < 5000
    assert all("output_excerpt" in event for event in result["events"])
    assert cli.events_tail(project, limit=100)["tail_limit"] == 20


def test_status_summary_does_not_dump_full_state_or_event_history(tmp_path: Path):
    project = tmp_path / "status-project"
    cli.prepare_project(project, task="测试状态摘要")
    state = load_state(project / "loop-state.json")
    state["task_spec"]["attribute_matrix"] = [
        {
            "concept": "长字段",
            "role": "unknown",
            "attribute": "x" * 10000,
            "disposition": "pending",
        }
    ]
    state["history"] = [{"output": "y" * 10000}]
    summary = cli.status_summary(state, project)
    encoded = json.dumps(summary, ensure_ascii=False)
    assert len(encoded) < 3000
    assert summary["fields"]["total"] == 1
    assert "长字段" not in encoded
    assert "yyyy" not in encoded


def test_prepare_project_migrates_legacy_loop_header(tmp_path: Path):
    project = tmp_path / "legacy-project"
    legacy = project / ".claude" / "ralph-loop.local.md"
    legacy.parent.mkdir(parents=True)
    legacy.write_text(
        "loop_phase: 2-loop/05-综合报告 (COMPLETED)\n"
        "iteration: 42\n"
        "last_outcome: report complete\n",
        encoding="utf-8",
    )

    cli.prepare_project(project, task="继续检查旧报告")
    state = load_state(project / "loop-state.json")

    assert state["stage"]["id"] == "05"
    assert state["status"] == "completed"
    assert state["iteration"] == "42"
    assert state["task"]["description"] == "继续检查旧报告"


def test_run_reopens_completed_project_at_stage_one(tmp_path: Path):
    project = tmp_path / "completed-project"
    cli.prepare_project(project, task="旧任务")
    state_path = project / "loop-state.json"
    state = load_state(state_path)
    state["status"] = "completed"
    state["stage"]["id"] = "06"
    state_path.write_text(json.dumps(state, ensure_ascii=False), encoding="utf-8")

    cli.prepare_project(project, task="新任务", fresh_if_completed=True)
    updated = load_state(state_path)

    assert updated["status"] == "running"
    assert updated["stage"]["id"] == "01"
    assert updated["task"]["description"] == "新任务"
    assert updated["run_history"][-1]["task"]["description"] == "旧任务"


def test_run_project_passes_task_as_interactive_prompt(tmp_path: Path, monkeypatch):
    observed = {}

    def fake_call(command, cwd, env=None):
        observed["command"] = command
        observed["cwd"] = cwd
        observed["env"] = env
        return 0

    monkeypatch.setattr(cli.subprocess, "call", fake_call)
    assert cli.run_project(tmp_path / "run-project", "完成一个最小测试", "shadow") == 0
    assert observed["cwd"] == (tmp_path / "run-project").resolve()
    assert observed["command"][-1] == "完成一个最小测试"
    assert "-p" not in observed["command"]
    assert observed["env"]["CLAUDE_CODE_AUTO_COMPACT_WINDOW"] == str(cli.DEFAULT_AUTO_COMPACT_WINDOW)
    assert observed["env"]["CLAUDE_AUTOCOMPACT_PCT_OVERRIDE"] == str(cli.DEFAULT_AUTOCOMPACT_PERCENT)


def test_run_project_passes_session_only_model_override(tmp_path: Path, monkeypatch):
    observed = {}

    def fake_call(command, cwd, env=None):
        observed["command"] = command
        observed["cwd"] = cwd
        observed["env"] = env
        return 0

    monkeypatch.setattr(cli.subprocess, "call", fake_call)
    monkeypatch.setattr(cli, "_claude_executable", lambda: "claude")

    assert cli.run_project(
        tmp_path / "model-project",
        "完成一个最小测试",
        model="MLX-small-test-model",
    ) == 0
    model_index = observed["command"].index("--model")
    assert observed["command"][model_index + 1] == "MLX-small-test-model"


def test_run_project_allows_explicit_compaction_target(tmp_path: Path, monkeypatch):
    observed = {}

    def fake_call(command, cwd, env=None):
        observed["env"] = env
        return 0

    monkeypatch.setattr(cli.subprocess, "call", fake_call)
    monkeypatch.setattr(cli, "_claude_executable", lambda: "claude")

    assert cli.run_project(
        tmp_path / "compact-project",
        "测试压缩参数",
        auto_compact_window=64000,
        auto_compact_percent=75,
    ) == 0
    assert observed["env"]["CLAUDE_CODE_AUTO_COMPACT_WINDOW"] == "64000"
    assert observed["env"]["CLAUDE_AUTOCOMPACT_PCT_OVERRIDE"] == "75"


def test_recover_card_reopens_unreceipted_gate_card(tmp_path: Path):
    project = tmp_path / "recover-card"
    cli.prepare_project(project, task="测试恢复")
    state_path = project / "loop-state.json"
    state = load_state(state_path)
    card = gate_card_of(state)
    state = update_subagent_card(state, card["id"], "completed", agent_id="legacy-agent")
    save_state(state_path, state)
    materialize_contract_documents(project, state)

    result = cli.recover_card(project, card["id"], "legacy false completion")

    assert result["status"] == "pending"
    updated = load_state(state_path)["subagent_cards"][card["id"]]
    assert updated["status"] == "pending"
    assert "agent_id" not in updated
    assert "subagent_card_recovered" in (project / "loop-events.md").read_text(encoding="utf-8")


def test_recover_card_refuses_gate_with_verified_receipt(tmp_path: Path):
    project = tmp_path / "receipt-card"
    cli.prepare_project(project, task="测试恢复")
    state_path = project / "loop-state.json"
    state = load_state(state_path)
    card = gate_card_of(state)
    state = update_subagent_card(state, card["id"], "completed")
    save_state(state_path, state)
    receipt_dir = project / "loop-artifacts" / "gate-reviews"
    receipt_dir.mkdir(parents=True)
    (receipt_dir / f"{card['id']}-verified.json").write_text("{}\n", encoding="utf-8")

    import pytest

    with pytest.raises(ValueError, match="已有有效门禁回执"):
        cli.recover_card(project, card["id"], "must not overwrite receipt")


def test_recover_card_requires_explicit_force_for_stale_dispatched_card(tmp_path: Path):
    project = tmp_path / "stale-dispatched"
    cli.prepare_project(project, task="测试残留子代理")
    state_path = project / "loop-state.json"
    state = load_state(state_path)
    card = gate_card_of(state)
    state = update_subagent_card(state, card["id"], "dispatched", agent_id="stale-agent")
    save_state(state_path, state)
    materialize_contract_documents(project, state)

    import pytest

    with pytest.raises(ValueError, match="--force-dispatched"):
        cli.recover_card(project, card["id"], "must confirm first")

    recovered = cli.recover_card(
        project,
        card["id"],
        "子代理已退出且没有 SubagentStop 回执",
        force_dispatched=True,
    )
    assert recovered["prior_status"] == "dispatched"
    assert recovered["status"] == "pending"


def test_reconcile_stale_gate_uses_valid_receipt_instead_of_rerunning(tmp_path: Path):
    project = tmp_path / "reconcile-receipt"
    cli.prepare_project(project, task="测试门禁回收")
    state_path = project / "loop-state.json"
    state = load_state(state_path)
    card = gate_card_of(state)
    state = update_subagent_card(state, card["id"], "dispatched", agent_id="dead-agent")
    save_state(state_path, state)
    materialize_contract_documents(project, state)

    receipt_ref = f"loop-artifacts/gate-reviews/{card['id']}-receipt.json"
    receipt_path = project / receipt_ref
    receipt_path.parent.mkdir(parents=True, exist_ok=True)
    receipt_path.write_text(
        json.dumps({
            "reviewer_card_id": card["id"],
            "verdict": "rollback",
            "recommended_action": "rollback",
            "checks": [{"criterion": "task spec", "status": "fail"}],
        }, ensure_ascii=False),
        encoding="utf-8",
    )
    append_observation(
        project / "loop-events.md",
        "subagent_gate_review_received",
        {
            "task_card_id": card["id"],
            "agent_id": "dead-agent",
            "artifact_ref": receipt_ref,
            "verdict": "rollback",
        },
    )

    result = reconcile_stale_cards(project, reason="test supervisor recovery")

    assert result[0]["outcome"] == "completed"
    reconciled = load_state(state_path)["subagent_cards"][card["id"]]
    assert reconciled["status"] == "completed"
    assert reconciled["gate_verdict"] == "rollback"
    assert "subagent_card_reconciled" in (project / "loop-events.md").read_text(encoding="utf-8")


def test_loop_project_launches_fresh_context_and_stops_at_cycle_limit(tmp_path: Path, monkeypatch):
    observed = {}

    def fake_runner(command, cwd, env, idle_timeout):
        observed["command"] = command
        observed["cwd"] = cwd
        observed["env"] = env
        return 17, False

    monkeypatch.setattr(cli, "_run_claude_supervised", fake_runner)
    monkeypatch.setattr(cli, "_claude_executable", lambda: "claude")

    assert cli.loop_project(
        tmp_path / "supervised-project",
        task="测试持续监督",
        mode="shadow",
        max_cycles=1,
        retry_delay=0,
        agent_grace_seconds=0,
        idle_timeout=0,
    ) == 0
    assert observed["cwd"] == (tmp_path / "supervised-project").resolve()
    assert "当前任务：测试持续监督" in observed["command"][-1]
    assert "下一次工具调用只执行 `ralph field-init .`" in observed["command"][-1]
    events = (tmp_path / "supervised-project" / "loop-events.md").read_text(encoding="utf-8")
    assert "supervisor_cycle_started" in events
    assert "supervisor_cycle_finished" in events


def test_loop_project_circuit_breaker_stops_repeated_failed_cycles(tmp_path: Path, monkeypatch):
    calls = []

    def fake_runner(command, cwd, env, idle_timeout):
        calls.append(True)
        return 143, False

    monkeypatch.setattr(cli, "_run_claude_supervised", fake_runner)
    monkeypatch.setattr(cli, "_claude_executable", lambda: "claude")

    assert cli.loop_project(
        tmp_path / "circuit-breaker-project",
        task="测试失败熔断",
        mode="shadow",
        max_failed_cycles=2,
        retry_delay=0,
        agent_grace_seconds=0,
        idle_timeout=0,
    ) == 1
    assert len(calls) == 2
    events = (tmp_path / "circuit-breaker-project" / "loop-events.md").read_text(encoding="utf-8")
    assert "supervisor_circuit_breaker" in events


def test_auto_field_workers_are_fallback_after_first_commander_cycle(tmp_path: Path, monkeypatch):
    calls = []

    def fake_runner(command, cwd, env, idle_timeout):
        return 17, False

    def fake_launch(*args, **kwargs):
        calls.append(True)
        return []

    monkeypatch.setenv("RALPH_AUTO_FIELD_WORKERS", "1")
    monkeypatch.setattr(cli, "_run_claude_supervised", fake_runner)
    monkeypatch.setattr(cli, "_launch_auto_field_workers", fake_launch)
    monkeypatch.setattr(cli, "_claude_executable", lambda: "claude")

    assert cli.loop_project(
        tmp_path / "fallback-project",
        task="测试自动字段 fallback",
        mode="shadow",
        max_cycles=2,
        retry_delay=0,
        agent_grace_seconds=0,
        idle_timeout=0,
    ) == 0
    # Commander owns the first context; fallback is considered only at the
    # next cycle boundary, avoiding two local Claude processes at startup.
    assert len(calls) == 1


def test_auto_field_worker_is_waited_before_next_commander_context(tmp_path: Path, monkeypatch):
    order = []

    def fake_runner(command, cwd, env, idle_timeout):
        order.append("commander")
        return 17, False

    def fake_launch(*args, **kwargs):
        order.append("worker-start")
        return ["field-1"]

    def fake_wait(*args, **kwargs):
        order.append("worker-finished")

    monkeypatch.setenv("RALPH_AUTO_FIELD_WORKERS", "1")
    monkeypatch.setattr(cli, "_run_claude_supervised", fake_runner)
    monkeypatch.setattr(cli, "_launch_auto_field_workers", fake_launch)
    monkeypatch.setattr(cli, "_wait_for_auto_field_workers", fake_wait)
    monkeypatch.setattr(cli, "_claude_executable", lambda: "claude")

    assert cli.loop_project(
        tmp_path / "serial-fallback-project",
        task="测试字段 worker 串行恢复",
        mode="shadow",
        max_cycles=2,
        retry_delay=0,
        agent_grace_seconds=0,
        idle_timeout=0,
    ) == 0
    assert order == ["commander", "worker-start", "worker-finished", "commander"]


def test_supervisor_lock_rejects_second_owner(tmp_path: Path):
    project = tmp_path / "locked-project"
    with cli._supervisor_lock(project):
        import pytest

        with pytest.raises(cli.SupervisorAlreadyRunning, match="已有 ralph loop"):
            with cli._supervisor_lock(project):
                pass


def test_loop_rejects_absolute_project_without_task(tmp_path: Path):
    import pytest

    with pytest.raises(ValueError, match="看起来是项目路径"):
        cli._resolve_loop_project(tmp_path / "missing-project", None, None)
