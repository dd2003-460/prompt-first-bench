# N15: LRU有效命中率折扣因子 D_eff = H_effective / H_static，其中 H_effective = H_static * (1 - M_i

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N3

## Claim

LRU有效命中率折扣因子 D_eff = H_effective / H_static，其中 H_effective = H_static * (1 - M_invalidation)，H_static 为无更新情况下的稳态命中率，D_eff 直接反映更新率对命中率的线性折扣效应。

## Corrected Claim

LRU有效命中率折扣因子 D_eff = H_effective / H_static，其中 H_effective = H_static * (1 - M_invalidation)，H_static 为无更新情况下的稳态命中率，D_eff 直接反映更新率对命中率的线性折扣效应。

## Evidence

先验知识/题面给定，逻辑校验通过
