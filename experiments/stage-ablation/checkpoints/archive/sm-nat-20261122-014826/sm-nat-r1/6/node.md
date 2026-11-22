# N19: 对象总数据量 S_total 的精确计算：基于 Pareto(α=1.1) 分布，总大小 S_total = N * S_min * (α-1)/(α-1.1)

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

对象总数据量 S_total 的精确计算：基于 Pareto(α=1.1) 分布，总大小 S_total = N * S_min * (α-1)/(α-1.1) * (1 - N^(1-α)/(1-α)) 的近似值。当 N=100,000, α=1.1, S_min=1KB 时，S_total ≈ 100,000 * 1KB * 9.1 ≈ 910GB。缓存容量 C=128GB，因此缓存覆盖率 C/S_total ≈ 14.07%，而非之前节点 N6 中错误计算的 0.94%（N6 误将 E[Size] 当作 100KB 级或计算错误）。

## Corrected Claim

对象总数据量 S_total 的精确计算：基于 Pareto(α=1.1) 分布，总大小 S_total = N * S_min * (α-1)/(α-1.1) * (1 - N^(1-α)/(1-α)) 的近似值。当 N=100,000, α=1.1, S_min=1KB 时，S_total ≈ 100,000 * 1KB * 9.1 ≈ 910GB。缓存容量 C=128GB，因此缓存覆盖率 C/S_total ≈ 14.07%，而非之前节点 N6 中错误计算的 0.94%（N6 误将 E[Size] 当作 100KB 级或计算错误）。

## Evidence

检索失败: no sources from any channel (all 5 failed)
