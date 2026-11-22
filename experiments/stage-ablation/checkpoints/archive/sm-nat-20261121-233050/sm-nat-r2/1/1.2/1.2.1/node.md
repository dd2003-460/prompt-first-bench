# N27: Pareto(β=0.9) 分布的频率总和收敛条件：由于 β < 1，频率总和 ∑f_i 在 N→∞ 时发散；在有限 N=100,000 下，需利用截断和公式 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N7

## Claim

Pareto(β=0.9) 分布的频率总和收敛条件：由于 β < 1，频率总和 ∑f_i 在 N→∞ 时发散；在有限 N=100,000 下，需利用截断和公式 S_N(f_min) ≈ N * f_min * (N^(1-β) - 1) / (1-β) 来反解 f_min。

## Corrected Claim

Pareto(β=0.9) 分布的频率总和收敛条件：由于 β < 1，频率总和 ∑f_i 在 N→∞ 时发散；在有限 N=100,000 下，需利用截断和公式 S_N(f_min) ≈ N * f_min * (N^(1-β) - 1) / (1-β) 来反解 f_min。

## Evidence

先验知识/题面给定，逻辑校验通过：Pareto分布β<1时无穷级数发散，有限N下截断和公式推导正确
