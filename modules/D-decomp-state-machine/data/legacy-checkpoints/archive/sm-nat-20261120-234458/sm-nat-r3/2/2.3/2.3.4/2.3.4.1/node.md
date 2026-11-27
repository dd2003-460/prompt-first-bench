# N135: 头部 10% 对象（Top 10000）的平均大小 S_top10% 的精确值需通过联合分布积分 ∫_{q∈Top10%} E[S|q] f(q) dq 计算，

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N42

## Claim

头部 10% 对象（Top 10000）的平均大小 S_top10% 的精确值需通过联合分布积分 ∫_{q∈Top10%} E[S|q] f(q) dq 计算，无法直接由 ρ=-0.3 线性推导

## Corrected Claim

头部 10% 对象（Top 10000）的平均大小 S_top10% 的精确值需通过联合分布积分 ∫_{q∈Top10%} E[S|q] f(q) dq 计算，无法直接由 ρ=-0.3 线性推导

## Evidence

先验知识/题面给定，逻辑校验通过：相关系数仅描述线性趋势，无法确定条件期望的具体函数形式，因此必须通过联合分布积分计算精确值，逻辑自洽。
