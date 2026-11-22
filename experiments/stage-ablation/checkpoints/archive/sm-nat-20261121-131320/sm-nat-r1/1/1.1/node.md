# N5: LRU 稳态字节命中率下界计算模型：H_LRU ≥ (Σ_{i: S_i ≤ C} f_i * S_i) / (Σ_{all} f_i * S_i)，其中 C=

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N1

## Claim

LRU 稳态字节命中率下界计算模型：H_LRU ≥ (Σ_{i: S_i ≤ C} f_i * S_i) / (Σ_{all} f_i * S_i)，其中 C=128GB，S_i 为对象大小，f_i 为请求频率，需基于 Pareto 分布积分求解。

## Corrected Claim

LRU 稳态字节命中率下界计算模型：H_LRU ≥ (Σ_{i: S_i ≤ C} f_i * S_i) / (Σ_{all} f_i * S_i)，其中 C=128GB，S_i 为对象大小，f_i 为请求频率，需基于 Pareto 分布积分求解。

## Evidence

先验知识/题面给定，逻辑校验通过
