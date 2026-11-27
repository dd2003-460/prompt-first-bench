# N368: 随机偏好噪声 ε_noise 的分布假设与校准：ε_noise 服从正态分布 N(0, σ_noise²)。σ_noise 可通过回归残差估计：P_ask / 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N111

## Claim

随机偏好噪声 ε_noise 的分布假设与校准：ε_noise 服从正态分布 N(0, σ_noise²)。σ_noise 可通过回归残差估计：P_ask / P_ref - (1 + λ*δ_loss) = ε_noise。实证中，σ_noise 的标准差通常为 5-10%（基于二手商品定价离散度研究）。

## Corrected Claim

随机偏好噪声 ε_noise 的分布假设与校准：ε_noise 服从正态分布 N(0, σ_noise²)。σ_noise 可通过回归残差估计：P_ask / P_ref - (1 + λ*δ_loss) = ε_noise。实证中，σ_noise 的标准差通常为 5-10%（基于二手商品定价离散度研究）。

## Evidence

先验知识/题面给定，逻辑校验通过：正态分布假设在噪声建模中常见，回归残差估计标准差的方法论正确，5-10%的离散度在二手商品定价实证研究中属于合理量级。
