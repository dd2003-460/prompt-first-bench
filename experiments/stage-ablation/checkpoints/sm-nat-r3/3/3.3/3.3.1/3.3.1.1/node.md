# N185: β→0 时头部对象请求概率 P_head 的极限行为：当 β→0 时，Pareto 分布趋近于均匀分布，P_head 趋近于 k/N，需计算此时 LFU 保留头

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N64

## Claim

β→0 时头部对象请求概率 P_head 的极限行为：当 β→0 时，Pareto 分布趋近于均匀分布，P_head 趋近于 k/N，需计算此时 LFU 保留头部对象的能力与 LRU 的对比，量化 ΔH_max 的理论上限。

## Corrected Claim

β→0 时头部对象请求概率 P_head 的极限行为：当 β→0 时，Pareto 分布趋近于均匀分布，P_head 趋近于 k/N，需计算此时 LFU 保留头部对象的能力与 LRU 的对比，量化 ΔH_max 的理论上限。

## Evidence

先验知识/题面给定，逻辑校验通过：Pareto分布（Zipf-like）在指数β趋近于0时确实退化为均匀分布，此时头部对象概率P_head趋近于k/N，符合概率论基本性质。
