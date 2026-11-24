# N552: 年 OSS GET 请求费用估算：Annual_Request_Fee = (R_daily / 10,000) * Unit_Price_GET * 365 

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N181

## Claim

年 OSS GET 请求费用估算：Annual_Request_Fee = (R_daily / 10,000) * Unit_Price_GET * 365 = (1,638,400 / 10,000) * ¥0.01 * 365 ≈ ¥598 / 年（相对于存储费可忽略）。

## Corrected Claim

年 OSS GET 请求费用估算：Annual_Request_Fee = (R_daily / 10,000) * Unit_Price_GET * 365 = (1,638,400 / 10,000) * ¥0.01 * 365 ≈ ¥598 / 年（相对于存储费可忽略）。

## Evidence

先验知识/题面给定，逻辑校验通过：算术计算 (1638400/10000)*0.01*365 = 598.016 正确，量级合理，符合OSS计费逻辑。
