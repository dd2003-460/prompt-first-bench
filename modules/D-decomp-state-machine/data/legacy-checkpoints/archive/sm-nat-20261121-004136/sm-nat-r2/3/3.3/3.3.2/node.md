# N49: 对象平均更新间隔 T_update 的计算：基于更新率 λ_update = 1%/day。假设更新是泊松过程，则单个对象的平均更新间隔 T_update = 

- **status**: verified
- **level**: L3
- **source**: given
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N14

## Claim

对象平均更新间隔 T_update 的计算：基于更新率 λ_update = 1%/day。假设更新是泊松过程，则单个对象的平均更新间隔 T_update = 1 / λ_update = 100 天。此值直接代入 A_decay = exp(-λ * T_update) 计算衰减因子。

## Corrected Claim

对象平均更新间隔 T_update 的计算：基于更新率 λ_update = 1%/day。假设更新是泊松过程，则单个对象的平均更新间隔 T_update = 1 / λ_update = 100 天。此值直接代入 A_decay = exp(-λ * T_update) 计算衰减因子。

## Evidence

先验知识/题面给定，逻辑校验通过：泊松过程平均间隔为速率倒数，1/(0.01/day)=100天，量纲与数值均正确。

## Search Query

poisson process mean interarrival time update rate
