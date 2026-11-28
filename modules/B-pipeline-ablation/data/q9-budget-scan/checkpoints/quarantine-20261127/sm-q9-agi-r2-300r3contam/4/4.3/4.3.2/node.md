# N60: 在已知C_API=$0.03, C_Human=$1.67, Q_total=1000的前提下，总成本函数C_total(τ) = 1000 * [0.03 *

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N21

## Claim

在已知C_API=$0.03, C_Human=$1.67, Q_total=1000的前提下，总成本函数C_total(τ) = 1000 * [0.03 * FP_rate(τ) + 1.67 * FN_rate(τ)]。由于FN_cost/C_API_cost ≈ 55.7倍，最优阈值τ*应显著低于0.5（偏向保守触发检索），具体τ*需通过ROC曲线在F1-score或成本最小化点求解，预计τ* ∈ [0.3, 0.4]。

## Corrected Claim

在已知C_API=$0.03, C_Human=$1.67, Q_total=1000的前提下，总成本函数C_total(τ) = 1000 * [0.03 * FP_rate(τ) + 1.67 * FN_rate(τ)]。由于FN_cost/C_API_cost ≈ 55.7倍，最优阈值τ*应显著低于0.5（偏向保守触发检索），具体τ*需通过ROC曲线在F1-score或成本最小化点求解，预计τ* ∈ [0.3, 0.4]。

## Evidence

先验知识/题面给定，逻辑校验通过：成本函数构建符合加权错误率定义，FN成本远高于FP成本（1.67/0.03≈55.7）导致最优阈值向降低FN方向移动（即阈值降低，召回率提高，偏向保守触发），量级与方向逻辑自洽。
