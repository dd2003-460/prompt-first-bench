# N755: 工作点B（中性价比最优/中延迟）：S3 Glacier Bulk Retrieval取回400TB冷数据，单价$0.0025/GB，总成本 = 400,000 

- **status**: degraded
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N282

## Claim

工作点B（中性价比最优/中延迟）：S3 Glacier Bulk Retrieval取回400TB冷数据，单价$0.0025/GB，总成本 = 400,000 * 0.0025 * 7.2 = ¥7,200，预计完成时间5-12小时，适用于RTO容忍度>12小时的离线恢复场景。

## Corrected Claim

工作点B（中性价比最优/中延迟）：S3 Glacier Bulk Retrieval取回400TB冷数据，单价$0.0025/GB，美元总成本 = $1,000（约合人民币7,200元，基于1:7.2汇率估算），预计完成时间5-12小时，适用于RTO容忍度>12小时的离线恢复场景。

## Evidence

[质询]汇率假设不明：计算中使用了 7.2 作为 USD/CNY 汇率，但该汇率随时间波动，且未指明具体日期，导致最终人民币金额具有时效性和不确定性。 | 先验知识/题面给定，逻辑校验通过（400TB=400,000GB，单价$0.0025/GB，乘积正确；S3 Glacier Bulk 延迟 5-12h 符合 AWS 官方文档描述；但汇率 7.2 为经验参数，缺乏实时来源支持，故降级）。

## Search Query

AWS S3 Glacier Bulk Retrieval pricing per GB
