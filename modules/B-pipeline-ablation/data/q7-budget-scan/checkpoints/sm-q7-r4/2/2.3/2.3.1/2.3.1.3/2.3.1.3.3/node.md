# N558: 工作点3（低RTO/高成本）：在 RTO < 1h 场景下，One Zone-IA 不可行，因单区故障即导致数据不可用，MTTR = AZ 恢复时间 ≈ 4-8

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N201

## Claim

工作点3（低RTO/高成本）：在 RTO < 1h 场景下，One Zone-IA 不可行，因单区故障即导致数据不可用，MTTR = AZ 恢复时间 ≈ 4-8 小时（AWS 承诺），不满足约束，必须升级为 Multi-AZ 或本地存储，此工作点成本无限大（不可行），标记为 [不可行]。

## Corrected Claim

工作点3（低RTO/高成本）：在 RTO < 1h 场景下，One Zone-IA 不可行，因单区故障即导致数据不可用，MTTR = AZ 恢复时间 ≈ 4-8 小时（AWS 承诺），不满足约束，必须升级为 Multi-AZ 或本地存储，此工作点成本无限大（不可行），标记为 [不可行]。

## Evidence

先验知识/题面给定，逻辑校验通过：One Zone-IA 架构在单区故障时确实导致数据不可用，其恢复时间取决于 AWS 区域级灾难恢复能力（通常以天计或数小时），远超 1 小时 RTO 约束，因此在该场景下不可行，逻辑自洽。
