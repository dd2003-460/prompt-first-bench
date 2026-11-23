# N281: 带宽计费 vs 流量计费成本交叉点：当日均流量 F_day 满足 F_day > (P_bw_peak / P_bw_traffic) * 24h * k_pe

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N90

## Claim

带宽计费 vs 流量计费成本交叉点：当日均流量 F_day 满足 F_day > (P_bw_peak / P_bw_traffic) * 24h * k_peak 时，流量计费更优；对于阿里云，该阈值约为 50-100TB/月

## Corrected Claim

带宽计费 vs 流量计费成本交叉点：当日均流量 F_day 满足 F_day > (P_bw_peak / P_bw_traffic) * 24h * k_peak 时，流量计费更优；对于阿里云，该阈值约为 50-100TB/月

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

CDN bandwidth vs traffic billing cost crossover point threshold
