# N265: 推荐价差基准值 5% 的修正项 ΔS 为 0.02 * S，即实际推荐价差为 5% + 0.02 * S，S 为标准化程度，标准化程度越高推荐价差越小

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N88

## Claim

推荐价差基准值 5% 的修正项 ΔS 为 0.02 * S，即实际推荐价差为 5% + 0.02 * S，S 为标准化程度，标准化程度越高推荐价差越小

## Corrected Claim

推荐价差基准值 5% 的修正项 ΔS 为 -0.02 * S，即实际推荐价差为 5% - 0.02 * S，S 为标准化程度，标准化程度越高推荐价差越小

## Evidence

[质询]陈述内部存在逻辑矛盾：公式 '5% + 0.02 * S' 表明 S 越大推荐价差越大，但文字描述称 '标准化程度越高推荐价差越小'，两者方向相反。 | 先验知识/题面给定，但逻辑校验发现公式与文字描述方向矛盾，无法自洽。

## Search Query

price recommendation adjustment based on product standardization
