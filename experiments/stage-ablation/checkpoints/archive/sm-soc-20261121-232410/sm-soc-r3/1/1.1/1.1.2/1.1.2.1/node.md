# N96: k_anchor分布的偏度Skewness检验：若k_anchor分布右偏（Skewness > 0.5），则均值μ=0.20可能受少数极高溢价卖家拉高，中位数

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N32

## Claim

k_anchor分布的偏度Skewness检验：若k_anchor分布右偏（Skewness > 0.5），则均值μ=0.20可能受少数极高溢价卖家拉高，中位数更适合作为参考；需计算样本Skewness及95% CI，判断正态假设是否成立。

## Corrected Claim

k_anchor分布的偏度Skewness检验：若k_anchor分布右偏（Skewness > 0.5），则均值μ=0.20可能受少数极高溢价卖家拉高，中位数更适合作为参考；需计算样本Skewness及95% CI，判断正态假设是否成立。

## Evidence

先验知识/题面给定，逻辑校验通过：偏度>0.5通常指示右偏分布，此时均值易受极端值影响，中位数更具鲁棒性，符合统计学基本原理。

## Search Query

skewness test price anchor distribution
