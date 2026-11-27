# N115: 在 ρ=-0.3 负相关约束下，Top 10 对象的大小分布并非均匀最小，而是服从截断 Pareto(α=1.1) 的条件分布，其平均大小 E[s|Top10]

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N34

## Claim

在 ρ=-0.3 负相关约束下，Top 10 对象的大小分布并非均匀最小，而是服从截断 Pareto(α=1.1) 的条件分布，其平均大小 E[s|Top10] 可通过 ∫_{s_min}^{s_99.99} s * f(s|h_top) ds 计算，该值直接影响 H_top10 的分子项

## Corrected Claim

在 ρ=-0.3 负相关约束下，Top 10 对象的大小分布并非均匀最小，而是服从截断 Pareto(α=1.1) 的条件分布，其平均大小 E[s|Top10] 可通过 ∫_{s_min}^{s_99.99} s * f(s|h_top) ds 计算，该值直接影响 H_top10 的分子项

## Evidence

先验知识/题面给定，逻辑校验通过：在负相关约束下，Top-K 对象通常对应分布尾部，截断 Pareto 分布符合长尾特征，积分公式在数学上正确描述了条件期望的计算逻辑。
