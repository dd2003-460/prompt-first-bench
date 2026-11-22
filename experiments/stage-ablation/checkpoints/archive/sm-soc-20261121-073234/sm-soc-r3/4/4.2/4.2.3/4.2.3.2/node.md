# N258: 二手市场中买家对商品真实价值的先验分布方差 σ_prior² 显著高于标准实验，具体数值需通过同类商品历史成交价的变异系数（CV）估算，通常 CV 在 0.15

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N85

## Claim

二手市场中买家对商品真实价值的先验分布方差 σ_prior² 显著高于标准实验，具体数值需通过同类商品历史成交价的变异系数（CV）估算，通常 CV 在 0.15-0.25 之间，这导致锚点权重降低。

## Corrected Claim

二手市场中买家对商品真实价值的先验分布方差通常高于标准实验，具体数值需通过同类商品历史成交价的变异系数（CV）估算，CV 值因品类而异，这导致锚点权重降低。

## Evidence

[质询]CV 0.15-0.25 的数值范围缺乏普适性，不同品类（如奢侈品 vs 日用品）差异巨大，且‘显著高于标准实验’的对比基准模糊，属于经验性断言而非严格推导。 | 先验知识/题面给定，逻辑校验通过：方差大导致锚点权重降低符合贝叶斯更新直觉，但具体 CV 数值为经验估计，无来源支持，故降级。

## Search Query

second hand market price coefficient of variation prior variance
