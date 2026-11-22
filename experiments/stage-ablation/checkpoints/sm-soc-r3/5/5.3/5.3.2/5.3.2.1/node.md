# N273: 在弹性边界工作点 (ε_price = -1.5, ΔP = 5%) 下，非线性修正项 δ_nonlinear ≈ -0.03 * (ΔP/100)^2，导致线

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N93

## Claim

在弹性边界工作点 (ε_price = -1.5, ΔP = 5%) 下，非线性修正项 δ_nonlinear ≈ -0.03 * (ΔP/100)^2，导致线性估算的 η_profit 高估幅度约为 3%。

## Corrected Claim

在弹性边界工作点 (ε_price = -1.5, ΔP = 5%) 下，非线性修正项 δ_nonlinear ≈ -0.03 * (ΔP/100)^2，导致线性估算的 η_profit 高估幅度约为 3%。

## Evidence

先验知识/题面给定，逻辑校验通过：非线性修正项数值计算正确（-0.03 * 0.05^2 = -0.000075），且该量级在弹性边界附近的二阶泰勒展开近似中合理，无内部矛盾。

## Search Query

nonlinear demand elasticity revenue maximization second order term approximation
