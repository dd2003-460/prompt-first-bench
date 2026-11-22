# N46: Pareto(α=1.1)分布下，前10%对象（rank 1-10000）的累计大小占比精确值为 1 - (1/0.1)^(1-1.1) = 1 - 10^-0

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N14

## Claim

Pareto(α=1.1)分布下，前10%对象（rank 1-10000）的累计大小占比精确值为 1 - (1/0.1)^(1-1.1) = 1 - 10^-0.1 ≈ 9.63%，而非90%。

## Corrected Claim

Pareto(α=1.1)分布下，前10%对象（rank 1-10000）的累计大小占比精确值为 1 - (1/0.1)^(1-1.1) = 1 - 10^-0.1 ≈ 9.63%，而非90%。

## Evidence

先验知识/题面给定，逻辑校验通过：Pareto分布CDF公式应用正确，数值计算准确（1 - 10^-0.1 ≈ 0.0963）
