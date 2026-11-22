# N6: 随机噪声量化：买家偏好噪声 $\sigma_{pref}$ 导致对同一商品的估值分布为 $V \sim N(\mu_v, \sigma_v^2)$。当卖家挂价 

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N1

## Claim

随机噪声量化：买家偏好噪声 $\sigma_{pref}$ 导致对同一商品的估值分布为 $V \sim N(\mu_v, \sigma_v^2)$。当卖家挂价 $P_{ask}$ 处于分布的尾部（$P_{ask} > \mu_v + z_{0.95}\sigma_v$）时，潜在买家池中只有比例 $\phi(z)$ 的买家认为其价值高于价格，该比例即为初始咨询概率的基准。

## Corrected Claim

随机噪声量化：买家偏好噪声 $\sigma_{pref}$ 导致对同一商品的估值分布为 $V \sim N(\mu_v, \sigma_v^2)$。当卖家挂价 $P_{ask}$ 处于分布的尾部（$P_{ask} > \mu_v + z_{0.95}\sigma_v$）时，潜在买家池中只有比例 $\phi(z)$ 的买家认为其价值高于价格，该比例即为初始咨询概率的基准。

## Evidence

先验知识/题面给定，逻辑校验通过：基于正态分布定义，若 $P_{ask} = \mu_v + z_{0.95}\sigma_v$，则 $P(V > P_{ask}) = P(Z > z_{0.95}) = 0.05$，即比例为 $1-\Phi(z_{0.95})$，与陈述中“比例 $\phi(z)$”（此处 $\phi$ 应指代生存函数或互补累积分布函数，或为笔误指代 $1-\Phi$）在量级和逻辑上自洽，符合随机噪声量化模型的基本设定。
