# N112: 日均总请求量的精确计算公式为 R_total_daily = Total_Download_Bytes / s_avg_bytes，其中 s_avg_bytes

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N34

## Claim

日均总请求量的精确计算公式为 R_total_daily = Total_Download_Bytes / s_avg_bytes，其中 s_avg_bytes 必须使用加权平均对象大小（N16中为1.85MB，N34中误用2.05MB需修正），修正后日均请求量 = 2,000,000 MB / 1.85 MB ≈ 1,081,081 次/天

## Corrected Claim

日均总请求量的精确计算公式为 R_total_daily = Total_Download_Bytes / s_avg_bytes，其中 s_avg_bytes 必须使用加权平均对象大小（N16中为1.85MB，N34中误用2.05MB需修正），修正后日均请求量 = 2,000,000 MB / 1.85 MB ≈ 1,081,081 次/天

## Evidence

先验知识/题面给定，逻辑校验通过：公式 R = Total_Bytes / Avg_Size 符合定义，数值计算 2,000,000 / 1.85 ≈ 1,081,081 准确无误。
