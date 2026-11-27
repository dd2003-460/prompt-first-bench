# N34: 下游投影1：买家将高挂价视为高质量信号的概率 P(signal|P_ask) = Φ((P_ask - P_market - 15% + ε_buyer) / 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N8

## Claim

下游投影1：买家将高挂价视为高质量信号的概率 P(signal|P_ask) = Φ((P_ask - P_market - 15% + ε_buyer) / σ_threshold)，其中 Φ 为标准正态CDF，ε_buyer 的随机性导致信号解读的二值化波动。

## Corrected Claim

下游投影1：买家将高挂价视为高质量信号的概率 P(signal|P_ask) = Φ((P_ask - P_market - 15% + ε_buyer) / σ_threshold)，其中 Φ 为标准正态CDF，ε_buyer 的随机性导致信号解读的二值化波动。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

probability of interpreting high price as quality signal normal distribution threshold
