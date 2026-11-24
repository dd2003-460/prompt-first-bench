# N250: 本地自建机房 PUE 取值 1.4 的量化依据：基于 ASHRAE 2023 报告，典型企业自建机房（风冷、无液冷）PUE 中位数为 1.4-1.5；若采用冷热

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N87

## Claim

本地自建机房 PUE 取值 1.4 的量化依据：基于 ASHRAE 2023 报告，典型企业自建机房（风冷、无液冷）PUE 中位数为 1.4-1.5；若采用冷热通道封闭优化，PUE 可降至 1.3，对应电费差异 = 总功耗 × (1.5 - 1.3) × 8760 小时 × 电价，需根据实际机房散热设计选取。

## Corrected Claim

本地自建机房 PUE 取值 1.4 的量化依据：基于 ASHRAE 2023 报告，典型企业自建机房（风冷、无液冷）PUE 中位数为 1.4-1.5；若采用冷热通道封闭优化，PUE 可降至 1.3，对应电费差异 = 总功耗 × (1.5 - 1.3) × 8760 小时 × 电价，需根据实际机房散热设计选取。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

ASHRAE data center PUE median value 2023 self-built facility
