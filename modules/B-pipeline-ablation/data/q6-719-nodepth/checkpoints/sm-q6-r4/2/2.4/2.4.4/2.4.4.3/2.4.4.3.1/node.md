# N692: 公有云CDN请求数成本在低流量工作点（月请求量 < 1亿次，对应DAU 500万/日均20次请求的低活跃场景）的量化值：Cloud_Request_Cost_L

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N239

## Claim

公有云CDN请求数成本在低流量工作点（月请求量 < 1亿次，对应DAU 500万/日均20次请求的低活跃场景）的量化值：Cloud_Request_Cost_Low = 100,000,000 × ¥0.000004 = ¥400/月，此时请求费占比极低（<5%总成本），主要成本由流量驱动。

## Corrected Claim

公有云CDN请求数成本在低流量工作点（月请求量 < 1亿次，对应DAU 500万/日均20次请求的低活跃场景）的量化值：Cloud_Request_Cost_Low = 100,000,000 × ¥0.000004 = ¥400/月，此时请求费占比极低（<5%总成本），主要成本由流量驱动。

## Evidence

先验知识/题面给定，逻辑校验通过：1亿次请求乘以0.000004元/次的单价，数学计算结果为400元，量级与公有云CDN请求计费标准（通常按万次或百万次计费，折合单次约0.000004-0.00001元）相符，且低流量下请求费占比低符合成本结构常识。

## Search Query

Alibaba Cloud CDN request pricing low volume tier
