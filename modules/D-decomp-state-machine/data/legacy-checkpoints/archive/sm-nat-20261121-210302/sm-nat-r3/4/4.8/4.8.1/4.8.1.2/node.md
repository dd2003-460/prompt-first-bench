# N187: T_evict 在高缓存占用率下的工作点（N_cap/N_total ≈ 1.0）：假设缓存接近满载（N_cap ≈ 100,000），代入公式 T_evict

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N66

## Claim

T_evict 在高缓存占用率下的工作点（N_cap/N_total ≈ 1.0）：假设缓存接近满载（N_cap ≈ 100,000），代入公式 T_evict ≈ 1 / (1 + 0.01 * 1.0) ≈ 0.990 天，此时更新率导致驱逐周期略微缩短，需考虑边界效应。

## Corrected Claim

T_evict 在高缓存占用率下的工作点（N_cap/N_total ≈ 1.0）：假设缓存接近满载（N_cap ≈ 100,000），代入公式 T_evict ≈ 1 / (1 + 0.01 * 1.0) ≈ 0.990 天，此时更新率导致驱逐周期略微缩短，需考虑边界效应。

## Evidence

先验知识/题面给定，逻辑校验通过：公式 T_evict ≈ 1 / (1 + 0.01 * 1.0) 计算结果为 0.990，数值量级与逻辑自洽。
