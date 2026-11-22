# N236: 在重尾分布下，公式 ρ_P ≈ ρ_S * (1 - 0.5 * Var(log(s))/E[log(s)]^2) 的误差项 ε 可通过二阶泰勒展开量化，其量级

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N81, N82, N83

## Claim

在重尾分布下，公式 ρ_P ≈ ρ_S * (1 - 0.5 * Var(log(s))/E[log(s)]^2) 的误差项 ε 可通过二阶泰勒展开量化，其量级取决于分布的偏度系数，对于 α=1.1 需验证该近似是否失效

## Corrected Claim

在重尾分布下，公式 ρ_P ≈ ρ_S * (1 - 0.5 * Var(log(s))/E[log(s)]^2) 的误差项 ε 可通过二阶泰勒展开量化，其量级取决于分布的偏度系数，对于 α=1.1 需验证该近似是否失效

## Evidence

先验知识/题面给定，逻辑校验通过
