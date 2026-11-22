# N40: 共享随机源投影（买家筛选）：买家发起咨询的条件概率 Prob(Consult) = Φ((V_buyer - P_ask) / σ)，其中 V_buyer = 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N8

## Claim

共享随机源投影（买家筛选）：买家发起咨询的条件概率 Prob(Consult) = Φ((V_buyer - P_ask) / σ)，其中 V_buyer = V_true + ε_buyer，ε_buyer ~ N(0, σ²) 为共享随机源；当 P_ask = V_true + k·σ 且 k > θ 时，Prob(Consult) < 0.5，具体数值取决于 k-θ 的差值。

## Corrected Claim

共享随机源投影（买家筛选）：买家发起咨询的条件概率 Prob(Consult) = Φ((V_buyer - P_ask) / σ)，其中 V_buyer = V_true + ε_buyer，ε_buyer ~ N(0, σ²) 为共享随机源；当 P_ask = V_true + k·σ 且 k > θ 时，Prob(Consult) < 0.5，具体数值取决于 k-θ 的差值。

## Evidence

先验知识/题面给定，逻辑校验通过：根据正态分布性质，当均值差 (V_true - P_ask) = -kσ 且 k > 0 时，标准正态分布函数 Φ(-k) < Φ(0) = 0.5，推导自洽。

## Search Query

buyer consultation probability normal distribution threshold
