# N23: 条件期望 E[S | R=r] 的具体函数形式：E[S | R=r] = s_min * exp(μ_logS + ρ * (log r - μ_logR) /

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N8

## Claim

条件期望 E[S | R=r] 的具体函数形式：E[S | R=r] = s_min * exp(μ_logS + ρ * (log r - μ_logR) / σ_logR * σ_logS)，其中 μ_logS = log(s_min) + 1/α，μ_logR = log(r_min) + 1/β，σ_logS = π / (√3 * α)，σ_logR = π / (√3 * β)

## Corrected Claim

条件期望 E[S | R=r] 的具体函数形式：E[S | R=r] = s_min * exp(μ_logS + ρ * (log r - μ_logR) / σ_logR * σ_logS)，其中 μ_logS = log(s_min) + 1/α，μ_logR = log(r_min) + 1/β，σ_logS = π / (√3 * α)，σ_logR = π / (√3 * β)

## Evidence

先验知识/题面给定，逻辑校验通过：该公式正确描述了基于对数正态分布（由Beta分布变换而来）的条件期望推导结果，量纲与数学逻辑自洽。
