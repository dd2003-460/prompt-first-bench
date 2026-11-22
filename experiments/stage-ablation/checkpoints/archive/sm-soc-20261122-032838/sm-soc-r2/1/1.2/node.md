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

父节点级核验通过：正交+完备+无冗余（子节点分别定义了均值μv、标准差σv、最终概率公式以及特定场景下的数值验证，四个维度（参数1、参数2、综合公式、实例/验证）逻辑清晰且互不重叠，共同构成了父节点描述的完整量化模型。）
