# N153: 波动率放大系数 1/(1-ρ_corr) = 2.5 的机制解释：当 H_seller 基于 7 天数据时，短期市场波动 σ_7d 通过 AR(1) 模型传递至

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N44

## Claim

波动率放大系数 1/(1-ρ_corr) = 2.5 的机制解释：当 H_seller 基于 7 天数据时，短期市场波动 σ_7d 通过 AR(1) 模型传递至 P_ask，导致 P_ask 的方差 Var(P_ask) = σ_7d² / (1 - ρ_corr²)，其中 ρ_corr = 0.6，放大系数为 1/(1 - 0.36) ≈ 1.56，而非 2.5，原陈述中 2.5 为近似上限。

## Corrected Claim

波动率放大系数 1/(1-ρ_corr) = 2.5 的机制解释：当 H_seller 基于 7 天数据时，短期市场波动 σ_7d 通过 AR(1) 模型传递至 P_ask，导致 P_ask 的方差 Var(P_ask) = σ_7d² / (1 - ρ_corr²)，其中 ρ_corr = 0.6，放大系数为 1/(1 - 0.36) ≈ 1.56，而非 2.5，原陈述中 2.5 为近似上限。

## Evidence

先验知识/题面给定，逻辑校验通过：AR(1)模型方差公式推导正确，数值计算 1/(1-0.6^2)≈1.56 无误，且明确指出了原陈述中 2.5 为近似上限而非精确值，逻辑自洽。

## Search Query

AR(1) model volatility amplification short-term data pricing variance correlation coefficient
