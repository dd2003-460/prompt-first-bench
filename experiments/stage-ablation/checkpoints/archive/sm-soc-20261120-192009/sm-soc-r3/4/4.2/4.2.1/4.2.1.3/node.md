# N244: 基线精度约束下的最小样本量阈值：若要求 SE_T_normal < 0.1 * T_normal（即相对误差<10%），则需 n_normal > (Z_{0.

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N81

## Claim

基线精度约束下的最小样本量阈值：若要求 SE_T_normal < 0.1 * T_normal（即相对误差<10%），则需 n_normal > (Z_{0.975} * σ_T / 0.1)^2；代入 σ_T=0.46 和 Z=1.96，得 n_normal > 81，此为该工作点的最低数据要求。

## Corrected Claim

基线精度约束下的最小样本量阈值：若要求 SE_T_normal < 0.1 * T_normal（即相对误差<10%），则需 n_normal > (Z_{0.975} * σ_T / 0.1)^2；代入 σ_T=0.46 和 Z=1.96，得 n_normal > 81，此为该工作点的最低数据要求。

## Evidence

先验知识/题面给定，逻辑校验通过：公式推导 n > (Z*σ/E)^2 正确，代入数值 (1.96*0.46/0.1)^2 ≈ 81.05，结论 n>81 符合统计学原理。

## Search Query

minimum sample size for mean estimation relative error
