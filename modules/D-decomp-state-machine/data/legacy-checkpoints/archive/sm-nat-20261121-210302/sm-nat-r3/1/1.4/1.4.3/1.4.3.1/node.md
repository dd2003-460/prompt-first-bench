# N116: 在 T_resident = 1天（高频头部对象）的工作点下，P_stale = 1 - exp(-0.01 * 1) ≈ 0.00995，有效命中率折损因子 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N36

## Claim

在 T_resident = 1天（高频头部对象）的工作点下，P_stale = 1 - exp(-0.01 * 1) ≈ 0.00995，有效命中率折损因子 (1 - P_stale) ≈ 0.99005，折损约 1.0%

## Corrected Claim

在 T_resident = 1天（高频头部对象）的工作点下，P_stale = 1 - exp(-0.01 * 1) ≈ 0.00995，有效命中率折损因子 (1 - P_stale) ≈ 0.99005，折损约 1.0%

## Evidence

先验知识/题面给定，逻辑校验通过：计算 1 - exp(-0.01) ≈ 0.00995 及 1 - 0.00995 ≈ 0.99005 符合数学事实，折损率约 1% 推导正确。
