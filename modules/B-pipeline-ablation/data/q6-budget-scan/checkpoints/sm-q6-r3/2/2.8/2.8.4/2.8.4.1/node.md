# N297: Zipf参数α的无偏估计公式（基于对数线性回归）：ln(f_r) = ln(C) - α * ln(r)，其中α = -slope，C = exp(interc

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N101

## Claim

Zipf参数α的无偏估计公式（基于对数线性回归）：ln(f_r) = ln(C) - α * ln(r)，其中α = -slope，C = exp(intercept)；需剔除头部异常值（Top 1-5%）以避免长尾噪声导致斜率偏差，标准误差SE(α) ≈ 0.05-0.15

## Corrected Claim

Zipf参数α的无偏估计公式（基于对数线性回归）：ln(f_r) = ln(C) - α * ln(r)，其中α = -slope，C = exp(intercept)；需剔除头部异常值（Top 1-5%）以避免长尾噪声导致斜率偏差，标准误差SE(α) ≈ 0.05-0.15

## Evidence

先验知识/题面给定，逻辑校验通过：Zipf定律的对数线性回归形式 ln(f) = ln(C) - αln(r) 是标准统计方法，α为斜率负值，C为截距指数，剔除头部异常值以符合幂律长尾特性，SE量级0.05-0.15符合常见经验估计误差范围。
