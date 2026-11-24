# N9: 混合策略（核心区域自建+长尾走公有云）的 P99 延迟基准值约为 180ms（核心区域低延迟 100ms 与长尾公有云 250ms 的加权平均，权重取决于流量分

- **status**: pending
- **level**: L2
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N1

## Claim

混合策略（核心区域自建+长尾走公有云）的 P99 延迟基准值约为 180ms（核心区域低延迟 100ms 与长尾公有云 250ms 的加权平均，权重取决于流量分布，假设核心区域占 60% 流量）

## Corrected Claim

混合策略的 P99 延迟主要受长尾公有云路径影响，预计接近或高于 250ms，而非核心与长尾延迟的加权平均值。

## Evidence

父节点级核验未通过：非正交, 有冗余（1. 非正交性：子节点1（TPF修正）直接基于子节点2和3推导出的P99值进行计算，存在逻辑依赖而非独立分解；且子节点1的结论（260ms）与父节点陈述（180ms）直接矛盾，未作为‘修正’而是作为‘否定’存在，破坏了分解的一致性。2. 冗余性：子节点2和3结构高度相似（均为RTT+处理+排队/回源），且包含大量假设参数（如具体RTT值、负载率、命中率），这些本质上是同一类‘延迟构成模型’在不同区域的参数实例化，可合并为一个通用公式节点，参数化区分核心/长尾。）

## Search Query

Hybrid CDN strategy P99 latency weighted average core region self-hosted long-tail public cloud
