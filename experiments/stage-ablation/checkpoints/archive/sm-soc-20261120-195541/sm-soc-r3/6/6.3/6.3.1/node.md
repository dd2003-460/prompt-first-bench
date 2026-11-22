# N176: 流动性阈值 L_min 的回归估计模型：以 T_deal 对 P_ask 的弹性 β_price 为因变量，以市场流动性 L（日均搜索量/在售商品数）为自变量，

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N60

## Claim

流动性阈值 L_min 的回归估计模型：以 T_deal 对 P_ask 的弹性 β_price 为因变量，以市场流动性 L（日均搜索量/在售商品数）为自变量，建立分段线性回归 T_deal = β0 + β1*P_ask + β2*L*P_ask + ε，β2 的显著性为负且 β2*P_ask < -β1 时的 L 值即为 L_min。

## Corrected Claim

流动性阈值 L_min 的回归估计模型：以 T_deal 对 P_ask 的弹性 β_price 为因变量，以市场流动性 L（日均搜索量/在售商品数）为自变量，建立分段线性回归 T_deal = β0 + β1*P_ask + β2*L*P_ask + ε，β2 的显著性为负且 β2*P_ask < -β1 时的 L 值即为 L_min。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

regression analysis market liquidity threshold price elasticity transaction time
