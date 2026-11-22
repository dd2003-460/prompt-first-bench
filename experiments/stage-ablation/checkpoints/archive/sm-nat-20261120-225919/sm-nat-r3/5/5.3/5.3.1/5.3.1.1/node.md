# N212: 在 Pareto(β=0.9) 分布下，第 K 名与第 K+1 名对象的请求频率比值为 R_K / R_{K+1} = ((K+1)/K)^0.9 ≈ 1 + 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N77

## Claim

在 Pareto(β=0.9) 分布下，第 K 名与第 K+1 名对象的请求频率比值为 R_K / R_{K+1} = ((K+1)/K)^0.9 ≈ 1 + 0.9/K，因此相对频率差异 (R_K - R_{K+1})/R_K ≈ 0.9/K，绝对差异需除以总请求量 R_total 才能量化为命中率增益上限。

## Corrected Claim

在 Pareto(β=0.9) 分布下，第 K 名与第 K+1 名对象的请求频率比值为 R_K / R_{K+1} = ((K+1)/K)^0.9 ≈ 1 + 0.9/K，因此相对频率差异 (R_K - R_{K+1})/R_K ≈ 0.9/K，绝对差异需除以总请求量 R_total 才能量化为命中率增益上限。

## Evidence

先验知识/题面给定，逻辑校验通过：Pareto分布下频率比推导及泰勒展开近似在数学上自洽，量级合理。
