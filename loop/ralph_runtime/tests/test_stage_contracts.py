import json

import pytest

from conftest import complete_required_card, gate_card_of, stage_one_payload, stage_review
from ralph_runtime.contracts import agent_prompt_for_card, ensure_stage_cards, materialize_contract_documents, factor_groups
from ralph_runtime.hooks import (
    handle_posttooluse,
    handle_pretooluse,
    handle_subagentstart,
    handle_subagentstop,
    handle_userpromptsubmit,
)
from ralph_runtime.nodes import DEFAULT_GRAPH
from ralph_runtime.prompt_renderer import PromptRenderer
from ralph_runtime.protocol import ProtocolError, parse_action, validate_action
from ralph_runtime.state import apply_action, create_state, load_state, save_state, update_subagent_card


def _plan_payload():
    return {
        "stage_review": stage_review("02", "02-r1-dag-auditor"),
        "plan": {
            "revision": "r1",
            "decomposition_rationale": ["按价格与技术适配两个正交维度分解"],
            "coverage_proof": ["覆盖成本、硬件适配和验证"],
            "risk_notes": ["价格需要按地区和日期核验"],
            "nodes": [
                {
                    "id": "T1.1",
                    "title": "价格证据研究",
                    "objective": "收集有日期和地区的价格证据",
                    "evidence_plan": ["零售商和成交记录"],
                    "acceptance_criteria": ["每项价格有来源和日期"],
                    "execution_mode": "parallel",
                    "parallel_group_id": "G1",
                    "orthogonal_key": "price",
                    "input_refs": [],
                    "output_schema": {"type": "object"},
                    "preconditions": [],
                    "postconditions": ["价格账本"],
                    "writes": ["evidence/price.json"],
                },
                {
                    "id": "T1.2",
                    "title": "工作负载适配研究",
                    "objective": "核验模型和推理工作负载的显存需求",
                    "evidence_plan": ["官方模型卡和复现计算"],
                    "acceptance_criteria": ["每个需求有版本与方法"],
                    "execution_mode": "parallel",
                    "parallel_group_id": "G1",
                    "orthogonal_key": "workload",
                    "input_refs": [],
                    "output_schema": {"type": "object"},
                    "preconditions": [],
                    "postconditions": ["工作负载账本"],
                    "writes": ["evidence/workload.json"],
                },
                {
                    "id": "J1",
                    "title": "候选方案汇总",
                    "objective": "汇总价格与工作负载证据，形成待核验方案",
                    "evidence_plan": ["两个上游任务输出"],
                    "acceptance_criteria": ["输入完整且不混淆结论"],
                    "depends_on": ["T1.1", "T1.2"],
                    "execution_mode": "serial",
                    "input_refs": ["T1.1.output", "T1.2.output"],
                    "output_schema": {"type": "object"},
                    "preconditions": ["上游完成"],
                    "postconditions": ["候选事实账本"],
                    "writes": ["evidence/join.json"],
                },
            ],
            "parallel_groups": [{"id": "G1", "join": "J1"}],
            "joins": [{"id": "J1", "depends_on": ["T1.1", "T1.2"]}],
        }
    }


def test_prompt_requires_semantic_decomposition_and_task_card():
    rendered = PromptRenderer().render(create_state("fixture", task="调研性价比 GPU"))
    text = rendered.text
    # Commander prompt must stay compact: it references decomposition files
    # instead of inlining the full contract / submission JSON.
    assert "当前阶段第一动作闸门" in text
    assert "RALPH_TASK_CARD=loop-artifacts/task-cards/01-r1-builder-task_spec-context.md" in text
    assert "RALPH_TASK_CARD=loop-artifacts/task-cards/01-r1-requirements-auditor.md" in text
    assert "loop-artifacts/contracts/01-r1-stage-contract.md" in text
    assert "01-r1-submission-template.json" in text
    assert "payload.stage_review" in text
    assert "ralph assemble" in text
    assert "ralph validate --result" in text
    assert "Commander 不得用 Agent、Write 或 Edit 创建、补写、修复" in text
    assert "不得直接 Read 完整 `loop-events.md`" in text
    # Methodology (七类语义角色 / 需求分流闸门 / 30-35B) lives in the
    # materialized contract file, not inlined into the Commander prompt.
    assert "决策语义而非字面词语拆解" not in text
    assert "30-35B" not in text


def test_gate_card_receives_bounded_package_and_submission_template(tmp_path):
    state = create_state("fixture", task="调研性价比 GPU")
    materialize_contract_documents(tmp_path, state)
    card = gate_card_of(state)
    assert card["context_mode"] == "bounded_artifacts"
    assert "loop-state.json" not in card["document_refs"]
    assert "loop-artifacts/contracts/01-r1-stage-input-package.json" in card["document_refs"]
    assert "loop-artifacts/contracts/01-r1-submission-template.json" in card["document_refs"]
    gate_card_text = (tmp_path / card["card_ref"]).read_text(encoding="utf-8")
    assert "<RALPH_GATE_REVIEW>" in gate_card_text
    package = json.loads(
        (tmp_path / "loop-artifacts/contracts/01-r1-stage-input-package.json").read_text(encoding="utf-8")
    )
    assert package["context_mode"] == "bounded_artifacts"
    assert "Commander 主对话" in package["purpose"]


def test_enforce_rejects_bare_agent_and_tracks_card_completion(tmp_path):
    state = create_state("fixture")
    save_state(tmp_path / "loop-state.json", state)
    materialize_contract_documents(tmp_path, state)

    bare = handle_pretooluse(
        {"cwd": str(tmp_path), "tool_name": "Agent", "tool_input": {"prompt": "请调研"}},
        mode="enforce",
    )
    assert bare["hookSpecificOutput"]["permissionDecision"] == "deny"

    card = gate_card_of(state)
    prompt = agent_prompt_for_card(card)
    approved = handle_pretooluse(
        {"cwd": str(tmp_path), "tool_name": "Agent", "tool_input": {"prompt": prompt}},
        mode="enforce",
    )
    assert approved["hookSpecificOutput"]["permissionDecision"] == "allow"
    assert load_state(tmp_path / "loop-state.json")["subagent_cards"][card["id"]]["status"] == "dispatched"

    duplicate = handle_pretooluse(
        {"cwd": str(tmp_path), "tool_name": "Agent", "tool_input": {"prompt": prompt}},
        mode="enforce",
    )
    assert duplicate["hookSpecificOutput"]["permissionDecision"] == "deny"
    duplicate_reason = duplicate["hookSpecificOutput"]["permissionDecisionReason"]
    assert "不要再次调用 Agent" in duplicate_reason
    assert "blocked_human" in duplicate_reason

    handle_posttooluse(
        {
            "cwd": str(tmp_path),
            "tool_name": "Agent",
            "tool_input": {"prompt": prompt},
            "tool_response": {"success": True},
        },
        mode="enforce",
    )
    assert load_state(tmp_path / "loop-state.json")["subagent_cards"][card["id"]]["status"] == "dispatched"
    handle_subagentstop(
        {
            "cwd": str(tmp_path),
            "agent_id": "agent-foreground",
            "stop_reason": "end_turn",
            "last_assistant_message": "<RALPH_GATE_REVIEW>\n" + json.dumps(stage_review("01", card["id"]), ensure_ascii=False),
        },
        mode="enforce",
    )
    assert load_state(tmp_path / "loop-state.json")["subagent_cards"][card["id"]]["status"] == "completed"


def test_async_card_waits_for_subagent_stop(tmp_path):
    state = create_state("fixture")
    save_state(tmp_path / "loop-state.json", state)
    card = gate_card_of(state)
    prompt = agent_prompt_for_card(card)
    handle_pretooluse({"cwd": str(tmp_path), "tool_name": "Agent", "tool_input": {"prompt": prompt}}, mode="enforce")
    handle_posttooluse(
        {
            "cwd": str(tmp_path),
            "tool_name": "Agent",
            "tool_input": {"prompt": prompt},
            "tool_response": {"status": "async_launched", "isAsync": True, "agentId": "agent-1"},
        },
        mode="enforce",
    )
    assert load_state(tmp_path / "loop-state.json")["subagent_cards"][card["id"]]["status"] == "dispatched"
    handle_subagentstop(
        {
            "cwd": str(tmp_path),
            "agent_id": "agent-1",
            "stop_reason": "end_turn",
            "last_assistant_message": "<RALPH_GATE_REVIEW>\n" + json.dumps(stage_review("01", card["id"]), ensure_ascii=False),
        },
        mode="enforce",
    )
    assert load_state(tmp_path / "loop-state.json")["subagent_cards"][card["id"]]["status"] == "completed"


def test_subagentstart_binds_card_and_enforces_bounded_worker_tools(tmp_path):
    state = create_state("fixture")
    save_state(tmp_path / "loop-state.json", state)
    materialize_contract_documents(tmp_path, state)
    card = gate_card_of(state)
    prompt = agent_prompt_for_card(card)
    handle_pretooluse({"cwd": str(tmp_path), "tool_name": "Agent", "tool_input": {"prompt": prompt}}, mode="enforce")

    started = handle_subagentstart(
        {"cwd": str(tmp_path), "agent_id": "agent-bound", "agent_type": "general-purpose"},
        mode="enforce",
    )
    assert "01-r1-requirements-auditor" in started["hookSpecificOutput"]["additionalContext"]
    bound = load_state(tmp_path / "loop-state.json")["subagent_cards"][card["id"]]
    assert bound["agent_id"] == "agent-bound"

    allowed = handle_pretooluse(
        {
            "cwd": str(tmp_path),
            "agent_id": "agent-bound",
            "tool_name": "Read",
            "tool_input": {"file_path": str(tmp_path / card["card_ref"])},
        },
        mode="enforce",
    )
    assert allowed["hookSpecificOutput"]["permissionDecision"] == "allow"

    outside = handle_pretooluse(
        {
            "cwd": str(tmp_path),
            "agent_id": "agent-bound",
            "tool_name": "Read",
            "tool_input": {"file_path": str(tmp_path / "loop-state.json")},
        },
        mode="enforce",
    )
    assert outside["hookSpecificOutput"]["permissionDecision"] == "deny"

    forbidden = handle_pretooluse(
        {
            "cwd": str(tmp_path),
            "agent_id": "agent-bound",
            "tool_name": "Bash",
            "tool_input": {"command": "pwd"},
        },
        mode="enforce",
    )
    assert forbidden["hookSpecificOutput"]["permissionDecision"] == "deny"


def test_gate_card_requires_tagged_receipt_before_completion(tmp_path):
    state = create_state("fixture")
    save_state(tmp_path / "loop-state.json", state)
    card = gate_card_of(state)
    prompt = agent_prompt_for_card(card)
    handle_pretooluse({"cwd": str(tmp_path), "tool_name": "Agent", "tool_input": {"prompt": prompt}}, mode="enforce")
    handle_subagentstart({"cwd": str(tmp_path), "agent_id": "agent-gate"}, mode="enforce")

    rejected = handle_subagentstop(
        {"cwd": str(tmp_path), "agent_id": "agent-gate", "stop_reason": "end_turn", "last_assistant_message": "审计完成"},
        mode="enforce",
    )
    assert rejected["decision"] == "block"
    assert "RALPH_FEEDBACK[GATE_RECEIPT_INVALID]" in rejected["reason"]
    assert "<RALPH_GATE_REVIEW>" in rejected["reason"]
    assert card["id"] in rejected["reason"]
    assert load_state(tmp_path / "loop-state.json")["subagent_cards"][card["id"]]["status"] == "dispatched"


def test_stage_one_advance_requires_audit_and_structured_task_spec():
    state = create_state("fixture")
    invalid = parse_action(json.dumps({
        "action": "advance", "status": "passed", "stage_id": "01", "revision": "r1", "next_stage": "02",
        "payload": stage_one_payload(),
    }, ensure_ascii=False))
    with pytest.raises(ProtocolError, match="required subagent cards"):
        validate_action(invalid, state)

    state = complete_required_card(state)
    validate_action(invalid, state)
    advanced = apply_action(state, invalid)
    assert advanced["stage"]["id"] == "02"
    assert advanced["task_spec"]["status"] == "clarified"


def test_stage_one_rollback_can_write_clarify_and_create_new_auditor_revision():
    state = complete_required_card(create_state("fixture"))
    task_spec = stage_one_payload()["task_spec"]
    action = parse_action(json.dumps({
        "action": "clarify",
        "status": "structured_pending_audit",
        "stage_id": "01",
        "revision": "r1",
        "next_stage": None,
        "rollback_to": None,
        "message": "根据 requirements auditor 的 rollback 完成完整语义分解。",
        "payload": {
            "task_spec": task_spec,
            "repair": {
                "auditor_card_id": "01-r1-requirements-auditor",
                "auditor_verdict": "rollback",
                "audit_artifact_ref": "loop-artifacts/gate-reviews/01-r1-requirements-auditor.json",
                "reason": "原 task_spec 为空，需要补全七类语义角色和场景。",
            },
        },
    }, ensure_ascii=False))
    validate_action(action, state)
    repaired = apply_action(state, action)

    assert repaired["stage"]["id"] == "01"
    assert repaired["stage"]["revision"] == "r2"
    assert repaired["task_spec"]["status"] == "structured_pending_audit"
    assert repaired["subagent_cards"]["01-r1-requirements-auditor"]["status"] == "completed"
    assert repaired["subagent_cards"]["01-r2-requirements-auditor"]["status"] == "pending"
    assert repaired["clarification_history"][-1]["to_stage"] == "01-r2"


def test_clarify_accepts_model_labeling_the_new_revision():
    state = complete_required_card(create_state("fixture"))
    task_spec = stage_one_payload()["task_spec"]
    action = parse_action(json.dumps({
        "action": "clarify",
        "status": "structured_pending_audit",
        "stage_id": "01",
        "revision": "r2",
        "next_stage": None,
        "rollback_to": None,
        "payload": {
            "task_spec": task_spec,
            "repair": {
                "auditor_card_id": "01-r1-requirements-auditor",
                "auditor_verdict": "rollback",
                "audit_artifact_ref": "loop-artifacts/gate-reviews/01-r1-requirements-auditor.json",
                "reason": "补全结构化任务规格。",
            },
        },
    }, ensure_ascii=False))

    validate_action(action, state)
    repaired = apply_action(state, action)

    assert repaired["stage"]["revision"] == "r2"
    assert repaired["clarification_history"][-1]["from_stage"] == "01-r1"


def test_completed_card_cannot_regress_from_late_hook_observation():
    state = create_state("fixture")
    card = next(iter(state["subagent_cards"].values()))
    state = update_subagent_card(state, card["id"], "completed", agent_id="gate-agent")
    state = update_subagent_card(state, card["id"], "dispatched", agent_id="late-posttool")
    assert state["subagent_cards"][card["id"]]["status"] == "completed"


def test_stage_two_plan_generates_ready_research_task_cards():
    state = complete_required_card(create_state("fixture"))
    state = apply_action(
        state,
        parse_action(json.dumps({
            "action": "advance", "status": "passed", "stage_id": "01", "revision": "r1", "next_stage": "02",
            "payload": stage_one_payload(),
        }, ensure_ascii=False)),
    )
    state = complete_required_card(state, "02")
    state = apply_action(
        state,
        parse_action(json.dumps({
            "action": "advance", "status": "passed", "stage_id": "02", "revision": "r1", "next_stage": "03",
            "payload": _plan_payload(),
        }, ensure_ascii=False)),
    )
    cards = state["subagent_cards"]
    assert cards["03-r1-T1.1"]["task_id"] == "T1.1"
    assert cards["03-r1-T1.2"]["task_id"] == "T1.2"
    assert "03-r1-J1" not in cards


def test_stage_three_creates_independent_join_gate_only_after_all_tasks_finish():
    state = complete_required_card(create_state("fixture"))
    state = apply_action(
        state,
        parse_action(json.dumps({
            "action": "advance", "status": "passed", "stage_id": "01", "revision": "r1", "next_stage": "02",
            "payload": stage_one_payload(),
        }, ensure_ascii=False)),
    )
    state = complete_required_card(state, "02")
    state = apply_action(
        state,
        parse_action(json.dumps({
            "action": "advance", "status": "passed", "stage_id": "02", "revision": "r1", "next_stage": "03",
            "payload": _plan_payload(),
        }, ensure_ascii=False)),
    )
    # Complete the DAG worker cards (those with a task_id and not the stage
    # gate). Re-evaluate each round because completing the parallel workers
    # makes the join node ready, and finishing every node lets ensure_stage_cards
    # generate the builder + independent join gate. Leave the gate pending to
    # prove advance refuses until the gate finishes.
    while True:
        pending = [
            cid for cid, c in state["subagent_cards"].items()
            if c.get("task_id") and not c.get("is_stage_gate") and c.get("status") != "completed"
        ]
        if not pending:
            break
        state = update_subagent_card(state, pending[0], "completed")
    assert "03-r1-builder-execution_summary" in state["subagent_cards"]
    state = update_subagent_card(state, "03-r1-builder-execution_summary", "completed")
    assert state["subagent_cards"]["03-r1-execution-join-auditor"]["is_stage_gate"] is True
    payload = {
        "stage_review": stage_review("03", "03-r1-execution-join-auditor"),
        "execution_summary": {
            "completed_task_ids": ["T1.1", "T1.2", "J1"],
            "artifact_refs": ["evidence/join.json"],
            "unresolved_claims": [],
        },
    }
    action = parse_action(json.dumps({
        "action": "advance", "status": "passed", "stage_id": "03", "revision": "r1", "next_stage": "04",
        "payload": payload,
    }, ensure_ascii=False))
    with pytest.raises(ProtocolError, match="required subagent cards"):
        validate_action(action, state)
    state = complete_required_card(state, "03")
    validate_action(action, state)


def test_human_input_is_written_to_canonical_task_spec(tmp_path):
    state = create_state("fixture", task="调研 GPU")
    save_state(tmp_path / "loop-state.json", state)
    handle_userpromptsubmit({"cwd": str(tmp_path), "prompt": "场景是云端 API，缓存命中率约 90%"})
    persisted = load_state(tmp_path / "loop-state.json")
    assert persisted["task_spec"]["authoritative_inputs"][-1]["text"] == "场景是云端 API，缓存命中率约 90%"


def test_stage_four_rejects_claims_without_fact_ledger():
    node = DEFAULT_GRAPH.get("04")
    state = create_state("fixture")
    state["stage"] = {"id": node.id, "revision": "r1", **node.to_dict()}
    state = ensure_stage_cards(state)
    state = complete_required_card(state, "04")
    action = parse_action(json.dumps({
        "action": "advance", "status": "passed", "stage_id": "04", "revision": "r1", "next_stage": "05",
        "payload": {"stage_review": stage_review("04", "04-r1-evidence-verifier"), "verification": {}},
    }, ensure_ascii=False))
    with pytest.raises(ProtocolError, match="claim_ledger"):
        validate_action(action, state)


def test_decision_and_handoff_stages_each_require_and_persist_a_gate_review():
    node = DEFAULT_GRAPH.get("05")
    state = create_state("fixture")
    state["stage"] = {"id": node.id, "revision": "r1", **node.to_dict()}
    state = ensure_stage_cards(state)
    state = complete_required_card(state, "05")
    decision_action = parse_action(json.dumps({
        "action": "advance", "status": "passed", "stage_id": "05", "revision": "r1", "next_stage": "06",
        "payload": {
            "stage_review": stage_review("05", "05-r1-decision-auditor"),
            "decision": {
                "selected_option": "候选 A",
                "decision_rationale": "满足已验证的默认场景约束",
                "evidence_refs": ["loop-artifacts/verification.json"],
                "rejected_options": ["候选 B：显存不足"],
                "risks": ["价格需在购买日复核"],
                "human_approval_needed": False,
            },
        },
    }, ensure_ascii=False))
    state = apply_action(state, decision_action)
    assert state["stage"]["id"] == "06"
    assert state["decision"]["selected_option"] == "候选 A"

    state = complete_required_card(state, "06")
    handoff_action = parse_action(json.dumps({
        "action": "advance", "status": "passed", "stage_id": "06", "revision": "r1", "next_stage": "exploration",
        "payload": {
            "stage_review": stage_review("06", "06-r1-handoff-auditor"),
            "handoff": {
                "deliverables": ["report.md"],
                "decision_ref": "loop-state.json.decision",
                "remaining_tasks": [],
                "blocked_human": [],
                "candidates": [],
                "resume_instruction": "如价格变化，回到 04 重新核验。",
            },
        },
    }, ensure_ascii=False))
    state = apply_action(state, handoff_action)
    assert state["status"] == "exploration"
    assert state["stage"]["id"] == "exploration"
    assert state["handoff"]["deliverables"] == ["report.md"]

def test_factor_groups_default_keeps_named_buckets():
    # 默认 7 角色仍映射到 context / options / output 三张命名卡，兼容历史路径。
    groups = factor_groups({"task_spec": {}}, "01", "task_spec")
    assert [g for g, _ in groups] == ["context", "options", "output"]
    flat = [role for _, roles in groups for role in roles]
    assert flat == ["background", "decision_object", "objective", "comparison_set", "constraints", "deliverable", "uncertainty"]


def test_factor_groups_more_factors_yields_more_cards():
    # 因素增多 -> 卡数随之增多，且每卡 ≤3 个字段。
    many = ["f1", "f2", "f3", "f4", "f5", "f6", "f7", "f8", "f9"]
    groups = factor_groups({"task_spec": {"factor_roles": many}}, "01", "task_spec")
    assert len(groups) == 3  # ceil(9/3)
    flat = [role for _, roles in groups for role in roles]
    assert flat == many
    assert all(len(roles) <= 3 for _, roles in groups)


def test_factor_groups_fewer_factors_yields_fewer_cards():
    # 因素减少 -> 卡数随之减少（2 因素合成 1 张 g1 卡）。
    few = ["background", "objective"]
    groups = factor_groups({"task_spec": {"factor_roles": few}}, "01", "task_spec")
    assert len(groups) == 1
    assert groups[0][0] == "g1"


def test_factor_groups_single_factor_named_group():
    # 单个因素时，group 直接取因素名（路径友好）。
    groups = factor_groups({"task_spec": {"factor_roles": ["background"]}}, "01", "task_spec")
    assert len(groups) == 1
    assert groups[0][0] == "background"


def test_merge_partials_uses_factor_groups_state():
    # merge_task_spec_partials 必须按 state 中的因素动态合并，而非写死常量。
    state = {"task_spec": {"factor_roles": ["alpha", "beta", "gamma", "delta"]}}
    groups = factor_groups(state, "01", "task_spec")
    assert len(groups) == 2


def test_stage_one_builder_card_count_follows_factors():
    # 阶段 01 的 builder 卡数随因素个数变化（默认仍是 3 张命名卡）。
    state = create_state("fixture", task="调研性价比 GPU")
    state = ensure_stage_cards(state)
    builder_ids = [
        cid for cid, c in state["subagent_cards"].items()
        if cid.endswith("-builder-task_spec-context")
        or cid.endswith("-builder-task_spec-options")
        or cid.endswith("-builder-task_spec-output")
    ]
    assert builder_ids == [
        "01-r1-builder-task_spec-context",
        "01-r1-builder-task_spec-options",
        "01-r1-builder-task_spec-output",
    ]

def test_recovery_prompt_forces_builder_before_gate_when_builders_pending():
    # 存在 pending builder 时，第一动作闸门必须禁止提前派发 gate（防死锁）。
    state = create_state("fixture", task="调研性价比 GPU")
    state = ensure_stage_cards(state)
    for cid in ("01-r1-builder-task_spec-context", "01-r1-builder-task_spec-options",
                "01-r1-builder-task_spec-output"):
        state["subagent_cards"][cid]["status"] = "pending"
    state["subagent_cards"]["01-r1-requirements-auditor"]["status"] = "pending"
    rendered = PromptRenderer().compact_recovery_prompt(state, reason="测试", fresh_session=True)
    assert "第一动作闸门" in rendered.text
    assert "严禁" in rendered.text
    assert "01-r1-builder-task_spec-context" in rendered.text


def test_recovery_prompt_no_ordering_gate_when_builders_done():
    # builder 全部 completed 后，不应再出现强制排序闸门。
    state = create_state("fixture", task="调研性价比 GPU")
    state = ensure_stage_cards(state)
    for cid, c in state["subagent_cards"].items():
        c["status"] = "completed"
    rendered = PromptRenderer().compact_recovery_prompt(state, reason="测试", fresh_session=True)
    assert "第一动作闸门" not in rendered.text

