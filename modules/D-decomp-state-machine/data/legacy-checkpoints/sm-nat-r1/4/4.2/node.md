# N20: 对象 i 的更新间隔 T_update 服从指数分布，其均值 E[T_update] = 1 / λ_update，其中 λ_update = 0.01 / 天

- **status**: verified
- **level**: L2
- **source**: given
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N4

## Claim

对象 i 的更新间隔 T_update 服从指数分布，其均值 E[T_update] = 1 / λ_update，其中 λ_update = 0.01 / 天 = 1.157e-7 / 秒（基于 1%/天 的更新率）。

## Corrected Claim

对象 i 的更新间隔 T_update 服从指数分布，其均值 E[T_update] = 1 / λ_update，其中 λ_update = 0.01 / 天 = 1.157e-7 / 秒（基于 1%/天 的更新率）。

## Evidence

先验知识/题面给定，逻辑校验通过：指数分布均值公式 E[T]=1/λ 正确，单位换算 0.01/day ÷ 86400 s/day ≈ 1.157e-7/s 数值准确。
