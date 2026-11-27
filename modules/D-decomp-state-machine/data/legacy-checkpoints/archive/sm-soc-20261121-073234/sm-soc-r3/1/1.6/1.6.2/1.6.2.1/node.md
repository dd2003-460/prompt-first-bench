# N154: 共享随机源：买家估值分布 V 的参数估计，均值 μ_v 需通过同类商品近期成交价中位数 P_median 校准（μ_v ≈ P_median * (1 + Ri

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N46, N47, N48

## Claim

共享随机源：买家估值分布 V 的参数估计，均值 μ_v 需通过同类商品近期成交价中位数 P_median 校准（μ_v ≈ P_median * (1 + Risk_Premium)），标准差 σ_v 需通过买家出价/点击行为的离散度估算（σ_v ≈ 0.15 * P_median），该分布是所有下游占比计算的唯一随机源。

## Corrected Claim

共享随机源：买家估值分布 V 的参数估计，均值 μ_v 需通过同类商品近期成交价中位数 P_median 校准（μ_v ≈ P_median * (1 + Risk_Premium)），标准差 σ_v 需通过买家出价/点击行为的离散度估算（σ_v ≈ 0.15 * P_median），该分布是所有下游占比计算的唯一随机源。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

second hand market buyer valuation distribution parameters median price variance
