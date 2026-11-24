# N722: 工作点3（企业级私有云专线）的实际单位成本 Unit_Cost_Actual = F_line_10G / (Daily_Upload_GB × 30)，当日均

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N248

## Claim

工作点3（企业级私有云专线）的实际单位成本 Unit_Cost_Actual = F_line_10G / (Daily_Upload_GB × 30)，当日均上传量为 200GB（题面给定）时，Unit_Cost_Actual = 50,000 / (200 × 30) ≈ ¥8.33/GB，远高于按量付费，证实该策略在低流量下不可行

## Corrected Claim

工作点3（企业级私有云专线）的实际单位成本 Unit_Cost_Actual = F_line_10G / (Daily_Upload_GB × 30)，当日均上传量为 200GB（题面给定）时，Unit_Cost_Actual = 50,000 / (200 × 30) ≈ ¥8.33/GB，远高于按量付费，证实该策略在低流量下不可行

## Evidence

先验知识/题面给定，逻辑校验通过：50000/(200*30) = 8.333...，计算无误，且8.33 > 按量付费通常价格（如0.5-1元/GB），结论成立。
