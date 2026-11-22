# N175: σ_logS = 0.828 的推导基于 Pareto 分布的对数变换性质：若 S ~ Pareto(α, s_min)，则 ln(S/s_min) ~ Exp

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N75, N76, N77

## Claim

σ_logS = 0.828 的推导基于 Pareto 分布的对数变换性质：若 S ~ Pareto(α, s_min)，则 ln(S/s_min) ~ Exp(α)，其方差为 1/α²，故 Var[ln S] = 1/α² = 1/1.21 ≈ 0.826，标准差 σ_logS = √0.826 ≈ 0.909，此处 N76 的 0.828 存在计算误差，正确值应为 0.909，需修正以维持后续 K(ρ) 计算的准确性。

## Corrected Claim

σ_logS = 0.828 的推导基于 Pareto 分布的对数变换性质：若 S ~ Pareto(α, s_min)，则 ln(S/s_min) ~ Exp(α)，其方差为 1/α²，故 Var[ln S] = 1/α² = 1/1.21 ≈ 0.826，标准差 σ_logS = √0.826 ≈ 0.909，此处 N76 的 0.828 存在计算误差，正确值应为 0.909，需修正以维持后续 K(ρ) 计算的准确性。

## Evidence

先验知识/题面给定，逻辑校验通过：Pareto分布对数变换性质及方差计算正确，0.828确为计算误差，正确标准差约为0.909
