# N150: 先验标准差 σ_prior 的构成：σ_prior = σ_market_volatility * (1 / sqrt(n_category_reviews))

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N48, N49, N50

## Claim

先验标准差 σ_prior 的构成：σ_prior = σ_market_volatility * (1 / sqrt(n_category_reviews)) * (1 + I_uncertainty)，其中 σ_market_volatility 为该品类近期成交价波动率，n_category_reviews 为买家可见的同类商品评论数量，I_uncertainty 为信息不透明度指数（0-1），σ_prior 越大，买家对初始高价的容忍度（噪声解释空间）越大。

## Corrected Claim

先验标准差 σ_prior 的构成：σ_prior = σ_market_volatility * (1 / sqrt(n_category_reviews)) * (1 + I_uncertainty)，其中 σ_market_volatility 为该品类近期成交价波动率，n_category_reviews 为买家可见的同类商品评论数量，I_uncertainty 为信息不透明度指数（0-1），σ_prior 越大，买家对初始高价的容忍度（噪声解释空间）越大。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

prior variance estimation based on market volatility and review count Bayesian model
