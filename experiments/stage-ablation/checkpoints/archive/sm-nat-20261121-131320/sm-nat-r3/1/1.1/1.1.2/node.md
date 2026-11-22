# N20: Pareto(α=1.1) 大小分布的截断上限 S_max：由于 α=1.1 < 2，分布无有限方差，需设定 S_max 以截断积分，通常取 S_max = 1

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N5

## Claim

Pareto(α=1.1) 大小分布的截断上限 S_max：由于 α=1.1 < 2，分布无有限方差，需设定 S_max 以截断积分，通常取 S_max = 100 * E[S] 或基于实际 CDN 对象最大大小（如 100MB）进行敏感性分析。

## Corrected Claim

Pareto(α=1.1) 大小分布的截断上限 S_max：由于 α=1.1 < 2，分布无有限方差，需设定 S_max 以截断积分，通常取 S_max = 100 * E[S] 或基于实际 CDN 对象最大大小（如 100MB）进行敏感性分析。

## Evidence

父节点级核验未通过：有冗余（子节点A、B、C本质上是对同一参数 S_max 的不同取值（保守、标准、极端）的列举，属于同一维度的参数扫描，而非正交的不同概念或方法论分支。虽然它们覆盖了不同的应用场景，但在知识分解上，它们应被合并为一个节点，内部通过变量或列表区分不同取值。）
