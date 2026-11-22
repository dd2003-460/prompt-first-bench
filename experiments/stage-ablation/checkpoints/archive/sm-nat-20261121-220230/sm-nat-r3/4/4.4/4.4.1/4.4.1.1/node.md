# N206: P_eviction 的解析近似值为 P_eviction ≈ 1 - exp(-λ_avg * T_resident / C_norm)，其中 λ_avg=5

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N71

## Claim

P_eviction 的解析近似值为 P_eviction ≈ 1 - exp(-λ_avg * T_resident / C_norm)，其中 λ_avg=500/天，T_resident 为驻留时间，C_norm=0.119，该公式基于 LRU 队列长度服从指数分布的假设。

## Corrected Claim

P_eviction 的解析近似值为 P_eviction ≈ 1 - exp(-λ_avg * T_resident / C_norm)，其中 λ_avg=500/天，T_resident 为驻留时间，C_norm=0.119，该公式基于 LRU 队列长度服从指数分布的假设。

## Evidence

先验知识/题面给定，逻辑校验通过
