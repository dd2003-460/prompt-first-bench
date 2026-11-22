# N194: 置信度衰减临界时间 t_crit 的计算：当 C_0 = 0.8, σ_noise = 0.3, τ = 24h 时，C_low(t) < 0.6 的临界时间 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N63

## Claim

置信度衰减临界时间 t_crit 的计算：当 C_0 = 0.8, σ_noise = 0.3, τ = 24h 时，C_low(t) < 0.6 的临界时间 t_crit = -τ * ln(0.6/0.8) / σ_noise^2 ≈ 24 * 0.2877 / 0.09 ≈ 76.7h。

## Corrected Claim

置信度衰减临界时间 t_crit 的计算：当 C_0 = 0.8, σ_noise = 0.3, τ = 24h 时，C_low(t) < 0.6 的临界时间 t_crit = -τ * ln(0.6/0.8) / σ_noise^2 ≈ 24 * 0.2877 / 0.09 ≈ 76.7h。

## Evidence

先验知识/题面给定，逻辑校验通过：公式推导符合指数衰减模型，数值计算 24 * ln(4/3) / 0.09 ≈ 76.7 准确无误。
