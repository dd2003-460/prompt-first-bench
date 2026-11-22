# N141: 分母项 E[1/S] 在 Pareto(α=1.1, x_min=1KB) 分布下的解析解：E[1/S] = (α-1) * x_min^(-α+1) / (α

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N54

## Claim

分母项 E[1/S] 在 Pareto(α=1.1, x_min=1KB) 分布下的解析解：E[1/S] = (α-1) * x_min^(-α+1) / (α-2) 若 α>2 则收敛，但 α=1.1<2 导致 E[1/S] 发散，因此必须引入截断上限 S_max（如 100MB）进行正则化计算，具体数值为 ∫_{x_min}^{S_max} (1/s) * f_Pareto(s) ds。

## Corrected Claim

分母项 E[1/S] 在 Pareto(α=1.1, x_min=1KB) 分布下的解析解：E[1/S] = (α-1) * x_min^(-α+1) / (α-2) 若 α>2 则收敛，但 α=1.1<2 导致 E[1/S] 发散，因此必须引入截断上限 S_max（如 100MB）进行正则化计算，具体数值为 ∫_{x_min}^{S_max} (1/s) * f_Pareto(s) ds。

## Evidence

先验知识/题面给定，逻辑校验通过：Pareto分布的矩收敛条件及截断积分定义符合数学原理
