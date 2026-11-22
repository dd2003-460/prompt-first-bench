# N6: LRU 稳态字节命中率下界 H_LRU ≈ 1 - (1 - F_req(N_cap)) * (S_mean_cached / S_mean_total)，其中

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N1, N2, N3

## Claim

LRU 稳态字节命中率下界 H_LRU ≈ 1 - (1 - F_req(N_cap)) * (S_mean_cached / S_mean_total)，其中 F_req 是热度 Pareto(β=0.9) 的 CDF，N_cap 是缓存对象数

## Corrected Claim

LRU 稳态字节命中率下界 H_LRU ≈ 1 - (1 - F_req(N_cap)) * (S_mean_cached / S_mean_total)，其中 F_req 是热度 Pareto(β=0.9) 的 CDF，N_cap 是缓存对象数

## Evidence

先验知识/题面给定，逻辑校验通过
