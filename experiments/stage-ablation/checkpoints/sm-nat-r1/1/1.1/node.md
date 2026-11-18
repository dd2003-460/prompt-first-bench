# N5: LRU稳态字节命中率下界公式：H_LRU ≈ (1 - C_eff / S_total) * (1 - 1/β)，其中C_eff为有效缓存容量，S_total为

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N1

## Claim

LRU稳态字节命中率下界公式：H_LRU ≈ (1 - C_eff / S_total) * (1 - 1/β)，其中C_eff为有效缓存容量，S_total为总数据量，β为热度Pareto指数

## Corrected Claim

LRU稳态字节命中率下界公式：H_LRU ≈ (1 - C_eff / S_total) * (1 - 1/β)，其中C_eff为有效缓存容量，S_total为总数据量，β为热度Pareto指数

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

LRU steady-state hit ratio Pareto distribution lower bound formula
