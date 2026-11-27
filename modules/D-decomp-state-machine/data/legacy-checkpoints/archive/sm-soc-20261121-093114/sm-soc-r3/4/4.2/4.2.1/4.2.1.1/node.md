# N174: 共享随机源：市场均衡价 P_equilibrium 的随机游走过程，建模为几何布朗运动 dP_eq = μ_eq * P_eq * dt + σ_market 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N55

## Claim

共享随机源：市场均衡价 P_equilibrium 的随机游走过程，建模为几何布朗运动 dP_eq = μ_eq * P_eq * dt + σ_market * P_eq * dW_t，其中 σ_market 为瞬时波动率，是贝叶斯估计误差的主要来源。

## Corrected Claim

共享随机源：市场均衡价 P_equilibrium 的随机游走过程，建模为几何布朗运动 dP_eq = μ_eq * P_eq * dt + σ_market * P_eq * dW_t，其中 σ_market 为瞬时波动率，是贝叶斯估计误差的主要来源。

## Evidence

先验知识/题面给定，逻辑校验通过：几何布朗运动是金融市场中资产价格（含均衡价）的标准建模方式，且随机波动项确实是贝叶斯估计中不确定性（误差）的主要来源，符合金融数学与统计推断的基本原理。
