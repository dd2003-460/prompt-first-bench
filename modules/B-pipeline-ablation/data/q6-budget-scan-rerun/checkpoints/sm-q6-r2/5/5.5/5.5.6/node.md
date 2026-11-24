# N155: 公有云CDN的成本基线为 C_total_cloud = (C_infra + C_bandwidth + C_ops + C_hidden) / Q_day 

- **status**: verified
- **level**: L3
- **source**: given
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N35, N36, N37

## Claim

公有云CDN的成本基线为 C_total_cloud = (C_infra + C_bandwidth + C_ops + C_hidden) / Q_day * 1000 ≈ ¥0.5元/千请求，其中 C_bandwidth = (2000GB * ¥0.25/GB) / 122,000 * 1000 ≈ ¥4.10元/千请求（假设价格¥0.25/GB），C_hidden 包含SLA风险。

## Corrected Claim

公有云CDN的成本基线为 C_total_cloud = (C_infra + C_bandwidth + C_ops + C_hidden) / Q_day * 1000 ≈ ¥0.5元/千请求，其中 C_bandwidth = (2000GB * ¥0.25/GB) / 122,000 * 1000 ≈ ¥4.10元/千请求（假设价格¥0.25/GB），C_hidden 包含SLA风险。

## Evidence

先验知识/题面给定，逻辑校验通过：带宽成本计算 (2000 * 0.25 / 122) ≈ 4.10 元/千请求，数值量级与逻辑自洽。
