# N153: 价格收敛的时间常数 τ_convergence 计算：τ_convergence = 1 / (β_transparency * f_update)，其中 f_

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N54

## Claim

价格收敛的时间常数 τ_convergence 计算：τ_convergence = 1 / (β_transparency * f_update)，其中 f_update 为卖家查看参考价的频率（次/天，典型值2.5），故 τ_convergence ≈ 1 / (0.4 * 2.5) = 1天；该时间常数决定了从干预实施到价格回归中位数所需的平均天数。

## Corrected Claim

价格收敛的时间常数 τ_convergence 计算：τ_convergence = 1 / (β_transparency * f_update)，其中 f_update 为卖家查看参考价的频率（次/天，典型值2.5），故 τ_convergence ≈ 1 / (0.4 * 2.5) = 1天；该时间常数决定了从干预实施到价格回归中位数所需的平均天数。

## Evidence

先验知识/题面给定，逻辑校验通过
