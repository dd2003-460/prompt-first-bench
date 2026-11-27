# N199: 随机偏好噪声 ε_noise 的来源分解：ε_noise = ε_seller_bias + ε_platform_noise + ε_demand_shock

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N73

## Claim

随机偏好噪声 ε_noise 的来源分解：ε_noise = ε_seller_bias + ε_platform_noise + ε_demand_shock，其中 ε_seller_bias 为卖家主观定价偏差（均值 0，标准差 2-3%），ε_platform_noise 为平台推荐算法波动引起的价格感知噪声（标准差 1-2%），ε_demand_shock 为短期需求冲击（标准差 5-10%）。

## Corrected Claim

随机偏好噪声 ε_noise 可分解为卖家主观定价偏差、平台推荐算法波动及短期需求冲击三部分，具体各分量的标准差需依据特定市场数据或模型校准确定，通常需求冲击的波动幅度大于卖家偏差和平台噪声。

## Evidence

[质询]该陈述包含具体的经验性数值参数（如卖家偏差标准差2-3%、需求冲击5-10%），这些属于特定市场或模型设定下的经验事实，无法从第一性原理或数学公理中严格推导出来，且参考来源均未提供此类具体数值支持。 | 逻辑上噪声分解结构自洽，但具体数值量级属于经验事实，参考来源[1][2][3]均讨论ε-SVR、ε-滤波器或抽象概念，与该具体经济/平台场景的噪声参数无关，缺乏直接来源支持。

## Search Query

pricing noise decomposition seller bias platform algorithm noise demand shock standard deviation

## Retrieval Sources

- {'url': 'https://link.springer.com/chapter/10.1007/3-540-44668-0_57&rut=aa55cd0c8648642242a723100a873ccb808d70b41ec3a330354e389b24730f10', 'type': 'ddg', 'title': 'Linear Dependency between ε and the Input Noise in ε ... - Springer'}
- {'url': 'https://www.jstage.jst.go.jp/article/transinf/E92.D/6/E92.D_6_1312/_pdf&rut=53ddf086430af8b875ea85d5fe6d4ebbd95f889f0fad74f135ea2944210bf2b0', 'type': 'ddg', 'title': 'Estimation of Optimal Parameter in ε-Filter Based on Signal-Noise ...'}
- {'url': 'https://memeticcowboy.github.io/nemetics/glossary/epsilon-noise.html&rut=d56c4e1bd91258dff36c3beecb30cafe1f17dd3876a1bbbef335a49198245949', 'type': 'ddg', 'title': 'Epsilon Noise — Nemetics'}
