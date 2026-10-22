import json
import subprocess
import time
from datetime import datetime, timedelta, timezone
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor

import pytest

from ralph_runtime.cli import (
    _field_agent_stall_requested,
    _field_task_stall_requested,
    _reap_auto_field_workers,
    apply_fields,
    init_fields,
)
from ralph_runtime.field_tasks import (
    claim_field_task,
    materialize_field_tasks,
    reconcile_applied_field_tasks,
    reopen_deferred_field_tasks,
    rebind_field_task_to_path,
)
from ralph_runtime.graph_tasks import apply_graph_task, materialize_graph_tasks
from ralph_runtime.events import apply_and_record
from ralph_runtime.hooks import handle_posttooluse, handle_pretooluse, handle_stop, handle_subagentstart, handle_subagentstop, handle_userpromptsubmit
from ralph_runtime.prompt_renderer import PromptRenderer
from ralph_runtime.protocol import ProtocolError, parse_action, validate_action
from ralph_runtime.result_artifacts import state_stage_artifact_dir
from ralph_runtime.stage_policy import decide_tool
from ralph_runtime.state import create_state, load_state, record_human_input, save_state
import ralph_runtime.cli as cli


def _project(tmp_path: Path) -> Path:
    root = tmp_path / "project"
    root.mkdir()
    save_state(root / "loop-state.json", create_state("project", task="调研本地 AI GPU"))
    return root


def _flow_graph() -> dict:
    return {
        "nodes": [
            {
                "id": "T1.1", "depends_on": [], "execution_mode": "parallel",
                "parallel_group_id": "G1", "orthogonal_key": "dimension_a",
                "input_refs": [], "output_schema": {"result": "string"},
                "preconditions": [], "postconditions": ["A"],
                "writes": ["loop-artifacts/stages/03/r1/outputs/T1.1.json"],
            },
            {
                "id": "T1.2", "depends_on": [], "execution_mode": "parallel",
                "parallel_group_id": "G1", "orthogonal_key": "dimension_b",
                "input_refs": [], "output_schema": {"result": "string"},
                "preconditions": [], "postconditions": ["B"],
                "writes": ["loop-artifacts/stages/03/r1/outputs/T1.2.json"],
            },
            {
                "id": "J1", "depends_on": ["T1.1", "T1.2"], "execution_mode": "serial",
                "input_refs": [
                    "loop-artifacts/stages/03/r1/outputs/T1.1.json",
                    "loop-artifacts/stages/03/r1/outputs/T1.2.json",
                ],
                "output_schema": {"joined": "string"},
                "preconditions": ["inputs complete"], "postconditions": ["joined"],
                "writes": ["loop-artifacts/stages/03/r1/outputs/J1.json"],
            },
        ],
        "parallel_groups": [{"id": "G1", "members": ["T1.1", "T1.2"]}],
        "joins": [{"id": "J1", "depends_on": ["T1.1", "T1.2"]}],
    }


def test_field_init_creates_stage_scoped_draft_without_overwriting(tmp_path: Path):
    root = _project(tmp_path)

    first = init_fields(root)
    second = init_fields(root)

    draft = Path(first["fields_file"])
    assert first["created"] is True
    assert second["created"] is False
    assert draft.parent == state_stage_artifact_dir(root, load_state(root / "loop-state.json"))
    assert json.loads(draft.read_text(encoding="utf-8")) == {"fields": []}


def test_stage_prompts_advertise_stage_executor_skill():
    state = create_state("skill-prompt", task="完成 RALPH 阶段")
    renderer = PromptRenderer()

    assert "/ralph-stage-executor" in renderer.render(state).text
    assert "/ralph-stage-executor" in renderer.compact_recovery_prompt(state).text


def test_ralph_attaches_stage_executor_skill_as_system_context(tmp_path: Path, monkeypatch):
    skill = tmp_path / "ralph-stage-executor.md"
    skill.write_text(
        "---\nname: ralph-stage-executor\ndescription: test\n---\n\n# Workflow\nUse field-status first.\n",
        encoding="utf-8",
    )
    monkeypatch.setenv("RALPH_STAGE_EXECUTOR_SKILL", str(skill))
    command = ["claude"]

    source = cli._append_stage_executor_skill(command)

    assert source == skill
    index = command.index("--append-system-prompt")
    assert "Required RALPH stage-execution skill" in command[index + 1]
    assert "Use field-status first." in command[index + 1]


def test_auto_field_worker_loads_stage_skill_before_its_prompt(tmp_path: Path, monkeypatch):
    """Fallback contexts must receive the same workflow as their Commander."""

    root = _project(tmp_path)
    state = load_state(root / "loop-state.json")
    state["task_spec"]["attribute_matrix"] = [{
        "concept": "阶段 01 输出：goal",
        "role": "goal",
        "attribute": "给出一个最小目标",
        "disposition": "pending",
        "rationale": "测试恢复 worker 的阶段技能注入。",
        "evidence_refs": [],
    }]
    save_state(root / "loop-state.json", state)
    task = materialize_field_tasks(root, state)[0]
    save_state(root / "loop-state.json", state)

    skill = tmp_path / "ralph-stage-executor.md"
    skill.write_text(
        "---\nname: ralph-stage-executor\ndescription: test\n---\n\n# Worker workflow\nApply one field.\n",
        encoding="utf-8",
    )
    started: list[list[str]] = []

    class FakeProcess:
        pid = 4242

    def fake_popen(command, **kwargs):
        started.append(command)
        return FakeProcess()

    monkeypatch.setenv("RALPH_STAGE_EXECUTOR_SKILL", str(skill))
    monkeypatch.setenv("RALPH_AUTO_FIELD_WORKERS", "1")
    monkeypatch.setenv("RALPH_AUTO_PENDING_FIELD_WORKERS", "1")
    monkeypatch.setattr(cli, "_claude_executable", lambda: "claude")
    monkeypatch.setattr(cli.subprocess, "Popen", fake_popen)

    workers: dict[str, dict] = {}
    assert cli._launch_auto_field_workers(
        root,
        root / ".claude" / "settings.ralph.json",
        {},
        model=None,
        effort="low",
        skip_permissions=False,
        workers=workers,
    ) == [task["id"]]

    command = started[0]
    skill_index = command.index("--append-system-prompt")
    prompt_index = command.index("-p")
    assert skill_index < prompt_index == len(command) - 2
    assert "Required RALPH stage-execution skill" in command[skill_index + 1]
    assert "Apply one field." in command[skill_index + 1]
    assert command[prompt_index + 1].startswith("RALPH_FIELD_TASK=")


def test_auto_graph_worker_loads_skill_and_uses_graph_apply(tmp_path: Path, monkeypatch):
    root = _project(tmp_path)
    state = load_state(root / "loop-state.json")
    state["stage"] = {**state["stage"], "id": "03", "revision": "r1"}
    state["plan"] = _flow_graph()
    materialize_graph_tasks(root, state)
    save_state(root / "loop-state.json", state)

    skill = tmp_path / "ralph-stage-executor.md"
    skill.write_text("# Graph workflow\nRun graph-apply.\n", encoding="utf-8")
    started: list[list[str]] = []

    class FakeProcess:
        pid = 4243

    def fake_popen(command, **kwargs):
        started.append(command)
        return FakeProcess()

    monkeypatch.setenv("RALPH_STAGE_EXECUTOR_SKILL", str(skill))
    monkeypatch.setattr(cli, "_claude_executable", lambda: "claude")
    monkeypatch.setattr(cli.subprocess, "Popen", fake_popen)
    workers: dict[str, dict] = {}
    launched = cli._launch_auto_graph_workers(
        root,
        root / ".claude" / "settings.ralph.json",
        {},
        model=None,
        effort="low",
        skip_permissions=False,
        workers=workers,
    )

    assert launched == ["03-r1-node-T1.1"]
    command = started[0]
    assert command.index("--append-system-prompt") < command.index("-p") == len(command) - 2
    assert "Graph workflow" in command[command.index("--append-system-prompt") + 1]
    assert "RALPH_GRAPH_TASK=" in command[-1]
    assert "ralph graph-apply" in command[-1]
    decision = decide_tool(state, "worker", "Bash", command="ralph graph-apply . task.json")
    assert decision.decision == "allow"


def test_flow_stage03_waits_for_graph_apply_artifacts_before_auto_advance(tmp_path: Path):
    root = _project(tmp_path)
    state = load_state(root / "loop-state.json")
    graph = _flow_graph()
    state["run_mode"] = "flow_only"
    state["stage"] = {
        **state["stage"], "id": "03", "revision": "r1", "on_success": "04",
        "required_outputs": ["task_graph", "coverage_proof"],
    }
    state["task_spec"]["attribute_matrix"] = [
        {"concept": "task_graph", "role": "task_graph", "attribute": "validated graph", "task_graph": graph, "disposition": "inferred", "rationale": "仅用于验证流程", "evidence_refs": []},
        {"concept": "coverage_proof", "role": "coverage_proof", "attribute": "covers all nodes", "disposition": "inferred", "rationale": "仅用于验证流程", "evidence_refs": []},
    ]
    state["plan"] = graph
    save_state(root / "loop-state.json", state)

    assert cli._field_engine_tick(root, state) is False
    assert load_state(root / "loop-state.json")["stage"]["id"] == "03"

    completed_graph = _flow_graph()
    completed_graph["completed"] = ["T1.1", "T1.2", "J1"]
    completed_graph["task_results"] = {}
    for node in completed_graph["nodes"]:
        ref = node["writes"][0]
        output = root / ref
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(json.dumps({"node": node["id"]}), encoding="utf-8")
        completed_graph["task_results"][node["id"]] = {
            "artifact_refs": [ref],
            "output": {"node": node["id"]},
            "evidence": [ref],
        }
    live = load_state(root / "loop-state.json")
    live["plan"] = completed_graph
    save_state(root / "loop-state.json", live)

    assert cli._field_engine_tick(root, live) is True
    assert load_state(root / "loop-state.json")["stage"]["id"] == "04"


def test_flow_final_cross_validation_marks_run_completed(tmp_path: Path):
    root = _project(tmp_path)
    state = load_state(root / "loop-state.json")
    state["run_mode"] = "flow_only"
    state["stage"] = {
        **state["stage"], "id": "04.5", "revision": "r1", "on_success": "exploration",
        "required_outputs": ["cross_validation_out"],
    }
    state["task_spec"]["attribute_matrix"] = [{
        "concept": "cross_validation_out", "role": "cross_validation_out",
        "attribute": "独立核验、矛盾与残余不确定性已记录",
        "disposition": "inferred", "rationale": "仅用于验证流程", "evidence_refs": [],
    }]
    save_state(root / "loop-state.json", state)

    assert cli._field_engine_tick(root, state) is True
    assert load_state(root / "loop-state.json")["status"] == "completed"


def test_flow_only_stage02_auto_advance_does_not_require_web_evidence(tmp_path: Path):
    root = _project(tmp_path)
    state = load_state(root / "loop-state.json")
    state["run_mode"] = "flow_only"
    state["stage"] = {
        **state["stage"], "id": "02", "revision": "r1", "on_success": "02.5",
        "required_outputs": ["research_findings"],
    }
    state["task_spec"]["attribute_matrix"] = [{
        "concept": "闭环研究结论", "role": "research_findings",
        "attribute": "本地固定输入的推导结论", "disposition": "inferred",
        "rationale": "仅用于验证流程", "evidence_refs": [],
    }]
    save_state(root / "loop-state.json", state)

    assert cli._field_engine_tick(root, state) is True
    assert load_state(root / "loop-state.json")["stage"]["id"] == "02.5"


def test_field_tasks_are_generated_from_current_factor_count(tmp_path: Path):
    root = _project(tmp_path)
    state = load_state(root / "loop-state.json")
    state["stage"]["id"] = "02"
    state["task_spec"]["attribute_matrix"] = [
        {
            "concept": f"因素-{index}",
            "role": "constraint",
            "attribute": f"待研究属性-{index}",
            "disposition": "research_required",
            "evidence_refs": [],
        }
        for index in range(1, 6)
    ]
    tasks = materialize_field_tasks(root, state)
    assert len(tasks) == 5
    assert {task["concept"] for task in tasks} == {f"因素-{index}" for index in range(1, 6)}

    # Removing two factors changes only the generated queue; there is no
    # hard-coded six-field assumption and completed concepts would remain
    # preserved by the normal materializer.
    state["task_spec"]["attribute_matrix"] = state["task_spec"]["attribute_matrix"][:3]
    tasks = materialize_field_tasks(root, state)
    assert {task["concept"] for task in tasks} == {"因素-1", "因素-2", "因素-3"}


def test_stage02_synthesizes_research_tasks_from_stage01_unknown(tmp_path: Path):
    root = _project(tmp_path)
    prior_dir = root / "loop-artifacts/stages/01/r1"
    prior_dir.mkdir(parents=True, exist_ok=True)
    (prior_dir / "state.json").write_text(json.dumps({
        "attribute_matrix": [{
            "concept": "阶段 01 输出：unknown",
            "role": "unknown",
            "attribute": "价格区间；显存容量；驱动兼容性",
            "disposition": "inferred",
            "evidence_refs": [],
        }]
    }, ensure_ascii=False), encoding="utf-8")
    state = load_state(root / "loop-state.json")
    state["stage"]["id"] = "02"
    state["stage"]["required_outputs"] = ["research_findings"]
    state["task_spec"] = None
    tasks = materialize_field_tasks(root, state)
    assert [task["concept"] for task in tasks] == [
        "研究未知因素：价格区间",
        "研究未知因素：显存容量",
        "研究未知因素：驱动兼容性",
    ]
    assert all(task["disposition"] == "research_required" for task in tasks)
    assert state["task_spec"]["attribute_matrix"][0]["role"] == "research_findings"
def test_stage01_required_outputs_materialize_as_bounded_tasks(tmp_path: Path):
    root = _project(tmp_path)
    state = load_state(root / "loop-state.json")
    state["stage"] = {
        "id": "01",
        "revision": "r1",
        "required_outputs": ["goal", "known", "unknown"],
    }
    state["task_spec"]["attribute_matrix"] = []
    tasks = materialize_field_tasks(root, state)
    assert {task["field"]["role"] for task in tasks} == {"goal", "known", "unknown"}
    assert all(task["status"] == "ready" for task in tasks)


def test_stage01_placeholder_can_be_saved_as_incremental_progress(tmp_path: Path):
    root = _project(tmp_path)
    state = load_state(root / "loop-state.json")
    state["stage"]["id"] = "01"
    state["task_spec"]["attribute_matrix"] = []
    tasks = materialize_field_tasks(root, state)
    task_path = root / tasks[0]["path"]
    result = apply_fields(root, task_path)
    assert result["ok"] is True
    assert result["remaining"]["pending"]


def test_invalid_json_never_changes_state_and_returns_repair_location(tmp_path: Path):
    root = _project(tmp_path)
    draft = Path(init_fields(root)["fields_file"])
    before = load_state(root / "loop-state.json")["task_spec"]["attribute_matrix"]
    draft.write_text('{"fields": [}', encoding="utf-8")
    with pytest.raises(ValueError, match="JSON 语法错误") as error:
        apply_fields(root, draft)
    assert str(draft) in str(error.value)
    after = load_state(root / "loop-state.json")["task_spec"]["attribute_matrix"]
    assert after == before


def test_flow_only_worker_cannot_submit_unchanged_pending_placeholder(tmp_path: Path, monkeypatch):
    root = _project(tmp_path)
    state = load_state(root / "loop-state.json")
    state["run_mode"] = "flow_only"
    state["stage"]["id"] = "exploration"
    state["stage"]["required_outputs"] = ["candidate_tasks"]
    state["task_spec"]["attribute_matrix"] = [{
        "concept": "阶段 01 输出：candidate_tasks",
        "role": "candidate_tasks",
        "attribute": "请填写 candidate_tasks 的正交因素分解",
        "disposition": "pending",
        "rationale": "由运行时为缺失的 required output 生成的增量字段任务。",
        "evidence_refs": [],
    }]
    save_state(root / "loop-state.json", state)
    task_path = Path(materialize_field_tasks(root, state)[0]["path"])
    monkeypatch.setenv("RALPH_ROLE", "worker")
    with pytest.raises(ValueError, match="worker 必须先用 Write/Edit"):
        apply_fields(root, task_path)
    assert load_state(root / "loop-state.json")["task_spec"]["attribute_matrix"][0]["disposition"] == "pending"


def test_flow_only_worker_research_draft_is_merged_as_inferred(tmp_path: Path, monkeypatch):
    root = _project(tmp_path)
    state = load_state(root / "loop-state.json")
    state["run_mode"] = "flow_only"
    state["stage"] = {**state["stage"], "id": "02", "required_outputs": ["research_findings"]}
    state["task_spec"]["attribute_matrix"] = [{
        "concept": "闭环未知项", "role": "research_findings", "attribute": "虚构本地输入",
        "disposition": "research_required", "rationale": "初始 synthetic 字段", "evidence_refs": [],
    }]
    save_state(root / "loop-state.json", state)
    task_path = root / materialize_field_tasks(root, state)[0]["path"]
    task = json.loads(task_path.read_text(encoding="utf-8"))
    task["field"].update({
        "disposition": "research_required", "rationale": "网页被禁用，因此保留闭环测试结论", "evidence_refs": [],
    })
    task_path.write_text(json.dumps(task, ensure_ascii=False), encoding="utf-8")

    monkeypatch.setenv("RALPH_ROLE", "worker")
    assert apply_fields(root, task_path)["ok"] is True
    merged = load_state(root / "loop-state.json")["task_spec"]["attribute_matrix"][0]
    assert merged["disposition"] == "inferred"
    assert "仅用于验证流程" in merged["rationale"]


def test_field_apply_is_incremental_and_preserves_previous_fields(tmp_path: Path):
    root = _project(tmp_path)
    draft = Path(init_fields(root)["fields_file"])

    draft.write_text(
        json.dumps(
            {
                "fields": [
                    {
                        "concept": "工作负载",
                        "role": "background",
                        "attribute": "本地 LLM 推理",
                        "disposition": "pending",
                    }
                ]
            },
            ensure_ascii=False,
        ),
        encoding="utf-8",
    )
    first = apply_fields(root, draft)
    assert first["ok"] is True
    assert "工作负载" in first["remaining"]["pending"]

    # The second turn only updates one concept and adds another.  The initial
    # user task and the first concept must remain in the canonical state.
    draft.write_text(
        json.dumps(
            {
                "fields": [
                    {
                        "concept": "工作负载",
                        "role": "background",
                        "attribute": "本地 LLM 推理",
                        "disposition": "inferred",
                        "rationale": "由本地 AI 需求推断",
                        "evidence_refs": [],
                        "confidence": 0.8,
                    },
                    {
                        "concept": "预算",
                        "role": "constraint",
                        "attribute": "需要分层比较",
                        "disposition": "research_required",
                        "evidence_refs": [],
                    },
                ]
            },
            ensure_ascii=False,
        ),
        encoding="utf-8",
    )
    second = apply_fields(root, draft)
    assert second["total"] == 3  # original user task + two concepts
    matrix = load_state(root / "loop-state.json")["task_spec"]["attribute_matrix"]
    by_concept = {field["concept"]: field for field in matrix}
    assert by_concept["工作负载"]["disposition"] == "inferred"
    assert by_concept["预算"]["disposition"] == "research_required"
    assert by_concept["用户原始任务"]["disposition"] == "confirmed"


def test_applied_incomplete_field_attempt_allows_next_field_without_fake_pass(tmp_path: Path):
    root = _project(tmp_path)
    state = load_state(root / "loop-state.json")
    state["stage"]["id"] = "02"
    state["task_spec"]["attribute_matrix"] = [{
        "concept": "显存容量",
        "role": "constraint",
        "attribute": "最大模型规模",
        "disposition": "research_required",
        "evidence_refs": [],
    }]
    tasks = materialize_field_tasks(root, state)
    state["field_tasks"][0].update({
        "status": "dispatched",
        "agent_id": "child-vram",
        "agent_ids": ["child-vram"],
        "apply_count_at_dispatch": 0,
    })
    save_state(root / "loop-state.json", state)
    task_path = root / tasks[0]["path"]
    task = json.loads(task_path.read_text(encoding="utf-8"))
    task["field"]["rationale"] = "网页工具不可用，保留待补研究状态"
    task_path.write_text(json.dumps(task, ensure_ascii=False), encoding="utf-8")
    result = apply_fields(root, task_path)
    assert result["ok"] is True
    assert load_state(root / "loop-state.json")["field_tasks"][0]["apply_count"] == 1

    handle_subagentstop({"cwd": str(root), "agent_id": "child-vram", "stop_reason": "completed"}, mode="hybrid")
    live = load_state(root / "loop-state.json")
    assert live["field_tasks"][0]["status"] == "deferred"
    assert live["task_spec"]["attribute_matrix"][0]["disposition"] == "research_required"
    reopened = reopen_deferred_field_tasks(root, live)
    assert reopened == [live["field_tasks"][0]["id"]]
    assert live["field_tasks"][0]["status"] == "ready"


def test_late_parent_agent_receipt_does_not_revive_deferred_field(tmp_path: Path):
    """SubagentStop may precede PostToolUse(Agent) in Claude's hook stream."""

    root = _project(tmp_path)
    state = load_state(root / "loop-state.json")
    state["stage"]["id"] = "02"
    state["task_spec"]["attribute_matrix"] = [{
        "concept": "价格证据",
        "role": "research_findings",
        "attribute": "当前市场价",
        "disposition": "research_required",
        "evidence_refs": [],
    }]
    tasks = materialize_field_tasks(root, state)
    state["field_tasks"][0].update({
        "status": "dispatched",
        "agent_id": "child-price",
        "agent_ids": ["child-price"],
        "apply_count": 1,
        "apply_count_at_dispatch": 0,
    })
    save_state(root / "loop-state.json", state)

    handle_subagentstop(
        {"cwd": str(root), "agent_id": "child-price", "stop_reason": "completed"},
        mode="hybrid",
    )
    task_path = tasks[0]["path"]
    handle_posttooluse({
        "cwd": str(root),
        "tool_name": "Agent",
        "tool_input": {"prompt": f"RALPH_FIELD_TASK={task_path}\n只处理一个字段"},
        "tool_response": {"status": "completed", "agentId": "child-price"},
    }, mode="hybrid")

    live = load_state(root / "loop-state.json")
    assert live["field_tasks"][0]["status"] == "deferred"
    assert live["field_tasks"][0].get("agent_id") == "child-price"


def test_reconcile_applied_field_reopens_historical_late_receipt_without_losing_draft(tmp_path: Path):
    root = _project(tmp_path)
    state = load_state(root / "loop-state.json")
    state["stage"]["id"] = "02"
    state["task_spec"]["attribute_matrix"] = [{
        "concept": "价格证据",
        "role": "research_findings",
        "attribute": "当前市场价",
        "disposition": "research_required",
        "rationale": "第一次来源请求失败，保留为待补。",
        "evidence_refs": [],
    }]
    tasks = materialize_field_tasks(root, state)
    state["field_tasks"][0].update({
        "status": "dispatched",
        "agent_id": "old-child",
        "agent_ids": ["old-child"],
        "apply_count": 1,
        "apply_count_at_dispatch": 0,
    })
    save_state(root / "loop-state.json", state)

    reconciled = reconcile_applied_field_tasks(root, state)

    assert reconciled == [{"field_task_id": tasks[0]["id"], "status": "ready"}]
    assert state["field_tasks"][0]["status"] == "ready"
    assert state["field_tasks"][0].get("agent_id") is None
    draft = json.loads((root / tasks[0]["path"]).read_text(encoding="utf-8"))
    assert draft["field"]["rationale"] == "第一次来源请求失败，保留为待补。"


def test_top_level_worker_field_apply_releases_its_reservation(tmp_path: Path, monkeypatch):
    root = _project(tmp_path)
    state = load_state(root / "loop-state.json")
    state["stage"]["id"] = "02"
    state["task_spec"]["attribute_matrix"] = [{
        "concept": "网页证据",
        "role": "research_findings",
        "attribute": "待核验事实",
        "disposition": "research_required",
        "evidence_refs": [],
    }]
    tasks = materialize_field_tasks(root, state)
    tasks[0].update({"status": "dispatched", "agent_id": "auto-worker", "apply_count_at_dispatch": 0})
    state["field_tasks"] = tasks
    save_state(root / "loop-state.json", state)
    task_path = root / tasks[0]["path"]
    task = json.loads(task_path.read_text(encoding="utf-8"))
    task["field"]["rationale"] = "外部网页暂时不可用，保留待补状态"
    task_path.write_text(json.dumps(task, ensure_ascii=False), encoding="utf-8")

    monkeypatch.setenv("RALPH_ROLE", "worker")
    result = apply_fields(root, task_path)
    assert result["ok"] is True
    live = load_state(root / "loop-state.json")
    assert live["field_tasks"][0]["status"] == "deferred"
    assert live["field_tasks"][0].get("agent_id") is None


def test_deferred_fields_do_not_starve_ready_queue(tmp_path: Path):
    root = _project(tmp_path)
    state = load_state(root / "loop-state.json")
    state["stage"]["id"] = "02"
    state["task_spec"]["attribute_matrix"] = [
        {
            "concept": "暂时缺证据",
            "role": "research_findings",
            "attribute": "待补",
            "disposition": "research_required",
            "evidence_refs": [],
        },
        {
            "concept": "另一个待研究因素",
            "role": "research_findings",
            "attribute": "待补",
            "disposition": "research_required",
            "evidence_refs": [],
        },
    ]
    tasks = materialize_field_tasks(root, state)
    tasks[0]["status"] = "deferred"
    tasks[0]["last_applied_at"] = "2026-07-25T00:00:00+00:00"
    tasks[1]["status"] = "ready"
    tasks[1]["last_applied_at"] = "2026-07-25T01:00:00+00:00"
    state["field_tasks"] = tasks
    save_state(root / "loop-state.json", state)

    assert reopen_deferred_field_tasks(root, state) == []
    state["field_tasks"][1]["status"] = "deferred"
    reopened = reopen_deferred_field_tasks(root, state)
    assert reopened == [tasks[0]["id"]]
    assert state["field_tasks"][0]["status"] == "ready"
    assert state["field_tasks"][1]["status"] == "deferred"


def test_auto_worker_timeout_reopens_field_without_leaking_slot(tmp_path: Path, monkeypatch):
    root = _project(tmp_path)
    state = load_state(root / "loop-state.json")
    state["stage"]["id"] = "02"
    state["task_spec"]["attribute_matrix"] = [{
        "concept": "自动超时字段",
        "role": "research_findings",
        "attribute": "待补证据",
        "disposition": "research_required",
        "evidence_refs": [],
    }]
    tasks = materialize_field_tasks(root, state)
    tasks[0].update({"status": "dispatched", "agent_id": "auto-timeout", "updated_at": "now"})
    state["field_tasks"] = tasks
    save_state(root / "loop-state.json", state)
    task_path = root / tasks[0]["path"]
    draft = json.loads(task_path.read_text(encoding="utf-8"))
    draft["field"]["rationale"] = "外部网页暂时不可用，保留待补状态"
    task_path.write_text(json.dumps(draft, ensure_ascii=False), encoding="utf-8")

    log = (root / "worker.log").open("wb")
    process = subprocess.Popen(["sleep", "10"], stdout=log, stderr=subprocess.STDOUT)
    workers = {
        tasks[0]["id"]: {
            "process": process,
            "log": log,
            "agent_id": "auto-timeout",
            "started_at": time.monotonic() - 1,
        }
    }
    monkeypatch.setenv("RALPH_AUTO_FIELD_WORKER_TIMEOUT", "0.01")
    assert _reap_auto_field_workers(root, workers) == set()
    live = load_state(root / "loop-state.json")
    assert live["field_tasks"][0]["status"] == "ready"
    assert live["field_tasks"][0].get("agent_id") is None
    saved = next(
        item for item in live["task_spec"]["attribute_matrix"]
        if item["concept"] == "自动超时字段"
    )
    assert saved["rationale"] == "外部网页暂时不可用，保留待补状态"
    assert "auto_field_draft_applied_on_timeout" in (root / "loop-events.md").read_text(encoding="utf-8")
    assert not workers


def test_live_auto_worker_is_reaped_when_state_reopened_to_ready(tmp_path: Path):
    root = _project(tmp_path)
    state = load_state(root / "loop-state.json")
    state["stage"]["id"] = "02"
    state["task_spec"]["attribute_matrix"] = [{
        "concept": "孤儿字段",
        "role": "research_findings",
        "attribute": "待研究",
        "disposition": "research_required",
        "evidence_refs": [],
    }]
    tasks = materialize_field_tasks(root, state)
    tasks[0].update({"status": "ready", "agent_id": None})
    state["field_tasks"] = tasks
    save_state(root / "loop-state.json", state)

    log = (root / "orphan-worker.log").open("wb")
    process = subprocess.Popen(["sleep", "10"], stdout=log, stderr=subprocess.STDOUT)
    workers = {
        tasks[0]["id"]: {
            "process": process,
            "log": log,
            "agent_id": "orphan-worker",
            "started_at": time.monotonic(),
        }
    }
    assert _reap_auto_field_workers(root, workers) == set()
    assert not workers
    assert process.poll() is not None
    assert "auto_field_worker_orphan_reaped" in (root / "loop-events.md").read_text(encoding="utf-8")


def test_stale_auto_worker_releases_dispatched_slot_and_preserves_process_group(tmp_path: Path, monkeypatch):
    """A stale fallback worker must not kill the invoking test/supervisor group."""

    root = _project(tmp_path)
    state = load_state(root / "loop-state.json")
    state["stage"]["id"] = "02"
    state["task_spec"]["attribute_matrix"] = [{
        "concept": "旧字段 worker",
        "role": "research_findings",
        "attribute": "待补证据",
        "disposition": "research_required",
        "evidence_refs": [],
    }]
    tasks = materialize_field_tasks(root, state)
    tasks[0].update({
        "status": "dispatched",
        "agent_id": "auto-stale",
        "updated_at": (datetime.now(timezone.utc) - timedelta(seconds=120)).isoformat(),
    })
    state["field_tasks"] = tasks
    save_state(root / "loop-state.json", state)

    log = (root / "stale-worker.log").open("wb")
    process = subprocess.Popen(["sleep", "10"], stdout=log, stderr=subprocess.STDOUT)
    workers = {
        tasks[0]["id"]: {
            "process": process,
            "log": log,
            "agent_id": "auto-stale",
            "started_at": time.monotonic(),
        }
    }
    monkeypatch.setenv("RALPH_FIELD_AGENT_STALL_SECONDS", "90")

    assert _reap_auto_field_workers(root, workers) == set()
    live = load_state(root / "loop-state.json")
    assert live["field_tasks"][0]["status"] == "ready"
    assert live["field_tasks"][0].get("agent_id") is None
    assert process.poll() is not None
    assert "auto_field_worker_stall_reaped" in (root / "loop-events.md").read_text(encoding="utf-8")


def test_disabled_field_worker_heartbeat_does_not_reap_a_fresh_reservation(monkeypatch):
    """The default disabled watchdog must not turn every elapsed duration into a stall."""

    now = datetime.now(timezone.utc)
    task = {
        "status": "dispatched",
        "web_failures": 0,
        "updated_at": (now - timedelta(seconds=120)).isoformat(),
    }

    monkeypatch.delenv("RALPH_FIELD_AGENT_STALL_SECONDS", raising=False)
    assert _field_task_stall_requested(task, now=now) is False

    monkeypatch.setenv("RALPH_FIELD_AGENT_STALL_SECONDS", "90")
    assert _field_task_stall_requested(task, now=now) is True


def test_invalid_json_draft_does_not_mutate_state(tmp_path: Path):
    root = _project(tmp_path)
    draft = Path(init_fields(root)["fields_file"])
    before = load_state(root / "loop-state.json")
    draft.write_text('{"fields": [', encoding="utf-8")

    with pytest.raises(ValueError, match="JSON 语法错误"):
        apply_fields(root, draft)

    assert load_state(root / "loop-state.json") == before


def test_field_agent_watchdog_catches_no_progress_without_web_failure(tmp_path: Path, monkeypatch):
    root = _project(tmp_path)
    state = load_state(root / "loop-state.json")
    state["stage"]["id"] = "02"
    state["task_spec"]["attribute_matrix"] = [{
        "concept": "模型规模",
        "role": "constraint",
        "attribute": "可加载规模",
        "disposition": "research_required",
        "evidence_refs": [],
    }]
    tasks = materialize_field_tasks(root, state)
    tasks[0]["status"] = "dispatched"
    tasks[0]["updated_at"] = (
        datetime.now(timezone.utc) - timedelta(seconds=120)
    ).isoformat()
    tasks[0]["apply_count_at_dispatch"] = 0
    state["field_tasks"] = tasks
    save_state(root / "loop-state.json", state)

    monkeypatch.setenv("RALPH_FIELD_AGENT_STALL_SECONDS", "90")
    assert _field_agent_stall_requested(root) is True


def test_field_gate_requires_current_stage_outputs_before_advance(tmp_path: Path):
    root = _project(tmp_path)
    state = load_state(root / "loop-state.json")
    state["stage"] = {
        **state["stage"],
        "id": "02",
        "required_outputs": ["research_findings"],
    }
    state["task_spec"] = {
        "attribute_matrix": [{
            "concept": "显存容量",
            "role": "constraint",
            "attribute": "当前证据",
            "disposition": "confirmed",
            "evidence_refs": ["source-a"],
        }]
    }
    action = parse_action({
        "action": "advance",
        "status": "passed",
        "stage_id": "02",
        "revision": "r1",
        "next_stage": "02.5",
        "payload": {"research_findings": "待写入"},
    })
    with pytest.raises(ProtocolError, match="required_outputs"):
        validate_action(action, state)


def test_hybrid_hook_synthesizes_missing_stage02_research_entry(tmp_path: Path):
    root = _project(tmp_path)
    state = load_state(root / "loop-state.json")
    state["stage"]["id"] = "02"
    state["task_spec"]["attribute_matrix"] = []
    save_state(root / "loop-state.json", state)
    result = handle_pretooluse(
        {
            "cwd": str(root),
            "tool_name": "Agent",
            "tool_input": {"prompt": "分析一个窄研究问题"},
            "ralph_role": "commander",
        },
        mode="hybrid",
    )
    output = result["hookSpecificOutput"]
    assert output["permissionDecision"] == "allow"
    assert "FIELD_TASK_MARKER_AUTOFILLED" in output["permissionDecisionReason"]
    assert "ralph field-init" in output["additionalContext"]
    assert "ralph field-apply" in output["additionalContext"]
    assert "ralph apply" in output["additionalContext"]


def test_hybrid_hook_autobinds_missing_field_marker_without_widening_scope(tmp_path: Path):
    root = _project(tmp_path)
    state = load_state(root / "loop-state.json")
    state["stage"]["id"] = "02"
    state["task_spec"]["attribute_matrix"] = [{
        "concept": "价格",
        "role": "constraint",
        "attribute": "当前市场价",
        "disposition": "research_required",
        "evidence_refs": [],
    }]
    materialize_field_tasks(root, state)
    save_state(root / "loop-state.json", state)

    result = handle_pretooluse(
        {
            "cwd": str(root),
            "tool_name": "Agent",
            # Simulates a local frontend that drops the first prompt line.
            "tool_input": {"description": "调研价格"},
            "ralph_role": "commander",
        },
        mode="hybrid",
    )
    hook = result["hookSpecificOutput"]
    assert hook["permissionDecision"] == "allow"
    assert "自动绑定字段任务" in hook["additionalContext"]
    updated = load_state(root / "loop-state.json")
    assert updated["field_tasks"][0]["status"] == "dispatching"


def test_hook_injects_commands_for_every_commander_tool(tmp_path: Path):
    root = _project(tmp_path)
    for tool_name in ("Read", "Grep", "Glob", "WebSearch", "Bash", "Write", "Edit", "Agent"):
        result = handle_pretooluse(
            {
                "cwd": str(root),
                "tool_name": tool_name,
                "tool_input": {"command": "ralph status ."} if tool_name == "Bash" else {},
                "ralph_role": "commander",
            },
            mode="hybrid",
        )
        context = result["hookSpecificOutput"].get("additionalContext", "")
        assert "ralph field-init" in context
        assert "ralph field-apply" in context
        assert "ralph apply" in context


def test_worker_hook_injects_incremental_commands_without_state_write_path(tmp_path: Path):
    root = _project(tmp_path)
    state = load_state(root / "loop-state.json")
    state["stage"]["id"] = "02"
    state["task_spec"]["attribute_matrix"] = [{
        "concept": "价格",
        "role": "constraint",
        "attribute": "当前市场价",
        "disposition": "research_required",
        "evidence_refs": [],
    }]
    tasks = materialize_field_tasks(root, state)
    save_state(root / "loop-state.json", state)
    result = handle_pretooluse(
        {
            "cwd": str(root),
            "tool_name": "Read",
            "tool_input": {"file_path": tasks[0]["path"]},
            "agent_id": "field-worker-commands",
        },
        mode="hybrid",
    )
    context = result["hookSpecificOutput"]["additionalContext"]
    assert "ralph field-apply" in context
    assert "不要修改 loop-state.json" in context


def test_worker_cannot_edit_another_field_file(tmp_path: Path):
    root = _project(tmp_path)
    state = load_state(root / "loop-state.json")
    state["stage"]["id"] = "02"
    state["task_spec"]["attribute_matrix"] = [{
        "concept": "价格",
        "role": "constraint",
        "attribute": "当前市场价",
        "disposition": "research_required",
        "evidence_refs": [],
    }]
    tasks = materialize_field_tasks(root, state)
    tasks[0].update({"status": "dispatched", "agent_id": "path-worker"})
    state["field_tasks"] = tasks
    save_state(root / "loop-state.json", state)

    result = handle_pretooluse(
        {
            "cwd": str(root),
            "tool_name": "Edit",
            "tool_input": {"file_path": "loop-artifacts/stages/02/r1/other.json"},
            "agent_id": "path-worker",
        },
        mode="hybrid",
    )
    hook = result["hookSpecificOutput"]
    assert hook["permissionDecision"] == "deny"
    assert "FIELD_TASK_PATH_CORRECTION" in hook["permissionDecisionReason"]
    assert tasks[0]["path"] in hook["permissionDecisionReason"]


def test_worker_repeated_read_is_hard_denied_after_three_reads(tmp_path: Path):
    root = _project(tmp_path)
    state = load_state(root / "loop-state.json")
    state["stage"]["id"] = "02"
    state["task_spec"]["attribute_matrix"] = [{
        "concept": "价格",
        "role": "constraint",
        "attribute": "当前市场价",
        "disposition": "research_required",
        "evidence_refs": [],
    }]
    tasks = materialize_field_tasks(root, state)
    tasks[0].update({"status": "dispatched", "agent_id": "read-once-worker"})
    state["field_tasks"] = tasks
    save_state(root / "loop-state.json", state)
    payload = {
        "cwd": str(root),
        "tool_name": "Read",
        "tool_input": {"file_path": tasks[0]["path"]},
        "agent_id": "read-once-worker",
    }
    for _ in range(3):
        first = handle_posttooluse(payload, mode="hybrid")
        assert "下一次工具调用必须是 Write 或 Edit" in first["hookSpecificOutput"]["additionalContext"]
    fourth = handle_pretooluse(payload, mode="hybrid")
    hook = fourth["hookSpecificOutput"]
    assert hook["permissionDecision"] == "deny"
    assert "FIELD_WRITE_AFTER_READ" in hook["permissionDecisionReason"]
    assert "field-apply" in hook["permissionDecisionReason"]


def test_new_field_dispatch_resets_read_budget_after_stale_retry(tmp_path: Path):
    root = _project(tmp_path)
    state = load_state(root / "loop-state.json")
    state["stage"]["id"] = "02"
    state["task_spec"]["attribute_matrix"] = [{
        "concept": "价格",
        "role": "constraint",
        "attribute": "当前市场价",
        "disposition": "research_required",
        "evidence_refs": [],
    }]
    tasks = materialize_field_tasks(root, state)
    state["field_tasks"][0].update({
        "status": "ready",
        "field_read_count": 3,
        "last_error": "stale worker",
    })
    save_state(root / "loop-state.json", state)

    updated, claimed = claim_field_task(root, tasks[0]["id"], dispatch_name="retry-worker")

    assert claimed is not None
    assert claimed["status"] == "dispatching"
    assert claimed["field_read_count"] == 0
    assert updated["field_tasks"][0]["field_read_count"] == 0


def test_dispatch_first_is_hard_denied_when_ready_fields_exist(tmp_path: Path):
    root = _project(tmp_path)
    state = load_state(root / "loop-state.json")
    state["stage"]["id"] = "02"
    state["task_spec"]["attribute_matrix"] = [{
        "concept": "价格",
        "role": "constraint",
        "attribute": "当前市场价",
        "disposition": "research_required",
        "evidence_refs": [],
    }]
    materialize_field_tasks(root, state)
    save_state(root / "loop-state.json", state)

    result = handle_pretooluse(
        {
            "cwd": str(root),
            "tool_name": "Read",
            "tool_input": {"file_path": "notes.md"},
            "ralph_role": "commander",
        },
        mode="hybrid",
    )
    hook = result["hookSpecificOutput"]
    assert hook["permissionDecision"] == "deny"
    assert "FIELD_DISPATCH_FIRST" in hook["permissionDecisionReason"]


def test_pending_structural_fields_do_not_force_agent_dispatch(tmp_path: Path):
    root = _project(tmp_path)
    state = load_state(root / "loop-state.json")
    state["stage"]["id"] = "01"
    state["task_spec"]["attribute_matrix"] = [{
        "concept": "目标摘要",
        "role": "goal",
        "attribute": "待补充的目标语义",
        "disposition": "pending",
        "evidence_refs": [],
    }]
    materialize_field_tasks(root, state)
    save_state(root / "loop-state.json", state)

    result = handle_pretooluse(
        {
            "cwd": str(root),
            "tool_name": "Read",
            "tool_input": {"file_path": "notes.md"},
            "ralph_role": "commander",
        },
        mode="hybrid",
    )
    hook = result["hookSpecificOutput"]
    assert hook["permissionDecision"] == "allow"
    assert "FIELD_DISPATCH_FIRST" not in hook.get("permissionDecisionReason", "")

    rendered = PromptRenderer().render(load_state(root / "loop-state.json"))
    assert "Commander 可直接增量填写" in rendered.text
    assert "只有 disposition=research_required 的字段必须逐字段派 Agent" in rendered.text
    assert "下一次工具调用必须是 Agent" not in rendered.text


def test_field_commander_cannot_use_unlisted_coordination_tool_in_hybrid(tmp_path: Path):
    root = _project(tmp_path)
    result = handle_pretooluse(
        {
            "cwd": str(root),
            "tool_name": "SendMessage",
            "tool_input": {"to": "field-worker", "message": "继续"},
            "ralph_role": "commander",
        },
        mode="hybrid",
    )
    hook = result["hookSpecificOutput"]
    assert hook["permissionDecision"] == "deny"
    assert "TOOL_STAGE_SCOPE_FIELD" in hook["permissionDecisionReason"]


def test_failed_incremental_command_returns_posttool_repair_prompt(tmp_path: Path):
    root = _project(tmp_path)
    result = handle_posttooluse(
        {
            "cwd": str(root),
            "tool_name": "Bash",
            "tool_input": {"command": "ralph field-apply . fields.json"},
            "tool_response": {"success": False, "stderr": "JSON 语法错误"},
        },
        mode="hybrid",
    )
    context = result["hookSpecificOutput"]["additionalContext"]
    assert "JSON 语法错误" in context
    assert "只修复错误指出的 JSON 语法或缺失字段" in context
    assert load_state(root / "loop-state.json").get("subagent_cards") is None


def test_worker_second_read_is_hard_prompt_to_write(tmp_path: Path):
    root = _project(tmp_path)
    state = load_state(root / "loop-state.json")
    state["stage"]["id"] = "02"
    state["task_spec"]["attribute_matrix"] = [{
        "concept": "价格",
        "role": "constraint",
        "attribute": "当前市场价",
        "disposition": "research_required",
        "evidence_refs": [],
    }]
    tasks = materialize_field_tasks(root, state)
    state["field_tasks"] = [{
        "id": tasks[0]["id"],
        "path": tasks[0]["path"],
        "status": "dispatched",
        "disposition": "research_required",
        "agent_id": "worker-1",
        "field_read_count": 1,
    }]
    save_state(root / "loop-state.json", state)
    result = handle_pretooluse({
        "cwd": str(root),
        "ralph_role": "worker",
        "agent_id": "worker-1",
        "tool_name": "Read",
        "tool_input": {"file_path": tasks[0]["path"]},
    }, mode="hybrid")
    reason = result["hookSpecificOutput"]["permissionDecisionReason"]
    assert result["hookSpecificOutput"]["permissionDecision"] == "deny"
    assert "FIELD_WRITE_AFTER_READ" in reason
    assert "Write/Edit" in reason


def test_generated_ralph_prompt_does_not_accumulate_as_authoritative_input(tmp_path: Path):
    root = _project(tmp_path)
    state = load_state(root / "loop-state.json")
    before = len(state["task_spec"].get("authoritative_inputs", []))
    updated = record_human_input(
        state,
        "# RALPH 字段增量提示（02-r1）\nRALPH_FIELD_TASK=loop-artifacts/x.json",
    )
    assert len(updated["task_spec"]["authoritative_inputs"]) == before
    recovery = "# RALPH 最小恢复（01-r1）\n下一次工具调用只执行 `ralph field-init .`。"
    assert record_human_input(updated, recovery) == updated

    handle_userpromptsubmit({"cwd": str(root), "prompt": recovery})
    persisted = load_state(root / "loop-state.json")
    assert persisted == state
    event_log = root / "loop-events.md"
    assert not event_log.exists() or "human_input_received" not in event_log.read_text(encoding="utf-8")


def test_real_human_input_is_deduplicated_and_bounded(tmp_path: Path):
    root = _project(tmp_path)
    state = load_state(root / "loop-state.json")
    text = "真实需求 " + ("x" * 5000)
    once = record_human_input(state, text, source="human")
    twice = record_human_input(once, text, source="human")
    inputs = twice["task_spec"]["authoritative_inputs"]
    assert len(inputs) == 2
    assert inputs[-1]["characters"] == len(text)
    assert len(inputs[-1]["text"]) < len(text)


def test_hybrid_hook_still_hard_denies_direct_state_mutation(tmp_path: Path):
    root = _project(tmp_path)
    result = handle_pretooluse(
        {
            "cwd": str(root),
            "tool_name": "Write",
            "tool_input": {"file_path": "loop-state.json", "content": "{}"},
            "ralph_role": "commander",
        },
        mode="hybrid",
    )
    output = result["hookSpecificOutput"]
    assert output["permissionDecision"] == "deny"
    assert "loop-state.json" in output["permissionDecisionReason"]


def test_rendered_prompt_has_no_legacy_card_protocol(tmp_path: Path):
    root = _project(tmp_path)
    prompt = PromptRenderer().render(load_state(root / "loop-state.json")).text
    assert "ralph field-apply" in prompt
    assert "RALPH_TASK_CARD" not in prompt
    assert "requirements-auditor" not in prompt
    assert "task card" not in prompt.lower()


def test_legacy_last_result_recovers_task_spec_when_stage_artifact_is_empty(tmp_path: Path):
    root = _project(tmp_path)
    state_path = root / "loop-state.json"
    state = load_state(state_path)
    recovered_spec = {
        "status": "structured",
        "semantic_map": {"unknown": ["显存带宽", "价格"]},
        "attribute_matrix": [
            {
                "concept": "显存带宽",
                "role": "objective",
                "attribute": "影响 token/s",
                "disposition": "research_required",
                "evidence_refs": [],
            }
        ],
        "constraints": ["本地部署"],
    }
    state["last_result"] = {"payload": {"task_spec": recovered_spec}}
    save_state(state_path, state)
    artifact = state_path.parent / str(load_state(state_path)["current_artifact"])
    artifact.write_text('{"status":"unclarified","attribute_matrix":[]}', encoding="utf-8")

    loaded = load_state(state_path)
    assert loaded["task_spec"]["attribute_matrix"][0]["concept"] == "显存带宽"
    assert loaded["task_spec"]["semantic_map"]["unknown"] == ["显存带宽", "价格"]


def test_richer_last_result_is_merged_when_stage_artifact_is_only_seed_field(tmp_path: Path):
    root = _project(tmp_path)
    state_path = root / "loop-state.json"
    state = load_state(state_path)
    state["stage"]["id"] = "02"
    state["current_artifact"] = "loop-artifacts/stages/02/r1/state.json"
    state["last_result"] = {
        "payload": {
            "task_spec": {
                "attribute_matrix": [
                    {
                        "concept": "显存容量",
                        "role": "constraint",
                        "attribute": "影响可加载模型规模",
                        "disposition": "research_required",
                        "evidence_refs": [],
                    },
                    {
                        "concept": "显存带宽",
                        "role": "objective",
                        "attribute": "影响 token/s",
                        "disposition": "research_required",
                        "evidence_refs": [],
                    },
                ],
                "semantic_map": {"unknown": ["显存容量", "显存带宽"]},
            }
        }
    }
    save_state(state_path, state)
    artifact = root / "loop-artifacts/stages/02/r1/state.json"
    artifact.parent.mkdir(parents=True, exist_ok=True)
    artifact.write_text(
        json.dumps({"attribute_matrix": [state["task_spec"]["attribute_matrix"][0]]}, ensure_ascii=False),
        encoding="utf-8",
    )

    loaded = load_state(state_path)
    concepts = {item["concept"] for item in loaded["task_spec"]["attribute_matrix"]}
    assert {"显存容量", "显存带宽"}.issubset(concepts)
    assert loaded["task_spec"]["semantic_map"]["unknown"] == ["显存容量", "显存带宽"]


def test_field_tasks_are_generated_one_per_unresolved_factor(tmp_path: Path):
    root = _project(tmp_path)
    state = load_state(root / "loop-state.json")
    state["stage"]["id"] = "02"
    state["task_spec"]["attribute_matrix"] = [
        {"concept": "显存", "role": "constraint", "attribute": "容量", "disposition": "research_required"},
        {"concept": "价格", "role": "constraint", "attribute": "市场价", "disposition": "research_required"},
        {"concept": "已知背景", "role": "background", "attribute": "本地部署", "disposition": "confirmed"},
    ]
    tasks = materialize_field_tasks(root, state)
    assert [task["concept"] for task in tasks] == ["显存", "价格"]
    assert all(Path(root / task["path"]).exists() for task in tasks)
    assert all(task["type"] == "field_task" for task in tasks)


def test_task_file_is_an_incremental_draft_and_can_apply_directly(tmp_path: Path):
    root = _project(tmp_path)
    state = load_state(root / "loop-state.json")
    state["task_spec"]["attribute_matrix"] = [
        {
            "concept": "显存",
            "role": "constraint",
            "attribute": "容量",
            "disposition": "research_required",
            "evidence_refs": [],
        }
    ]
    save_state(root / "loop-state.json", state)
    task_state = load_state(root / "loop-state.json")
    task = materialize_field_tasks(root, task_state)[0]
    save_state(root / "loop-state.json", task_state)
    task_path = root / task["path"]
    payload = json.loads(task_path.read_text(encoding="utf-8"))
    payload["field"] = {
        "concept": "显存",
        "role": "constraint",
        "attribute": "容量决定可加载模型规模",
        "disposition": "confirmed",
        "rationale": "完成一轮窄字段核验",
        "evidence_refs": ["https://example.com/vram"],
        "confidence": 0.9,
    }
    task_path.write_text(json.dumps(payload, ensure_ascii=False), encoding="utf-8")

    result = apply_fields(root, task_path)
    assert result["ok"] is True
    assert result["remaining"]["researching"] == []
    assert load_state(root / "loop-state.json")["task_spec"]["attribute_matrix"][0]["concept"] == "显存"


def test_research_field_with_evidence_is_not_rematerialized(tmp_path: Path):
    root = _project(tmp_path)
    state = load_state(root / "loop-state.json")
    state["stage"]["id"] = "02"
    state["task_spec"]["attribute_matrix"] = [{
        "concept": "显存",
        "role": "constraint",
        "attribute": "容量",
        "disposition": "research_required",
        "evidence_refs": ["https://example.com/vram"],
    }]
    tasks = materialize_field_tasks(root, state)
    assert tasks == []
    assert state["field_tasks"] == []


def test_research_field_requires_agent_before_commander_reads(tmp_path: Path):
    root = _project(tmp_path)
    state = load_state(root / "loop-state.json")
    state["stage"]["id"] = "02"
    state["task_spec"]["attribute_matrix"] = [
        {
            "concept": "价格",
            "role": "constraint",
            "attribute": "当前市场价",
            "disposition": "research_required",
            "evidence_refs": [],
        }
    ]
    tasks = materialize_field_tasks(root, state)
    decision = decide_tool(state, "commander", "Read", target_path="notes.md")
    assert tasks and decision.decision == "deny"
    assert "FIELD_DISPATCH_FIRST" in decision.reason


def test_field_worker_agent_id_is_not_blocked_by_commander_gate(tmp_path: Path):
    root = _project(tmp_path)
    state = load_state(root / "loop-state.json")
    state["stage"]["id"] = "02"
    state["task_spec"]["attribute_matrix"] = [
        {
            "concept": "价格",
            "role": "constraint",
            "attribute": "当前市场价",
            "disposition": "research_required",
            "evidence_refs": [],
        }
    ]
    materialize_field_tasks(root, state)
    result = handle_pretooluse(
        {
            "cwd": str(root),
            "tool_name": "Read",
            "tool_input": {"file_path": "loop-artifacts/stages/02/r1/tasks/x.json"},
            "agent_id": "field-worker-1",
        },
        mode="enforce",
    )
    assert result["hookSpecificOutput"]["permissionDecision"] == "allow"


def test_stage_02_field_worker_can_use_web_tools(tmp_path: Path):
    root = _project(tmp_path)
    state = load_state(root / "loop-state.json")
    state["stage"]["id"] = "02"
    state["task_spec"]["attribute_matrix"] = [{
        "concept": "价格",
        "role": "constraint",
        "attribute": "当前市场价",
        "disposition": "research_required",
        "evidence_refs": [],
    }]
    materialize_field_tasks(root, state)
    save_state(root / "loop-state.json", state)
    for tool_name in ("ToolSearch", "WebSearch", "WebFetch"):
        result = handle_pretooluse(
            {"cwd": str(root), "tool_name": tool_name, "tool_input": {}, "agent_id": "field-worker"},
            mode="hybrid",
        )
        assert result["hookSpecificOutput"]["permissionDecision"] == "allow", tool_name


def test_field_worker_cannot_modify_runtime_state_directly(tmp_path: Path):
    root = _project(tmp_path)
    result = handle_pretooluse(
        {
            "cwd": str(root),
            "tool_name": "Write",
            "tool_input": {"file_path": "loop-state.json", "content": "{}"},
            "agent_id": "field-worker-1",
        },
        mode="hybrid",
    )
    assert result["hookSpecificOutput"]["permissionDecision"] == "deny"
    assert "STATE_FILE_PROTECTED_FIELD" in result["hookSpecificOutput"]["permissionDecisionReason"]


def test_field_agent_lifecycle_is_soft_in_hybrid_and_hard_in_enforce(tmp_path: Path):
    root = _project(tmp_path)
    state = load_state(root / "loop-state.json")
    state["stage"]["id"] = "02"
    state["task_spec"]["attribute_matrix"] = [{
        "concept": "价格",
        "role": "constraint",
        "attribute": "当前市场价",
        "disposition": "research_required",
        "evidence_refs": [],
    }]
    save_state(root / "loop-state.json", state)
    task = materialize_field_tasks(root, load_state(root / "loop-state.json"))[0]
    prompt = f"RALPH_FIELD_TASK={task['path']}\n只研究一个字段"
    pre = handle_pretooluse({
        "cwd": str(root),
        "tool_name": "Agent",
        "tool_input": {"prompt": prompt},
        "ralph_role": "commander",
    }, mode="hybrid")
    assert pre["hookSpecificOutput"]["permissionDecision"] == "allow"
    handle_posttooluse({
        "cwd": str(root),
        "tool_name": "Agent",
        "tool_input": {"prompt": prompt},
        "tool_response": [{"type": "text", "text": "Spawned successfully. agent_id: worker-price"}],
    }, mode="hybrid")
    live = load_state(root / "loop-state.json")
    assert live["field_tasks"][0]["status"] == "dispatched"
    stop = handle_stop({"cwd": str(root), "last_assistant_message": "已派发，等待回执"}, mode="hybrid")
    assert "systemMessage" in stop
    assert "字段 Agent" in stop["systemMessage"]
    enforce_stop = handle_stop(
        {"cwd": str(root), "last_assistant_message": "已派发，等待回执"},
        mode="enforce",
    )
    assert enforce_stop["decision"] == "block"


def test_repeated_web_failures_force_field_fallback(tmp_path: Path):
    root = _project(tmp_path)
    state = load_state(root / "loop-state.json")
    state["stage"]["id"] = "02"
    state["task_spec"]["attribute_matrix"] = [{
        "concept": "当前价格",
        "role": "constraint",
        "attribute": "市场价格",
        "disposition": "research_required",
        "evidence_refs": [],
    }]
    save_state(root / "loop-state.json", state)
    task_state = load_state(root / "loop-state.json")
    task = materialize_field_tasks(root, task_state)[0]
    save_state(root / "loop-state.json", task_state)
    task_id = task["id"]
    live = load_state(root / "loop-state.json")
    live["field_tasks"][0]["status"] = "dispatched"
    live["field_tasks"][0]["agent_id"] = "worker-price"
    save_state(root / "loop-state.json", live)

    payload = {
        "cwd": str(root),
        "tool_name": "WebFetch",
        "agent_id": "worker-price",
        "tool_input": {"url": "https://example.invalid"},
        "tool_response": {"code": 403, "codeText": "Forbidden", "result": "Forbidden"},
    }
    first = handle_posttooluse(payload, mode="hybrid")
    assert "可换一个权威来源重试一次" in first["hookSpecificOutput"]["additionalContext"]
    second = handle_posttooluse(payload, mode="hybrid")
    assert "不要继续重复搜索" in second["hookSpecificOutput"]["additionalContext"]
    current = load_state(root / "loop-state.json")
    assert current["field_tasks"][0]["web_failures"] == 2

    denied = handle_pretooluse(
        {
            "cwd": str(root),
            "tool_name": "WebSearch",
            "agent_id": "worker-price",
            "tool_input": {"query": "GPU price"},
        },
        mode="hybrid",
    )
    reason = denied["hookSpecificOutput"]["permissionDecisionReason"]
    assert denied["hookSpecificOutput"]["permissionDecision"] == "deny"
    assert "FIELD_WEB_FAILURE_LOOP" in reason
    assert task_id in current["field_tasks"][0]["id"]


def test_zero_result_search_envelope_counts_as_external_failure(tmp_path: Path):
    root = _project(tmp_path)
    state = load_state(root / "loop-state.json")
    state["stage"]["id"] = "02"
    state["task_spec"]["attribute_matrix"] = [{
        "concept": "显存容量",
        "role": "constraint",
        "attribute": "可加载模型规模",
        "disposition": "research_required",
        "evidence_refs": [],
    }]
    task = materialize_field_tasks(root, state)[0]
    state["field_tasks"][0].update({"status": "dispatched", "agent_id": "worker-vram"})
    save_state(root / "loop-state.json", state)

    payload = {
        "cwd": str(root),
        "tool_name": "WebSearch",
        "agent_id": "worker-vram",
        "tool_input": {"query": "GPU VRAM"},
        "tool_response": {
            "query": "GPU VRAM",
            "results": ["I'll search for information about GPU VRAM."],
            "durationSeconds": 12.0,
            "searchCount": 0,
        },
    }
    result = handle_posttooluse(payload, mode="hybrid")
    assert "外部工具 `WebSearch` 失败" in result["hookSpecificOutput"]["additionalContext"]
    assert load_state(root / "loop-state.json")["field_tasks"][0]["web_failures"] == 1


def test_successful_web_result_resets_consecutive_failure_fuse(tmp_path: Path):
    root = _project(tmp_path)
    state = load_state(root / "loop-state.json")
    state["stage"]["id"] = "02"
    state["task_spec"]["attribute_matrix"] = [{
        "concept": "显存容量",
        "role": "constraint",
        "attribute": "可加载模型规模",
        "disposition": "research_required",
        "evidence_refs": [],
    }]
    task = materialize_field_tasks(root, state)[0]
    state["field_tasks"][0].update({"status": "dispatched", "agent_id": "worker-vram", "web_failures": 1})
    save_state(root / "loop-state.json", state)
    payload = {
        "cwd": str(root),
        "tool_name": "WebSearch",
        "agent_id": "worker-vram",
        "tool_input": {"query": "GPU VRAM"},
        "tool_response": {
            "query": "GPU VRAM",
            "results": [{"title": "A source", "url": "https://example.com/gpu"}],
            "durationSeconds": 1.0,
            "searchCount": 1,
        },
    }
    result = handle_posttooluse(payload, mode="hybrid")
    assert "下一次工具调用必须是 Write 或 Edit" in result["hookSpecificOutput"]["additionalContext"]
    assert load_state(root / "loop-state.json")["field_tasks"][0]["web_failures"] == 0


def test_web_attempt_limit_blocks_hung_tool_retries_without_posttooluse(tmp_path: Path):
    root = _project(tmp_path)
    state = load_state(root / "loop-state.json")
    state["stage"]["id"] = "02"
    state["task_spec"]["attribute_matrix"] = [{
        "concept": "显存容量",
        "role": "constraint",
        "attribute": "可加载模型规模",
        "disposition": "research_required",
        "evidence_refs": [],
    }]
    task = materialize_field_tasks(root, state)[0]
    state["field_tasks"][0].update({"status": "dispatched", "agent_id": "worker-vram"})
    save_state(root / "loop-state.json", state)
    base = {
        "cwd": str(root),
        "tool_name": "WebFetch",
        "agent_id": "worker-vram",
        "tool_input": {"url": "https://example.invalid"},
    }
    for _ in range(3):
        allowed = handle_pretooluse(base, mode="hybrid")
        assert allowed["hookSpecificOutput"]["permissionDecision"] == "allow"
    denied = handle_pretooluse(base, mode="hybrid")
    assert denied["hookSpecificOutput"]["permissionDecision"] == "deny"
    assert "FIELD_WEB_ATTEMPT_LIMIT" in denied["hookSpecificOutput"]["permissionDecisionReason"]


def test_parent_agent_posttooluse_does_not_erase_child_binding_alias(tmp_path: Path):
    root = _project(tmp_path)
    state = load_state(root / "loop-state.json")
    state["stage"]["id"] = "02"
    state["task_spec"]["attribute_matrix"] = [{
        "concept": "显存容量",
        "role": "constraint",
        "attribute": "可加载模型规模",
        "disposition": "research_required",
        "evidence_refs": [],
    }]
    task = materialize_field_tasks(root, state)[0]
    state["field_tasks"][0].update({
        "status": "dispatched",
        "agent_id": "child-vram",
        "agent_ids": ["child-vram"],
    })
    save_state(root / "loop-state.json", state)
    prompt = f"RALPH_FIELD_TASK={task['path']}"
    handle_posttooluse({
        "cwd": str(root),
        "tool_name": "Agent",
        "agent_id": "field-vram@session-parent",
        "tool_input": {"prompt": prompt},
        "tool_response": {"agent_id": "field-vram@session-parent", "status": "teammate_spawned"},
    }, mode="hybrid")
    live = load_state(root / "loop-state.json")["field_tasks"][0]
    assert "child-vram" in live["agent_ids"]
    assert "field-vram@session-parent" in live["agent_ids"]


def test_parallel_materialization_uses_unique_atomic_temp_files(tmp_path: Path):
    root = _project(tmp_path)
    state = load_state(root / "loop-state.json")
    state["stage"]["id"] = "02"
    state["task_spec"]["attribute_matrix"] = [
        {"concept": "显存", "role": "constraint", "attribute": "容量", "disposition": "research_required", "evidence_refs": []},
        {"concept": "带宽", "role": "objective", "attribute": "吞吐", "disposition": "research_required", "evidence_refs": []},
    ]
    save_state(root / "loop-state.json", state)

    def materialize_once():
        local = load_state(root / "loop-state.json")
        return materialize_field_tasks(root, local)

    with ThreadPoolExecutor(max_workers=4) as pool:
        results = list(pool.map(lambda _: materialize_once(), range(4)))
    assert all(len(result) == 2 for result in results)
    assert not list((root / "loop-artifacts").rglob("*.tmp"))


def test_parallel_subagent_start_binds_two_distinct_field_tasks(tmp_path: Path):
    root = _project(tmp_path)
    state = load_state(root / "loop-state.json")
    state["stage"]["id"] = "02"
    state["task_spec"]["attribute_matrix"] = [
        {"concept": "显存", "role": "constraint", "attribute": "容量", "disposition": "research_required", "evidence_refs": []},
        {"concept": "带宽", "role": "objective", "attribute": "吞吐", "disposition": "research_required", "evidence_refs": []},
    ]
    materialize_field_tasks(root, state)
    save_state(root / "loop-state.json", state)
    state = load_state(root / "loop-state.json")
    tasks = state["field_tasks"]
    prompts = [f"RALPH_FIELD_TASK={task['path']}\n只处理 {task['concept']}" for task in tasks]
    for prompt in prompts:
        result = handle_pretooluse(
            {"cwd": str(root), "tool_name": "Agent", "tool_input": {"prompt": prompt}, "ralph_role": "commander"},
            mode="hybrid",
        )
        assert result["hookSpecificOutput"]["permissionDecision"] == "allow"
    first = handle_subagentstart({"cwd": str(root), "agent_id": "child-1"}, mode="hybrid")
    second = handle_subagentstart({"cwd": str(root), "agent_id": "child-2"}, mode="hybrid")
    assert "显存" in first["hookSpecificOutput"]["additionalContext"]
    assert "带宽" in second["hookSpecificOutput"]["additionalContext"]
    live = load_state(root / "loop-state.json")
    assert {task.get("agent_id") for task in live["field_tasks"]} == {"child-1", "child-2"}


def test_concurrent_subagent_start_binds_distinct_tasks_under_lock(tmp_path: Path):
    root = _project(tmp_path)
    state = load_state(root / "loop-state.json")
    state["stage"]["id"] = "02"
    state["task_spec"]["attribute_matrix"] = [
        {"concept": "显存", "role": "constraint", "attribute": "容量", "disposition": "research_required", "evidence_refs": []},
        {"concept": "带宽", "role": "objective", "attribute": "吞吐", "disposition": "research_required", "evidence_refs": []},
    ]
    materialize_field_tasks(root, state)
    save_state(root / "loop-state.json", state)
    tasks = load_state(root / "loop-state.json")["field_tasks"]
    for task in tasks:
        handle_pretooluse(
            {
                "cwd": str(root),
                "tool_name": "Agent",
                "tool_input": {"prompt": f"RALPH_FIELD_TASK={task['path']}"},
                "ralph_role": "commander",
            },
            mode="hybrid",
        )
    with ThreadPoolExecutor(max_workers=2) as pool:
        results = list(pool.map(
            lambda agent: handle_subagentstart({"cwd": str(root), "agent_id": agent}, mode="hybrid"),
            ("child-a", "child-b"),
        ))
    assert all("字段 Agent 已绑定任务" in result["hookSpecificOutput"]["additionalContext"] for result in results)
    live = load_state(root / "loop-state.json")
    assert {task.get("agent_id") for task in live["field_tasks"]} == {"child-a", "child-b"}


def test_worker_task_path_repairs_swapped_parallel_identity(tmp_path: Path):
    root = _project(tmp_path)
    state = load_state(root / "loop-state.json")
    state["stage"]["id"] = "02"
    state["task_spec"]["attribute_matrix"] = [
        {"concept": "显存", "role": "constraint", "attribute": "容量", "disposition": "research_required", "evidence_refs": []},
        {"concept": "带宽", "role": "objective", "attribute": "吞吐", "disposition": "research_required", "evidence_refs": []},
    ]
    materialize_field_tasks(root, state)
    state["field_tasks"][0].update({"status": "dispatched", "agent_id": "child-token", "agent_ids": ["child-token"]})
    state["field_tasks"][1].update({"status": "dispatched", "agent_id": "child-vram", "agent_ids": ["child-vram"]})
    save_state(root / "loop-state.json", state)
    token_path = state["field_tasks"][1]["path"]
    _, rebound = rebind_field_task_to_path(root, "child-token", token_path)
    assert rebound["concept"] == "带宽"
    live = load_state(root / "loop-state.json")
    assert live["field_tasks"][1]["agent_id"] == "child-token"
    assert "child-token" not in (live["field_tasks"][0].get("agent_ids") or [])


def test_parallel_subagent_start_prefers_agent_name_over_start_order(tmp_path: Path):
    root = _project(tmp_path)
    state = load_state(root / "loop-state.json")
    state["stage"]["id"] = "02"
    state["task_spec"]["attribute_matrix"] = [
        {"concept": "显存", "role": "constraint", "attribute": "容量", "disposition": "research_required", "evidence_refs": []},
        {"concept": "带宽", "role": "objective", "attribute": "吞吐", "disposition": "research_required", "evidence_refs": []},
    ]
    materialize_field_tasks(root, state)
    save_state(root / "loop-state.json", state)
    tasks = load_state(root / "loop-state.json")["field_tasks"]
    for task, name in zip(tasks, ("field-vram", "field-bandwidth")):
        result = handle_pretooluse(
            {
                "cwd": str(root),
                "tool_name": "Agent",
                "tool_input": {"name": name, "prompt": f"RALPH_FIELD_TASK={task['path']}"},
                "ralph_role": "commander",
            },
            mode="hybrid",
        )
        assert result["hookSpecificOutput"]["permissionDecision"] == "allow"
    # Starts arrive in the opposite order; identity must still select the
    # correct reserved field.
    first = handle_subagentstart({"cwd": str(root), "agent_id": "child-bandwidth", "agent_type": "field-bandwidth"}, mode="hybrid")
    second = handle_subagentstart({"cwd": str(root), "agent_id": "child-vram", "agent_type": "field-vram"}, mode="hybrid")
    assert "带宽" in first["hookSpecificOutput"]["additionalContext"]
    assert "显存" in second["hookSpecificOutput"]["additionalContext"]


def test_wrong_js_task_path_gets_json_correction(tmp_path: Path):
    root = _project(tmp_path)
    state = load_state(root / "loop-state.json")
    state["stage"]["id"] = "02"
    state["task_spec"]["attribute_matrix"] = [{
        "concept": "价格",
        "role": "constraint",
        "attribute": "当前市场价",
        "disposition": "research_required",
        "evidence_refs": [],
    }]
    save_state(root / "loop-state.json", state)
    task = materialize_field_tasks(root, load_state(root / "loop-state.json"))[0]
    result = handle_pretooluse({
        "cwd": str(root),
        "tool_name": "Read",
        "tool_input": {"file_path": task["path"].replace(".json", ".js")},
        "ralph_role": "commander",
    }, mode="hybrid")
    reason = result["hookSpecificOutput"]["permissionDecisionReason"]
    assert result["hookSpecificOutput"]["permissionDecision"] == "deny"
    assert "FIELD_TASK_PATH_CORRECTION" in reason or "正确路径" in reason


def test_commander_cannot_read_current_field_task(tmp_path: Path):
    root = _project(tmp_path)
    state = load_state(root / "loop-state.json")
    state["stage"]["id"] = "02"
    state["task_spec"]["attribute_matrix"] = [{
        "concept": "价格",
        "role": "constraint",
        "attribute": "当前市场价",
        "disposition": "research_required",
        "evidence_refs": [],
    }]
    save_state(root / "loop-state.json", state)
    task = materialize_field_tasks(root, load_state(root / "loop-state.json"))[0]
    result = handle_pretooluse({
        "cwd": str(root),
        "tool_name": "Read",
        "tool_input": {"file_path": task["path"]},
        "ralph_role": "commander",
    }, mode="hybrid")
    output = result["hookSpecificOutput"]
    assert output["permissionDecision"] == "deny"
    assert "FIELD_TASK_PATH_CORRECTION" in output["permissionDecisionReason"]
    assert "Agent" in output["permissionDecisionReason"]


def test_commander_read_of_pending_field_task_recovers_to_stage_draft(tmp_path: Path):
    root = _project(tmp_path)
    state = load_state(root / "loop-state.json")
    state["stage"]["id"] = "01"
    state["task_spec"]["attribute_matrix"] = [{
        "concept": "目标",
        "role": "goal",
        "attribute": "完成离线比较工作流",
        "disposition": "pending",
        "evidence_refs": [],
    }]
    save_state(root / "loop-state.json", state)
    task = materialize_field_tasks(root, load_state(root / "loop-state.json"))[0]

    result = handle_pretooluse({
        "cwd": str(root),
        "tool_name": "Read",
        "tool_input": {"file_path": task["path"]},
        "ralph_role": "commander",
    }, mode="hybrid")

    output = result["hookSpecificOutput"]
    assert output["permissionDecision"] == "deny"
    assert "FIELD_TASK_PATH_CORRECTION" in output["permissionDecisionReason"]
    assert "fields.json" in output["permissionDecisionReason"]
    assert "Agent" not in output["permissionDecisionReason"]


def test_commander_can_read_current_stage_fields_draft(tmp_path: Path):
    root = _project(tmp_path)
    state = load_state(root / "loop-state.json")
    state["stage"]["id"] = "02.5"
    save_state(root / "loop-state.json", state)
    fields_file = init_fields(root)["fields_file"]

    result = handle_pretooluse({
        "cwd": str(root),
        "tool_name": "Read",
        "tool_input": {"file_path": fields_file},
        "ralph_role": "commander",
    }, mode="hybrid")

    output = result["hookSpecificOutput"]
    assert output["permissionDecision"] == "allow"
    assert "FIELD_TASK_PATH_CORRECTION" not in output["permissionDecisionReason"]


def test_task_graph_field_is_validated_and_materialized_incrementally(tmp_path: Path):
    root = _project(tmp_path)
    draft = Path(init_fields(root)["fields_file"])
    graph = {
        "nodes": [
            {
                "id": "T1.1",
                "depends_on": [],
                "execution_mode": "parallel",
                "parallel_group_id": "G1",
                "orthogonal_key": "vram",
                "output_schema": {"facts": "array"},
                "writes": ["artifacts/vram.md"],
            },
            {
                "id": "T1.2",
                "depends_on": [],
                "execution_mode": "parallel",
                "parallel_group_id": "G1",
                "orthogonal_key": "throughput",
                "output_schema": {"facts": "array"},
                "writes": ["artifacts/throughput.md"],
            },
            {
                "id": "J1",
                "depends_on": ["T1.1", "T1.2"],
                "input_refs": ["artifacts/vram.md", "artifacts/throughput.md"],
                "output_schema": {"recommendation": "string"},
                "writes": ["artifacts/join.md"],
            },
        ],
        "joins": [{"id": "J1", "depends_on": ["T1.1", "T1.2"]}],
    }
    draft.write_text(
        json.dumps({"fields": [{
            "concept": "task_graph",
            "role": "task_graph",
            "task_graph": graph,
            "disposition": "confirmed",
        }]}, ensure_ascii=False),
        encoding="utf-8",
    )
    result = apply_fields(root, draft)
    assert result["ok"] is True
    state = load_state(root / "loop-state.json")
    assert [task["node_id"] for task in state["graph_tasks"]] == ["T1.1", "T1.2", "J1"]
    assert {task["status"] for task in state["graph_tasks"]} == {"ready", "blocked"}
    assert all(Path(root / task["path"]).exists() for task in state["graph_tasks"])


def test_graph_apply_completes_parallel_nodes_then_opens_join(tmp_path: Path):
    root = _project(tmp_path)
    draft = Path(init_fields(root)["fields_file"])
    graph = {
        "nodes": [
            {
                "id": "T1.1", "depends_on": [], "execution_mode": "parallel",
                "parallel_group_id": "G1", "orthogonal_key": "vram",
                "output_schema": {"facts": "array"}, "writes": ["artifacts/vram.md"],
            },
            {
                "id": "T1.2", "depends_on": [], "execution_mode": "parallel",
                "parallel_group_id": "G1", "orthogonal_key": "throughput",
                "output_schema": {"facts": "array"}, "writes": ["artifacts/throughput.md"],
            },
            {
                "id": "J1", "depends_on": ["T1.1", "T1.2"],
                "input_refs": ["artifacts/vram.md", "artifacts/throughput.md"],
                "output_schema": {"recommendation": "string"}, "writes": ["artifacts/join.md"],
            },
        ],
        "joins": [{"id": "J1", "depends_on": ["T1.1", "T1.2"]}],
    }
    draft.write_text(json.dumps({"fields": [{
        "concept": "task_graph", "role": "task_graph",
        "task_graph": graph, "disposition": "confirmed",
    }]}, ensure_ascii=False), encoding="utf-8")
    apply_fields(root, draft)

    state = load_state(root / "loop-state.json")
    first_batch = [task for task in state["graph_tasks"] if task["status"] == "ready"]
    assert {task["node_id"] for task in first_batch} == {"T1.1", "T1.2"}
    for task in first_batch:
        path = root / task["path"]
        payload = json.loads(path.read_text(encoding="utf-8"))
        node = next(node for node in graph["nodes"] if node["id"] == task["node_id"])
        for relative in node["writes"]:
            output_path = root / relative
            output_path.parent.mkdir(parents=True, exist_ok=True)
            output_path.write_text(f"result for {task['node_id']}", encoding="utf-8")
        payload.update({"output": {"node": task["node_id"]}, "evidence": [f"{task['node_id']}.json"]})
        path.write_text(json.dumps(payload, ensure_ascii=False), encoding="utf-8")
        assert apply_graph_task(root, path)["status"] == "completed"

    state = load_state(root / "loop-state.json")
    join = next(task for task in state["graph_tasks"] if task["node_id"] == "J1")
    assert join["status"] == "ready"
    join_path = root / join["path"]
    (root / "artifacts/join.md").write_text("joined recommendation", encoding="utf-8")
    join_payload = json.loads(join_path.read_text(encoding="utf-8"))
    join_payload.update({"output": {"recommendation": "join"}, "evidence": ["join.json"]})
    join_path.write_text(json.dumps(join_payload, ensure_ascii=False), encoding="utf-8")
    apply_graph_task(root, join_path)
    final = load_state(root / "loop-state.json")
    assert set(final["plan"]["completed"]) == {"T1.1", "T1.2", "J1"}


def test_field_chain_research_cross_validation_and_execution_dag(tmp_path: Path, monkeypatch):
    # The integration fixture exercises the no-provider path; real authorized
    # projects have separate receipt tests and must use web-llm-check.
    monkeypatch.setattr("ralph_runtime.cli.web_llm_crosscheck_enabled", lambda project: False)
    root = _project(tmp_path)
    state = load_state(root / "loop-state.json")
    state["stage"] = {**state["stage"], "id": "02", "revision": "r1"}
    state["task_spec"] = {"attribute_matrix": [
        {
            "concept": "显存容量", "role": "constraint", "attribute": "最大模型规模",
            "disposition": "research_required", "evidence_refs": [],
        },
        {
            "concept": "research_findings", "role": "research_findings", "attribute": "字段调研汇总",
            "disposition": "pending", "evidence_refs": [],
        },
    ]}
    save_state(root / "loop-state.json", state)

    draft = Path(init_fields(root)["fields_file"])
    draft.write_text(json.dumps({"fields": [
        {
            "concept": "显存容量", "role": "constraint", "attribute": "最大模型规模",
            "disposition": "confirmed", "evidence_refs": ["https://spec.example.com/gpu/vram"],
        },
        {
            "concept": "research_findings", "role": "research_findings", "attribute": "字段调研汇总",
            "disposition": "confirmed", "evidence_refs": ["https://research.example.com/vram-report"],
        },
    ]}, ensure_ascii=False), encoding="utf-8")
    assert apply_fields(root, draft)["remaining"]["complete"] is True
    apply_and_record(
        root / "loop-state.json", root / "loop-events.md",
        {"action": "advance", "status": "passed", "stage_id": "02", "revision": "r1", "next_stage": "02.5", "payload": {}},
    )

    draft = Path(init_fields(root)["fields_file"])
    draft.write_text(json.dumps({"fields": [{
        "concept": "cross_validation", "role": "cross_validation", "attribute": "交叉验证摘要",
        "disposition": "confirmed", "evidence_refs": ["https://review-a.example.com/vram", "https://review-b.example.com/vram"],
        "validation_records": [
            {"claim_ref": "显存容量", "source_refs": ["https://review-a.example.com/vram", "https://review-b.example.com/vram"], "observed_at": "2026-07-29T00:00:00+08:00", "verdict": "supported"},
            {"claim_ref": "research_findings", "source_refs": ["https://research.example.com/vram-report", "https://review-b.example.com/vram"], "observed_at": "2026-07-29T00:00:00+08:00", "verdict": "supported"},
        ],
    }]}, ensure_ascii=False), encoding="utf-8")
    assert apply_fields(root, draft)["remaining"]["complete"] is True
    apply_and_record(
        root / "loop-state.json", root / "loop-events.md",
        {"action": "advance", "status": "passed", "stage_id": "02.5", "revision": "r1", "next_stage": "03", "payload": {}},
    )

    graph = {
        "nodes": [
            {"id": "T1.1", "depends_on": [], "execution_mode": "parallel", "parallel_group_id": "G1", "orthogonal_key": "price", "output_schema": {"facts": "array"}, "writes": ["price.json"]},
            {"id": "T1.2", "depends_on": [], "execution_mode": "parallel", "parallel_group_id": "G1", "orthogonal_key": "compatibility", "output_schema": {"facts": "array"}, "writes": ["compatibility.json"]},
            {"id": "J1", "depends_on": ["T1.1", "T1.2"], "input_refs": ["price.json", "compatibility.json"], "output_schema": {"recommendation": "string"}, "writes": ["join.json"]},
        ],
        "joins": [{"id": "J1", "depends_on": ["T1.1", "T1.2"]}],
    }
    draft = Path(init_fields(root)["fields_file"])
    draft.write_text(json.dumps({"fields": [
        {"concept": "task_graph", "role": "task_graph", "attribute": "执行 DAG", "task_graph": graph, "disposition": "confirmed"},
        {"concept": "coverage_proof", "role": "coverage_proof", "attribute": "目标和约束覆盖证明", "disposition": "confirmed"},
    ]}, ensure_ascii=False), encoding="utf-8")
    assert apply_fields(root, draft)["remaining"]["complete"] is True
    state = load_state(root / "loop-state.json")
    assert {task["node_id"] for task in state["graph_tasks"] if task["status"] == "ready"} == {"T1.1", "T1.2"}
    for task in list(state["graph_tasks"]):
        if task["status"] != "ready":
            continue
        path = root / task["path"]
        payload = json.loads(path.read_text(encoding="utf-8"))
        node = next(node for node in graph["nodes"] if node["id"] == task["node_id"])
        for relative in node["writes"]:
            output_path = root / relative
            output_path.parent.mkdir(parents=True, exist_ok=True)
            output_path.write_text(f"result for {task['node_id']}", encoding="utf-8")
        payload.update({"output": {"node": task["node_id"]}, "evidence": [task["node_id"] + ".json"]})
        path.write_text(json.dumps(payload, ensure_ascii=False), encoding="utf-8")
        apply_graph_task(root, path)
    join = next(task for task in load_state(root / "loop-state.json")["graph_tasks"] if task["node_id"] == "J1")
    assert join["status"] == "ready"
    join_path = root / join["path"]
    (root / "join.json").write_text("joined recommendation", encoding="utf-8")
    payload = json.loads(join_path.read_text(encoding="utf-8"))
    payload.update({"output": {"recommendation": "ok"}, "evidence": ["join.json"]})
    join_path.write_text(json.dumps(payload, ensure_ascii=False), encoding="utf-8")
    apply_graph_task(root, join_path)
    final = apply_and_record(
        root / "loop-state.json", root / "loop-events.md",
        {"action": "advance", "status": "passed", "stage_id": "03", "revision": "r1", "next_stage": "04", "payload": {}},
    )
    assert final["stage"]["id"] == "04"


def test_exploration_tail_is_not_blocked_by_empty_attribute_matrix(tmp_path: Path):
    state = create_state("exploration-project", task="继续寻找可验证任务")
    state = state.copy()
    node = state["stage"]
    state["stage"] = {**node, "id": "exploration", "revision": "r1"}
    action = parse_action({
        "action": "advance", "status": "passed", "stage_id": "exploration",
        "revision": "r1", "next_stage": "01", "payload": {
            "exploration": {
                "preference_brief": "优先任务板中的 P1，候选只入队不静默执行",
                "scanned_sources": ["tasks/TASKS.md"],
                "selection_mode": "task_board",
                "selected_task": {
                    "task_id": "T1", "title": "可验证的小任务", "source": "task_board",
                    "source_path": "tasks/TASKS.md", "priority": "P1", "reason": "依赖已满足",
                },
                "candidate_tasks": [],
            }
        },
    })
    validate_action(action, state)


def test_stage03_field_gate_rejects_prose_graph_and_unexecuted_plan(tmp_path: Path):
    root = _project(tmp_path)
    state = load_state(root / "loop-state.json")
    state["stage"] = {**state["stage"], "id": "03", "required_outputs": ["task_graph", "coverage_proof"]}
    state["task_spec"] = {"attribute_matrix": [
        {
            "concept": "task_graph", "role": "decomposition", "attribute": "NODE-1 then NODE-2",
            "disposition": "confirmed", "evidence_refs": [],
        },
        {
            "concept": "coverage_proof", "role": "coverage", "attribute": "all covered",
            "disposition": "confirmed", "evidence_refs": [],
        },
    ]}
    action = parse_action({
        "action": "advance", "status": "passed", "stage_id": "03", "revision": "r1", "next_stage": "04", "payload": {},
    })
    with pytest.raises(ProtocolError, match="结构化 task_graph"):
        validate_action(action, state)


def test_stage02_field_gate_rejects_generic_domain_for_current_market_fact(tmp_path: Path):
    root = _project(tmp_path)
    state = load_state(root / "loop-state.json")
    state["stage"] = {**state["stage"], "id": "02", "required_outputs": ["research_findings"]}
    state["task_spec"] = {"attribute_matrix": [
        {
            "concept": "research_findings", "role": "research_findings", "attribute": "current GPU market price",
            "disposition": "confirmed", "evidence_refs": ["https://www.jd.com"],
        },
    ]}
    action = parse_action({
        "action": "advance", "status": "passed", "stage_id": "02", "revision": "r1", "next_stage": "02.5", "payload": {},
    })
    with pytest.raises(ProtocolError, match="具体 HTTPS 来源"):
        validate_action(action, state)


def test_field_apply_rejects_asserted_market_fact_with_site_homepage(tmp_path: Path):
    root = _project(tmp_path)
    state = load_state(root / "loop-state.json")
    state["stage"] = {**state["stage"], "id": "02", "required_outputs": ["research_findings"]}
    save_state(root / "loop-state.json", state)
    draft = Path(init_fields(root)["fields_file"])
    draft.write_text(json.dumps({"fields": [{
        "concept": "research_findings", "role": "research_findings", "attribute": "current GPU market price",
        "disposition": "confirmed", "evidence_refs": ["https://www.jd.com"],
    }]}), encoding="utf-8")
    with pytest.raises(ValueError, match="具体 HTTPS 来源"):
        apply_fields(root, draft)


def test_cross_validation_requires_claim_level_records(tmp_path: Path):
    root = _project(tmp_path)
    state = load_state(root / "loop-state.json")
    state["stage"] = {**state["stage"], "id": "02.5", "required_outputs": ["cross_validation"]}
    state["task_spec"] = {"attribute_matrix": [
        {
            "concept": "GPU price", "role": "research_findings", "attribute": "price evidence",
            "disposition": "confirmed", "evidence_refs": ["https://shop.example.com/item/1"],
        },
        {
            "concept": "cross_validation", "role": "validation", "attribute": "summary",
            "disposition": "confirmed", "evidence_refs": ["https://source-a.example.com/a", "https://source-b.example.com/b"],
        },
    ]}
    action = parse_action({
        "action": "advance", "status": "passed", "stage_id": "02.5", "revision": "r1", "next_stage": "03", "payload": {},
    })
    with pytest.raises(ProtocolError, match="validation_records"):
        validate_action(action, state)


def test_field_apply_rejects_task_graph_written_as_prose(tmp_path: Path):
    root = _project(tmp_path)
    state = load_state(root / "loop-state.json")
    state["stage"] = {**state["stage"], "id": "03", "required_outputs": ["task_graph", "coverage_proof"]}
    save_state(root / "loop-state.json", state)
    draft = Path(init_fields(root)["fields_file"])
    draft.write_text(json.dumps({"fields": [{
        "concept": "task_graph", "role": "decomposition", "attribute": "a prose task list",
        "disposition": "confirmed", "evidence_refs": [],
    }]}), encoding="utf-8")
    with pytest.raises(ValueError, match="role 必须精确为 task_graph"):
        apply_fields(root, draft)


def test_invalid_task_graph_does_not_mutate_state(tmp_path: Path):
    root = _project(tmp_path)
    draft = Path(init_fields(root)["fields_file"])
    before = load_state(root / "loop-state.json")
    draft.write_text(json.dumps({"fields": [{
        "concept": "task_graph",
        "role": "task_graph",
        "task_graph": {"nodes": [{"id": "A", "depends_on": ["missing"]}]},
        "disposition": "confirmed",
    }]}), encoding="utf-8")
    with pytest.raises(ValueError, match="task_graph 校验失败"):
        apply_fields(root, draft)
    assert load_state(root / "loop-state.json") == before
