"""Declarative prompt nodes used by the first RALPH runtime."""

from __future__ import annotations

from dataclasses import asdict, dataclass
from typing import Any, Iterable, Mapping


@dataclass(frozen=True)
class LoopNode:
    id: str
    name: str
    input_description: str
    required_outputs: tuple[str, ...]
    success_condition: str
    failure_condition: str
    on_success: str | None
    on_failure: str | None
    on_human_block: str | None

    def to_dict(self) -> dict[str, Any]:
        result = asdict(self)
        result["required_outputs"] = list(self.required_outputs)
        return result


class NodeGraph:
    def __init__(self, nodes: Iterable[LoopNode]):
        self._nodes = {node.id: node for node in nodes}
        if not self._nodes:
            raise ValueError("node graph cannot be empty")

    def get(self, node_id: str) -> LoopNode:
        try:
            return self._nodes[node_id]
        except KeyError as exc:
            raise KeyError(f"unknown RALPH node: {node_id}") from exc

    def __contains__(self, node_id: str) -> bool:
        return node_id in self._nodes

    def ids(self) -> tuple[str, ...]:
        return tuple(self._nodes)

    def as_dict(self) -> dict[str, dict[str, Any]]:
        return {node_id: node.to_dict() for node_id, node in self._nodes.items()}

    @classmethod
    def from_mapping(cls, mapping: Mapping[str, Mapping[str, Any]]) -> "NodeGraph":
        nodes = []
        for node_id, raw in mapping.items():
            nodes.append(
                LoopNode(
                    id=node_id,
                    name=str(raw.get("name", node_id)),
                    input_description=str(raw.get("input_description", "")),
                    required_outputs=tuple(raw.get("required_outputs", ())),
                    success_condition=str(raw.get("success_condition", "")),
                    failure_condition=str(raw.get("failure_condition", "")),
                    on_success=raw.get("on_success"),
                    on_failure=raw.get("on_failure"),
                    on_human_block=raw.get("on_human_block"),
                )
            )
        return cls(nodes)


DEFAULT_GRAPH = NodeGraph(
    [
        LoopNode(
            "01", "目标与背景分解", "只填 3 个字段：目标因素(goal)、已知因素(known，含假设/默认推断偏好)、未知因素(unknown)；目标须包含后两者，已知与未知词语不重叠",
            ("goal", "known", "unknown"),
            "仅填 goal/known/unknown 三字段，goal⊇known 且 goal⊇unknown，known 与 unknown 词语无重叠，无 pending", "三字段未填齐或后两者重叠/目标未包含",
            "02", "01", "exploration"
        ),
        LoopNode(
            "02", "未知信息调研", "目标 + 已知背景 = 已知与目标的差额；针对该差额派窄调研 subagent 直接搜索（关键词不加年份，获取最新结果）",
            ("research_findings",),
            "所有 research_required 字段已调研带回 evidence_refs，无未带证据的调研字段",
            "存在未调研或证据不足的 research_required 字段", "02.5", "02", "exploration"
        ),
        LoopNode(
            "02.5", "调研后交叉验证", "02 的调研结果与字段；逐字段派 subagent 去问多种网页 LLM + 权威数据，检查矛盾",
            ("cross_validation",),
            "每个关键调研字段有逐 claim validation_records（≥2 独立具体来源、日期、裁决），矛盾已记录并更新 confidence", "核验不足或矛盾未处置",
            "03", "02", "exploration"
        ),
        LoopNode(
            "03", "执行任务分解", "已调研、已交叉验证的字段；把任务分解到最小执行单元，模块间接口清晰对准、解耦",
            ("task_graph", "coverage_proof"),
            "结构化任务图分解到最小执行单元且所有节点已写出 declared artifacts 并经 graph-apply 回写，接口清晰对准、模块化解耦，无遗漏无冲突",
            "分解不完整、接口未对齐或耦合不清", "04", "02.5", "exploration"
        ),
        LoopNode(
            "04", "验证与交叉验证", "执行产物和验证证据", ("verification_report",),
            "验证通过且证据充分", "发现问题或证据不足", "04.5", "03", "exploration"
        ),
        LoopNode(
            "04.5", "产出后交叉验证", "04 的 claim ledger 与结论", ("cross_validation_out",),
            "每条关键 claim 有逐 claim validation_records（≥2 独立具体来源、日期、裁决），矛盾已记录", "核验不足或矛盾未处置", "exploration", "04", "exploration"
        ),
        LoopNode(
            "05", "决策", "验证报告和候选方案", ("decision",),
            "决策条件满足", "需要重新分解或补充证据", "06", "02", "exploration"
        ),
        LoopNode(
            "06", "交接与队列", "最终产物和决策", ("handoff",),
            "已交接并完成队列扫描", "交接或队列状态不完整", "exploration", "06", "exploration"
        ),
        LoopNode(
            "exploration", "探索与任务接续", "全局偏好、项目 tasks/ 和当前队列", ("preference_brief", "candidate_tasks"),
            "已扫描任务板并选定可执行任务，或已输出带 candidate 标记的新目标", "探索输入不足", "01", "exploration", "exploration"
        ),
        LoopNode(
            "completed", "完成", "已验证交接结果", (), "任务已完成", "不可回滚", None, None, None
        ),
    ]
)
