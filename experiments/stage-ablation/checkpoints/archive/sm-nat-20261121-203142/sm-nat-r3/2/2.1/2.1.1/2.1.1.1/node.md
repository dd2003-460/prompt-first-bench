# N98: LRU 工作集命中概率 P_hit_object 的解析下界：在稳态下，P_hit_object ≈ 1 - exp(-λ_r * T_residence)，其

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N36

## Claim

LRU 工作集命中概率 P_hit_object 的解析下界：在稳态下，P_hit_object ≈ 1 - exp(-λ_r * T_residence)，其中 λ_r 为该对象的请求率；对于热度最高的对象（λ_r_max），P_hit_object_max ≈ 1 - exp(-λ_r_max * T_residence)，需计算 λ_r_max 的具体数值以评估头部对象命中率。

## Corrected Claim

LRU 工作集命中概率 P_hit_object 的解析下界：在稳态下，P_hit_object ≈ 1 - exp(-λ_r * T_residence)，其中 λ_r 为该对象的请求率；对于热度最高的对象（λ_r_max），P_hit_object_max ≈ 1 - exp(-λ_r_max * T_residence)，需计算 λ_r_max 的具体数值以评估头部对象命中率。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

LRU working set hit probability steady state exponential decay request rate
