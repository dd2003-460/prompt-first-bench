# N53: 买家缺陷概率后验更新公式：P(Defective | Price_Drop) = P(Defective | Prior) * (1 + δ_defect * 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N10

## Claim

买家缺陷概率后验更新公式：P(Defective | Price_Drop) = P(Defective | Prior) * (1 + δ_defect * (P_initial - P_drop)/P_initial)，其中 δ_defect 为缺陷信号强度系数（预期 δ_defect ∈ [0.5, 1.0]）；需量化在 P_drop = 0.9 * P_initial 时，P(Defective | Price_Drop) 相对于 P(Defective | Price_Stable) 的提升幅度（预期提升 10-20%）。

## Corrected Claim

买家缺陷概率后验更新公式：P(Defective | Price_Drop) = P(Defective | Prior) * (1 + δ_defect * (P_initial - P_drop)/P_initial)，其中 δ_defect 为缺陷信号强度系数（预期 δ_defect ∈ [0.5, 1.0]）；需量化在 P_drop = 0.9 * P_initial 时，P(Defective | Price_Drop) 相对于 P(Defective | Price_Stable) 的提升幅度（预期提升 10-20%）。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

bayesian updating defect probability price signal second hand market
