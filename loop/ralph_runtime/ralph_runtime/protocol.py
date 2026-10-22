"""Structured Agent action protocol and validation."""

from __future__ import annotations

import json
import os
import re
from dataclasses import dataclass
from typing import Any, Mapping
from urllib.parse import urlparse

from .dag import DAGValidationError, validate_plan
from .runtime_config import field_mode_enabled, flow_only_mode


ALLOWED_ACTIONS = frozenset(
    {
        "advance",
        "rollback",
        "blocked_human",
        "skip_blocked",
        "candidate",
        "explore",
        "dispatch",
        "join",
        "clarify",
        "repair_prompt",
    }
)


class ProtocolError(ValueError):
    """Raised when an Agent result cannot be safely accepted."""


_EXTERNAL_FACT_ROLES = frozenset(
    {
        "market_data",
        "benchmark_data",
        "spec_data",
        "research_findings",
        "ecosystem_analysis",
    }
)
_CURRENT_MARKET_MARKERS = (
    "current",
    "latest",
    "price",
    "market",
    "listing",
    "现价",
    "当前",
    "最新",
    "价格",
    "行情",
    "市场",
    "报价",
)
_CROSS_VALIDATION_ROLES = frozenset({"cross_validation", "cross_validation_out", "validation"})
_VALIDATION_VERDICTS = frozenset({"supported", "contradicted", "uncertain"})


def _field_text(field: Mapping[str, Any]) -> str:
    return " ".join(
        str(field.get(key) or "")
        for key in ("concept", "role", "attribute", "rationale")
    ).lower()


def _is_specific_source_url(value: Any) -> bool:
    """Accept a claim-level public URL, never a bare site/home-page citation."""

    if not isinstance(value, str) or not value.strip():
        return False
    parsed = urlparse(value.strip())
    return parsed.scheme == "https" and bool(parsed.netloc) and bool(parsed.path.strip("/"))


def _is_current_market_field(field: Mapping[str, Any]) -> bool:
    role = str(field.get("role") or "").strip().lower()
    return role == "market_data" or any(marker in _field_text(field) for marker in _CURRENT_MARKET_MARKERS)


def _needs_external_evidence(field: Mapping[str, Any]) -> bool:
    role = str(field.get("role") or "").strip().lower()
    return role in _EXTERNAL_FACT_ROLES or _is_current_market_field(field)


def _external_evidence_issues(matrix: list[Any], stage_id: str) -> list[str]:
    """Reject invented current facts and generic-domain citations.

    A field table is intentionally flexible, but an external fact cannot become
    ``confirmed`` merely because it names a website.  These checks begin at
    research stage 02: stage 01 may record *what needs research*, while later
    stages must carry claim-level sources.  Market facts additionally require
    an observation date, because a stale price is not a current price.
    """

    if stage_id not in {"02", "02.5", "03", "04", "04.5"}:
        return []
    issues: list[str] = []
    for raw in matrix:
        if not isinstance(raw, Mapping) or not _needs_external_evidence(raw):
            continue
        disposition = str(raw.get("disposition") or "")
        if disposition == "assumed_default":
            concept = str(raw.get("concept") or raw.get("attribute") or "?")
            issues.append(
                f"外部事实字段 {concept} 不能用 assumed_default 绕过调研；默认只适用于偏好，事实应保留 research_required/uncertain。"
            )
            continue
        if disposition == "pending":
            continue
        concept = str(raw.get("concept") or raw.get("attribute") or "?")
        refs = raw.get("evidence_refs")
        specific_refs = [item for item in refs if _is_specific_source_url(item)] if isinstance(refs, list) else []
        if not specific_refs:
            issues.append(
                f"外部事实字段 {concept} 缺少可复核的具体 HTTPS 来源；站点首页/根域名不是证据。"
            )
        if _is_current_market_field(raw):
            observed_at = raw.get("observed_at")
            if not isinstance(observed_at, str) or not re.match(r"^\d{4}-\d{2}-\d{2}(?:T|$)", observed_at.strip()):
                issues.append(
                    f"时效字段 {concept} 必须提供 observed_at（ISO 日期/时间）；无法现场核对时降为 research_required 或 uncertain。"
                )
    return issues


def _cross_validation_issues(matrix: list[Any], stage_id: str) -> list[str]:
    """Require claim-level, independently sourced cross-validation records."""

    if stage_id not in {"02.5", "04.5"}:
        return []
    issues: list[str] = []
    records_by_field: list[tuple[str, list[Any]]] = []
    for raw in matrix:
        if not isinstance(raw, Mapping):
            continue
        role = str(raw.get("role") or "").strip().lower()
        concept = str(raw.get("concept") or "")
        if role not in _CROSS_VALIDATION_ROLES and concept not in {"cross_validation", "cross_validation_out"}:
            continue
        records = raw.get("validation_records")
        label = concept or role or "cross_validation"
        if not isinstance(records, list) or not records:
            issues.append(
                f"交叉验证字段 {label} 缺少 validation_records；不能用一段摘要宣称“已由多源验证”。"
            )
            continue
        records_by_field.append((label, records))
        for index, record in enumerate(records):
            prefix = f"交叉验证 {label}.validation_records[{index}]"
            if not isinstance(record, Mapping):
                issues.append(f"{prefix} 必须是对象")
                continue
            claim = record.get("claim") or record.get("claim_ref")
            if not isinstance(claim, str) or not claim.strip():
                issues.append(f"{prefix} 必须填写 claim 或 claim_ref")
            refs = record.get("source_refs")
            if not isinstance(refs, list):
                issues.append(f"{prefix}.source_refs 必须是来源数组")
            else:
                specific = [ref for ref in refs if _is_specific_source_url(ref)]
                hosts = {urlparse(ref).netloc.lower() for ref in specific}
                if len(hosts) < 2:
                    issues.append(f"{prefix} 必须包含两个不同域名的具体 HTTPS 来源")
            verdict = record.get("verdict")
            if verdict not in _VALIDATION_VERDICTS:
                issues.append(f"{prefix}.verdict 必须为 supported / contradicted / uncertain")
            observed_at = record.get("observed_at")
            if not isinstance(observed_at, str) or not re.match(r"^\d{4}-\d{2}-\d{2}(?:T|$)", observed_at.strip()):
                issues.append(f"{prefix}.observed_at 必须是 ISO 日期/时间")

    if not records_by_field:
        issues.append("本阶段缺少 cross_validation 字段；必须逐 claim 记录独立来源、裁决与 observed_at。")
        return issues

    # At 02.5 each evidence-backed research field needs an explicit record;
    # otherwise a model can validate one convenient fact and call the whole
    # research packet verified.  Stage 04.5 validates the claim ledger summary
    # instead, so it is deliberately not subject to this field-name matching.
    if stage_id == "02.5":
        expected = {
            str(raw.get("concept") or "")
            for raw in matrix
            if isinstance(raw, Mapping)
            and str(raw.get("concept") or "")
            and str(raw.get("role") or "").strip().lower() not in _CROSS_VALIDATION_ROLES
            and isinstance(raw.get("evidence_refs"), list)
            and raw.get("evidence_refs")
        }
        recorded = {
            str(record.get("claim_ref") or "")
            for _, records in records_by_field
            for record in records
            if isinstance(record, Mapping)
        }
        missing = sorted(expected - recorded)
        if missing:
            issues.append(
                "02.5 尚未逐字段交叉核验以下已调研字段（validation_records.claim_ref 必须精确引用 concept）："
                + "，".join(missing)
            )
    return issues


def _execution_gate_issues(state: Mapping[str, Any]) -> list[str]:
    """Field-mode equivalent of the legacy execution-summary gate."""

    issues: list[str] = []
    plan = state.get("plan") if isinstance(state.get("plan"), Mapping) else {}
    nodes = plan.get("nodes", []) if isinstance(plan, Mapping) else []
    if not isinstance(nodes, list) or not nodes:
        return ["阶段 03 必须先用 role=task_graph 的结构化 task_graph 提交可执行 DAG；自然语言任务列表不算。"]
    try:
        validate_plan(plan, strict=True)
    except (DAGValidationError, TypeError, ValueError) as exc:
        return [f"阶段 03 task_graph 无效：{exc}"]
    expected = {str(node.get("id")) for node in nodes if isinstance(node, Mapping)}
    completed = {str(item) for item in (plan.get("completed", []) if isinstance(plan, Mapping) else [])}
    pending = sorted(expected - completed)
    if pending:
        issues.append("DAG 仍有未完成节点（先执行并运行 ralph graph-apply）：" + "，".join(pending))
    results = plan.get("task_results") if isinstance(plan, Mapping) else None
    if not isinstance(results, Mapping):
        issues.append("阶段 03 缺少 plan.task_results；不能只把节点 ID 标为 completed。")
        return issues
    for node_id in sorted(expected):
        result = results.get(node_id)
        if not isinstance(result, Mapping):
            issues.append(f"DAG 节点 {node_id} 缺少结构化 task_result。")
            continue
        if result.get("output") in (None, "", {}, []) and not result.get("evidence"):
            issues.append(f"DAG 节点 {node_id} 的 task_result 缺少 output/evidence。")
        refs = result.get("artifact_refs")
        if not isinstance(refs, list) or not refs:
            issues.append(f"DAG 节点 {node_id} 的 task_result 缺少实际交付 artifact_refs。")
    return issues


def _next_revision(current: str) -> str:
    """Return the one-step revision used by the clarify repair branch."""

    try:
        return f"r{int(current.lstrip('r')) + 1}"
    except (AttributeError, ValueError):
        return "r1"


@dataclass(frozen=True)
class ActionResult:
    action: str
    status: str
    stage_id: str
    revision: str
    next_stage: str | None = None
    rollback_to: str | None = None
    evidence: tuple[Any, ...] = ()
    artifact_refs: tuple[str, ...] = ()
    message: str = ""
    task_id: str | None = None
    payload: Mapping[str, Any] | None = None

    def to_dict(self) -> dict[str, Any]:
        result = {
            "action": self.action,
            "status": self.status,
            "stage_id": self.stage_id,
            "revision": self.revision,
            "next_stage": self.next_stage,
            "rollback_to": self.rollback_to,
            "evidence": list(self.evidence),
            "artifact_refs": list(self.artifact_refs),
            "message": self.message,
        }
        if self.task_id is not None:
            result["task_id"] = self.task_id
        if self.payload:
            result["payload"] = dict(self.payload)
        return result


def _decode_object(value: Any) -> dict[str, Any]:
    if not isinstance(value, dict):
        raise ProtocolError("RALPH action must be a JSON object")
    return value


def _extract_json(text: str) -> dict[str, Any]:
    stripped = text.strip()
    marker_patterns = (
        r"<RALPH_STAGE_RESULT>(?P<body>.*?)</RALPH_STAGE_RESULT>",
        r"<!--\s*RALPH_STAGE_RESULT(?P<body>.*?)RALPH_STAGE_RESULT\s*-->",
    )
    for pattern in marker_patterns:
        matches = list(re.finditer(pattern, text, flags=re.DOTALL))
        if matches:
            body = matches[-1].group("body")
            try:
                return _decode_json_fragment(body)
            except json.JSONDecodeError as exc:
                raise ProtocolError(f"invalid JSON in RALPH result marker: {exc}") from exc

    if stripped.startswith("```"):
        stripped = re.sub(r"^```(?:json)?\s*", "", stripped)
        stripped = re.sub(r"\s*```$", "", stripped)

    try:
        return _decode_object(json.loads(stripped))
    except json.JSONDecodeError:
        decoder = json.JSONDecoder()
        for index, character in enumerate(text):
            if character != "{":
                continue
            try:
                value, _ = decoder.raw_decode(text[index:])
                return _decode_object(value)
            except json.JSONDecodeError:
                continue
    raise ProtocolError("no valid JSON RALPH action found")


def _decode_json_fragment(text: str) -> dict[str, Any]:
    """Decode the first complete JSON object in a marker body, including nested payloads."""

    decoder = json.JSONDecoder()
    start = text.find("{")
    if start < 0:
        raise json.JSONDecodeError("no JSON object", text, 0)
    value, _ = decoder.raw_decode(text[start:])
    return _decode_object(value)


def parse_action(text: str | Mapping[str, Any]) -> ActionResult:
    raw = _decode_object(text) if isinstance(text, Mapping) else _extract_json(text)
    missing = [key for key in ("action", "status", "stage_id", "revision") if key not in raw]
    if missing:
        raise ProtocolError(f"RALPH action missing required fields: {', '.join(missing)}")
    for key in ("action", "status", "stage_id", "revision"):
        if not isinstance(raw[key], str) or not raw[key].strip():
            raise ProtocolError(f"RALPH action field {key} must be a non-empty string")
    action = str(raw["action"])
    if action not in ALLOWED_ACTIONS:
        raise ProtocolError(f"unsupported RALPH action: {action}")
    evidence = raw.get("evidence", ())
    artifact_refs = raw.get("artifact_refs", ())
    if not isinstance(evidence, (list, tuple)) or not isinstance(artifact_refs, (list, tuple)):
        raise ProtocolError("evidence and artifact_refs must be arrays")
    for key in ("next_stage", "rollback_to", "task_id"):
        if key in raw and raw[key] is not None and (not isinstance(raw[key], str) or not raw[key].strip()):
            raise ProtocolError(f"RALPH action field {key} must be a non-empty string when present")
    return ActionResult(
        action=action,
        status=str(raw["status"]),
        stage_id=str(raw["stage_id"]),
        revision=str(raw["revision"]),
        next_stage=str(raw["next_stage"]) if raw.get("next_stage") is not None else None,
        rollback_to=str(raw["rollback_to"]) if raw.get("rollback_to") is not None else None,
        evidence=tuple(evidence),
        artifact_refs=tuple(str(item) for item in artifact_refs),
        message=str(raw.get("message", "")),
        task_id=str(raw["task_id"]) if raw.get("task_id") is not None else None,
        payload=raw.get("payload") if isinstance(raw.get("payload"), Mapping) else None,
    )


def _require_mapping(value: Any, label: str) -> Mapping[str, Any]:
    if not isinstance(value, Mapping):
        raise ProtocolError(f"{label} must be an object")
    return value


def _require_list(value: Any, label: str, *, non_empty: bool = False) -> list[Any]:
    if not isinstance(value, list):
        raise ProtocolError(f"{label} must be an array")
    if non_empty and not value:
        raise ProtocolError(f"{label} must not be empty")
    return value


def _require_non_empty_string(value: Any, label: str) -> None:
    if not isinstance(value, str) or not value.strip():
        raise ProtocolError(f"{label} must be a non-empty string")


def _collect_stage_cards_issues(
    state: Mapping[str, Any], stage_id: str, revision: str
) -> list[str]:
    """Accumulate every subagent-card gate problem instead of stopping at the first."""

    issues: list[str] = []
    cards = state.get("subagent_cards", {})
    if not isinstance(cards, Mapping):
        issues.append("state has no subagent_cards")
        return issues
    required = [
        card for card in cards.values()
        if isinstance(card, Mapping)
        and str(card.get("stage_id")) == stage_id
        and str(card.get("revision")) == revision
        and bool(card.get("required_for_advance"))
    ]
    if not required:
        issues.append(f"stage {stage_id} requires an approved subagent task card")
        return issues
    pending = [str(card.get("id", "?")) for card in required if card.get("status") != "completed"]
    if pending:
        issues.append("required subagent cards are not completed: " + ", ".join(pending))
    return issues


def _require_stage_cards_completed(state: Mapping[str, Any], stage_id: str, revision: str) -> None:
    issues = _collect_stage_cards_issues(state, stage_id, revision)
    if issues:
        raise ProtocolError("; ".join(issues))


def _collect_stage_review_issues(
    payload: Mapping[str, Any],
    state: Mapping[str, Any],
    stage_id: str,
    revision: str,
) -> list[str]:
    """Accumulate every independent-gate problem instead of stopping at the first."""

    issues: list[str] = []
    review = payload.get("stage_review")
    if not isinstance(review, Mapping):
        issues.append(f"stage {stage_id} payload.stage_review must be an object")
        return issues
    for key in ("reviewer_card_id", "context_mode", "verdict", "recommended_action", "summary"):
        value = review.get(key)
        if not isinstance(value, str) or not value.strip():
            issues.append(f"stage_review.{key} must not be empty")
    if isinstance(review.get("context_mode"), str) and review["context_mode"] != "bounded_artifacts":
        issues.append("stage_review.context_mode must be bounded_artifacts")
    if isinstance(review.get("verdict"), str) and review["verdict"] != "pass":
        issues.append("a stage can advance only after the independent review returns pass/advance")
    if isinstance(review.get("recommended_action"), str) and review["recommended_action"] != "advance":
        issues.append("a stage can advance only after the independent review returns pass/advance")

    cards = state.get("subagent_cards", {})
    reviewer = (
        cards.get(review.get("reviewer_card_id"))
        if isinstance(cards, Mapping) and isinstance(review.get("reviewer_card_id"), str)
        else None
    )
    if not isinstance(reviewer, Mapping):
        issues.append("stage_review.reviewer_card_id does not identify an approved card")
    else:
        if not reviewer.get("is_stage_gate"):
            issues.append("stage_review.reviewer_card_id is not an independent stage gate")
        if str(reviewer.get("stage_id")) != stage_id or str(reviewer.get("revision")) != revision:
            issues.append("stage_review reviewer does not belong to the current stage revision")
        if reviewer.get("status") != "completed":
            issues.append("stage_review reviewer card is not completed")

    # The independent gate's authority is its verdict.  When it explicitly
    # returns ``pass`` + ``advance`` we trust that decision and only require the
    # structural fields above; the detailed findings/checks are advisory.  When
    # the verdict is *not* pass the review must be internally consistent
    # (no blocking findings, every check pass) before an advance is allowed.
    passed = (
        isinstance(review.get("verdict"), str)
        and review["verdict"] == "pass"
        and isinstance(review.get("recommended_action"), str)
        and review["recommended_action"] == "advance"
    )
    if not passed:
        checked_inputs = review.get("checked_input_refs")
        if not isinstance(checked_inputs, list) or not checked_inputs:
            issues.append("stage_review.checked_input_refs must not be empty")
        else:
            for index, value in enumerate(checked_inputs):
                if not isinstance(value, str) or not value.strip():
                    issues.append(f"stage_review.checked_input_refs[{index}] must not be empty")
        checked_outputs = review.get("checked_output_refs")
        if not isinstance(checked_outputs, list) or not checked_outputs:
            issues.append("stage_review.checked_output_refs must not be empty")
        else:
            for index, value in enumerate(checked_outputs):
                if not isinstance(value, str) or not value.strip():
                    issues.append(f"stage_review.checked_output_refs[{index}] must not be empty")

        checks = review.get("checks")
        if not isinstance(checks, list) or not checks:
            issues.append("stage_review.checks must not be empty")
        else:
            for index, check in enumerate(checks):
                if not isinstance(check, Mapping):
                    issues.append(f"stage_review.checks[{index}] must be an object")
                    continue
                for key in ("criterion", "status", "note"):
                    value = check.get(key)
                    if not isinstance(value, str) or not value.strip():
                        issues.append(f"stage_review.checks[{index}].{key} must not be empty")
                if not isinstance(check.get("evidence_refs"), list):
                    issues.append(f"stage_review.checks[{index}].evidence_refs must be an array")
                if isinstance(check.get("status"), str) and check["status"] != "pass":
                    issues.append("a stage can advance only when every independent review check is pass")

        blocking = review.get("blocking_findings")
        if isinstance(blocking, list) and blocking:
            issues.append("stage_review has blocking_findings; rollback or blocked_human is required")
    return issues


def _validate_stage_review(
    payload: Mapping[str, Any],
    state: Mapping[str, Any],
    stage_id: str,
    revision: str,
) -> None:
    """Require a context-bounded independent gate before any stage advance."""

    issues = _collect_stage_review_issues(payload, state, stage_id, revision)
    if issues:
        raise ProtocolError("; ".join(issues))


def _collect_task_spec_issues(payload: Mapping[str, Any]) -> list[str]:
    """Accumulate every task-spec field problem instead of stopping at the first."""

    issues: list[str] = []
    task_spec = payload.get("task_spec")
    if not isinstance(task_spec, Mapping):
        issues.append("stage 01 payload.task_spec must be an object")
        return issues
    semantic_map = task_spec.get("semantic_map")
    if not isinstance(semantic_map, Mapping):
        issues.append("task_spec.semantic_map must be an object")
    else:
        for role in ("background", "decision_object", "objective", "comparison_set", "constraints", "deliverable", "uncertainty"):
            if role not in semantic_map:
                issues.append(f"task_spec.semantic_map missing role: {role}")
    attribute_matrix = task_spec.get("attribute_matrix")
    if not isinstance(attribute_matrix, list) or not attribute_matrix:
        issues.append("task_spec.attribute_matrix must not be empty")
    else:
        for index, leaf in enumerate(attribute_matrix):
            if not isinstance(leaf, Mapping):
                issues.append(f"task_spec.attribute_matrix[{index}] must be an object")
                continue
            for key in ("concept", "role", "attribute", "disposition", "rationale"):
                value = leaf.get(key)
                if not isinstance(value, str) or not value.strip():
                    issues.append(f"task_spec.attribute_matrix[{index}].{key} must not be empty")
            if leaf.get("disposition") not in {"confirmed", "inferred", "ask_human", "assume", "research"}:
                issues.append(
                    f"task_spec.attribute_matrix[{index}].disposition must be confirmed, inferred, ask_human, assume or research"
                )
    for key in ("constraints", "assumptions", "open_questions", "scenarios", "success_criteria"):
        if not isinstance(task_spec.get(key), list):
            issues.append(f"task_spec.{key} must be an array")
    if not isinstance(task_spec.get("scenarios"), list) or not task_spec.get("scenarios"):
        issues.append("task_spec.scenarios must not be empty")
    audit = task_spec.get("requirements_audit")
    if not isinstance(audit, Mapping):
        issues.append("task_spec.requirements_audit must be an object")
    else:
        for key in ("card_id", "artifact_ref", "summary"):
            value = audit.get(key)
            if not isinstance(value, str) or not value.strip():
                issues.append(f"task_spec.requirements_audit.{key} must not be empty")
    return issues


def _validate_task_spec(payload: Mapping[str, Any]) -> None:
    issues = _collect_task_spec_issues(payload)
    if issues:
        raise ProtocolError("; ".join(issues))


def _has_content(value: Any) -> bool:
    return bool(value.strip()) if isinstance(value, str) else bool(value)


def _collect_plan_issues(payload: Mapping[str, Any]) -> list[str]:
    """Accumulate every plan field problem instead of stopping at the first."""

    issues: list[str] = []
    plan = payload.get("plan")
    if not isinstance(plan, Mapping):
        issues.append("stage 02 payload.plan must be an object")
        return issues
    raw_nodes = plan.get("nodes")
    if not isinstance(raw_nodes, list) or not raw_nodes:
        issues.append("plan.nodes must not be empty")
    else:
        for index, node in enumerate(raw_nodes):
            if not isinstance(node, Mapping):
                issues.append(f"plan.nodes[{index}] must be an object")
                continue
            for key in ("id", "title", "objective", "evidence_plan", "acceptance_criteria"):
                if not _has_content(node.get(key)):
                    issues.append(f"plan.nodes[{index}].{key} must not be empty")
    for key in ("decomposition_rationale", "coverage_proof", "risk_notes"):
        if not _has_content(plan.get(key)):
            issues.append(f"plan.{key} must not be empty")
    try:
        validate_plan(plan, strict=True)
    except DAGValidationError as exc:
        issues.append(f"stage 02 plan validation failed: {exc}")
    return issues


def _validate_plan_payload(payload: Mapping[str, Any]) -> None:
    issues = _collect_plan_issues(payload)
    if issues:
        raise ProtocolError("; ".join(issues))


def _collect_verification_issues(payload: Mapping[str, Any]) -> list[str]:
    """Accumulate every verification field problem instead of stopping at the first."""

    issues: list[str] = []
    verification = payload.get("verification")
    if not isinstance(verification, Mapping):
        issues.append("stage 04 payload.verification must be an object")
        return issues
    claims = verification.get("claim_ledger")
    if not isinstance(claims, list) or not claims:
        issues.append("verification.claim_ledger must not be empty")
    else:
        for index, claim in enumerate(claims):
            if not isinstance(claim, Mapping):
                issues.append(f"verification.claim_ledger[{index}] must be an object")
                continue
            for key in ("claim", "source_url", "source_type", "checked_by", "status"):
                value = claim.get(key)
                if not isinstance(value, str) or not value.strip():
                    issues.append(f"verification.claim_ledger[{index}].{key} must not be empty")
            if claim.get("status") not in {"verified", "rejected", "uncertain"}:
                issues.append(f"verification.claim_ledger[{index}].status is invalid")
    if not isinstance(verification.get("summary"), Mapping):
        issues.append("verification.summary must be an object")
    return issues


def _validate_verification_payload(payload: Mapping[str, Any]) -> None:
    issues = _collect_verification_issues(payload)
    if issues:
        raise ProtocolError("; ".join(issues))


def _collect_execution_issues(payload: Mapping[str, Any], state: Mapping[str, Any]) -> list[str]:
    """Accumulate every execution-summary field problem instead of stopping at the first."""

    issues: list[str] = []
    summary = payload.get("execution_summary")
    if not isinstance(summary, Mapping):
        issues.append("stage 03 payload.execution_summary must be an object")
        return issues
    completed_ids = summary.get("completed_task_ids")
    if not isinstance(completed_ids, list) or not completed_ids:
        issues.append("execution_summary.completed_task_ids must not be empty")
    else:
        for index, task_id in enumerate(completed_ids):
            if not isinstance(task_id, str) or not task_id.strip():
                issues.append(f"execution_summary.completed_task_ids[{index}] must not be empty")
    artifact_refs = summary.get("artifact_refs")
    if not isinstance(artifact_refs, list) or not artifact_refs:
        issues.append("execution_summary.artifact_refs must not be empty")
    else:
        for index, artifact_ref in enumerate(artifact_refs):
            if not isinstance(artifact_ref, str) or not artifact_ref.strip():
                issues.append(f"execution_summary.artifact_refs[{index}] must not be empty")
    if not isinstance(summary.get("unresolved_claims"), list):
        issues.append("execution_summary.unresolved_claims must be an array")

    plan = state.get("plan", {})
    nodes = plan.get("nodes", []) if isinstance(plan, Mapping) else []
    expected = {str(node.get("id", "")) for node in nodes if isinstance(node, Mapping)}
    if set(str(item) for item in completed_ids if isinstance(completed_ids, list)) != expected:
        issues.append("execution_summary.completed_task_ids must exactly cover the current DAG")
    return issues


def _validate_execution_summary(payload: Mapping[str, Any], state: Mapping[str, Any]) -> None:
    issues = _collect_execution_issues(payload, state)
    if issues:
        raise ProtocolError("; ".join(issues))


def _collect_decision_issues(payload: Mapping[str, Any]) -> list[str]:
    """Accumulate every decision field problem instead of stopping at the first."""

    issues: list[str] = []
    decision = payload.get("decision")
    if not isinstance(decision, Mapping):
        issues.append("stage 05 payload.decision must be an object")
        return issues
    for key in ("selected_option", "decision_rationale"):
        value = decision.get(key)
        if not isinstance(value, str) or not value.strip():
            issues.append(f"decision.{key} must not be empty")
    evidence_refs = decision.get("evidence_refs")
    if not isinstance(evidence_refs, list) or not evidence_refs:
        issues.append("decision.evidence_refs must not be empty")
    if not isinstance(decision.get("rejected_options"), list):
        issues.append("decision.rejected_options must be an array")
    if not isinstance(decision.get("risks"), list):
        issues.append("decision.risks must be an array")
    if not isinstance(decision.get("human_approval_needed"), bool):
        issues.append("decision.human_approval_needed must be boolean")
    return issues


def _validate_decision_payload(payload: Mapping[str, Any]) -> None:
    issues = _collect_decision_issues(payload)
    if issues:
        raise ProtocolError("; ".join(issues))


def _collect_handoff_issues(payload: Mapping[str, Any]) -> list[str]:
    """Accumulate every handoff field problem instead of stopping at the first."""

    issues: list[str] = []
    handoff = payload.get("handoff")
    if not isinstance(handoff, Mapping):
        issues.append("stage 06 payload.handoff must be an object")
        return issues
    deliverables = handoff.get("deliverables")
    if not isinstance(deliverables, list) or not deliverables:
        issues.append("handoff.deliverables must not be empty")
    decision_ref = handoff.get("decision_ref")
    if not isinstance(decision_ref, str) or not decision_ref.strip():
        issues.append("handoff.decision_ref must not be empty")
    for key in ("remaining_tasks", "blocked_human", "candidates"):
        if not isinstance(handoff.get(key), list):
            issues.append(f"handoff.{key} must be an array")
    resume_instruction = handoff.get("resume_instruction")
    if not isinstance(resume_instruction, str) or not resume_instruction.strip():
        issues.append("handoff.resume_instruction must not be empty")
    return issues


def _validate_handoff_payload(payload: Mapping[str, Any]) -> None:
    issues = _collect_handoff_issues(payload)
    if issues:
        raise ProtocolError("; ".join(issues))


def _collect_exploration_issues(payload: Mapping[str, Any]) -> list[str]:
    """Accumulate every exploration field problem instead of stopping at the first."""

    issues: list[str] = []
    exploration = payload.get("exploration")
    if not isinstance(exploration, Mapping):
        issues.append("exploration payload.exploration must be an object")
        return issues
    for key in ("preference_brief", "selection_mode"):
        value = exploration.get(key)
        if not isinstance(value, str) or not value.strip():
            issues.append(f"exploration.{key} must not be empty")
    if exploration.get("selection_mode") not in {"task_board", "candidate"}:
        issues.append("exploration.selection_mode must be task_board or candidate")
    scanned_sources = exploration.get("scanned_sources")
    if not isinstance(scanned_sources, list) or not scanned_sources:
        issues.append("exploration.scanned_sources must not be empty")
    else:
        for index, source in enumerate(scanned_sources):
            if not isinstance(source, str) or not source.strip():
                issues.append(f"exploration.scanned_sources[{index}] must not be empty")
    candidate_tasks = exploration.get("candidate_tasks")
    if not isinstance(candidate_tasks, list):
        issues.append("exploration.candidate_tasks must be an array")
    else:
        for index, candidate in enumerate(candidate_tasks):
            if not isinstance(candidate, Mapping):
                issues.append(f"exploration.candidate_tasks[{index}] must be an object")
                continue
            for key in ("title", "research_summary", "reason", "scope"):
                value = candidate.get(key)
                if not isinstance(value, str) or not value.strip():
                    issues.append(f"exploration.candidate_tasks[{index}].{key} must not be empty")
            if candidate.get("status", "candidate") != "candidate":
                issues.append("exploration candidate_tasks must be explicitly marked candidate")

    selected = exploration.get("selected_task")
    if not isinstance(selected, Mapping):
        issues.append("exploration.selected_task must be an object")
    else:
        for key in ("task_id", "title", "source_path", "priority", "reason"):
            value = selected.get(key)
            if not isinstance(value, str) or not value.strip():
                issues.append(f"exploration.selected_task.{key} must not be empty")
        source = str(selected.get("source", exploration.get("selection_mode")))
        if source != exploration.get("selection_mode"):
            issues.append("selected_task.source must match exploration.selection_mode")
        if exploration.get("selection_mode") == "task_board" and not str(selected.get("source_path", "")).startswith("tasks/"):
            issues.append("task_board selection must come from a project tasks/ path")
        if exploration.get("selection_mode") == "candidate" and selected.get("human_approved") is not True:
            issues.append("candidate task cannot be executed without human_approved=true")
    return issues


def _validate_exploration_payload(payload: Mapping[str, Any]) -> None:
    issues = _collect_exploration_issues(payload)
    if issues:
        raise ProtocolError("; ".join(issues))


def _collect_question_bundle_issues(payload: Mapping[str, Any]) -> list[str]:
    """Accumulate every question-bundle field problem instead of stopping at the first."""

    issues: list[str] = []
    questions = payload.get("questions")
    if not isinstance(questions, list) or not questions:
        issues.append("stage 01 blocked_human payload.questions must not be empty")
        return issues
    for index, question in enumerate(questions):
        if not isinstance(question, Mapping):
            issues.append(f"questions[{index}] must be an object")
            continue
        for key in ("question", "why_it_matters", "recommended_option"):
            value = question.get(key)
            if not isinstance(value, str) or not value.strip():
                issues.append(f"questions[{index}].{key} must not be empty")
    return issues


def _validate_question_bundle(payload: Mapping[str, Any]) -> None:
    issues = _collect_question_bundle_issues(payload)
    if issues:
        raise ProtocolError("; ".join(issues))


def _collect_clarify_issues(
    payload: Mapping[str, Any], state: Mapping[str, Any], revision: str
) -> list[str]:
    """Accumulate every clarify field problem instead of stopping at the first."""

    issues: list[str] = []
    issues.extend(_collect_stage_cards_issues(state, "01", revision))
    # A clarify may omit task_spec entirely: the runtime bumps the revision and
    # recreates pending builder cards, and the subagents refill the spec (<=3
    # fields each). This keeps the Commander from emitting one giant inline
    # task_spec that overflows a small local model's context window.
    if "task_spec" in payload:
        issues.extend(_collect_task_spec_issues(payload))
    repair = payload.get("repair")
    if not isinstance(repair, Mapping):
        issues.append("stage 01 clarify payload.repair must be an object")
        return issues
    for key in ("auditor_card_id", "auditor_verdict", "reason"):
        value = repair.get(key)
        if not isinstance(value, str) or not value.strip():
            issues.append(f"clarify.repair.{key} must not be empty")
    # audit_artifact_ref is optional: if the Commander omits it, apply_action
    # derives the latest gate receipt for the auditor card automatically. This
    # keeps a small local model from having to guess an opaque artifact path
    # (which previously caused every clarify to be rejected -> repair budget
    # exhaustion).
    if isinstance(repair.get("auditor_verdict"), str) and repair["auditor_verdict"] != "rollback":
        issues.append("clarify.repair.auditor_verdict must be rollback")
    card_id = repair.get("auditor_card_id")
    cards = state.get("subagent_cards", {})
    card = cards.get(card_id) if isinstance(cards, Mapping) and isinstance(card_id, str) else None
    if not isinstance(card, Mapping):
        issues.append("clarify.repair.auditor_card_id does not identify a task card")
    else:
        if not card.get("is_stage_gate") or str(card.get("stage_id")) != "01" or str(card.get("revision")) != revision:
            issues.append("clarify repair auditor must be the completed stage-01 gate for the current revision")
        if card.get("status") != "completed":
            issues.append("clarify repair auditor card is not completed")
    return issues


def _validate_clarify_payload(payload: Mapping[str, Any], state: Mapping[str, Any], revision: str) -> None:
    """Validate the non-advancing stage-01 repair/write-back action.

    A rollback receipt alone is not useful to the runtime: the Commander must
    convert it into a complete, machine-checkable task_spec.  The clarify
    action stores that package under a new revision and regenerates the auditor
    card; it never bypasses the auditor or stage-01 gate.
    """

    issues = _collect_clarify_issues(payload, state, revision)
    if issues:
        raise ProtocolError("; ".join(issues))


def _collect_field_gate_issues(state: Mapping[str, Any], payload: Mapping[str, Any]) -> list[str]:
    """Lightweight, field-centric gate used by the D1-ralph-field-centric redesign.

    Validates only that every *required* field has a non-pending disposition and
    that research fields carry evidence. It intentionally does NOT require the
    heavy ``stage_review`` / ``reviewer_card_id`` / full ``task_spec`` shape, so a
    normal agent can advance incrementally (fill some fields, get told which are
    still missing) instead of being rejected for an all-or-nothing result.

    Disabled unless ``RALPH_FIELD_GATE`` is set, so default protocol behaviour and
    existing tests are untouched.
    """
    import os
    if not field_mode_enabled():
        return []
    issues: list[str] = []
    stage = state.get("stage", {}) if isinstance(state.get("stage"), Mapping) else {}
    if str(stage.get("id", "")) == "exploration":
        # Exploration is a queue/choice node, not an attribute-matrix node.
        # Requiring a synthetic task_spec here would make the tail node
        # impossible to use after the field-centric migration.
        return _collect_exploration_issues(payload if isinstance(payload, Mapping) else {})
    # In field mode the agent proposes a new matrix via the payload; prefer it
    # over the (possibly stale) persisted state so the gate validates what the
    # agent is actually submitting this turn.
    if field_mode_enabled() and isinstance(payload.get("task_spec"), Mapping):
        spec = payload.get("task_spec")
    else:
        spec = state.get("task_spec") if isinstance(state.get("task_spec"), Mapping) else (
            payload.get("task_spec") if isinstance(payload.get("task_spec"), Mapping) else None
        )
    matrix = spec.get("attribute_matrix") if isinstance(spec, Mapping) else None
    if not isinstance(matrix, list) or not matrix:
        issues.append("task_spec.attribute_matrix 为空：本阶段尚无字段可校验（先按契约填字段）")
        return issues
    from .state import field_completeness
    # ``required_outputs`` are part of the current node contract, not an
    # optional decoration.  Keep this check here (as well as in
    # ``ralph field-apply``) so a complete-looking field table cannot silently
    # jump over an output such as ``research_findings``, ``cross_validation``
    # or ``task_graph``.  The output may be supplied incrementally as a field
    # whose concept/role/attribute matches the contract name.
    required_outputs = stage.get("required_outputs", []) if isinstance(stage, Mapping) else []
    verdict = field_completeness(matrix, required_outputs)
    if verdict["splittable"]:
        issues.append(
            "以下维度还可继续分解（用逗号分隔的子维度仍可拆成独立字段，补上即可）："
            + "，".join(verdict["splittable"])
        )
    if verdict["researching"]:
        issues.append(
            "以下字段仍需调研（派单字段调研 subagent 带回 evidence_refs 即可）："
            + "，".join(verdict["researching"])
        )
    if verdict["pending"]:
        issues.append(
            "以下字段尚未标注 disposition（confirmed/assumed_default/research_required）："
            + "，".join(verdict["pending"])
        )
    if verdict["required_outputs"]:
        issues.append(
            "本阶段仍缺少 required_outputs（可增量添加 concept/role/attribute 同名字段）："
            + "，".join(verdict["required_outputs"])
        )
    stage_id = str(stage.get("id", ""))
    # Completion of a *field table* never proves that the research happened,
    # the web sources are claim-level, or a DAG was actually executed.  Keep
    # these independent gates after field_completeness rather than returning
    # early, which was the route that let the GPU test formally pass 01→04.5.
    # A closed-world flow-only E2E deliberately proves orchestration with
    # inferred local inputs; it must not manufacture web citations or
    # claim-level external validation records merely to satisfy production
    # research gates.  Keep the structural DAG execution gate below active in
    # both modes, so this exception cannot turn the test into a trivial pass.
    if not flow_only_mode(state):
        issues.extend(_external_evidence_issues(matrix, stage_id))
        issues.extend(_cross_validation_issues(matrix, stage_id))
    if stage_id == "03":
        issues.extend(_execution_gate_issues(state))
    if issues:
        issues.append("分解完全后可运行 `ralph advance` 或输出 <RALPH_STAGE_RESULT> advance 进入下一阶段。")
    return issues

def collect_validation_issues(
    action: ActionResult,
    state: Mapping[str, Any],
    *,
    enforce_contracts: bool = True,
) -> list[str]:
    """Return every protocol problem for ``action`` instead of raising on the first.

    Used by the fill-in workflow (``ralph validate --result``) so the model can
    fix all field gaps in one pass, and by the Stop hook to surface all
    problems at once.  ``validate_action`` keeps the original raise-on-first
    behaviour by wrapping this.
    """

    issues: list[str] = []
    stage = state.get("stage", {})
    current_stage = str(stage.get("id", ""))
    if action.stage_id != current_stage:
        issues.append(f"action stage {action.stage_id!r} does not match current stage {current_stage!r}")
        return issues
    if not re.fullmatch(r"r\d+", action.revision):
        issues.append("revision must use r<number>, for example r1")
        return issues
    if action.action == "advance" and not action.next_stage:
        issues.append("advance requires next_stage")
    if enforce_contracts and action.action == "advance" and current_stage == "exploration" and action.next_stage != "01":
        issues.append("exploration can advance only by selecting a next task and returning to stage 01")
    if enforce_contracts and action.action == "advance" and current_stage == "06" and action.next_stage != "exploration":
        issues.append("stage 06 must enter exploration before another task can be selected")
    if action.action == "rollback" and not action.rollback_to:
        issues.append("rollback requires rollback_to")
    if action.action == "skip_blocked" and not action.next_stage:
        issues.append("skip_blocked requires next_stage")
    if action.action == "clarify":
        if current_stage != "01":
            issues.append("clarify is only available in stage 01")
        if action.next_stage is not None:
            issues.append("clarify must not specify next_stage")
        current_revision = str(stage.get("revision", "r1"))
        if action.revision not in {current_revision, _next_revision(current_revision)}:
            issues.append(
                f"clarify revision must be {current_revision} or its next revision "
                f"{_next_revision(current_revision)}"
            )
    if action.action == "candidate":
        required_candidate_fields = {"title", "research_summary", "reason", "scope"}
        if action.payload is None or not required_candidate_fields.issubset(action.payload):
            issues.append("candidate requires title, research_summary, reason and scope")
        else:
            for key in required_candidate_fields:
                value = action.payload[key]
                if not isinstance(value, str) or not value.strip():
                    issues.append(f"candidate field {key} must be a non-empty string")
        if current_stage == "exploration":
            preference_brief = action.payload.get("preference_brief") if isinstance(action.payload, Mapping) else None
            if not isinstance(preference_brief, str) or not preference_brief.strip():
                issues.append("candidate.preference_brief must be a non-empty string")
            scanned_sources = action.payload.get("scanned_sources") if isinstance(action.payload, Mapping) else None
            if not isinstance(scanned_sources, list) or not scanned_sources:
                issues.append("candidate.scanned_sources must not be empty")
            else:
                for index, source in enumerate(scanned_sources):
                    if not isinstance(source, str) or not source.strip():
                        issues.append(f"candidate.scanned_sources[{index}] must not be empty")
    if not enforce_contracts:
        return issues
    if action.action == "blocked_human" and current_stage == "01":
        issues.extend(
            _collect_question_bundle_issues(action.payload if isinstance(action.payload, Mapping) else {})
        )
    if action.action == "clarify":
        issues.extend(
            _collect_clarify_issues(
                action.payload if isinstance(action.payload, Mapping) else {},
                state,
                str(stage.get("revision", "r1")),
            )
        )
        return issues
    if action.action != "advance":
        return issues
    if field_mode_enabled():
        # Field-centric mode: the field gate is the only gate.  It validates
        # that every required field is dispositioned (no pending / no
        # research_required-without-evidence) and, on success, skips the heavy
        # stage_review / task_spec shape checks that a small local model cannot
        # reliably produce.
        payload_fg = action.payload if isinstance(action.payload, Mapping) else {}
        fg_issues = _collect_field_gate_issues(state, payload_fg)
        if fg_issues:
            issues.extend(fg_issues)
            return issues
        # field gate passed: skip the heavy stage_review / task_spec shape checks
        return issues
    if current_stage not in {"01", "02", "03", "04", "05", "06", "exploration"}:
        return issues
    issues.extend(_collect_stage_cards_issues(state, current_stage, action.revision))
    payload = action.payload
    if not isinstance(payload, Mapping):
        issues.append(f"stage {current_stage} advance payload must be an object")
        return issues
    issues.extend(_collect_stage_review_issues(payload, state, current_stage, action.revision))
    if current_stage == "01":
        # The Commander/auditor must not inline the entire task_spec (it
        # overflows a small local model's context window).  The assembled
        # spec already lives in state["task_spec"] (written by builders +
        # reconcile_partial_merges), so validate that when the payload omits
        # an inline copy.  This mirrors the clarify path's no-inline design.
        inline_spec = payload.get("task_spec") if isinstance(payload.get("task_spec"), Mapping) else None
        spec = inline_spec or state.get("task_spec")
        if not isinstance(spec, Mapping):
            issues.append("stage 01 task_spec is missing (neither in payload nor assembled state)")
        else:
            issues.extend(_collect_task_spec_issues({"task_spec": spec}))
    elif current_stage == "02":
        issues.extend(_collect_plan_issues(payload))
    elif current_stage == "03":
        plan = state.get("plan", {})
        nodes = plan.get("nodes", []) if isinstance(plan, Mapping) else []
        completed = set(plan.get("completed", []) if isinstance(plan, Mapping) else [])
        pending = [str(node.get("id", "?")) for node in nodes if isinstance(node, Mapping) and node.get("id") not in completed]
        if pending:
            issues.append("stage 03 still has unfinished DAG tasks: " + ", ".join(pending))
        issues.extend(_collect_execution_issues(payload, state))
    elif current_stage == "04":
        issues.extend(_collect_verification_issues(payload))
    elif current_stage == "05":
        issues.extend(_collect_decision_issues(payload))
    elif current_stage == "06":
        issues.extend(_collect_handoff_issues(payload))
    elif current_stage == "exploration":
        issues.extend(_collect_exploration_issues(payload))
    return issues


def validate_action(
    action: ActionResult,
    state: Mapping[str, Any],
    *,
    enforce_contracts: bool = True,
) -> None:
    issues = collect_validation_issues(action, state, enforce_contracts=enforce_contracts)
    if issues:
        raise ProtocolError("; ".join(issues))


def canonical_json(action: ActionResult) -> str:
    return json.dumps(action.to_dict(), ensure_ascii=False, sort_keys=True, separators=(",", ":"))
