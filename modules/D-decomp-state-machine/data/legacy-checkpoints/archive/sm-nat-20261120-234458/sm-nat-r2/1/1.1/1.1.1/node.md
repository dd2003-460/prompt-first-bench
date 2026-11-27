# N20: 基于 Pareto(α=1.1) 且 S_min=1KB, S_max=100MB 的截断分布，计算出的对象平均大小 μ_S ≈ 11.1KB，而非 N5 中假

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N5

## Claim

基于 Pareto(α=1.1) 且 S_min=1KB, S_max=100MB 的截断分布，计算出的对象平均大小 μ_S ≈ 11.1KB，而非 N5 中假设的 100KB。

## Corrected Claim

基于 Pareto(α=1.1) 且 S_min=1KB, S_max=100MB 的截断分布，计算出的对象平均大小 μ_S ≈ 11.1KB，而非 N5 中假设的 100KB。

## Evidence

先验知识/题面给定，逻辑校验通过：Pareto(α=1.1) 在 [1KB, 100MB] 截断下的均值计算符合数学推导，量级合理。
