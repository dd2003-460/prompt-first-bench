# N218: 在 Gaussian Copula 下，K 因子关于 ρ 的一阶修正项为 K ≈ 1 - ρ * (β/α)，当 ρ=-0.3, β=0.9, α=1.1 时，

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N80, N81, N82

## Claim

在 Gaussian Copula 下，K 因子关于 ρ 的一阶修正项为 K ≈ 1 - ρ * (β/α)，当 ρ=-0.3, β=0.9, α=1.1 时，K ≈ 1 + 0.3*(0.9/1.1) ≈ 1.245，显著高于 N23 的 0.74（线性假设错误方向）。

## Corrected Claim

在 Gaussian Copula 下，K 因子关于 ρ 的一阶修正项为 K ≈ 1 - ρ * (β/α)，当 ρ=-0.3, β=0.9, α=1.1 时，K ≈ 1 + 0.3*(0.9/1.1) ≈ 1.245，显著高于 N23 的 0.74（线性假设错误方向）。

## Evidence

先验知识/题面给定，逻辑校验通过：数值计算 1 + 0.3*(0.9/1.1) ≈ 1.245 正确，且符合 Gaussian Copula 下负相关导致因子放大（K>1）的定性逻辑。
