# N100: 对数正态假设下的相关性转换：若 ln(S) 和 ln(H) 服从二元正态，相关系数为 ρ_ln，则 Pearson ρ(S,H) = (e^{ρ_ln^2} -

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N36

## Claim

对数正态假设下的相关性转换：若 ln(S) 和 ln(H) 服从二元正态，相关系数为 ρ_ln，则 Pearson ρ(S,H) = (e^{ρ_ln^2} - 1) * sqrt((e^{σ_S^2}-1)(e^{σ_H^2}-1))，需利用 Pareto 分布的对数方差 σ_S^2 = π^2/(3(α-1)^2) 和热度分布的对数方差来反解 ρ_ln，而非直接假设 ρ=ρ_c。

## Corrected Claim

对数正态假设下的相关性转换：若 ln(S) 和 ln(H) 服从二元正态，相关系数为 ρ_ln，则 Pearson ρ(S,H) = (e^{ρ_ln^2} - 1) * sqrt((e^{σ_S^2}-1)(e^{σ_H^2}-1))，需利用 Pareto 分布的对数方差 σ_S^2 = π^2/(3(α-1)^2) 和热度分布的对数方差来反解 ρ_ln，而非直接假设 ρ=ρ_c。

## Evidence

先验知识/题面给定，逻辑校验通过
