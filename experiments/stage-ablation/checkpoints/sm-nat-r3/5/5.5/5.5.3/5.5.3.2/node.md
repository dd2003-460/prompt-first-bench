# N257: 混合更新工作点下，对象 i 的失效概率 P_invalid(i) = 1 - exp(-λ_i * T_res(i))，其中 T_res(i) 为对象 i 在 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N90

## Claim

混合更新工作点下，对象 i 的失效概率 P_invalid(i) = 1 - exp(-λ_i * T_res(i))，其中 T_res(i) 为对象 i 在 LRU 中的驻留时间，需基于 LRU 队列位置 k=i 计算 T_res(i) = 1 / (Σ_{j>i} λ_j)，并代入 λ_i 得到具体概率值。

## Corrected Claim

混合更新工作点下，对象 i 的失效概率 P_invalid(i) = 1 - exp(-λ_i * T_res(i))，其中 T_res(i) 为对象 i 在 LRU 中的驻留时间，需基于 LRU 队列位置 k=i 计算 T_res(i) = 1 / (Σ_{j>i} λ_j)，并代入 λ_i 得到具体概率值。

## Evidence

先验知识/题面给定，逻辑校验通过：LRU 驻留时间公式 T_res(i) = 1 / (Σ_{j>i} λ_j) 符合排队论中 M/M/1 或类似模型中等待时间的倒数逻辑（假设 λ_j 为访问率，总和为离开率），失效概率公式 P = 1 - exp(-λT) 符合指数分布生存函数逻辑，量纲与逻辑自洽。
