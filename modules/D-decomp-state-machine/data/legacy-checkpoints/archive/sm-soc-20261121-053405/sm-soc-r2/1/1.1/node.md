# N5: 共享随机源定义：定义随机偏好噪声 $\epsilon$ 的分布为均值为0、标准差为 $\sigma_p$ 的高斯分布，其中 $\sigma_p$ 代表买家对同类

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N1

## Claim

共享随机源定义：定义随机偏好噪声 $\epsilon$ 的分布为均值为0、标准差为 $\sigma_p$ 的高斯分布，其中 $\sigma_p$ 代表买家对同类商品价值评估的离散度（可量化为同类商品近期成交价的变异系数 CV = \sigma_p/\mu_p）。

## Corrected Claim

共享随机源定义：定义随机偏好噪声 $\epsilon$ 的分布为均值为0、标准差为 $\sigma_p$ 的高斯分布，其中 $\sigma_p$ 代表买家对同类商品价值评估的离散度（可量化为同类商品近期成交价的变异系数 CV = \sigma_p/\mu_p）。

## Evidence

先验知识/题面给定，逻辑校验通过：高斯分布作为偏好噪声的建模假设在经济学和统计决策理论中是标准做法，且变异系数（CV）的定义（标准差/均值）与文中公式一致，量纲和逻辑自洽。
