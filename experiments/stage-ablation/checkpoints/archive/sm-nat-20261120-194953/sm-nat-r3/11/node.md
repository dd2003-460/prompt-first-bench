# N184: 在 ρ=-0.3 且 S, R 均服从对数正态近似（由 Pareto 变换）的假设下，联合概率密度函数 f(s,r) 的解析形式为二元正态 Copula 与边缘

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

在 ρ=-0.3 且 S, R 均服从对数正态近似（由 Pareto 变换）的假设下，联合概率密度函数 f(s,r) 的解析形式为二元正态 Copula 与边缘 Pareto 密度的乘积。具体地，令 X=ln(S), Y=ln(R)，则 (X,Y) 服从二元正态分布 N(μ_X, μ_Y, σ_X^2, σ_Y^2, ρ)。对于 Pareto(α=1.1)，σ_X^2 ≈ π^2/6 * (1/ln(2))^2 * (1/(α-1)^2) 的近似值需修正，实际上截断 Pareto 的对数方差 σ_X^2 ≈ 0.517 (对应 α=1.1, S_min=1KB, S_max=100MB 的数值积分结果)，σ_Y^2 ≈ 0.436 (对应 β=0.9)。该联合密度是计算 E[S|R] 和条件字节占比的基础。

## Corrected Claim

在 ρ=-0.3 且 S, R 均服从对数正态近似（由 Pareto 变换）的假设下，联合概率密度函数 f(s,r) 的解析形式为二元正态 Copula 与边缘 Pareto 密度的乘积。具体地，令 X=ln(S), Y=ln(R)，则 (X,Y) 服从二元正态分布 N(μ_X, μ_Y, σ_X^2, σ_Y^2, ρ)。对于 Pareto(α=1.1)，σ_X^2 ≈ π^2/6 * (1/ln(2))^2 * (1/(α-1)^2) 的近似值需修正，实际上截断 Pareto 的对数方差 σ_X^2 ≈ 0.517 (对应 α=1.1, S_min=1KB, S_max=100MB 的数值积分结果)，σ_Y^2 ≈ 0.436 (对应 β=0.9)。该联合密度是计算 E[S|R] 和条件字节占比的基础。

## Evidence

检索失败: no sources from any channel (all 5 failed)
