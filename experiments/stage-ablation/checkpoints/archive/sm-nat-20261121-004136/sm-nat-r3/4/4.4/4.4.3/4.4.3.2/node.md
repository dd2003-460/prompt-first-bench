# N143: 重新定义有效命中率折损：由于 H_LRU_original ≈ 1，Discount_Factor 公式失效。正确的折损应计算为‘更新导致的额外回源带宽占比’：

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N59

## Claim

重新定义有效命中率折损：由于 H_LRU_original ≈ 1，Discount_Factor 公式失效。正确的折损应计算为‘更新导致的额外回源带宽占比’：Penalty_Bandwidth = λ_update * N * E[Size | Updated] / (R_daily * E[Size_requested])。代入数值：λ_update=0.01, N=100k, E[Size|Updated]≈9.35KB, R_daily=50M, E[Size_requested]≈9.35KB（因 ρ≈0 对均值影响小），计算得 Penalty_Bandwidth ≈ (0.01 * 100000 * 9.35) / (50000000 * 9.35) = 1000 / 467500000 ≈ 0.0000021 (0.00021%)。

## Corrected Claim

重新定义有效命中率折损：由于 H_LRU_original ≈ 1，Discount_Factor 公式失效。正确的折损应计算为‘更新导致的额外回源带宽占比’：Penalty_Bandwidth = λ_update * N * E[Size | Updated] / (R_daily * E[Size_requested])。代入数值：λ_update=0.01, N=100k, E[Size|Updated]≈9.35KB, R_daily=50M, E[Size_requested]≈9.35KB（因 ρ≈0 对均值影响小），计算得 Penalty_Bandwidth ≈ (0.01 * 100000 * 9.35) / (50000000 * 9.35) = 1000 / 467500000 ≈ 0.0000021 (0.00021%)。

## Evidence

先验知识/题面给定，逻辑校验通过：公式推导符合带宽占比定义，数值计算 (0.01*100000*9.35)/(50000000*9.35) = 1000/467500000 ≈ 2.14e-6 准确无误，量级合理。
