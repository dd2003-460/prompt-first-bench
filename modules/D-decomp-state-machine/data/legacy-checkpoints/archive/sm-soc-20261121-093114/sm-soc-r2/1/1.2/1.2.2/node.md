# N31: 下游投影1：实际损失厌恶系数 λ_loss_i = λ_mean + ε_seller,i，其中 λ_mean=2.5，ε_seller,i ~ N(0, σ_

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N7

## Claim

下游投影1：实际损失厌恶系数 λ_loss_i = λ_mean + ε_seller,i，其中 λ_mean=2.5，ε_seller,i ~ N(0, σ_ε^2)，导致不同卖家的溢价幅度 P_ask_i = P_market * (1 + 0.25 * (1 + ε_seller,i/λ_mean)) 呈现离散分布。

## Corrected Claim

下游投影1：实际损失厌恶系数 λ_loss_i = λ_mean + ε_seller,i，其中 λ_mean=2.5，ε_seller,i ~ N(0, σ_ε^2)，导致不同卖家的溢价幅度 P_ask_i = P_market * (1 + 0.25 * (1 + ε_seller,i/λ_mean)) 呈现离散分布。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

loss aversion coefficient individual variation pricing premium distribution
