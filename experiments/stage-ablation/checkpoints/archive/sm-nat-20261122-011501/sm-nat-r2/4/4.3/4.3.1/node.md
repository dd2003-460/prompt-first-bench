# N55: P_inval 的精确数值：基于 N14 的 P_inval = min(1, T_res / T_life)，代入 T_res ≈ 0.0023 days (

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N16

## Claim

P_inval 的精确数值：基于 N14 的 P_inval = min(1, T_res / T_life)，代入 T_res ≈ 0.0023 days (N26) 和 T_life = 100 days，P_inval ≈ 0.000023。这意味着在稳态 LRU 中，对象在被更新失效前极大概率已被驱逐，更新导致的‘强制失效’概率极低。

## Corrected Claim

P_inval 的精确数值：基于 N14 的 P_inval = min(1, T_res / T_life)，代入 T_res ≈ 0.0023 days (N26) 和 T_life = 100 days，P_inval ≈ 0.000023。这意味着在稳态 LRU 中，对象在被更新失效前极大概率已被驱逐，更新导致的‘强制失效’概率极低。

## Evidence

先验知识/题面给定，逻辑校验通过：数值计算 0.0023/100 = 0.000023 准确，且符合 LRU 缓存中短驻留时间对象极少被更新失效的直觉。
