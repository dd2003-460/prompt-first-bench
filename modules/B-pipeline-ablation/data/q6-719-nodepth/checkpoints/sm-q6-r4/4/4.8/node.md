# N32: 混合策略的P99延迟为加权最大值：P99_mix = max(P99_core, P99_tail)，其中P99_core对应自建POP区域，P99_tail对

- **status**: pending
- **level**: L2
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N4

## Claim

混合策略的P99延迟为加权最大值：P99_mix = max(P99_core, P99_tail)，其中P99_core对应自建POP区域，P99_tail对应公有云CDN区域，权重由流量占比 P_core 和 (1-P_core) 决定。

## Corrected Claim

混合策略的P99延迟通常介于 P99_core 和 P99_tail 之间，具体数值取决于流量占比及两个区域延迟分布的具体形态，不能简单等同于加权最大值。

## Evidence

父节点级核验未通过：非正交（子节点之间存在严重的逻辑矛盾。父节点明确定义 P99_mix 为“加权最大值”（即 max(P99_core, P99_tail)），而子节点4却声称 P99_mix “不是简单的加权最大值”，并给出了基于混合分布函数的分位数计算公式。这两者在数学定义和计算逻辑上是互斥的，导致分解结果自相矛盾。）
