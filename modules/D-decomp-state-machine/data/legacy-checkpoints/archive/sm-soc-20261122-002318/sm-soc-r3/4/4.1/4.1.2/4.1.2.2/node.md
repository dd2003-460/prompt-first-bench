# N165: 中性估计工作点（基准线）：假设 F(R) 为标准正态分布 N(μ, σ^2)，其中 μ = P_market, σ = 0.18 * P_market (引用 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N57

## Claim

中性估计工作点（基准线）：假设 F(R) 为标准正态分布 N(μ, σ^2)，其中 μ = P_market, σ = 0.18 * P_market (引用 N91)，TS_neutral = σ * [φ(Z) - Z * (1-Φ(Z))]，其中 Z = (P_actual - μ)/σ，此点代表信号噪声未导致分布整体偏移仅导致方差膨胀的情景。

## Corrected Claim

中性估计工作点（基准线）：假设 F(R) 为标准正态分布 N(μ, σ^2)，其中 μ = P_market, σ = 0.18 * P_market (引用 N91)，TS_neutral = σ * [φ(Z) - Z * (1-Φ(Z))]，其中 Z = (P_actual - μ)/σ，此点代表信号噪声未导致分布整体偏移仅导致方差膨胀的情景。

## Evidence

先验知识/题面给定，逻辑校验通过
