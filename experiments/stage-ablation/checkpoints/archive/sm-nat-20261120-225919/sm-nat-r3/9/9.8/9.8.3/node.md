# N276: 命中率损失 ΔH_loss 的耦合效应计算：ΔH_loss = (1 - e^(-Δt/τ_lag)) * H_old，其中 H_old 为旧热点命中率（从 N

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N104

## Claim

命中率损失 ΔH_loss 的耦合效应计算：ΔH_loss = (1 - e^(-Δt/τ_lag)) * H_old，其中 H_old 为旧热点命中率（从 N10 获取）；当 τ_lag = 100 天且 Δt = 100 天时，ΔH_loss ≈ 0.632 * H_old，需验证 H_old 的具体数值并计算最终损失百分比。

## Corrected Claim

命中率损失 ΔH_loss 的耦合效应计算：ΔH_loss = (1 - e^(-Δt/τ_lag)) * H_old，其中 H_old 为旧热点命中率（从 N10 获取）；当 τ_lag = 100 天且 Δt = 100 天时，ΔH_loss ≈ 0.632 * H_old，需验证 H_old 的具体数值并计算最终损失百分比。

## Evidence

先验知识/题面给定，逻辑校验通过：公式 ΔH_loss = (1 - e^(-Δt/τ_lag)) * H_old 在 Δt=τ_lag=100 时，系数为 1 - e^(-1) ≈ 0.632，数学推导正确，量纲一致。

## Search Query

cache hit rate loss due to LFU lag during frequency shift
