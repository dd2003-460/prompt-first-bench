# N6: 随机偏好噪声参数：卖家对商品价值的个体评估误差标准差 σ_noise，假设服从正态分布 N(0, σ_noise²)，其中 σ_noise ≈ 0.15 * P

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N1, N2, N3

## Claim

随机偏好噪声参数：卖家对商品价值的个体评估误差标准差 σ_noise，假设服从正态分布 N(0, σ_noise²)，其中 σ_noise ≈ 0.15 * P_market（基于二手市场异质性商品评估误差经验值），导致挂价 P_ask = P_reserve * (1 + ε)，ε ~ N(0, σ_noise²)。

## Corrected Claim

随机偏好噪声参数：卖家对商品价值的个体评估误差标准差 σ_noise，假设服从正态分布 N(0, σ_noise²)，其中 σ_noise ≈ 0.15 * P_market（基于二手市场异质性商品评估误差经验值），导致挂价 P_ask = P_reserve * (1 + ε)，ε ~ N(0, σ_noise²)。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

consumer valuation error standard deviation heterogeneous goods second-hand market
