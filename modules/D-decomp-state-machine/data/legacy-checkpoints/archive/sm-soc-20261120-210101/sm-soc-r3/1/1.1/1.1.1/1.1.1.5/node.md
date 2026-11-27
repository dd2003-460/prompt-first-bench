# N123: 协方差项 Cov(λ_loss, α_anchor) 的量化：假设损失厌恶与锚定效应在高不确定性市场中正相关，Cov(λ, α) = ρ * sqrt(Var(

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N30

## Claim

协方差项 Cov(λ_loss, α_anchor) 的量化：假设损失厌恶与锚定效应在高不确定性市场中正相关，Cov(λ, α) = ρ * sqrt(Var(λ_loss) * Var(α_anchor))，其中相关系数 ρ 需通过历史数据回归估计，初始假设 ρ=0.6。

## Corrected Claim

协方差项 Cov(λ_loss, α_anchor) 的量化：假设损失厌恶与锚定效应在高不确定性市场中正相关，Cov(λ, α) = ρ * sqrt(Var(λ_loss) * Var(α_anchor))，其中相关系数 ρ 需通过历史数据回归估计，初始假设 ρ=0.6。

## Evidence

先验知识/题面给定，逻辑校验通过
