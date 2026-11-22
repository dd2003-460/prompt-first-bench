# N46: 高估值买家占比计算：假设估值 V ~ N(μ_v, σ_v)，高估值买家占比 q_high = P(V > P_ask) = 1 - Φ((P_ask - μ_

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N10

## Claim

高估值买家占比计算：假设估值 V ~ N(μ_v, σ_v)，高估值买家占比 q_high = P(V > P_ask) = 1 - Φ((P_ask - μ_v) / σ_v)，其中 Φ 为标准正态分布累积函数，需计算当 P_ask = 1.2 * μ_v 时 q_high 的具体数值以解释快速成交子集。

## Corrected Claim

高估值买家占比计算：假设估值 V ~ N(μ_v, σ_v)，高估值买家占比 q_high = P(V > P_ask) = 1 - Φ((P_ask - μ_v) / σ_v)，其中 Φ 为标准正态分布累积函数，需计算当 P_ask = 1.2 * μ_v 时 q_high 的具体数值以解释快速成交子集。

## Evidence

先验知识/题面给定，逻辑校验通过：正态分布概率计算逻辑自洽，数值推导符合数学定义

## Search Query

normal distribution cumulative probability high valuation buyers share
