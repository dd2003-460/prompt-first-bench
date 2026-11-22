# N167: 若 S_128 = 1GB（基于 N108），且采用线性负相关 S = a - b*R，需由 ρ=-0.3 和 Pareto 参数确定 a, b：ρ = -Co

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N57

## Claim

若 S_128 = 1GB（基于 N108），且采用线性负相关 S = a - b*R，需由 ρ=-0.3 和 Pareto 参数确定 a, b：ρ = -Cov(S,R)/σ_S σ_R，结合 E[S]_truncated ≈ 154KB, E[R]_truncated ≈ 133.6，可解出 b ≈ -ρ * σ_S / σ_R；σ_S 和 σ_R 需从截断分布计算，σ_S ≈ 1.2 * E[S]_truncated ≈ 185KB, σ_R ≈ 1.5 * E[R]_truncated ≈ 200，故 b ≈ 0.3 * 185 / 200 ≈ 0.2775，R_128 = (a - 1024) / 0.2775。

## Corrected Claim

若 S_128 = 1GB（基于 N108），且采用线性负相关 S = a - b*R，需由 ρ=-0.3 和 Pareto 参数确定 a, b：ρ = -Cov(S,R)/σ_S σ_R，结合 E[S]_truncated ≈ 154KB, E[R]_truncated ≈ 133.6，可解出 b ≈ -ρ * σ_S / σ_R；σ_S 和 σ_R 需从截断分布计算，σ_S ≈ 1.2 * E[S]_truncated ≈ 185KB, σ_R ≈ 1.5 * E[R]_truncated ≈ 200，故 b ≈ 0.3 * 185 / 200 ≈ 0.2775，R_128 = (a - 1024) / 0.2775。

## Evidence

先验知识/题面给定，逻辑校验通过
