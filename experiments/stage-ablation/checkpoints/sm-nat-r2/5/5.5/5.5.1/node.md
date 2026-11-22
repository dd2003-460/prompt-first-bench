# N88: 均匀更新工作点：假设 1%/天 更新率均匀分布在所有 10 万对象上，则缓存中对象的平均失效概率 P_invalid = 1 - (1-0.01)^{T_res

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N29

## Claim

均匀更新工作点：假设 1%/天 更新率均匀分布在所有 10 万对象上，则缓存中对象的平均失效概率 P_invalid = 1 - (1-0.01)^{T_residence_days}，其中 T_residence_days 为对象在 LRU 中的平均驻留天数；在此工作点下，LRU 有效命中率折损因子 D_uniform ≈ 1 - P_invalid，且该折损与对象热度分布无关。

## Corrected Claim

均匀更新工作点：假设 1%/天 更新率均匀分布在所有 10 万对象上，则缓存中对象的平均失效概率 P_invalid = 1 - (1-0.01)^{T_residence_days}，其中 T_residence_days 为对象在 LRU 中的平均驻留天数；在此工作点下，LRU 有效命中率折损因子 D_uniform ≈ 1 - P_invalid，且该折损与对象热度分布无关。

## Evidence

先验知识/题面给定，逻辑校验通过：均匀更新假设下，对象失效概率仅取决于驻留时间，与热度分布无关，公式推导自洽。
