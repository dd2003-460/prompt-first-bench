# N117: 在 T_resident = 30天（中频长尾对象）的工作点下，P_stale = 1 - exp(-0.01 * 30) ≈ 0.259，有效命中率折损因子 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N36

## Claim

在 T_resident = 30天（中频长尾对象）的工作点下，P_stale = 1 - exp(-0.01 * 30) ≈ 0.259，有效命中率折损因子 (1 - P_stale) ≈ 0.741，折损约 25.9%

## Corrected Claim

在 T_resident = 30天（中频长尾对象）的工作点下，P_stale = 1 - exp(-0.01 * 30) ≈ 0.259，有效命中率折损因子 (1 - P_stale) ≈ 0.741，折损约 25.9%

## Evidence

先验知识/题面给定，逻辑校验通过：计算 1 - exp(-0.3) ≈ 0.2592，折损因子 0.7408，数值与陈述一致。
