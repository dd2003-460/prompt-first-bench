# N47: T_LRU 的计算公式：T_LRU = C / (Σ_{i=1}^{k_eff} λ_i * S_i)，其中 k_eff 是满足 Σ_{i=1}^{k_eff}

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N16, N17, N18

## Claim

T_LRU 的计算公式：T_LRU = C / (Σ_{i=1}^{k_eff} λ_i * S_i)，其中 k_eff 是满足 Σ_{i=1}^{k_eff} S_i <= C 的最大对象数，λ_i 是对象 i 的请求速率（次/天），S_i 是对象 i 的大小（bytes）。

## Corrected Claim

T_LRU 的计算公式：T_LRU = C / (Σ_{i=1}^{k_eff} λ_i * S_i)，其中 k_eff 是满足 Σ_{i=1}^{k_eff} S_i <= C 的最大对象数，λ_i 是对象 i 的请求速率（次/天），S_i 是对象 i 的大小（bytes）。

## Evidence

先验知识/题面给定，逻辑校验通过
