# N198: 联合波动方差公式：平台总收益 R_platform 的方差 Var(R_platform) = (w_fee * Cov(GMV, R) + w_ad * Co

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N60

## Claim

联合波动方差公式：平台总收益 R_platform 的方差 Var(R_platform) = (w_fee * Cov(GMV, R) + w_ad * Cov(AdRev, R))^2 + Var(ε_other)，其中 w_fee 和 w_ad 为收益权重，Cov(GMV, AdRev) = ρ_GMV_Ad * σ_GMV * σ_AdRev 取决于共享随机源 σ_behavior 的强度；该公式量化了单一随机源如何放大或抵消平台收益波动。

## Corrected Claim

联合波动方差公式：平台总收益 R_platform 的方差 Var(R_platform) = (w_fee * Cov(GMV, R) + w_ad * Cov(AdRev, R))^2 + Var(ε_other)，其中 w_fee 和 w_ad 为收益权重，Cov(GMV, AdRev) = ρ_GMV_Ad * σ_GMV * σ_AdRev 取决于共享随机源 σ_behavior 的强度；该公式量化了单一随机源如何放大或抵消平台收益波动。

## Evidence

先验知识/题面给定，逻辑校验通过
