# N97: 共享随机源参数：卖家异质性噪声 ε_seller 的截断正态分布截断点设定为 [λ_loss_min, λ_loss_max] = [1.0, 4.0]，以排除

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N30

## Claim

共享随机源参数：卖家异质性噪声 ε_seller 的截断正态分布截断点设定为 [λ_loss_min, λ_loss_max] = [1.0, 4.0]，以排除非理性极端值，确保 λ_loss_i 始终处于行为经济学实证观测的合理区间内。

## Corrected Claim

共享随机源参数：卖家异质性噪声 ε_seller 的截断正态分布截断点设定为 [λ_loss_min, λ_loss_max] = [1.0, 4.0]，以排除非理性极端值，确保 λ_loss_i 始终处于行为经济学实证观测的合理区间内。

## Evidence

先验知识/题面给定，逻辑校验通过：截断正态分布用于限制参数范围符合建模惯例，[1.0, 4.0] 作为损失厌恶系数的合理区间在行为经济学中常见，逻辑自洽。
