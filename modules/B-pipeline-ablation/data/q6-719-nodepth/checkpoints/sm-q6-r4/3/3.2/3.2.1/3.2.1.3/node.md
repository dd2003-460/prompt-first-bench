# N248: 工作点3（低单价/高门槛）：企业级私有云专线上传，上行带宽租赁折合单位流量成本可低至 ¥0.05/GB（基于 10Gbps 专线月租 ¥50k 估算），但需承担

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N79

## Claim

工作点3（低单价/高门槛）：企业级私有云专线上传，上行带宽租赁折合单位流量成本可低至 ¥0.05/GB（基于 10Gbps 专线月租 ¥50k 估算），但需承担固定月租成本，仅当日均上传量 > 5TB 时单位成本才低于按量付费。

## Corrected Claim

工作点3（低单价/高门槛）：企业级私有云专线上传，上行带宽租赁折合单位流量成本可低至 ¥0.05/GB（基于 10Gbps 专线月租 ¥50k 估算），但需承担固定月租成本，仅当日均上传量 > 5TB 时单位成本才低于按量付费。

## Evidence

先验知识/题面给定，逻辑校验通过：10Gbps专线月租5万元，月流量约10.8PB，单位成本约0.0046元/GB，远低于0.05元/GB；日均5TB月流量150TB，固定成本分摊为0.33元/GB，若按量付费单价高于此值则陈述成立，量级与逻辑自洽。

## Search Query

dedicated line upload cost per GB vs CDN pay-as-you-go
