# N305: 公有云CDN跨AZ请求占比 P_cross_az_request 的典型取值：若采用就近接入且AZ内无足够容量则跨AZ，通常 P_cross_az_reques

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N106

## Claim

公有云CDN跨AZ请求占比 P_cross_az_request 的典型取值：若采用就近接入且AZ内无足够容量则跨AZ，通常 P_cross_az_request ∈ [0.1, 0.4]，具体值取决于边缘节点容量规划与用户地理分布，需通过云厂商监控数据获取。

## Corrected Claim

公有云CDN跨AZ请求占比 P_cross_az_request 的典型取值：若采用就近接入且AZ内无足够容量则跨AZ，通常 P_cross_az_request ∈ [0.1, 0.4]，具体值取决于边缘节点容量规划与用户地理分布，需通过云厂商监控数据获取。

## Evidence

先验知识/题面给定，逻辑校验通过
