# N220: 下游投影2 - 高挂价商品曝光衰减系数 λ_exposure：在排序逻辑偏移后，高挂价商品（低CTR高Prob）的曝光量变化率，λ_exposure = 1 -

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N70

## Claim

下游投影2 - 高挂价商品曝光衰减系数 λ_exposure：在排序逻辑偏移后，高挂价商品（低CTR高Prob）的曝光量变化率，λ_exposure = 1 - (w_new/w_old)^α，其中 α 为排序指数敏感度（典型值 α ∈ [0.8, 1.2]），反映流量重分配的边际效应。

## Corrected Claim

下游投影2 - 高挂价商品曝光衰减系数 λ_exposure：在排序逻辑偏移后，高挂价商品（低CTR高Prob）的曝光量变化率，λ_exposure = 1 - (w_new/w_old)^α，其中 α 为排序指数敏感度（典型值 α ∈ [0.8, 1.2]），反映流量重分配的边际效应。

## Evidence

先验知识/题面给定，逻辑校验通过
