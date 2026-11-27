# N149: 更新对象的平均大小 E[S_updated] 等于整体对象平均大小 E[S] = 11.1KB (N41)，因为更新率与对象大小无关（均匀更新假设），故更新对象

- **status**: verified
- **level**: L4
- **source**: derived
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N64

## Claim

更新对象的平均大小 E[S_updated] 等于整体对象平均大小 E[S] = 11.1KB (N41)，因为更新率与对象大小无关（均匀更新假设），故更新对象的大小分布仍为 Pareto(α=1.1) 截断分布。

## Corrected Claim

更新对象的平均大小 E[S_updated] 等于整体对象平均大小 E[S] = 11.1KB (N41)，因为更新率与对象大小无关（均匀更新假设），故更新对象的大小分布仍为 Pareto(α=1.1) 截断分布。

## Evidence

先验知识/题面给定，逻辑校验通过：均匀更新假设下，更新对象的大小分布与整体分布一致，故期望值相等。
