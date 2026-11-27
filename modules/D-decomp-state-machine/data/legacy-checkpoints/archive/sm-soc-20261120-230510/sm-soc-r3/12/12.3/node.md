# N319: 噪声掩盖理性筛选的临界条件：当 P_ask - V > k * σ_total 且 ε_random > (P_ask - V) - k * σ_total 时

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N113

## Claim

噪声掩盖理性筛选的临界条件：当 P_ask - V > k * σ_total 且 ε_random > (P_ask - V) - k * σ_total 时，买家仍发起咨询；需计算该事件发生的概率 P(consult | high_premium) = 1 - Φ((P_ask - V - k*σ_total)/σ_random)，其中 Φ 为标准正态分布函数。

## Corrected Claim

噪声掩盖理性筛选的临界条件：当 P_ask - V > k * σ_total 且 ε_random > (P_ask - V) - k * σ_total 时，买家仍发起咨询；需计算该事件发生的概率 P(consult | high_premium) = 1 - Φ((P_ask - V - k*σ_total)/σ_random)，其中 Φ 为标准正态分布函数。

## Evidence

先验知识/题面给定，逻辑校验通过
