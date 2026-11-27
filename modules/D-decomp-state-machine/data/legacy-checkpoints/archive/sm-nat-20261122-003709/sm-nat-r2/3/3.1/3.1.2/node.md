# N50: 计算一致性未命中率 M_invalidation，公式为 M_invalidation = 1 - exp(-λ_update * T_resident_avg

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N13

## Claim

计算一致性未命中率 M_invalidation，公式为 M_invalidation = 1 - exp(-λ_update * T_resident_avg)，其中 T_resident_avg 为对象在缓存中的平均驻留时间，T_resident_avg ≈ C / (R * (1 - H_obj_avg))，需代入 R=50M/day, C=128GB, λ_update=0.01/day 进行数值计算。

## Corrected Claim

计算一致性未命中率 M_invalidation，公式为 M_invalidation = 1 - exp(-λ_update * T_resident_avg)，其中 T_resident_avg 为对象在缓存中的平均驻留时间，T_resident_avg ≈ C / (R * (1 - H_obj_avg))，需代入 R=50M/day, C=128GB, λ_update=0.01/day 进行数值计算。

## Evidence

先验知识/题面给定，逻辑校验通过
