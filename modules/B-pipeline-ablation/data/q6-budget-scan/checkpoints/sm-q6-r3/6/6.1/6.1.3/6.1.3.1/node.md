# N286: 公有云CDN日志服务基础费用：假设日志存储保留30天，日均日志量50GB，存储单价0.1元/GB/月，则月度日志存储成本为 $C_{log} = 50 \tex

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N107

## Claim

公有云CDN日志服务基础费用：假设日志存储保留30天，日均日志量50GB，存储单价0.1元/GB/月，则月度日志存储成本为 $C_{log} = 50 \text{ GB/day} \times 30 \text{ days} \times 0.1 \text{ 元/GB/月} = 150 \text{ 元/月}$。

## Corrected Claim

公有云CDN日志服务基础费用：假设日志存储保留30天，日均日志量50GB，存储单价0.1元/GB/月，则月度日志存储成本为 $C_{log} = 50 \text{ GB/day} \times 30 \text{ days} \times 0.1 \text{ 元/GB/月} = 150 \text{ 元/月}$。

## Evidence

先验知识/题面给定，逻辑校验通过：50 GB/day * 30 days = 1500 GB 总存储量，1500 GB * 0.1 元/GB/月 = 150 元/月，计算无误且量级合理。

## Search Query

aliyun sls log service pricing per gb per month 2024
