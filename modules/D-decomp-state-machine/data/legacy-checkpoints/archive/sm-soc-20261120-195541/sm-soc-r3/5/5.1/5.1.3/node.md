# N165: 漏斗分解的正交性验证：需控制商品质量（Item_Quality）和卖家评分（Seller_Rating）后，高挂价对 CTR 和 CVR 的独立效应；若高挂价同

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N56

## Claim

漏斗分解的正交性验证：需控制商品质量（Item_Quality）和卖家评分（Seller_Rating）后，高挂价对 CTR 和 CVR 的独立效应；若高挂价同时提升 CTR 和 CVR，则筛选效应可能被曝光倾斜混淆，需引入平台曝光权重 W_exposure 作为控制变量进行多元回归。

## Corrected Claim

漏斗分解的正交性验证：需控制商品质量（Item_Quality）和卖家评分（Seller_Rating）后，高挂价对 CTR 和 CVR 的独立效应；若高挂价同时提升 CTR 和 CVR，则筛选效应可能被曝光倾斜混淆，需引入平台曝光权重 W_exposure 作为控制变量进行多元回归。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

multivariate regression controlling for confounders in funnel analysis
