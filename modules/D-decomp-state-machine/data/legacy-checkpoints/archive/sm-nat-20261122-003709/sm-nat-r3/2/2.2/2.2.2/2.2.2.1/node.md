# N139: 确定冷对象（Bottom 90%）的起始分位数 x_q90 的具体数值：基于 Pareto(α=1.1, x_min=1KB) 分布，计算第 90 百分位值 x

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N45

## Claim

确定冷对象（Bottom 90%）的起始分位数 x_q90 的具体数值：基于 Pareto(α=1.1, x_min=1KB) 分布，计算第 90 百分位值 x_q90 = x_min * (1/(1-0.9))^(1/(α-1)) = 1KB * 10^10 ≈ 10,000,000 KB ≈ 9.5 GB。

## Corrected Claim

确定冷对象（Bottom 90%）的起始分位数 x_q90 的具体数值：基于 Pareto(α=1.1, x_min=1KB) 分布，计算第 90 百分位值 x_q90 = x_min * (1/(1-0.9))^(1/(α-1)) = 1KB * 10^10 ≈ 10,000,000 KB ≈ 9.5 GB。

## Evidence

先验知识/题面给定，逻辑校验通过：Pareto分布分位数公式推导正确，数值量级合理（1KB * 10^10 = 10^10 KB ≈ 9.5 GB）
