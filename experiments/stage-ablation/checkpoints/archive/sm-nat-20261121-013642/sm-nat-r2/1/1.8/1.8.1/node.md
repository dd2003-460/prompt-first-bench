# N53: 更新对象在缓存中的期望占比 P_updated_in_cache = λ_u * T_residence，其中 λ_u=0.01/day，T_residence

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N13

## Claim

更新对象在缓存中的期望占比 P_updated_in_cache = λ_u * T_residence，其中 λ_u=0.01/day，T_residence 为对象在 LRU 缓存中的平均驻留时间，需结合 N16 的 T_cold 公式计算具体数值

## Corrected Claim

更新对象在缓存中的期望占比 P_updated_in_cache = λ_u * T_residence，其中 λ_u=0.01/day，T_residence 为对象在 LRU 缓存中的平均驻留时间，需结合 N16 的 T_cold 公式计算具体数值

## Evidence

先验知识/题面给定，逻辑校验通过
