# N209: 在静态负载（无更新，τ_obj=∞）下，P_eviction=0，H_LRU_eff = H_static = 0.82，LRU 稳态命中率等于静态最优下界，无

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N76

## Claim

在静态负载（无更新，τ_obj=∞）下，P_eviction=0，H_LRU_eff = H_static = 0.82，LRU 稳态命中率等于静态最优下界，无动态惩罚，作为理想基准。

## Corrected Claim

在静态负载（无更新，τ_obj=∞）下，P_eviction=0，H_LRU_eff = H_static = 0.82，LRU 稳态命中率等于静态最优下界，无动态惩罚，作为理想基准。

## Evidence

先验知识/题面给定，逻辑校验通过：在静态负载（无更新）下，LRU 缓存内容不变，命中率即为静态最优命中率，无动态惩罚，符合定义。
