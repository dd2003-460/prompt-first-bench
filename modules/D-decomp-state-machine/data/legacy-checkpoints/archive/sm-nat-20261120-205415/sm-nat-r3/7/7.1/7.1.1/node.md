# N200: 在 α=1.1 的 Pareto 分布下，无截断时对象大小期望 E[S] 发散（因 α<2），必须引入物理截断上限 S_max（如 100MB 或 1GB）才能

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N75

## Claim

在 α=1.1 的 Pareto 分布下，无截断时对象大小期望 E[S] 发散（因 α<2），必须引入物理截断上限 S_max（如 100MB 或 1GB）才能定义有限期望，该截断值需基于 CDN 实际对象大小分布的 99.9 分位数确定

## Corrected Claim

在 α=1.1 的 Pareto 分布下，无截断时对象大小期望 E[S] 发散（因 α<2），必须引入物理截断上限 S_max（如 100MB 或 1GB）才能定义有限期望，该截断值需基于 CDN 实际对象大小分布的 99.9 分位数确定

## Evidence

先验知识/题面给定，逻辑校验通过：Pareto分布α<2时期望发散是数学定理，截断后期望有限且需基于实际分布确定截断值符合工程实践。
