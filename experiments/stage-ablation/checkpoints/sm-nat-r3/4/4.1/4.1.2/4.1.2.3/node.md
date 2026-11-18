# N132: 更新失效率 R_inv_i 在 T_i < 0.1 天时的线性近似误差：R_inv_i = 1 - e^{-u T_i} ≈ u T_i - 0.5 (u T_

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N55

## Claim

更新失效率 R_inv_i 在 T_i < 0.1 天时的线性近似误差：R_inv_i = 1 - e^{-u T_i} ≈ u T_i - 0.5 (u T_i)^2，当 u=0.01/day 且 T_i < 0.1 天时，二阶项 0.5 (u T_i)^2 < 5e-5，可忽略，因此 R_inv_i ≈ 0.01 * T_i 的相对误差 < 1%。

## Corrected Claim

更新失效率 R_inv_i 在 T_i < 0.1 天时的线性近似误差：R_inv_i = 1 - e^{-u T_i} ≈ u T_i - 0.5 (u T_i)^2，当 u=0.01/day 且 T_i < 0.1 天时，二阶项 0.5 (u T_i)^2 < 5e-5，可忽略，因此 R_inv_i ≈ 0.01 * T_i 的相对误差 < 1%。

## Evidence

先验知识/题面给定，逻辑校验通过：u=0.01, T_i<0.1 时 uT_i<0.001，二阶项 0.5*(0.001)^2=5e-7，远小于 5e-5，相对误差 < 0.1%，结论成立

## Search Query

exponential approximation error linearization small parameter
