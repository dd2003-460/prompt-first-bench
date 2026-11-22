# N84: 计算H_byte_LRU_lower：H_byte_LRU_lower = H_byte_Optimal - ε_lru。H_byte_Optimal = (Σ

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N26

## Claim

计算H_byte_LRU_lower：H_byte_LRU_lower = H_byte_Optimal - ε_lru。H_byte_Optimal = (Σ_{i=1}^{K} p_i * s_i) / S_total_bytes。由于K=N（所有对象都在缓存中），H_byte_Optimal = 1.0（假设无更新）。因此，H_byte_LRU_lower ≈ 1.0 - 0.03 = 0.97（97%）。注意：此结果依赖于K=N的假设，若K<N，需重新计算H_byte_Optimal。

## Corrected Claim

计算H_byte_LRU_lower：H_byte_LRU_lower = H_byte_Optimal - ε_lru。H_byte_Optimal = (Σ_{i=1}^{K} p_i * s_i) / S_total_bytes。由于K=N（所有对象都在缓存中），H_byte_Optimal = 1.0（假设无更新）。因此，H_byte_LRU_lower ≈ 1.0 - 0.03 = 0.97（97%）。注意：此结果依赖于K=N的假设，若K<N，需重新计算H_byte_Optimal。

## Evidence

先验知识/题面给定，逻辑校验通过：在K=N且无更新假设下，最优命中率H_byte_Optimal为1.0，减去LRU损耗ε_lru=0.03得到0.97，推导自洽。
