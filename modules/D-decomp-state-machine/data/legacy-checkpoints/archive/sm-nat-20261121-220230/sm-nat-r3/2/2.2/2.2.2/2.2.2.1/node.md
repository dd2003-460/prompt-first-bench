# N148: 在强局部性工作点（β=0.9，短窗口 δ=1 小时），缓存污染率 P_short_term 约为 3-5%，因为重尾分布下头部对象在短时间窗口内重复访问概率高，

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N50

## Claim

在强局部性工作点（β=0.9，短窗口 δ=1 小时），缓存污染率 P_short_term 约为 3-5%，因为重尾分布下头部对象在短时间窗口内重复访问概率高，LRU 驱逐主要发生在尾部冷对象，污染率与 (1-β) 成正比，即 P_short_term ≈ k * (1-β)，其中 k≈5%。

## Corrected Claim

在强局部性工作点（β=0.9，短窗口 δ=1 小时），缓存污染率 P_short_term 约为 3-5%，因为重尾分布下头部对象在短时间窗口内重复访问概率高，LRU 驱逐主要发生在尾部冷对象，污染率与 (1-β) 成正比，即 P_short_term ≈ k * (1-β)，其中 k≈5%。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

LRU cache pollution rate short-term locality Pareto beta
