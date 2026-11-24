# N184: 冗余投资成本 C_redundancy 计算：C_redundancy = (Num_POP * Redundancy_Factor * Cost_per_PO

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N44

## Claim

冗余投资成本 C_redundancy 计算：C_redundancy = (Num_POP * Redundancy_Factor * Cost_per_POP) / Q_day * 1000，其中 Redundancy_Factor 为冗余系数（自建通常需1.5-2倍硬件以支持N+1冗余，公有云通过多区域部署实现但按量计费），Cost_per_POP 为单POP年折旧成本。

## Corrected Claim

冗余投资成本 C_redundancy 计算：C_redundancy = (Num_POP * Redundancy_Factor * Cost_per_POP) / Q_day * 1000，其中 Redundancy_Factor 为冗余系数（自建通常需1.5-2倍硬件以支持N+1冗余，公有云通过多区域部署实现但按量计费），Cost_per_POP 为单POP年折旧成本。

## Evidence

先验知识/题面给定，逻辑校验通过
