# N83: σ_condition 与 σ_feature 的相关系数 ρ_cf 检验：若两者非独立（ρ_cf ≠ 0），则总噪声 σ_noise 的计算需修正为 sqrt

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N26

## Claim

σ_condition 与 σ_feature 的相关系数 ρ_cf 检验：若两者非独立（ρ_cf ≠ 0），则总噪声 σ_noise 的计算需修正为 sqrt(σ_condition² + σ_feature² + 2ρ_cf*σ_condition*σ_feature)；实证中成差差与功能缺陷往往正相关（如损坏导致成色差），预期 ρ_cf ∈ [0.2, 0.5]，需通过协方差矩阵估计验证。

## Corrected Claim

σ_condition 与 σ_feature 的相关系数 ρ_cf 检验：若两者非独立（ρ_cf ≠ 0），则总噪声 σ_noise 的计算需修正为 sqrt(σ_condition² + σ_feature² + 2ρ_cf*σ_condition*σ_feature)；实证中成差差与功能缺陷往往正相关（如损坏导致成色差），预期 ρ_cf ∈ [0.2, 0.5]，需通过协方差矩阵估计验证。

## Evidence

先验知识/题面给定，逻辑校验通过：方差合成公式 sqrt(σ1² + σ2² + 2ρσ1σ2) 符合统计学第一性原理；经验参数 ρ_cf ∈ [0.2, 0.5] 在图像质量评估领域属于合理的定性估计，无逻辑矛盾。

## Search Query

correlation between condition and functional defects in used goods pricing
