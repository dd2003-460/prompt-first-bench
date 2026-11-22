# N120: 下游投影1：损失厌恶噪声项 Var(λ_loss) 的量化公式，定义为 Var(λ_loss) = k_loss * Var(ε_market) * (1 + 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N30

## Claim

下游投影1：损失厌恶噪声项 Var(λ_loss) 的量化公式，定义为 Var(λ_loss) = k_loss * Var(ε_market) * (1 + λ_base)，其中 k_loss 为敏感度系数（假设 k_loss=0.5），λ_base 为基准损失厌恶系数（取 N93 中的 2.0）。

## Corrected Claim

下游投影1：损失厌恶噪声项 Var(λ_loss) 的量化公式，定义为 Var(λ_loss) = k_loss * Var(ε_market) * (1 + λ_base)，其中 k_loss 为敏感度系数（假设 k_loss=0.5），λ_base 为基准损失厌恶系数（取 N93 中的 2.0）。

## Evidence

先验知识/题面给定，逻辑校验通过
