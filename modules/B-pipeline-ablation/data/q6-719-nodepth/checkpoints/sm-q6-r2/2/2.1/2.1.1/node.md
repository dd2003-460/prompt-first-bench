# N68: 公有云CDN的基础设施成本 C_infra_public 主要体现为按请求计费的API调用费，公式为 C_infra_public = Q_day * P_re

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N12

## Claim

公有云CDN的基础设施成本 C_infra_public 主要体现为按请求计费的API调用费，公式为 C_infra_public = Q_day * P_request_public / 1000 * 1000，其中 P_request_public 为每千次请求的单价（¥/1000 requests）。

## Corrected Claim

公有云CDN的基础设施成本 C_infra_public 主要体现为按请求计费的API调用费，公式为 C_infra_public = Q_day * P_request_public / 1000 * 1000，其中 P_request_public 为每千次请求的单价（¥/1000 requests）。

## Evidence

先验知识/题面给定，逻辑校验通过
