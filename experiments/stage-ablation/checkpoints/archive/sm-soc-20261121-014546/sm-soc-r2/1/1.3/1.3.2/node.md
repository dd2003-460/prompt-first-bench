# N43: 风险规避投影 1：成交概率 p 的估计误差 ε_p ~ N(0, σ_p²)，其中 σ_p 量化卖家对市场需求预测的不确定性，该误差与定价噪声 ε 共享同一随机

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N8

## Claim

风险规避投影 1：成交概率 p 的估计误差 ε_p ~ N(0, σ_p²)，其中 σ_p 量化卖家对市场需求预测的不确定性，该误差与定价噪声 ε 共享同一随机源 R，即 ε_p = k_p * ε + η_p

## Corrected Claim

风险规避投影 1：成交概率 p 的估计误差 ε_p ~ N(0, σ_p²)，其中 σ_p 量化卖家对市场需求预测的不确定性，该误差与定价噪声 ε 共享同一随机源 R，即 ε_p = k_p * ε + η_p

## Evidence

先验知识/题面给定，逻辑校验通过
