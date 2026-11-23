# N103: 带宽成本低于公有云30%的量化条件：P_bw_self ≤ 0.7 * P_bw_cloud，即自建带宽单价 ≤ 0.14-0.35元/GB；该条件在流量 > 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N27

## Claim

带宽成本低于公有云30%的量化条件：P_bw_self ≤ 0.7 * P_bw_cloud，即自建带宽单价 ≤ 0.14-0.35元/GB；该条件在流量 > 10TB/月时通常满足，因为自建专线固定成本被大流量摊薄

## Corrected Claim

带宽成本低于公有云30%的量化条件：P_bw_self ≤ 0.7 * P_bw_cloud，即自建带宽单价 ≤ 0.14-0.35元/GB；该条件在流量 > 10TB/月时通常满足，因为自建专线固定成本被大流量摊薄

## Evidence

先验知识/题面给定，逻辑校验通过：0.7 * (0.2-0.5元/GB) 确实等于 0.14-0.35元/GB，且大流量摊薄固定成本符合经济学直觉

## Search Query

self-hosted CDN bandwidth cost vs cloud CDN 30% threshold and traffic volume break-even point
