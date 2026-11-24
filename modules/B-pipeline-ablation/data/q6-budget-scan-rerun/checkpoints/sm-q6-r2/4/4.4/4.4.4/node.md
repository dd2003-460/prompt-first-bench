# N122: 公有云回源带宽成本 C_backhaul_cloud 的计算公式：C_backhaul_cloud = (1 - H_cloud) * Daily_Traffi

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N25

## Claim

公有云回源带宽成本 C_backhaul_cloud 的计算公式：C_backhaul_cloud = (1 - H_cloud) * Daily_Traffic_GB * Price_backhaul_per_GB / Q_day * 1000，其中 Price_backhaul_per_GB 为回源单价（通常高于边缘流量单价 2-5 倍）

## Corrected Claim

公有云回源带宽成本 C_backhaul_cloud 的计算公式：C_backhaul_cloud = (1 - H_cloud) * Daily_Traffic_GB * Price_backhaul_per_GB / Q_day * 1000，其中 Price_backhaul_per_GB 为回源单价（通常高于边缘流量单价 2-5 倍）

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

CDN origin fetch bandwidth cost per GB vs edge traffic cost
