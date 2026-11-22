# N54: Pareto(α=1.1) 分布下 Top K% 对象占据的总字节数占比公式：B_top_K% = [∫_{S_K}^{S_max} s * f(s) ds] 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N15

## Claim

Pareto(α=1.1) 分布下 Top K% 对象占据的总字节数占比公式：B_top_K% = [∫_{S_K}^{S_max} s * f(s) ds] / [∫_{S_min}^{S_max} s * f(s) ds]，其中 S_K 为 Top K% 对象的阈值大小，需通过数值积分计算具体占比

## Corrected Claim

Pareto(α=1.1) 分布下 Top K% 对象占据的总字节数占比公式：B_top_K% = [∫_{S_K}^{S_max} s * f(s) ds] / [∫_{S_min}^{S_max} s * f(s) ds]，其中 S_K 为 Top K% 对象的阈值大小，需通过数值积分计算具体占比

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

Pareto distribution byte share top percentage heavy tail
