# N635: NVMe RAID 重建期间前台写延迟增加的量化公式：ΔLatency = Q_foreground * (1/(B_total - B_rebuild) - 

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N220

## Claim

NVMe RAID 重建期间前台写延迟增加的量化公式：ΔLatency = Q_foreground * (1/(B_total - B_rebuild) - 1/B_total)，其中 B_total 为阵列总写带宽，B_rebuild 为重建占用带宽，Q_foreground 为前台队列平均长度；若 B_rebuild=0.5*B_total，则 ΔLatency ≈ Q_foreground * (1/(0.5*B_total))，即延迟翻倍。

## Corrected Claim

NVMe RAID 重建期间前台写延迟增加的量化公式：ΔLatency = Q_foreground * (1/(B_total - B_rebuild) - 1/B_total)，其中 B_total 为阵列总写带宽，B_rebuild 为重建占用带宽，Q_foreground 为前台队列平均长度；若 B_rebuild=0.5*B_total，则 ΔLatency ≈ Q_foreground * (1/(0.5*B_total))，即延迟翻倍。

## Evidence

先验知识/题面给定，逻辑校验通过：基于排队论Little's Law及带宽竞争模型，当重建占用50%带宽时，剩余有效带宽减半，导致服务速率减半，在稳态下平均等待时间（延迟）近似翻倍，公式推导符合物理直觉与数学逻辑。
