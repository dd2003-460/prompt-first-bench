# N229: 卖家锚定解释的权重 W_seller_anchor = 0.15 * (1 + η_seller * ξ_s)，其中 η_seller 为卖家侧对信号敏感度波动

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N75

## Claim

卖家锚定解释的权重 W_seller_anchor = 0.15 * (1 + η_seller * ξ_s)，其中 η_seller 为卖家侧对信号敏感度波动的耦合系数（预期 0.05，因卖家更依赖历史数据而非实时信号），导致 W_seller_anchor 在 [0.14, 0.16] 区间内随机波动。

## Corrected Claim

卖家锚定解释的权重 W_seller_anchor = 0.15 * (1 + η_seller * ξ_s)，其中 η_seller 为卖家侧对信号敏感度波动的耦合系数（预期 0.05，因卖家更依赖历史数据而非实时信号），导致 W_seller_anchor 在 [0.14, 0.16] 区间内随机波动。

## Evidence

先验知识/题面给定，逻辑校验通过：公式结构合理，参数取值（0.05）与区间推导（0.15*0.95≈0.1425, 0.15*1.05≈0.1575，四舍五入或近似为[0.14, 0.16]）在数量级和逻辑上自洽，无内部矛盾。
