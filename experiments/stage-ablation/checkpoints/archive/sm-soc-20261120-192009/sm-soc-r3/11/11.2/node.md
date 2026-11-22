# N347: 市场时间 T_market 的量化：T_market 以小时为单位，若 T_market = 48 小时，则衰减项 e^{-λ_selection * 48/2

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N118

## Claim

市场时间 T_market 的量化：T_market 以小时为单位，若 T_market = 48 小时，则衰减项 e^{-λ_selection * 48/24} ≈ e^{-2 * λ_selection}，若 λ_selection = 0.2，则衰减项 ≈ 0.67，噪声保留 67%。

## Corrected Claim

市场时间 T_market 的量化：T_market 以小时为单位，若 T_market = 48 小时，则衰减项 e^{-λ_selection * 48/24} ≈ e^{-2 * λ_selection}，若 λ_selection = 0.2，则衰减项 ≈ 0.67，噪声保留 67%。

## Evidence

先验知识/题面给定，逻辑校验通过：数学计算 e^{-2*0.2} = e^{-0.4} ≈ 0.6703，与陈述一致；单位换算 48/24=2 正确。
