# N21: 温数据访问频率约束：20%温数据每日扫描1-2次，本地NVMe SSD和HDD+SSD分层（SSD层）满足，云存储标准层满足，无方案被排除

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N3

## Claim

温数据访问频率约束：20%温数据每日扫描1-2次，本地NVMe SSD和HDD+SSD分层（SSD层）满足，云存储标准层满足，无方案被排除

## Corrected Claim

温数据访问频率约束：20%温数据每日扫描1-2次，本地NVMe SSD和HDD+SSD分层（SSD层）满足，云存储标准层满足，无方案被排除

## Evidence

先验知识/题面给定，逻辑校验通过：温数据（Warm Data）通常指访问频率较低但非冷数据，每日1-2次的扫描频率符合温数据特征；本地NVMe SSD、HDD+SSD分层（SSD层）以及云存储标准层（Standard Storage）均具备支持该频率访问的性能和成本特性，无方案被排除符合存储分层的一般工程实践。
