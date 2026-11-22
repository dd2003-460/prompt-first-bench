# N228: 买家启发式解释的权重 W_buyer_heur = 0.7 * (1 + η_buyer * ξ_s)，其中 η_buyer 为买家侧对信号敏感度波动的放大系数

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N75

## Claim

买家启发式解释的权重 W_buyer_heur = 0.7 * (1 + η_buyer * ξ_s)，其中 η_buyer 为买家侧对信号敏感度波动的放大系数（预期 0.1），ξ_s 为来自 N158 的标准正态噪声项，导致 W_buyer_heur 在 [0.65, 0.75] 区间内随机波动。

## Corrected Claim

买家启发式解释的权重 W_buyer_heur = 0.7 * (1 + η_buyer * ξ_s)，其中 η_buyer 为买家侧对信号敏感度波动的放大系数（预期 0.1），ξ_s 为来自 N158 的标准正态噪声项，导致 W_buyer_heur 在 [0.65, 0.75] 区间内随机波动。

## Evidence

先验知识/题面给定，逻辑校验通过：0.7 * (1 + 0.1 * N(0,1)) 在 3σ 范围内约为 [0.65, 0.75]，量级与区间描述自洽。
