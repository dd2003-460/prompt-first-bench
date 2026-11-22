# N266: 个体噪声标准差 σ_noise_i 的分布形态检验：需验证其是否服从对数正态分布（Log-Normal），若成立则 Var(σ_noise_i) = (exp(

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N90

## Claim

个体噪声标准差 σ_noise_i 的分布形态检验：需验证其是否服从对数正态分布（Log-Normal），若成立则 Var(σ_noise_i) = (exp(μ_log + σ_log²/2))² * (exp(σ_log²) - 1)，其中 μ_log 和 σ_log 为对数空间参数，需基于分层抽样数据（如按卖家活跃度分层）进行 KS 检验。

## Corrected Claim

个体噪声标准差 σ_noise_i 的分布形态检验：需验证其是否服从对数正态分布（Log-Normal），若成立则 Var(σ_noise_i) = (exp(μ_log + σ_log²/2))² * (exp(σ_log²) - 1)，其中 μ_log 和 σ_log 为对数空间参数，需基于分层抽样数据（如按卖家活跃度分层）进行 KS 检验。

## Evidence

先验知识/题面给定，逻辑校验通过：对数正态分布的方差公式推导正确，KS检验用于分布形态检验符合统计学原理。

## Search Query

log-normal distribution variance formula for individual heterogeneity in behavioral economics
