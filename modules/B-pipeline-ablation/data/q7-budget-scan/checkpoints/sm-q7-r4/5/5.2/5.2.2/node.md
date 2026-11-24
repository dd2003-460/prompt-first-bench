# N94: 本地 NVMe SSD 扩容的停机迁移时间 Downtime_Hours 等于 迁移数据量 (Migration_Data_Size) 除以 迁移吞吐量 (Mi

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N27

## Claim

本地 NVMe SSD 扩容的停机迁移时间 Downtime_Hours 等于 迁移数据量 (Migration_Data_Size) 除以 迁移吞吐量 (Migration_Throughput)，假设迁移 100TB 数据，吞吐量 500MB/s，则 Downtime = 100*1024^3 / 500 / 3600 小时。

## Corrected Claim

本地 NVMe SSD 扩容的停机迁移时间 Downtime_Hours 等于 迁移数据量 (Migration_Data_Size) 除以 迁移吞吐量 (Migration_Throughput)，假设迁移 100TB 数据，吞吐量 500MB/s，则 Downtime = 100*1024^3 / 500 / 3600 小时。

## Evidence

父节点级核验未通过：不完备（子节点之间存在明显的逻辑维度错位。父节点仅讨论‘迁移时间’（Downtime_Hours），这是一个纯技术时延指标。子节点1（吞吐量瓶颈）直接支撑该公式的分母，是合格的输入参数分析。但子节点2（业务降级成本）讨论的是停机带来的‘经济/业务影响’（SLA罚款），这属于停机时间的后果评估，而非停机时间计算本身的组成部分。因此，子节点2偏离了父节点的主题（计算时长 vs 评估成本），导致不完备且不正交（一个讲物理限制，一个讲商业代价）。）
