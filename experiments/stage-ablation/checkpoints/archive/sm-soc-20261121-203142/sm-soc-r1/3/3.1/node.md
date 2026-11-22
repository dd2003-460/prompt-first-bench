# N13: 最小干预措施：平台调整曝光加权系数 W_exposure，使其对 P_ask > 1.2 * P_market 的商品降权，即 W_exposure = 1 -

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N3

## Claim

最小干预措施：平台调整曝光加权系数 W_exposure，使其对 P_ask > 1.2 * P_market 的商品降权，即 W_exposure = 1 - β * max(0, P_ask/P_market - 1.2)，β = 0.5，以抑制高挂价商品的过度曝光。

## Corrected Claim

最小干预措施：平台调整曝光加权系数 W_exposure，使其对 P_ask > 1.2 * P_market 的商品降权，即 W_exposure = 1 - β * max(0, P_ask/P_market - 1.2)，β = 0.5，以抑制高挂价商品的过度曝光。

## Evidence

先验知识/题面给定，逻辑校验通过
