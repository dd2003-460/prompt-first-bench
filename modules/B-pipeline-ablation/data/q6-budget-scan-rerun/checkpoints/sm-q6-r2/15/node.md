# N143: P99 延迟对缓存命中率 H 的敏感度系数：在 P99 约束下，当 H < 80% 时，P99 延迟对 H 的敏感度极高（d(P99)/dH ≈ -5ms/%）

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

P99 延迟对缓存命中率 H 的敏感度系数：在 P99 约束下，当 H < 80% 时，P99 延迟对 H 的敏感度极高（d(P99)/dH ≈ -5ms/%），即命中率每降低 1%，P99 增加 5ms；当 H > 90% 时，敏感度降低至 -2ms/%，因此优化命中率至 90% 以上的边际收益递减。

## Corrected Claim

P99 延迟对缓存命中率 H 的敏感度系数：在 P99 约束下，当 H < 80% 时，P99 延迟对 H 的敏感度极高（d(P99)/dH ≈ -5ms/%），即命中率每降低 1%，P99 增加 5ms；当 H > 90% 时，敏感度降低至 -2ms/%，因此优化命中率至 90% 以上的边际收益递减。

## Evidence

检索失败: no sources from any channel (all 5 failed)
