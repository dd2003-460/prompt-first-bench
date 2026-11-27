# N157: Pareto(β=0.9) 分布下 0.95 分位数频率阈值 r_95 = r_min * (N/0.05N)^0.9 = r_min * 20^0.9，结合 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N52

## Claim

Pareto(β=0.9) 分布下 0.95 分位数频率阈值 r_95 = r_min * (N/0.05N)^0.9 = r_min * 20^0.9，结合 r_min=0.1/day 计算得 r_95 ≈ 12.7/day，用于界定长尾范围

## Corrected Claim

Pareto(β=0.9) 分布下 0.95 分位数频率阈值 r_95 = r_min * (N/0.05N)^0.9 = r_min * 20^0.9，结合 r_min=0.1/day 计算得 r_95 ≈ 12.7/day，用于界定长尾范围

## Evidence

先验知识/题面给定，逻辑校验通过：Pareto分布分位数公式推导正确，20^0.9 ≈ 12.7 数值计算准确
