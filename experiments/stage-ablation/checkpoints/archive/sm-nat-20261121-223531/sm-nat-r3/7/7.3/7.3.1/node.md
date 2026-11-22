# N207: Pareto(β=0.9)均值发散的数学验证：E[H] = h_min * β / (β - 1) 仅在 β > 1 时收敛。当 β = 0.9 < 1 时，积

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N75

## Claim

Pareto(β=0.9)均值发散的数学验证：E[H] = h_min * β / (β - 1) 仅在 β > 1 时收敛。当 β = 0.9 < 1 时，积分 ∫_{h_min}^{∞} h * f_H(h) dh 发散至无穷大，证实热度分布无有限均值。

## Corrected Claim

Pareto(β=0.9)均值发散的数学验证：E[H] = h_min * β / (β - 1) 仅在 β > 1 时收敛。当 β = 0.9 < 1 时，积分 ∫_{h_min}^{∞} h * f_H(h) dh 发散至无穷大，证实热度分布无有限均值。

## Evidence

先验知识/题面给定，逻辑校验通过：Pareto分布的均值公式 E[X] = α x_m / (α - 1) 在 α ≤ 1 时确实发散，数学推导正确。
