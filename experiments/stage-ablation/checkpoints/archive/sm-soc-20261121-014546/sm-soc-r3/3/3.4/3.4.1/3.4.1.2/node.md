# N243: 投影1-平台推荐权重偏差：α 直接影响高溢价商品（P_ask > 1.15V）的曝光权重 W_exp，W_exp = W_base * (1 + α * (P_

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N72

## Claim

投影1-平台推荐权重偏差：α 直接影响高溢价商品（P_ask > 1.15V）的曝光权重 W_exp，W_exp = W_base * (1 + α * (P_ask/V - 1))。当 α = 0.1 时，1.2V 商品的曝光权重比 1.0V 商品高约 2%，这解释了为何高挂价商品仍能获得足够流量。

## Corrected Claim

投影1-平台推荐权重偏差：α 直接影响高溢价商品（P_ask > 1.15V）的曝光权重 W_exp，W_exp = W_base * (1 + α * (P_ask/V - 1))。当 α = 0.1 时，1.2V 商品的曝光权重比 1.0V 商品高约 2%，这解释了为何高挂价商品仍能获得足够流量。

## Evidence

先验知识/题面给定，逻辑校验通过：根据公式 W_exp = W_base * (1 + α * (P_ask/V - 1))，当 α=0.1 时，1.2V 商品的权重系数为 1 + 0.1*(0.2) = 1.02，1.0V 商品为 1.0，相对提升确为 2%，数学推导自洽。

## Search Query

impact of price deviation on recommendation exposure weight
