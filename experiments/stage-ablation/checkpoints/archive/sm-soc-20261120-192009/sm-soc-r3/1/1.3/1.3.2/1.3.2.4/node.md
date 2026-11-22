# N141: 下游投影 2：算法推荐误差率。平台推荐系统基于价格匹配度排序，其误差率 Error_Rate 与 σ_noise² 正相关：Error_Rate = P(|Pr

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N42

## Claim

下游投影 2：算法推荐误差率。平台推荐系统基于价格匹配度排序，其误差率 Error_Rate 与 σ_noise² 正相关：Error_Rate = P(|Price_Algo - Price_True| > ε) = 2 * Φ(-ε / σ_noise)；当 σ_noise 增大时，推荐系统误将高噪声（低标准化）商品推给不匹配买家的概率显著上升，导致转化率下降。

## Corrected Claim

下游投影 2：算法推荐误差率。平台推荐系统基于价格匹配度排序，其误差率 Error_Rate 与 σ_noise² 正相关：Error_Rate = P(|Price_Algo - Price_True| > ε) = 2 * Φ(-ε / σ_noise)；当 σ_noise 增大时，推荐系统误将高噪声（低标准化）商品推给不匹配买家的概率显著上升，导致转化率下降。

## Evidence

先验知识/题面给定，逻辑校验通过：基于正态分布假设，误差率公式推导正确，且噪声增大导致匹配度下降符合基本统计直觉。

## Search Query

recommendation system error rate price noise gaussian probability
