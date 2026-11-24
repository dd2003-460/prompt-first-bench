# N22: Pareto 前沿点 1（高性能低延迟）：策略为'核心区域自建+长尾公有云'，目标 P99 延迟 ≤ 50ms。成本构成：自建10个POP覆盖Top 80%流量

- **status**: pending
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N5

## Claim

Pareto 前沿点 1（高性能低延迟）：策略为'核心区域自建+长尾公有云'，目标 P99 延迟 ≤ 50ms。成本构成：自建10个POP覆盖Top 80%流量，剩余20%走公有云。量化：自建固定成本分摊 + 公有云按量计费。此点代表延迟最优但成本较高的工作点。

## Corrected Claim

Pareto 前沿点 1（高性能低延迟）：策略为'核心区域自建+长尾公有云'，目标 P99 延迟 ≤ 50ms。成本构成：自建10个POP覆盖Top 80%流量，剩余20%走公有云。量化：自建固定成本分摊 + 公有云按量计费。此点代表延迟最优但成本较高的工作点。

## Evidence

父节点级核验未通过：不完备, 有冗余（子节点1和2存在冗余，它们本质上是同一个总流量参数（2TB）在不同策略分量下的线性分解，可合并为一个“流量分配”节点或作为参数化处理。此外，父节点明确提到“量化：自建固定成本分摊”，但子节点3仅列出成本项名称，未提供具体的计算逻辑或数值示例（如摊销周期、单价），导致“完备性”不足，未能完全覆盖父节点中“量化”这一关键要求。）

## Search Query

hybrid CDN strategy P99 latency 50ms cost tradeoff self-hosted core public cloud tail
