# N72: 卖家价格敏感度弹性 E_price：定义为卖家挂价 P_ask 对锚点 P_median 的弹性，E_price = (ΔP_ask/P_ask) / (ΔP_

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N17

## Claim

卖家价格敏感度弹性 E_price：定义为卖家挂价 P_ask 对锚点 P_median 的弹性，E_price = (ΔP_ask/P_ask) / (ΔP_median/P_median)，当锚点显示时，E_price 从 1.0 降至 1.0 - δ_reduction，量化卖家对锚点的跟随程度。

## Corrected Claim

卖家价格敏感度弹性 E_price：定义为卖家挂价 P_ask 对锚点 P_median 的弹性，E_price = (ΔP_ask/P_ask) / (ΔP_median/P_median)，当锚点显示时，E_price 从 1.0 降至 1.0 - δ_reduction，量化卖家对锚点的跟随程度。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

seller price elasticity to anchor point
