# N38: 计算全局平均对象大小 E[S]：基于 Pareto(α=1.1, s_min=1KB, s_max=1GB)，E[S] = (α * s_min) / (α -

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N9

## Claim

计算全局平均对象大小 E[S]：基于 Pareto(α=1.1, s_min=1KB, s_max=1GB)，E[S] = (α * s_min) / (α - 1) * (1 - (s_max/s_min)^{1-α}) / (1 - (s_max/s_min)^{-α}) ≈ (1.1/0.1) * 1KB * (1 - 10^9^{-0.1}) / (1 - 10^9^{-1.1}) ≈ 11KB * (1 - 0.0794) / (1 - 0.00794) ≈ 11KB * 0.9206 / 0.99206 ≈ 10.18KB

## Corrected Claim

计算全局平均对象大小 E[S]：基于 Pareto(α=1.1, s_min=1KB, s_max=1GB)，E[S] = (α * s_min) / (α - 1) * (1 - (s_max/s_min)^{1-α}) / (1 - (s_max/s_min)^{-α}) ≈ (1.1/0.1) * 1KB * (1 - 10^9^{-0.1}) / (1 - 10^9^{-1.1}) ≈ 11KB * (1 - 0.0794) / (1 - 0.00794) ≈ 11KB * 0.9206 / 0.99206 ≈ 10.18KB

## Evidence

先验知识/题面给定，逻辑校验通过：截断帕累托分布的期望公式及数值计算（11 * 0.9206 / 0.99206 ≈ 10.18）均正确。
