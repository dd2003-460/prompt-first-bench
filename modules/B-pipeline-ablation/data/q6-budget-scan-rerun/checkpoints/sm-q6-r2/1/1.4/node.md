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

父节点级核验未通过：非正交（子节点1（尾部修正因子）与子节点2、3存在逻辑矛盾和重复。子节点1指出P99由最慢区域决定（max逻辑），并给出了260ms的结论；而子节点2和3分别计算了核心区和长尾区的P99（65-80ms和160-175ms），这些数据直接用于验证或反驳子节点1的结论。更严重的是，子节点1假设P99_tail=250ms，而子节点3计算出的P99_tail仅为160-175ms，两者数据冲突，导致分解内部不一致。）

## Search Query

Hybrid CDN strategy P99 latency weighted average core region self-hosted long-tail public cloud
