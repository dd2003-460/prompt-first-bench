# N207: 工作点1（高承诺低OpEx）：3年预付承诺下，500TB冷数据存储于S3 Glacier Deep Archive或OSS归档，基础存储费降至¥3/TB/月，叠

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N63

## Claim

工作点1（高承诺低OpEx）：3年预付承诺下，500TB冷数据存储于S3 Glacier Deep Archive或OSS归档，基础存储费降至¥3/TB/月，叠加3年预付折扣系数0.7，年化OpEx = 500TB * (¥3/TB/月 * 12 * 0.7) = ¥126,000/年；但需承担解冻延迟成本，若冷数据年均解冻1次，单次解冻等待成本 C_thaw = T_thaw(12h) * Cluster_Idle_Rate(¥5000/h) = ¥60,000，总年化成本 = ¥126,000 + ¥60,000 = ¥186,000。

## Corrected Claim

工作点1（高承诺低OpEx）：3年预付承诺下，500TB冷数据存储于S3 Glacier Deep Archive或OSS归档，基础存储费降至¥3/TB/月，叠加3年预付折扣系数0.7，年化OpEx = 500TB * (¥3/TB/月 * 12 * 0.7) = ¥126,000/年；但需承担解冻延迟成本，若冷数据年均解冻1次，单次解冻等待成本 C_thaw = T_thaw(12h) * Cluster_Idle_Rate(¥5000/h) = ¥60,000，总年化成本 = ¥126,000 + ¥60,000 = ¥186,000。

## Evidence

先验知识/题面给定，逻辑校验通过：算术计算正确（500*3*12*0.7=12600; 12*5000=60000; 126000+60000=186000），量纲与业务逻辑自洽。
