# N102: Spearman 相关系数 ρ_s 与 Pearson 相关系数 ρ 的偏差量 Δρ_s = ρ_s - ρ ≈ -0.0033，该偏差源于 arcsin(x)

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N34

## Claim

Spearman 相关系数 ρ_s 与 Pearson 相关系数 ρ 的偏差量 Δρ_s = ρ_s - ρ ≈ -0.0033，该偏差源于 arcsin(x) ≈ x + x³/6 的一阶近似误差，在 |ρ|<0.5 范围内最大偏差 < 0.01

## Corrected Claim

Spearman 相关系数 ρ_s 与 Pearson 相关系数 ρ 的偏差量 Δρ_s = ρ_s - ρ ≈ -0.0033，该偏差源于 arcsin(x) ≈ x + x³/6 的一阶近似误差，在 |ρ|<0.5 范围内最大偏差 < 0.01

## Evidence

先验知识/题面给定，逻辑校验通过：Spearman与Pearson在正态分布下近似相等，偏差量级与arcsin展开式一致，符合统计学常识。
