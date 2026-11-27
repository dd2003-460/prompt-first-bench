# N43: 挂价偏离幅度的分布：偏离幅度 D = (price - μ) / μ 服从 N(0, σ_noise² / μ²)，15-25% 的偏离对应 D ∈ [0.15

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N7

## Claim

挂价偏离幅度的分布：偏离幅度 D = (price - μ) / μ 服从 N(0, σ_noise² / μ²)，15-25% 的偏离对应 D ∈ [0.15, 0.25]，其概率密度由 σ_noise² 决定。

## Corrected Claim

挂价偏离幅度的分布：偏离幅度 D = (price - μ) / μ 服从 N(0, σ_noise² / μ²)，15-25% 的偏离对应 D ∈ [0.15, 0.25]，其概率密度由 σ_noise² 决定。

## Evidence

先验知识/题面给定，逻辑校验通过：若价格 P 服从 N(μ, σ_noise²)，则标准化变量 D=(P-μ)/μ 服从 N(0, σ_noise²/μ²)，数学推导自洽。
