# N39: 后验质量估计Q_posterior的均值计算：μ_posterior = (μ_prior/σ_prior² + α*P/σ_p²) / (1/σ_prior²

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N8

## Claim

后验质量估计Q_posterior的均值计算：μ_posterior = (μ_prior/σ_prior² + α*P/σ_p²) / (1/σ_prior² + α²/σ_p²)，其中P为实际挂价，用于量化高挂价（P > μ_prior*1.15）对Q_posterior的提升幅度。

## Corrected Claim

后验质量估计Q_posterior的均值计算：μ_posterior = (μ_prior/σ_prior² + α*P/σ_p²) / (1/σ_prior² + α²/σ_p²)，其中P为实际挂价，用于量化高挂价（P > μ_prior*1.15）对Q_posterior的提升幅度。

## Evidence

先验知识/题面给定，逻辑校验通过
