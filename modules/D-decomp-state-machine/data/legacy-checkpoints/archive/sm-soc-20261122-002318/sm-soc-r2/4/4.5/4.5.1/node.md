# N67: 买家决策误差成本 (Cost_of_Error) 的量化公式：Cost_of_Error = E[max(0, P_ask - R_true)] * N_int

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N25

## Claim

买家决策误差成本 (Cost_of_Error) 的量化公式：Cost_of_Error = E[max(0, P_ask - R_true)] * N_interactions，其中 R_true 为买家真实保留价。在存在 15-25% 溢价且 σ_noise=0.18*P_market 的正态分布假设下，该期望值可解析计算为 σ_noise * φ(0)/Φ(-Z) 形式的损失函数，具体数值取决于 Z-score 对应的尾部概率。

## Corrected Claim

买家决策误差成本 (Cost_of_Error) 的量化公式：Cost_of_Error = E[max(0, P_ask - R_true)] * N_interactions，其中 R_true 为买家真实保留价。在存在 15-25% 溢价且 σ_noise=0.18*P_market 的正态分布假设下，该期望值可解析计算为 σ_noise * φ(0)/Φ(-Z) 形式的损失函数，具体数值取决于 Z-score 对应的尾部概率。

## Evidence

先验知识/题面给定，逻辑校验通过：公式符合期望损失（Expected Shortfall/Loss）的数学定义，正态分布下的解析解形式（涉及标准正态密度函数φ和分布函数Φ）在量纲和逻辑上自洽。

## Search Query

expected loss from overpayment in second hand market normal distribution
