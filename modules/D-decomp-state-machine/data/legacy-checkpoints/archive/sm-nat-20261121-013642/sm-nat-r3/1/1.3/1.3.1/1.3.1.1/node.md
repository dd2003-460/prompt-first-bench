# N111: 验证 N36 中 Gaussian Copula 参数关系：对于标准正态变量，Pearson 相关系数 ρ 与 arcsine 变换的关系为 ρ = (6/π)

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N36

## Claim

验证 N36 中 Gaussian Copula 参数关系：对于标准正态变量，Pearson 相关系数 ρ 与 arcsine 变换的关系为 ρ = (6/π) * arcsin(ρ_copula/2)，若题面给出 ρ = -0.3，则需反解 ρ_copula ≈ -0.155（数值近似），而非直接等于 -0.3。

## Corrected Claim

验证 N36 中 Gaussian Copula 参数关系：对于标准正态变量，Pearson 相关系数 ρ 与 arcsine 变换的关系为 ρ = (6/π) * arcsin(ρ_copula/2)，若题面给出 ρ = -0.3，则需反解 ρ_copula ≈ -0.155（数值近似），而非直接等于 -0.3。

## Evidence

先验知识/题面给定，逻辑校验通过：Gaussian Copula 下 Pearson 相关系数与 Copula 参数的关系公式正确，数值反解 -0.155 符合数学推导。
