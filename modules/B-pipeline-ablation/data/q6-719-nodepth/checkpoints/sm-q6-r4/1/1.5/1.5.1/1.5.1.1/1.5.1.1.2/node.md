# N543: 在有效带宽 B_eff=100Mbps (12.5MB/s) 的工作点下，平均传输延迟 T_transfer_avg = 2.4MB / 12.5MB/s = 

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N184

## Claim

在有效带宽 B_eff=100Mbps (12.5MB/s) 的工作点下，平均传输延迟 T_transfer_avg = 2.4MB / 12.5MB/s = 192ms，此为低成本（带宽便宜）高延迟的工作点，需评估是否满足 P99 约束。

## Corrected Claim

在有效带宽 B_eff=100Mbps (12.5MB/s) 的工作点下，平均传输延迟 T_transfer_avg = 2.4MB / 12.5MB/s = 192ms，此为低成本（带宽便宜）高延迟的工作点，需评估是否满足 P99 约束。

## Evidence

先验知识/题面给定，逻辑校验通过：100Mbps = 12.5MB/s，2.4MB / 12.5MB/s = 0.192s = 192ms，计算无误且量级合理。
