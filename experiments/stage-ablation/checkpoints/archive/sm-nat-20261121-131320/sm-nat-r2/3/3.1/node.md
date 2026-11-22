# N11: 更新率导致的缓存失效概率 P_invalid：对象在缓存驻留时间 T_res 内被更新的概率 P_invalid = 1 - exp(-λ * T_res)，其

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N3

## Claim

更新率导致的缓存失效概率 P_invalid：对象在缓存驻留时间 T_res 内被更新的概率 P_invalid = 1 - exp(-λ * T_res)，其中 λ=0.01/day，T_res 由 LRU 替换策略下的平均驻留时间决定（T_res ≈ C / (Σ_{i in cache} f_i * S_i)）。

## Corrected Claim

更新率导致的缓存失效概率 P_invalid：对象在缓存驻留时间 T_res 内被更新的概率 P_invalid = 1 - exp(-λ * T_res)，其中 λ=0.01/day，T_res 由 LRU 替换策略下的平均驻留时间决定（T_res ≈ C / (Σ_{i in cache} f_i * S_i)）。

## Evidence

先验知识/题面给定，逻辑校验通过：泊松过程更新概率公式正确，LRU驻留时间近似公式量纲合理
