# N231: α_price（价格敏感度系数）的估计值：通过回归 ln(λ) = α0 + α_price * ln((P_market - P_ask)/P_market)

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N77

## Claim

α_price（价格敏感度系数）的估计值：通过回归 ln(λ) = α0 + α_price * ln((P_market - P_ask)/P_market) + ε 估算，在二手电商典型数据中 α_price 通常介于 1.5 至 2.5 之间（即价格偏离10%导致咨询率变化15%-25%）。

## Corrected Claim

α_price（价格敏感度系数）的估计值：通过回归 ln(λ) = α0 + α_price * ln((P_market - P_ask)/P_market) + ε 估算，在二手电商典型数据中 α_price 通常介于 1.5 至 2.5 之间（即价格偏离10%导致咨询率变化15%-25%）。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

second hand marketplace price elasticity of inquiry rate alpha price
