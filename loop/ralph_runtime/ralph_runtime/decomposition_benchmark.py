"""Semantic benchmark for the first RALPH decomposition stage.

The stage-01 protocol already checks that a ``task_spec`` has the right JSON
shape.  This module adds a small, deterministic rubric for one deliberately
simple task.  It does not try to judge the quality of a GPU recommendation;
it judges whether the Commander exposed the decision variables before doing
research.

This is intentionally a benchmark, not a general-purpose natural-language
grader.  A future domain can provide another profile without changing the
state machine or Hook rules.
"""

from __future__ import annotations

import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Mapping

from .runtime_config import field_mode_enabled


DEFAULT_SIMPLE_GPU_TASK = "我需要跑本地 AI，帮我调研性价比最高的 GPU"

SEMANTIC_ROLES = (
    "background",
    "decision_object",
    "objective",
    "comparison_set",
    "constraints",
    "deliverable",
    "uncertainty",
)

DISPOSITIONS = {"confirmed", "inferred", "ask_human", "assume", "research"}

# These are deliberately broad synonym groups.  The benchmark must not make
# Chinese wording deterministic; it only checks that the concept is present.
ROLE_HINTS: dict[str, tuple[str, ...]] = {
    "background": ("本地", "离线", "自托管", "推理", "工作站", "local", "self-host"),
    "decision_object": ("gpu", "显卡", "图形卡", "硬件", "加速卡", "graphics"),
    "objective": ("性价比", "性能价格", "性能/价格", "单位成本", "总拥有成本", "cost-performance", "value"),
    "comparison_set": ("候选", "比较", "对比", "型号", "方案", "替代", "基线", "candidate", "alternative"),
    "constraints": ("预算", "价格", "地区", "币种", "功耗", "电源", "兼容", "显存", "内存", "并发", "驱动", "本地"),
    "deliverable": ("调研", "研究", "报告", "推荐", "排名", "清单", "结论", "比较", "research", "recommend"),
    "uncertainty": ("未知", "不确定", "待确认", "假设", "场景", "敏感性", "日期", "实时", "模型规模", "价格区间", "风险", "uncertain"),
}

ATTRIBUTE_GROUPS: dict[str, tuple[str, ...]] = {
    "model_or_workload": ("模型", "模型规模", "参数", "30b", "35b", "推理", "并发", "工作负载", "context", "上下文"),
    "price_and_market": ("价格", "预算", "地区", "币种", "总成本", "电费", "价格日期", "市场", "tco"),
    "performance": ("性能", "吞吐", "延迟", "速度", "token/s", "benchmark", "基准测试", "利用率"),
    "memory": ("显存", "内存", "量化", "kv", "容量", "带宽", "上下文长度"),
    "compatibility_and_power": ("兼容", "驱动", "框架", "cuda", "mlx", "pcie", "电源", "功耗", "散热", "接口"),
    "comparison_logic": ("候选", "型号", "方案", "比较", "对比", "排序", "基线", "替代"),
}

UNNECESSARY_QUESTION_PATTERNS = (
    re.compile(r"(?:是否|要不要|需不需要|是不是).{0,12}(?:gpu|显卡|硬件)", re.I),
    re.compile(r"(?:是否|要不要).{0,16}(?:比较|考虑).{0,8}(?:云|云服务)", re.I),
    re.compile(r"(?:是否|要不要).{0,12}(?:本地|离线).{0,8}(?:运行|部署)", re.I),
    re.compile(r"(?:模型|大模型).{0,10}(?:是什么|用什么型号)", re.I),
)


def _text(value: Any) -> str:
    """Flatten a JSON value into searchable text without relying on wording."""

    if value is None:
        return ""
    if isinstance(value, str):
        return value
    if isinstance(value, Mapping):
        return " ".join(f"{_text(key)} {_text(item)}" for key, item in value.items())
    if isinstance(value, (list, tuple, set)):
        return " ".join(_text(item) for item in value)
    return str(value)


def _contains_any(text: str, hints: tuple[str, ...]) -> bool:
    lowered = text.casefold()
    return any(hint.casefold() in lowered for hint in hints)


def _finding(code: str, message: str, *, severity: str = "error", evidence: Any = None) -> dict[str, Any]:
    result: dict[str, Any] = {"code": code, "severity": severity, "message": message}
    if evidence is not None:
        result["evidence"] = evidence
    return result


@dataclass(frozen=True)
class BenchmarkResult:
    """Serializable result of one decomposition benchmark run."""

    task: str
    score: float
    threshold: float
    passed: bool
    checks: tuple[dict[str, Any], ...]
    findings: tuple[dict[str, Any], ...]

    def to_dict(self) -> dict[str, Any]:
        return {
            "benchmark": "simple_gpu_decomposition",
            "task": self.task,
            "score": round(self.score, 4),
            "threshold": self.threshold,
            "passed": self.passed,
            "checks": [dict(check) for check in self.checks],
            "findings": [dict(item) for item in self.findings],
        }


def _check(
    checks: list[dict[str, Any]],
    findings: list[dict[str, Any]],
    check_id: str,
    points: int,
    passed: bool,
    message: str,
    check_findings: list[dict[str, Any]] | None = None,
) -> None:
    local = list(check_findings or [])
    checks.append(
        {
            "id": check_id,
            "passed": passed,
            "points": points if passed else 0,
            "max_points": points,
            "message": message,
            "findings": local,
        }
    )
    findings.extend(local)


def evaluate_task_spec(
    task_spec: Mapping[str, Any],
    *,
    task: str = DEFAULT_SIMPLE_GPU_TASK,
    threshold: float = 0.8,
) -> BenchmarkResult:
    """Evaluate the semantic completeness of a simple local-GPU task spec.

    The function is intentionally read-only and deterministic.  It accepts
    the task-spec object directly so tests can grade a saved Agent result or a
    fixture without creating a project or invoking Claude Code.
    """

    if not isinstance(task_spec, Mapping):
        return BenchmarkResult(
            task=task,
            score=0.0,
            threshold=threshold,
            passed=False,
            checks=(),
            findings=(_finding("TASK_SPEC_MISSING", "没有可评估的 task_spec 对象"),),
        )

    checks: list[dict[str, Any]] = []
    findings: list[dict[str, Any]] = []
    semantic_map = task_spec.get("semantic_map")
    semantic_map = semantic_map if isinstance(semantic_map, Mapping) else {}

    # Check 1: all seven semantic roles are present and not merely filled by
    # empty placeholders.  Hints make the benchmark catch a role that exists
    # syntactically but was never semantically interpreted.
    role_findings: list[dict[str, Any]] = []
    role_ok = True
    for role in SEMANTIC_ROLES:
        value = semantic_map.get(role)
        content = _text(value).strip()
        if not content:
            role_ok = False
            role_findings.append(_finding("ROLE_EMPTY", f"semantic_map.{role} 为空", evidence=role))
        elif not _contains_any(content, ROLE_HINTS[role]):
            role_ok = False
            role_findings.append(
                _finding("ROLE_THIN", f"semantic_map.{role} 没有显示出该语义角色的内容", evidence=content[:240])
            )
    _check(
        checks,
        findings,
        "semantic_roles",
        2,
        role_ok,
        "七个决策语义角色都有具体内容",
        role_findings,
    )

    # Check 2: the matrix must descend to leaves for every role.  This is the
    # distinction between a nice summary and an actually executable input.
    raw_matrix = task_spec.get("attribute_matrix")
    matrix = raw_matrix if isinstance(raw_matrix, list) else []
    matrix_findings: list[dict[str, Any]] = []
    covered_roles: set[str] = set()
    matrix_ok = bool(matrix)
    for index, leaf in enumerate(matrix):
        if not isinstance(leaf, Mapping):
            matrix_ok = False
            matrix_findings.append(_finding("LEAF_NOT_OBJECT", f"attribute_matrix[{index}] 不是对象"))
            continue
        role = str(leaf.get("role", "")).strip()
        covered_roles.add(role)
        for key in ("concept", "role", "attribute", "disposition", "rationale"):
            if not str(leaf.get(key, "")).strip():
                matrix_ok = False
                matrix_findings.append(_finding("LEAF_FIELD_MISSING", f"attribute_matrix[{index}].{key} 为空"))
        if role not in SEMANTIC_ROLES:
            matrix_ok = False
            matrix_findings.append(_finding("LEAF_ROLE_UNKNOWN", f"attribute_matrix[{index}].role 不属于七个语义角色", evidence=role))
        disposition = str(leaf.get("disposition", ""))
        if disposition not in DISPOSITIONS:
            matrix_ok = False
            matrix_findings.append(_finding("DISPOSITION_INVALID", f"attribute_matrix[{index}].disposition 无效", evidence=disposition))
        if not isinstance(leaf.get("evidence_refs", []), list):
            matrix_ok = False
            matrix_findings.append(_finding("EVIDENCE_REFS_INVALID", f"attribute_matrix[{index}].evidence_refs 必须是数组"))
        confidence = leaf.get("confidence")
        if not isinstance(confidence, (int, float)) or not 0 <= float(confidence) <= 1:
            matrix_ok = False
            matrix_findings.append(_finding("CONFIDENCE_INVALID", f"attribute_matrix[{index}].confidence 必须是 0 到 1"))
    missing_roles = sorted(set(SEMANTIC_ROLES) - covered_roles)
    if missing_roles:
        matrix_ok = False
        matrix_findings.append(_finding("ATTRIBUTE_ROLE_GAP", "attribute_matrix 没有把所有语义角色落到叶节点", evidence=missing_roles))
    _check(
        checks,
        findings,
        "attribute_matrix",
        2,
        matrix_ok,
        "每个语义角色都被展开为带处置方式和证据元数据的叶节点",
        matrix_findings,
    )

    # Check 3: ensure the important hidden decision dimensions are visible.
    matrix_text = _text(matrix)
    attribute_hits = sorted(
        group for group, hints in ATTRIBUTE_GROUPS.items() if _contains_any(matrix_text, hints)
    )
    attribute_ok = len(attribute_hits) >= 5
    attribute_findings: list[dict[str, Any]] = []
    if not attribute_ok:
        attribute_findings.append(
            _finding(
                "HIDDEN_ATTRIBUTE_GAP",
                "隐藏属性覆盖不足；至少应覆盖模型/工作负载、价格市场、性能、内存、兼容/功耗和比较逻辑中的五类",
                evidence={"covered": attribute_hits, "required_minimum": 5},
            )
        )
    _check(
        checks,
        findings,
        "hidden_attributes",
        2,
        attribute_ok,
        "关键隐藏决策维度已显式列出",
        attribute_findings,
    )

    # Check 4: a complete decomposition must distinguish evidence status from
    # a human question.  At least one research branch and one non-question
    # disposition are required; an explicit assumption is acceptable when it
    # is paired with a scenario.
    dispositions = {
        str(leaf.get("disposition"))
        for leaf in matrix
        if isinstance(leaf, Mapping)
    }
    disposition_findings: list[dict[str, Any]] = []
    disposition_ok = (
        "research" in dispositions
        and bool(dispositions & {"confirmed", "inferred"})
        and bool(dispositions & {"assume", "ask_human"})
    )
    if not disposition_ok:
        disposition_findings.append(
            _finding(
                "DISPOSITION_MIX_INCOMPLETE",
                "必须同时出现 research、confirmed/inferred，以及 assume/ask_human 三类处置，不能把所有未知都变成问题",
                evidence=sorted(dispositions),
            )
        )
    _check(
        checks,
        findings,
        "disposition_gate",
        1,
        disposition_ok,
        "叶节点区分已知、推断、假设/问题和待研究",
        disposition_findings,
    )

    # Check 5: scenarios are the safe way to proceed when model size,
    # concurrency or market is unknown.  Requiring two scenarios is what
    # catches the earlier behavior of asking a question before doing the
    # decomposition.
    scenarios = task_spec.get("scenarios")
    scenarios = scenarios if isinstance(scenarios, list) else []
    scenario_text = _text(scenarios)
    scenario_ok = len(scenarios) >= 2 and _contains_any(
        scenario_text,
        ("模型", "规模", "30b", "35b", "并发", "负载", "价格", "地区", "预算", "显存", "内存"),
    )
    scenario_findings: list[dict[str, Any]] = []
    if not scenario_ok:
        scenario_findings.append(
            _finding(
                "SCENARIO_COVERAGE_GAP",
                "未知的模型规模/并发/市场条件没有被至少两个可比较场景覆盖",
                evidence={"count": len(scenarios), "text": scenario_text[:360]},
            )
        )
    _check(
        checks,
        findings,
        "scenario_coverage",
        1,
        scenario_ok,
        "不确定条件被转成可继续执行的场景",
        scenario_findings,
    )

    # Check 6: success criteria must be operational, not just "find the best
    # GPU".  Evidence/date/fit are the minimum needed for this benchmark.
    success = task_spec.get("success_criteria")
    success = success if isinstance(success, list) else []
    success_text = _text(success)
    success_ok = len(success) >= 2 and _contains_any(
        success_text,
        ("证据", "来源", "日期", "价格", "性能", "适配", "推荐", "验证", "可复现"),
    )
    success_findings: list[dict[str, Any]] = []
    if not success_ok:
        success_findings.append(
            _finding(
                "SUCCESS_CRITERIA_THIN",
                "成功标准没有同时约束证据、性能/价格比较和适配或推荐边界",
                evidence=success_text[:360],
            )
        )
    _check(
        checks,
        findings,
        "success_criteria",
        1,
        success_ok,
        "交付标准可验证且不是泛泛而谈",
        success_findings,
    )

    # Check 7: the question gate catches questions the prompt should have
    # prevented.  Legitimate high-impact questions (budget, market, hard
    # acceptance criteria) remain allowed.
    raw_questions = task_spec.get("open_questions")
    questions = raw_questions if isinstance(raw_questions, list) else []
    question_findings: list[dict[str, Any]] = []
    question_ok = True
    for index, question in enumerate(questions):
        question_text = _text(question).strip()
        if not question_text:
            question_ok = False
            question_findings.append(_finding("QUESTION_EMPTY", f"open_questions[{index}] 为空"))
            continue
        if any(pattern.search(question_text) for pattern in UNNECESSARY_QUESTION_PATTERNS):
            question_ok = False
            question_findings.append(
                _finding(
                    "UNNECESSARY_HUMAN_QUESTION",
                    "问题询问了输入已经明确、可以推断或可以研究的事项；应转为 confirmed/inferred/research/scene",
                    evidence=question_text,
                )
            )
        if isinstance(question, Mapping):
            for key in ("question", "why_it_matters", "recommended_option"):
                if not str(question.get(key, "")).strip():
                    question_ok = False
                    question_findings.append(_finding("QUESTION_FIELD_MISSING", f"open_questions[{index}].{key} 为空"))
    _check(
        checks,
        findings,
        "question_gate",
        1,
        question_ok,
        "没有把可推断/可调研事项错误地抛给人类",
        question_findings,
    )

    # Check 8: the independent requirements auditor is part of the capability
    # under test.  The pure task-spec function cannot prove it, so it checks
    # the receipt fields; evaluate_state below additionally checks lifecycle.
    audit = task_spec.get("requirements_audit")
    audit = audit if isinstance(audit, Mapping) else {}
    # The active protocol records incremental field validation and does not
    # require a legacy auditor card.  Historical fixtures may still carry the
    # old receipt, which remains accepted but is no longer a gate.
    audit_ok = field_mode_enabled() or all(
        str(audit.get(key, "")).strip() for key in ("card_id", "artifact_ref", "summary")
    )
    audit_findings: list[dict[str, Any]] = []
    if not audit_ok:
        audit_findings.append(_finding("REQUIREMENTS_AUDIT_MISSING", "缺少需求分解审计引用"))
    _check(
        checks,
        findings,
        "requirements_audit",
        1,
        audit_ok,
        "需求分解审计结果可追溯（field protocol 不要求旧 auditor card）",
        audit_findings,
    )

    points = sum(int(check["points"]) for check in checks)
    maximum = sum(int(check["max_points"]) for check in checks)
    score = points / maximum if maximum else 0.0
    has_errors = any(item.get("severity") == "error" for item in findings)
    passed = score >= threshold and not has_errors
    return BenchmarkResult(
        task=task,
        score=score,
        threshold=threshold,
        passed=passed,
        checks=tuple(checks),
        findings=tuple(findings),
    )


def evaluate_state(
    state: Mapping[str, Any],
    *,
    task: str | None = None,
    threshold: float = 0.8,
) -> BenchmarkResult:
    """Evaluate a persisted project using the active field protocol."""

    state_task = state.get("task", {})
    if task is None and isinstance(state_task, Mapping):
        task = str(state_task.get("description", "")) or DEFAULT_SIMPLE_GPU_TASK
    result = evaluate_task_spec(
        state.get("task_spec", {}) if isinstance(state, Mapping) else {},
        task=task or DEFAULT_SIMPLE_GPU_TASK,
        threshold=threshold,
    )
    checks = list(result.checks)
    findings = list(result.findings)

    task_spec = state.get("task_spec", {}) if isinstance(state, Mapping) else {}
    field_tasks = state.get("field_tasks") if isinstance(state, Mapping) else None
    field_tasks = [] if field_tasks is None else field_tasks
    field_lifecycle_ok = isinstance(field_tasks, list) and all(
        isinstance(task, Mapping) and str(task.get("status", "")) in {"ready", "pending", "dispatching", "dispatched", "completed"}
        for task in field_tasks
    )
    lifecycle_findings: list[dict[str, Any]] = []
    if not field_lifecycle_ok:
        lifecycle_findings.append(_finding("FIELD_TASK_LIFECYCLE_INVALID", "字段任务生命周期记录不是合法状态"))
    checks.append(
        {
            "id": "field_task_lifecycle",
            "passed": field_lifecycle_ok,
            "points": 1 if field_lifecycle_ok else 0,
            "max_points": 1,
            "message": "field task 只通过增量 apply 和 SubagentStop 生命周期推进",
            "findings": lifecycle_findings,
        }
    )
    findings.extend(lifecycle_findings)

    points = sum(int(check["points"]) for check in checks)
    maximum = sum(int(check["max_points"]) for check in checks)
    score = points / maximum if maximum else 0.0
    passed = score >= threshold and not any(item.get("severity") == "error" for item in findings)
    return BenchmarkResult(
        task=result.task,
        score=score,
        threshold=threshold,
        passed=passed,
        checks=tuple(checks),
        findings=tuple(findings),
    )


def load_task_spec_file(path: str | Path) -> tuple[dict[str, Any], str | None]:
    """Load a task-spec, action, or state JSON for the read-only benchmark."""

    raw = json.loads(Path(path).read_text(encoding="utf-8"))
    if not isinstance(raw, Mapping):
        raise ValueError("benchmark input must be a JSON object")
    if isinstance(raw.get("task_spec"), Mapping):
        return dict(raw["task_spec"]), str(raw.get("task", "")) or None
    payload = raw.get("payload")
    if isinstance(payload, Mapping) and isinstance(payload.get("task_spec"), Mapping):
        return dict(payload["task_spec"]), str(raw.get("task", "")) or None
    state = raw.get("state")
    if isinstance(state, Mapping) and isinstance(state.get("task_spec"), Mapping):
        task = state.get("task", {})
        description = task.get("description") if isinstance(task, Mapping) else None
        return dict(state["task_spec"]), str(description or "") or None
    raise ValueError("JSON input does not contain task_spec, payload.task_spec, or state.task_spec")
