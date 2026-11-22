# N355: 机器人/无效咨询的识别规则与过滤阈值：定义无效咨询为 (停留时间 < 5s) 或 (IP地址在已知爬虫黑名单) 或 (同一用户24h内重复访问>3次)；需量化过

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N104

## Claim

机器人/无效咨询的识别规则与过滤阈值：定义无效咨询为 (停留时间 < 5s) 或 (IP地址在已知爬虫黑名单) 或 (同一用户24h内重复访问>3次)；需量化过滤前后咨询量差异 ΔQ_bot，假设 ΔQ_bot = 15%，则 CTR_effective = (Unique_User_Queries * (1 - 0.15)) / Impressions。

## Corrected Claim

机器人/无效咨询的识别规则与过滤阈值：定义无效咨询为 (停留时间 < 5s) 或 (IP地址在已知爬虫黑名单) 或 (同一用户24h内重复访问>3次)；需量化过滤前后咨询量差异 ΔQ_bot，假设 ΔQ_bot = 15%，则 CTR_effective = (Unique_User_Queries * (1 - 0.15)) / Impressions。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

e-commerce bot traffic filtering rules clickthrough rate adjustment
