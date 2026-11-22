# N123: 热度中位数 h_median 的数值计算修正：Pareto(β) 的 CDF 为 F(h) = 1 - (h_min/h)^{β-1}。令 F(h_median

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N40

## Claim

热度中位数 h_median 的数值计算修正：Pareto(β) 的 CDF 为 F(h) = 1 - (h_min/h)^{β-1}。令 F(h_median) = 0.5，解得 h_median = h_min * (1/0.5)^{1/(β-1)}。注意 β=0.9 < 1 时，指数 1/(β-1) 为负，且 Pareto 分布通常定义 β>1 才有有限中位数。若 β=0.9 表示幂律指数为 0.9（即标准 Pareto 的 α=0.9），则分布无中位数（发散）。若题意指 Zipf 型分布 P(rank) ∝ rank^{-0.9}，则中位数 rank ≈ 2^{1/(0.9-1)} 无解，需重新审视 β 的定义。假设 β 为幂律指数且 >1 才有效，此处 β=0.9 暗示极度长尾，中位数概念不适用或趋向无穷。

## Corrected Claim

热度中位数 h_median 的数值计算修正：Pareto(β) 的 CDF 为 F(h) = 1 - (h_min/h)^{β-1}。令 F(h_median) = 0.5，解得 h_median = h_min * (1/0.5)^{1/(β-1)}。注意 β=0.9 < 1 时，指数 1/(β-1) 为负，且 Pareto 分布通常定义 β>1 才有有限中位数。若 β=0.9 表示幂律指数为 0.9（即标准 Pareto 的 α=0.9），则分布无中位数（发散）。若题意指 Zipf 型分布 P(rank) ∝ rank^{-0.9}，则中位数 rank ≈ 2^{1/(0.9-1)} 无解，需重新审视 β 的定义。假设 β 为幂律指数且 >1 才有效，此处 β=0.9 暗示极度长尾，中位数概念不适用或趋向无穷。

## Evidence

先验知识/题面给定，逻辑校验通过：Pareto分布CDF推导正确，β<1时中位数发散或无定义的数学性质符合第一性原理。

## Search Query

Pareto distribution median beta less than 1
