# N226: 混合效应模型方差估计：通过线性混合模型 (LMM) 估计 σ²_seller，模型设定为 P_dev_seller = β0 + β1 * Category +

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N81

## Claim

混合效应模型方差估计：通过线性混合模型 (LMM) 估计 σ²_seller，模型设定为 P_dev_seller = β0 + β1 * Category + u_seller + ε，其中 ε ~ N(0, σ²_platform)，若 σ²_seller / (σ²_seller + σ²_platform) > 0.3，则说明个体差异主导，平台归因置信度降至 0.5 以下。

## Corrected Claim

混合效应模型方差估计：通过线性混合模型 (LMM) 估计 σ²_seller，模型设定为 P_dev_seller = β0 + β1 * Category + u_seller + ε，其中 ε ~ N(0, σ²_platform)，若 σ²_seller / (σ²_seller + σ²_platform) > 0.3，则说明个体差异主导，平台归因置信度降至 0.5 以下。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

linear mixed model variance decomposition seller heterogeneity pricing
