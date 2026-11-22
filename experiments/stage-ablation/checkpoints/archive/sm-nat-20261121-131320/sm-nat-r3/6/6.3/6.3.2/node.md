# N128: LRU 稳态字节命中率 H_LRU 的下界积分表达式为 H_LRU_lower = (Σ_{i=1}^{K_max} f_i * S_i) / Total_By

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N50

## Claim

LRU 稳态字节命中率 H_LRU 的下界积分表达式为 H_LRU_lower = (Σ_{i=1}^{K_max} f_i * S_i) / Total_Bytes，其中 K_max 是满足 Σ_{j=1}^{K_max} S_j ≤ C 的最大整数；该下界假设 LRU 能完美锁定头部 K_max 个对象，忽略抖动惩罚，是 H_LRU 的理论最低值。

## Corrected Claim

LRU 稳态字节命中率 H_LRU 的下界积分表达式为 H_LRU_lower = (Σ_{i=1}^{K_max} f_i * S_i) / Total_Bytes，其中 K_max 是满足 Σ_{j=1}^{K_max} S_j ≤ C 的最大整数；该下界假设 LRU 能完美锁定头部 K_max 个对象，忽略抖动惩罚，是 H_LRU 的理论最低值。

## Evidence

先验知识/题面给定，逻辑校验通过
