# N283: 衰减系数 k 的估计值 k ≈ 2.0 仅适用于短尾品类（如手机），在长尾/非标品类（如家具、艺术品）中，由于买家对质量方差容忍度更高，k 应显著降低（估计 k

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N94, N95, N96

## Claim

衰减系数 k 的估计值 k ≈ 2.0 仅适用于短尾品类（如手机），在长尾/非标品类（如家具、艺术品）中，由于买家对质量方差容忍度更高，k 应显著降低（估计 k ≈ 0.8-1.2），需引入品类异质性修正项 H：k = k_base * (1 - alpha_H * H)。

## Corrected Claim

衰减系数 k 在长尾/非标品类中通常低于短尾品类，因为买家对质量方差容忍度更高；具体数值需根据品类数据实证估计，而非直接套用固定公式。

## Evidence

[质询]该陈述包含具体的经验性数值估计（k≈2.0, k≈0.8-1.2）及特定的修正公式结构，属于经验事实而非第一性原理可推导的数学/物理定律。虽然逻辑上自洽（长尾品类质量方差容忍度高导致价格对质量敏感度降低，从而衰减系数降低），但缺乏外部来源支持其具体数值量级和公式形式的普适性。 | 经验事实，逻辑自洽但缺来源支持（source=knowledge，但具体数值估计属于经验参数，无法仅凭逻辑推导验证其准确性，故降级）

## Search Query

used goods market attention decay coefficient category heterogeneity
