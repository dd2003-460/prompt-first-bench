# N21: 动态更新导致的 LRU 有效命中率折扣因子 D_update 定义为 D_update = H_eff_dynamic / H_static，其中 H_stat

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N4

## Claim

动态更新导致的 LRU 有效命中率折扣因子 D_update 定义为 D_update = H_eff_dynamic / H_static，其中 H_static 是无更新时的稳态字节命中率，H_eff_dynamic 是考虑更新失效后的稳态字节命中率。

## Corrected Claim

动态更新导致的 LRU 有效命中率折扣因子 D_update 定义为 D_update = H_eff_dynamic / H_static，其中 H_static 是无更新时的稳态字节命中率，H_eff_dynamic 是考虑更新失效后的稳态字节命中率。

## Evidence

先验知识/题面给定，逻辑校验通过
