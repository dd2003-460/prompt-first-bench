# N136: 按流量计费的成本模型：C_traffic_billing = V_total * P_bw_traffic_per_GB，其中 V_total = 2TB/da

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N39

## Claim

按流量计费的成本模型：C_traffic_billing = V_total * P_bw_traffic_per_GB，其中 V_total = 2TB/day * 30 = 60TB/month = 60,000GB，P_bw_traffic_per_GB 为公有云 CDN 流量单价（如 ¥0.22/GB），则 C_traffic_billing ≈ ¥13,200/月

## Corrected Claim

按流量计费的成本模型：C_traffic_billing = V_total * P_bw_traffic_per_GB，其中 V_total = 2TB/day * 30 = 60TB/month = 60,000GB，P_bw_traffic_per_GB 为公有云 CDN 流量单价（如 ¥0.22/GB），则 C_traffic_billing ≈ ¥13,200/月

## Evidence

先验知识/题面给定，逻辑校验通过：2TB/day * 30 = 60TB = 60,000GB，60,000GB * ¥0.22/GB = ¥13,200，计算无误且量级合理。
