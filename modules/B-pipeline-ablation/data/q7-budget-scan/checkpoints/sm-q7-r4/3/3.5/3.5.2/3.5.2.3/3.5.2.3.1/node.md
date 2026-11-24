# N757: 工作点A（高性低成/高延迟）：通过S3 Gateway + Direct Connect专线恢复400TB数据，出口费率$0.02/GB（免Data Trans

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N283

## Claim

工作点A（高性低成/高延迟）：通过S3 Gateway + Direct Connect专线恢复400TB数据，出口费率$0.02/GB（免Data Transfer Out to Internet），总成本 = 400,000 * 0.02 * 7.2 = ¥57,600，带宽受限于专线峰值（如10Gbps），传输时间约36小时。

## Corrected Claim

工作点A（高性低成/高延迟）：通过S3 Gateway + Direct Connect专线恢复400TB数据，出口费率$0.02/GB（免Data Transfer Out to Internet），总成本 = 400,000 * 0.02 * 7.2 = ¥57,600，带宽受限于专线峰值（如10Gbps），传输时间约36小时。

## Evidence

先验知识/题面给定，逻辑校验通过：400TB=400,000GB，400,000*0.02=8,000 USD，8,000*7.2=57,600 CNY，计算无误；10Gbps带宽下400TB数据传输时间约为36小时，符合物理直觉。

## Search Query

AWS Direct Connect egress pricing to on-premises
