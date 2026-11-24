# N479: 在日均下载 2TB (月均 60TB) 且请求量 204.8 万/天的工作点下，公有云 CDN 的实际带宽单价 P_actual 为 ¥0.25/GB * 0.

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N156

## Claim

在日均下载 2TB (月均 60TB) 且请求量 204.8 万/天的工作点下，公有云 CDN 的实际带宽单价 P_actual 为 ¥0.25/GB * 0.6 = ¥0.15/GB，由此推算的每千请求带宽成本 C_bw_per_1000req 为 (2000GB * ¥0.15/GB) / 2048 ≈ ¥0.147/1000req。

## Corrected Claim

在日均下载 2TB (月均 60TB) 且请求量 204.8 万/天的工作点下，公有云 CDN 的实际带宽单价 P_actual 为 ¥0.25/GB * 0.6 = ¥0.15/GB，由此推算的每千请求带宽成本 C_bw_per_1000req 为 (2000GB * ¥0.15/GB) / 2048 ≈ ¥0.147/1000req。

## Evidence

先验知识/题面给定，逻辑校验通过：2000GB * 0.15 / 2048 ≈ 0.14647，四舍五入为0.147，计算无误。
