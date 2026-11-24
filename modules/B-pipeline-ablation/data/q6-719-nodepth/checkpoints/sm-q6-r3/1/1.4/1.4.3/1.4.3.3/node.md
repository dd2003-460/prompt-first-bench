# N238: 混合分布函数 F_mix(x) 的解析表达式为 F_mix(x) = P_core * F_core(x) + P_tail * F_tail(x)，其中 F_

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N62, N63, N68

## Claim

混合分布函数 F_mix(x) 的解析表达式为 F_mix(x) = P_core * F_core(x) + P_tail * F_tail(x)，其中 F_core 和 F_tail 分别为核心和长尾区域的延迟累积分布函数，P_tail = 1 - P_core。

## Corrected Claim

混合分布函数 F_mix(x) 的解析表达式为 F_mix(x) = P_core * F_core(x) + P_tail * F_tail(x)，其中 F_core 和 F_tail 分别为核心和长尾区域的延迟累积分布函数，P_tail = 1 - P_core。

## Evidence

先验知识/题面给定，逻辑校验通过：混合分布函数定义为各分量分布的加权平均，权重之和为1，符合概率论基本定义。
