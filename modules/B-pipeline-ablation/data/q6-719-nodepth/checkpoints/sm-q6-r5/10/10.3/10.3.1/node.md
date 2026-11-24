# N384: 读请求成本权重w_read=1.0：读请求产生下行带宽成本，按CDN流量计费，每千请求成本 = (R_read_daily * s_avg * (1-H) * 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N129

## Claim

读请求成本权重w_read=1.0：读请求产生下行带宽成本，按CDN流量计费，每千请求成本 = (R_read_daily * s_avg * (1-H) * P_bw) / 1000，其中R_read_daily = R_daily * 0.95。

## Corrected Claim

读请求成本权重w_read=1.0：读请求产生下行带宽成本，按CDN流量计费，每千请求成本 = (R_read_daily * s_avg * (1-H) * P_bw) / 1000，其中R_read_daily = R_daily * 0.95。

## Evidence

先验知识/题面给定，逻辑校验通过
