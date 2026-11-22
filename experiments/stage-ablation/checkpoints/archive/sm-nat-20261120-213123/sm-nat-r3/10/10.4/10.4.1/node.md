# N179: 线性近似 B_corr ≈ B_indep * (1 + ρ * σ_logS * σ_logH) 的二阶泰勒展开误差项为 (1/2) * (ρ * σ_log

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N79

## Claim

线性近似 B_corr ≈ B_indep * (1 + ρ * σ_logS * σ_logH) 的二阶泰勒展开误差项为 (1/2) * (ρ * σ_logS * σ_logH)^2。当 x = ρ * σ_logS * σ_logH = -0.353 时，二阶项约为 0.062，表明线性近似低估了负相关的惩罚效应，实际修正因子应小于 0.647。

## Corrected Claim

线性近似 B_corr ≈ B_indep * (1 + ρ * σ_logS * σ_logH) 的二阶泰勒展开误差项为 (1/2) * (ρ * σ_logS * σ_logH)^2。当 x = ρ * σ_logS * σ_logH = -0.353 时，二阶项约为 0.062，表明线性近似低估了负相关的惩罚效应，实际修正因子应小于 0.647。

## Evidence

先验知识/题面给定，逻辑校验通过：数值计算准确（0.353^2/2 ≈ 0.0624），泰勒展开方向正确（凸函数线性近似低估实际值），符合数学推导逻辑。
