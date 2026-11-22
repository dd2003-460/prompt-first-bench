# N15: 线性折扣模型：有效命中率 H_eff ≈ H_steady × (1 - u × T_avg)，其中 u=0.01/天，T_avg 为 LRU 缓存中对象平均驻

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N4

## Claim

线性折扣模型：有效命中率 H_eff ≈ H_steady × (1 - u × T_avg)，其中 u=0.01/天，T_avg 为 LRU 缓存中对象平均驻留时间（天），需计算 T_avg = C_total / (R × S_avg_cached)

## Corrected Claim

线性折扣模型：有效命中率 H_eff ≈ H_steady × (1 - u × T_avg)，其中 u=0.01/天，T_avg 为 LRU 缓存中对象平均驻留时间（天），需计算 T_avg = C_total / (R × S_avg_cached)

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

LRU cache eviction rate update frequency hit rate reduction model
