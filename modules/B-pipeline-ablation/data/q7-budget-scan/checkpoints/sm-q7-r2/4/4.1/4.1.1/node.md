# N67: RAID6 重建期间的 I/O 抑制效应（I/O Throttling Factor），在重建过程中，正常业务 I/O 性能下降比例，通常导致业务延迟增加或需要

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N19

## Claim

RAID6 重建期间的 I/O 抑制效应（I/O Throttling Factor），在重建过程中，正常业务 I/O 性能下降比例，通常导致业务延迟增加或需要临时扩容，此因子影响 RTO 期间的隐性业务损失，典型值为 30%-50% 性能下降。

## Corrected Claim

RAID6 重建期间的 I/O 抑制效应（I/O Throttling Factor），在重建过程中，正常业务 I/O 性能下降比例，通常导致业务延迟增加或需要临时扩容，此因子影响 RTO 期间的隐性业务损失，典型值为 30%-50% 性能下降。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

raid 6 rebuild io performance degradation throttling percentage
