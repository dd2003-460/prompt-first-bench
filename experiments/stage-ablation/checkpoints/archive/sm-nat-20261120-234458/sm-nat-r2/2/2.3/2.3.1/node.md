# N39: Pareto(α=1.1) 分布的二阶矩（方差）为无穷大，导致基于均值的简单相关系数 ρ 失效，必须使用秩相关（Spearman ρ_s ≈ -0.3）或截断方

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N11

## Claim

Pareto(α=1.1) 分布的二阶矩（方差）为无穷大，导致基于均值的简单相关系数 ρ 失效，必须使用秩相关（Spearman ρ_s ≈ -0.3）或截断方差 σ²_S = ∫(s-μ)² f(s)ds (s∈[1KB, 100MB]) 来量化大小分布的离散程度。

## Corrected Claim

Pareto(α=1.1) 分布的二阶矩（方差）为无穷大，导致基于均值的简单相关系数 ρ 失效，必须使用秩相关（Spearman ρ_s ≈ -0.3）或截断方差 σ²_S = ∫(s-μ)² f(s)ds (s∈[1KB, 100MB]) 来量化大小分布的离散程度。

## Evidence

先验知识/题面给定，逻辑校验通过：Pareto分布当α≤2时二阶矩发散，α=1.1<2，故方差无穷大，导致基于矩的相关系数失效，需使用秩相关或截断统计量。

## Search Query

Pareto distribution second moment infinite variance alpha 1.1
