# N136: 尾部 90% 对象（Bottom 90000）的平均大小 S_tail90% 的精确值需通过联合分布积分 ∫_{q∈Tail90%} E[S|q] f(q) d

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N42

## Claim

尾部 90% 对象（Bottom 90000）的平均大小 S_tail90% 的精确值需通过联合分布积分 ∫_{q∈Tail90%} E[S|q] f(q) dq 计算，无法直接由 ρ=-0.3 线性推导

## Corrected Claim

尾部 90% 对象（Bottom 90000）的平均大小 S_tail90% 的精确值需通过联合分布积分 ∫_{q∈Tail90%} E[S|q] f(q) dq 计算，无法直接由 ρ=-0.3 线性推导

## Evidence

先验知识/题面给定，逻辑校验通过：尾部90%对象的平均大小是条件期望的积分，取决于联合分布的具体形态，仅凭相关系数ρ=-0.3（线性相关度量）无法唯一确定非线性或高阶矩的积分值，逻辑自洽。
