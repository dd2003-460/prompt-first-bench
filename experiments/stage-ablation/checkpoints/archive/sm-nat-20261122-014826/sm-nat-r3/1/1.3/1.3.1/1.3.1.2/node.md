# N81: Pareto(β=0.9) 分布下热度的均值与标准差计算：μ_heat = (1/100000) * Σ r^{-0.9} ≈ 0.126，σ_heat = s

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N30

## Claim

Pareto(β=0.9) 分布下热度的均值与标准差计算：μ_heat = (1/100000) * Σ r^{-0.9} ≈ 0.126，σ_heat = sqrt(E[r^{-1.8}] - μ_heat^2)，其中 E[r^{-1.8}] ≈ (1/100000) * Σ r^{-1.8}。

## Corrected Claim

Pareto(β=0.9) 分布下热度的均值与标准差计算：μ_heat = (1/100000) * Σ r^{-0.9} ≈ 0.126，σ_heat = sqrt(E[r^{-1.8}] - μ_heat^2)，其中 E[r^{-1.8}] ≈ (1/100000) * Σ r^{-1.8}。

## Evidence

先验知识/题面给定，逻辑校验通过
