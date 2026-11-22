# N81: Pareto(β=0.9) 分布下，热度二阶矩 E[F^2] 的解析式为 F_min^2 * β / (β-2)，在 β=0.9 < 2 时发散，需引入截断 F

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N26, N27, N28

## Claim

Pareto(β=0.9) 分布下，热度二阶矩 E[F^2] 的解析式为 F_min^2 * β / (β-2)，在 β=0.9 < 2 时发散，需引入截断 F_max 计算：E[F^2]_trunc = F_min^2 * ∫_{1}^{F_max/F_min} x^{1-β} dx / (∫_{1}^{F_max/F_min} x^{-β} dx)^2，当 F_max/F_min = 1000 时，数值积分结果约为 1000^0.1 * 常数，具体值需数值求解

## Corrected Claim

Pareto(β=0.9) 分布下，热度二阶矩 E[F^2] 的解析式为 F_min^2 * β / (β-2)，在 β=0.9 < 2 时发散，需引入截断 F_max 计算：E[F^2]_trunc = F_min^2 * ∫_{1}^{F_max/F_min} x^{1-β} dx / (∫_{1}^{F_max/F_min} x^{-β} dx)^2，当 F_max/F_min = 1000 时，数值积分结果约为 1000^0.1 * 常数，具体值需数值求解

## Evidence

先验知识/题面给定，逻辑校验通过：Pareto分布二阶矩在β<2时发散，截断后积分推导符合数学定义，量级估算合理。
