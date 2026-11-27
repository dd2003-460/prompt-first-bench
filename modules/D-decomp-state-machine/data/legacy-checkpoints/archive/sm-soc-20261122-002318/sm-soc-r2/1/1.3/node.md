# N8: 随机偏好噪声 (Preference Noise) 的标准差 σ_noise：买家对同类商品价值的评估存在随机波动，σ_noise 决定了买家搜索成本与最终成交

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N1, N2, N3

## Claim

随机偏好噪声 (Preference Noise) 的标准差 σ_noise：买家对同类商品价值的评估存在随机波动，σ_noise 决定了买家搜索成本与最终成交价的分布宽度；若 σ_noise > 0，则即使挂价高于市场价，仍有一部分买家因噪声感知到“价值”而快速成交。

## Corrected Claim

随机偏好噪声 (Preference Noise) 的标准差 σ_noise：买家对同类商品价值的评估存在随机波动，σ_noise 决定了买家搜索成本与最终成交价的分布宽度；若 σ_noise > 0，则即使挂价高于市场价，仍有一部分买家因噪声感知到“价值”而快速成交。

## Evidence

先验知识/题面给定，逻辑校验通过：在随机效用模型中，偏好噪声（随机项）的存在确实会导致买家对同一商品的价值评估产生分布，从而使得高于市场均衡价格的挂价仍可能因正向噪声而被部分买家接受，符合经济学直觉。

## Search Query

preference noise standard deviation buyer search behavior heterogeneous valuations
