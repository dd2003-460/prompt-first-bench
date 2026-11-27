# N236: P_market_post 的无偏估计：在干预后，P_market_post 需控制商品异质性，采用双重差分法（DID）估计的反事实均值，即 P_market_

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N85, N86, N87

## Claim

P_market_post 的无偏估计：在干预后，P_market_post 需控制商品异质性，采用双重差分法（DID）估计的反事实均值，即 P_market_post = P_observed_post - (P_control_post - P_control_pre)，以消除时间趋势干扰。

## Corrected Claim

P_market_post 的无偏估计：在干预后，P_market_post 需控制商品异质性，采用双重差分法（DID）估计的反事实均值，即 P_market_post = P_observed_post - (P_control_post - P_control_pre)，以消除时间趋势干扰。

## Evidence

先验知识/题面给定，逻辑校验通过：双重差分法（DID）的标准公式即为处理组干预后值减去（对照组干预后值减去对照组干预前值），该公式在逻辑上自洽且符合计量经济学基本原理，用于消除时间趋势和固定异质性。

## Search Query

difference in differences counterfactual estimation formula
