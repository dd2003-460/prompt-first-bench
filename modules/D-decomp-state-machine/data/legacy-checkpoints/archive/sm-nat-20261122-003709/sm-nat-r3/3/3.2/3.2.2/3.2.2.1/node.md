# N161: M_invalidation 在 T_resident=8.95 天时的精确值：M_invalidation = 1 - exp(-0.01 * 8.95) ≈

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N53

## Claim

M_invalidation 在 T_resident=8.95 天时的精确值：M_invalidation = 1 - exp(-0.01 * 8.95) ≈ 1 - exp(-0.0895) ≈ 0.0856（8.56%），远高于示例值 0.005，表明在 1%/天 更新率下，LRU 缓存的有效命中率将显著下降，D_eff ≈ 0.914。

## Corrected Claim

M_invalidation 在 T_resident=8.95 天时的精确值：M_invalidation = 1 - exp(-0.01 * 8.95) ≈ 1 - exp(-0.0895) ≈ 0.0856（8.56%），远高于示例值 0.005，表明在 1%/天 更新率下，LRU 缓存的有效命中率将显著下降，D_eff ≈ 0.914。

## Evidence

先验知识/题面给定，逻辑校验通过：计算 1 - exp(-0.0895) ≈ 0.0856 符合数学事实，D_eff = 1 - 0.0856 = 0.9144 逻辑自洽。
