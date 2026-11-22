# N117: 无界 Pareto 期望的基准项 E_unbounded = α * s_min / (α - 1)，代入 α=1.1, s_min=1KB 计算得 11KB，

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N38

## Claim

无界 Pareto 期望的基准项 E_unbounded = α * s_min / (α - 1)，代入 α=1.1, s_min=1KB 计算得 11KB，作为截断修正前的理论上限

## Corrected Claim

无界 Pareto 期望的基准项 E_unbounded = α * s_min / (α - 1)，代入 α=1.1, s_min=1KB 计算得 11KB，作为截断修正前的理论上限

## Evidence

先验知识/题面给定，逻辑校验通过：Pareto分布期望公式 E = α*s_min/(α-1) 代入 α=1.1, s_min=1KB 计算得 1.1*1/0.1 = 11KB，数学推导正确且量级合理。
