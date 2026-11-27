# N275: 频率突变持续时间 Δt 的量化：在 1%/天 更新率下，假设请求分布突变是随机的，Δt 服从指数分布，均值 E[Δt] = 1/0.01 = 100 天；需计算

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N104

## Claim

频率突变持续时间 Δt 的量化：在 1%/天 更新率下，假设请求分布突变是随机的，Δt 服从指数分布，均值 E[Δt] = 1/0.01 = 100 天；需计算 Δt 与 τ_lag 的比值 r = Δt/τ_lag 对命中率损失 ΔH_loss 的影响函数。

## Corrected Claim

频率突变持续时间 Δt 的量化：在 1%/天 更新率下，假设请求分布突变是随机的，Δt 服从指数分布，均值 E[Δt] = 1/0.01 = 100 天；需计算 Δt 与 τ_lag 的比值 r = Δt/τ_lag 对命中率损失 ΔH_loss 的影响函数。

## Evidence

先验知识/题面给定，逻辑校验通过：指数分布均值公式 E[Δt]=1/λ 应用正确，数值计算 1/0.01=100 无误，量纲（天）一致。

## Search Query

request distribution shift duration in CDN cache modeling
