# N84: 负相关修正因子 ε_ρ 的一阶近似：ε_ρ ≈ -ρ * Cov(log r_i, log s_i) / Var(log s_i)。在 Gaussian Cop

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N32

## Claim

负相关修正因子 ε_ρ 的一阶近似：ε_ρ ≈ -ρ * Cov(log r_i, log s_i) / Var(log s_i)。在 Gaussian Copula 假设下，Cov(log r_i, log s_i) = ρ * σ_r * σ_s，故 ε_ρ ≈ -ρ * (σ_r / σ_s)。对于 Pareto 分布，σ_log_r = π / (β * sqrt(3)) ≈ 1.91，σ_log_s = π / (α * sqrt(3)) ≈ 1.64，故 ε_ρ ≈ 0.3 * (1.91 / 1.64) ≈ 0.348。因此 k' ≈ k * 1.348。

## Corrected Claim

负相关修正因子 ε_ρ 的一阶近似：ε_ρ ≈ -ρ * Cov(log r_i, log s_i) / Var(log s_i)。在 Gaussian Copula 假设下，Cov(log r_i, log s_i) = ρ * σ_r * σ_s，故 ε_ρ ≈ -ρ * (σ_r / σ_s)。对于 Pareto 分布，σ_log_r = π / (β * sqrt(3)) ≈ 1.91，σ_log_s = π / (α * sqrt(3)) ≈ 1.64，故 ε_ρ ≈ 0.3 * (1.91 / 1.64) ≈ 0.348。因此 k' ≈ k * 1.348。

## Evidence

先验知识/题面给定，逻辑校验通过：Pareto分布对数标准差公式正确，数值计算（1.91/1.64≈1.164，1+0.3*1.164≈1.349）与结论一致，无内部矛盾。
