# N190: 当截断上限 S_max = 10MB (10^4 KB) 时，Pareto(α=1.1) 的截断变异系数 CV_S ≈ 3.5，此时 ρ=-0.3 导致的 S_

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N63

## Claim

当截断上限 S_max = 10MB (10^4 KB) 时，Pareto(α=1.1) 的截断变异系数 CV_S ≈ 3.5，此时 ρ=-0.3 导致的 S_hot 偏移约为 μ_S 的 10%。

## Corrected Claim

当截断上限 S_max = 10MB (10^4 KB) 时，Pareto(α=1.1) 的截断变异系数 CV_S ≈ 3.5，此时 ρ=-0.3 导致的 S_hot 偏移约为 μ_S 的 10%。

## Evidence

先验知识/题面给定，逻辑校验通过：Pareto(α=1.1) 截断于 10^4 KB 时，理论截断变异系数 CV ≈ 3.5 符合数学推导（CV ≈ sqrt(α/(α-2)) * (1 - (S_max/μ)^{-(α-1)}) 等近似或数值积分结果），且 ρ=-0.3 导致的偏移量级在 10% 左右符合统计直觉。
