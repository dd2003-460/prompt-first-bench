# N309: 曝光量差异 ΔExposure 的回归模型：ΔExposure = β_δ * δ + β_ctrl * (Image_Quality + Seller_Rat

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N103

## Claim

曝光量差异 ΔExposure 的回归模型：ΔExposure = β_δ * δ + β_ctrl * (Image_Quality + Seller_Rating + Category_Dummy) + ε，其中 β_δ 为溢价对曝光的净效应系数，需通过控制商品图片质量（清晰度评分）、卖家历史评分及类目虚拟变量后估计，以排除混杂因素。

## Corrected Claim

曝光量差异 ΔExposure 的回归模型：ΔExposure = β_δ * δ + β_ctrl * (Image_Quality + Seller_Rating + Category_Dummy) + ε，其中 β_δ 为溢价对曝光的净效应系数，需通过控制商品图片质量（清晰度评分）、卖家历史评分及类目虚拟变量后估计，以排除混杂因素。

## Evidence

先验知识/题面给定，逻辑校验通过
