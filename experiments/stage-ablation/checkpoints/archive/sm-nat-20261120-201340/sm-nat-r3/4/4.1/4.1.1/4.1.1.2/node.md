# N118: P_stale 的分对象计算：对于请求率为 r_i 的对象，其平均等待时间 T_wait_i = 1/r_i。该对象在下次请求前过期的概率 P_stale_i 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N53

## Claim

P_stale 的分对象计算：对于请求率为 r_i 的对象，其平均等待时间 T_wait_i = 1/r_i。该对象在下次请求前过期的概率 P_stale_i = 1 - exp(-λ * T_wait_i) = 1 - exp(-0.01 / r_i)。整体 P_stale 是所有对象按请求频率加权平均：P_stale_total = Σ (r_i * s_i * P_stale_i) / Σ (r_i * s_i)。

## Corrected Claim

P_stale 的分对象计算：对于请求率为 r_i 的对象，其平均等待时间 T_wait_i = 1/r_i。该对象在下次请求前过期的概率 P_stale_i = 1 - exp(-λ * T_wait_i) = 1 - exp(-0.01 / r_i)。整体 P_stale 是所有对象按请求频率加权平均：P_stale_total = Σ (r_i * s_i * P_stale_i) / Σ (r_i * s_i)。

## Evidence

先验知识/题面给定，逻辑校验通过：平均等待时间 1/r_i 符合泊松过程性质，指数衰减公式 1-exp(-λt) 符合指数分布生存函数，加权平均逻辑自洽。
