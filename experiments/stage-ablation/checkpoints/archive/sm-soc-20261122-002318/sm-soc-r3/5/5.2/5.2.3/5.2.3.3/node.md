# N227: 似然比 LR = P(D|H1)/P(D|H2) 在 [1.5, 3.0] 区间波动时，后验 P(H1|D) 的边界条件分析：计算使 P(H1|D) = 0.5

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N81

## Claim

似然比 LR = P(D|H1)/P(D|H2) 在 [1.5, 3.0] 区间波动时，后验 P(H1|D) 的边界条件分析：计算使 P(H1|D) = 0.5 的临界似然比 LR_crit，并验证区间 [1.5, 3.0] 是否完全位于 LR_crit 之上。

## Corrected Claim

似然比 LR = P(D|H1)/P(D|H2) 在 [1.5, 3.0] 区间波动时，后验 P(H1|D) 的边界条件分析：计算使 P(H1|D) = 0.5 的临界似然比 LR_crit，并验证区间 [1.5, 3.0] 是否完全位于 LR_crit 之上。

## Evidence

先验知识/题面给定，逻辑校验通过：根据贝叶斯定理，当先验概率 P(H1)=P(H2)=0.5 时，临界似然比 LR_crit = 1；区间 [1.5, 3.0] 完全大于 1，故后验 P(H1|D) > 0.5，逻辑自洽。
