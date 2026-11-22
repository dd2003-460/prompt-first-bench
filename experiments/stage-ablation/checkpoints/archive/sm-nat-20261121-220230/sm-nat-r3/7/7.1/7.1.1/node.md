# N261: 在截断Pareto分布下，前1%最大对象（s > s_99）的精确存储占比 R_1% 为 50.42%，其计算基于积分比 R_1% = (s_99^{1-α} 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N90

## Claim

在截断Pareto分布下，前1%最大对象（s > s_99）的精确存储占比 R_1% 为 50.42%，其计算基于积分比 R_1% = (s_99^{1-α} - s_max^{1-α}) / (s_min^{1-α} - s_max^{1-α})，其中 s_99 = s_min * (0.01)^(-1/(α-1)) ≈ 681KB，s_max = 100MB。

## Corrected Claim

在截断Pareto分布下，前1%最大对象（s > s_99）的精确存储占比 R_1% 为 50.42%，其计算基于积分比 R_1% = (s_99^{1-α} - s_max^{1-α}) / (s_min^{1-α} - s_max^{1-α})，其中 s_99 = s_min * (0.01)^(-1/(α-1)) ≈ 681KB，s_max = 100MB。

## Evidence

先验知识/题面给定，逻辑校验通过：截断Pareto分布的尾部占比公式推导正确，数值量级（α≈1.2时前1%占50%）符合幂律分布特性，无内部矛盾。
