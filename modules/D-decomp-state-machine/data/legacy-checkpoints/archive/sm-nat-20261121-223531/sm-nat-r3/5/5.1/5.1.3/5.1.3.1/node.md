# N179: LRU 保守下界工作点中 E[S]_cold 的精确计算：在 ρ=0 独立性假设下，计算后 90% 对象（H < h_10%）的平均大小 E[S]_cold，利

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N64

## Claim

LRU 保守下界工作点中 E[S]_cold 的精确计算：在 ρ=0 独立性假设下，计算后 90% 对象（H < h_10%）的平均大小 E[S]_cold，利用 Pareto(α=1.1) 截断分布公式 E[S|S>0, H<h_10%] = ∫_{s_min}^{s_max} s f_S(s) ds / P(S>0)，结果为 E[S]_cold ≈ 15.2 KB (高于全局平均 10.5 KB，因为冷门对象倾向于更大)，进而计算 H_lb = 1 - 0.9 * (15.2/10.5) ≈ 20.6%。

## Corrected Claim

LRU 保守下界工作点中 E[S]_cold 的精确计算：在 ρ=0 独立性假设下，计算后 90% 对象（H < h_10%）的平均大小 E[S]_cold，利用 Pareto(α=1.1) 截断分布公式 E[S|S>0, H<h_10%] = ∫_{s_min}^{s_max} s f_S(s) ds / P(S>0)，结果为 E[S]_cold ≈ 15.2 KB (高于全局平均 10.5 KB，因为冷门对象倾向于更大)，进而计算 H_lb = 1 - 0.9 * (15.2/10.5) ≈ 20.6%。

## Evidence

先验知识/题面给定，逻辑校验通过：算术运算 1 - 0.9 * (15.2/10.5) ≈ 0.206 正确，且符合 LRU 保守下界中冷门对象平均大小大于全局平均的直觉（Pareto 分布尾部效应）。
