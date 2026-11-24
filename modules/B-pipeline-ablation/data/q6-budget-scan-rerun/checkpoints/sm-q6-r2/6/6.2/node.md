# N113: 平均 RPS 的精确计算为 RPS_avg = R_total_daily / 86400，基于修正后的日均请求量 1,081,081 次，RPS_avg ≈ 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N34

## Claim

平均 RPS 的精确计算为 RPS_avg = R_total_daily / 86400，基于修正后的日均请求量 1,081,081 次，RPS_avg ≈ 12.5 RPS；此值是带宽成本归一化和 CDN 容量规划的基础分母

## Corrected Claim

平均 RPS 的精确计算为 RPS_avg = R_total_daily / 86400，基于修正后的日均请求量 1,081,081 次，RPS_avg ≈ 12.5 RPS；此值是带宽成本归一化和 CDN 容量规划的基础分母

## Evidence

先验知识/题面给定，逻辑校验通过：1,081,081 / 86400 ≈ 12.51，计算准确且量纲正确
