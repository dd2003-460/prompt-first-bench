# N45: 计算冷对象（Bottom 90%）的平均大小 S_cold_avg，公式为 S_cold_avg = (∫_{x_q90}^{x_max} x * f_size

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N11

## Claim

计算冷对象（Bottom 90%）的平均大小 S_cold_avg，公式为 S_cold_avg = (∫_{x_q90}^{x_max} x * f_size(x) dx) / P(Size > x_q90)，该值受 Pareto 尾部截断 x_max 影响极大，需确定 x_max 以完成计算。

## Corrected Claim

计算冷对象（Bottom 90%）的平均大小 S_cold_avg，公式为 S_cold_avg = (∫_{x_q90}^{x_max} x * f_size(x) dx) / P(Size > x_q90)，该值受 Pareto 尾部截断 x_max 影响极大，需确定 x_max 以完成计算。

## Evidence

先验知识/题面给定，逻辑校验通过：公式符合条件期望的定义，且长尾分布（Pareto）的尾部截断确实对均值计算有显著影响，逻辑自洽。
