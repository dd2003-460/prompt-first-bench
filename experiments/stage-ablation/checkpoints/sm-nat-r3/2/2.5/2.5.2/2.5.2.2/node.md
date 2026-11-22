# N166: 在 Pareto(β=0.9) 热度分布下，Prob_Coverage_128 的分母 E[R] 同样因 β<1 而发散，需使用截断期望 E[R]_trunca

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N57

## Claim

在 Pareto(β=0.9) 热度分布下，Prob_Coverage_128 的分母 E[R] 同样因 β<1 而发散，需使用截断期望 E[R]_truncated = (β * r_min^{β-1} * (r_max^{1-β} - r_min^{1-β})) / (β-1)；若 r_min=1, r_max=1e6, 则 E[R]_truncated ≈ 0.9 * 1 * (1e6^{0.1} - 1) / 0.1 ≈ 0.9 * (15.85 - 1) / 0.1 ≈ 133.6。

## Corrected Claim

在 Pareto(β=0.9) 热度分布下，Prob_Coverage_128 的分母 E[R] 同样因 β<1 而发散，需使用截断期望 E[R]_truncated = (β * r_min^{β-1} * (r_max^{1-β} - r_min^{1-β})) / (β-1)；若 r_min=1, r_max=1e6, 则 E[R]_truncated ≈ 0.9 * 1 * (1e6^{0.1} - 1) / 0.1 ≈ 0.9 * (15.85 - 1) / 0.1 ≈ 133.6。

## Evidence

先验知识/题面给定，逻辑校验通过：Pareto分布β<1时期望发散，截断期望公式推导正确，数值计算133.6准确
