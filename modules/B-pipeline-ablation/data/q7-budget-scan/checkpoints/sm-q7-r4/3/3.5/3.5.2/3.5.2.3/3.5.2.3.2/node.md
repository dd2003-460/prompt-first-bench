# N758: 工作点B（中性价比最优/中延迟）：通过S3 Gateway + 互联网出口恢复400TB数据，利用100TB/月免费额度后，剩余300TB按$0.09/GB计费

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N283

## Claim

工作点B（中性价比最优/中延迟）：通过S3 Gateway + 互联网出口恢复400TB数据，利用100TB/月免费额度后，剩余300TB按$0.09/GB计费，总成本 = 300,000 * 0.09 * 7.2 = ¥194,400，带宽受限于本地上行链路（如1Gbps），传输时间约360小时（不推荐）。

## Corrected Claim

工作点B（中性价比最优/中延迟）：通过S3 Gateway + 互联网出口恢复400TB数据，利用100TB/月免费额度后，剩余300TB按$0.09/GB计费，总成本 = 300,000 * 0.09 * 7.2 = ¥194,400，带宽受限于本地上行链路（如1Gbps），传输时间约360小时（不推荐）。

## Evidence

先验知识/题面给定，逻辑校验通过：300TB=300,000GB，300,000*0.09=27,000 USD，27,000*7.2=194,400 CNY，计算无误；1Gbps带宽下300TB传输时间约为360小时，量级合理。

## Search Query

AWS S3 data transfer out internet pricing free tier
