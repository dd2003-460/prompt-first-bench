# N160: 拒绝阈值 τ_reject 的分布参数：τ_reject 服从正态分布 N(μ_τ, σ_τ^2)。基于二手市场数据，假设 μ_τ = 0.25 (25% 偏差

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N55

## Claim

拒绝阈值 τ_reject 的分布参数：τ_reject 服从正态分布 N(μ_τ, σ_τ^2)。基于二手市场数据，假设 μ_τ = 0.25 (25% 偏差) 且 σ_τ = 0.05。则 P(Reject | ΔI > 0.25) = 0.5（均值处），P(Reject | ΔI > 0.30) ≈ 0.16。需验证在 ΔI = 0.25 时，拒绝概率是否显著高于 0.4 以支持双重打击假设。

## Corrected Claim

拒绝阈值 τ_reject 的分布参数：τ_reject 服从正态分布 N(μ_τ, σ_τ^2)。基于二手市场数据，假设 μ_τ = 0.25 (25% 偏差) 且 σ_τ = 0.05。则 P(Reject | ΔI > 0.25) = 0.5（均值处），P(Reject | ΔI > 0.30) ≈ 0.16。需验证在 ΔI = 0.25 时，拒绝概率是否显著高于 0.4 以支持双重打击假设。

## Evidence

先验知识/题面给定，逻辑校验通过：正态分布 N(0.25, 0.05^2) 在均值处概率密度最高，P(X>0.25)=0.5 符合定义；P(X>0.30) 对应 Z=1，尾部概率约 0.1587≈0.16，数值量级与逻辑自洽。

## Search Query

price rejection threshold distribution second hand market behavioral data
