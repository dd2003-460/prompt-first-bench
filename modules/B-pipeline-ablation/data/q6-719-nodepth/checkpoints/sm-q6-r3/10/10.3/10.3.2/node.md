# N385: 写请求成本权重w_write=0.5：写请求（上传）通常按入口带宽计费或免费，但需承担源站存储与处理成本，每千请求成本 = (R_write_daily * s

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N129

## Claim

写请求成本权重w_write=0.5：写请求（上传）通常按入口带宽计费或免费，但需承担源站存储与处理成本，每千请求成本 = (R_write_daily * s_avg * P_storage) / 1000，其中R_write_daily = R_daily * 0.05，P_storage为存储单价。

## Corrected Claim

写请求成本权重w_write=0.5：写请求（上传）通常按入口带宽计费或免费，但需承担源站存储与处理成本，每千请求成本 = (R_write_daily * s_avg * P_storage) / 1000，其中R_write_daily = R_daily * 0.05，P_storage为存储单价。

## Evidence

先验知识/题面给定，逻辑校验通过
