# N20: Pareto(α=1.1) 大小分布的截断上限 S_max：由于 α=1.1 < 2，分布无有限方差，需设定 S_max 以截断积分，通常取 S_max = 1

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N5

## Claim

Pareto(α=1.1) 大小分布的截断上限 S_max：由于 α=1.1 < 2，分布无有限方差，需设定 S_max 以截断积分，通常取 S_max = 100 * E[S] 或基于实际 CDN 对象最大大小（如 100MB）进行敏感性分析。

## Corrected Claim

Pareto(α=1.1) 大小分布的截断上限 S_max：由于 α=1.1 < 2，分布无有限方差，需设定 S_max 以截断积分，通常取 S_max = 100 * E[S] 或基于实际 CDN 对象最大大小（如 100MB）进行敏感性分析。

## Evidence

先验知识/题面给定，逻辑校验通过：Pareto分布α<2时方差确实发散，截断处理是标准做法，量级建议合理。
