# N274: F统计量的计算与阈值：F = σ²_noise / σ²_price_bias，若F > 1/0.25 = 4则拒绝'噪声淹没信号'假设，需基于N106和N10

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N93

## Claim

F统计量的计算与阈值：F = σ²_noise / σ²_price_bias，若F > 1/0.25 = 4则拒绝'噪声淹没信号'假设，需基于N106和N107的估计值计算

## Corrected Claim

F统计量的计算与阈值：F = σ²_noise / σ²_price_bias，若F > 1/0.25 = 4则拒绝'噪声淹没信号'假设，需基于N106和N107的估计值计算

## Evidence

先验知识/题面给定，逻辑校验通过：F统计量定义为噪声方差与偏差方差之比，阈值4对应显著性水平0.25（或特定置信区间设定），数学推导自洽。

## Search Query

F test variance ratio noise to signal threshold ANOVA
