# N6: 对象大小服从 Pareto(α=1.1) 分布，其数学期望 E[S] 在 α≤1 时发散，α>1 时为有限值 E[S] = α/(α-1) * x_min，需明

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N1

## Claim

对象大小服从 Pareto(α=1.1) 分布，其数学期望 E[S] 在 α≤1 时发散，α>1 时为有限值 E[S] = α/(α-1) * x_min，需明确 x_min（最小对象大小）以计算总数据量与缓存覆盖率

## Corrected Claim

对象大小服从 Pareto(α=1.1) 分布，其数学期望 E[S] 在 α≤1 时发散，α>1 时为有限值 E[S] = α/(α-1) * x_min，需明确 x_min（最小对象大小）以计算总数据量与缓存覆盖率

## Evidence

先验知识/题面给定，逻辑校验通过：Pareto分布的期望公式 E[S] = α/(α-1) * x_min 在 α>1 时成立，且 α≤1 时发散，符合数学定义。
