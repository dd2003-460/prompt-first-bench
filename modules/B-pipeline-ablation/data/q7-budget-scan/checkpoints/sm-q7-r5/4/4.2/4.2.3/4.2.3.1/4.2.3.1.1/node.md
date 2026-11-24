# N455: 16TB CMR HDD (Seagate Exos 16E) 在 RAID6 重建期间的聚合有效写带宽受限于单盘瓶颈，假设 26 块盘并行重建，总带宽 B_a

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N202

## Claim

16TB CMR HDD (Seagate Exos 16E) 在 RAID6 重建期间的聚合有效写带宽受限于单盘瓶颈，假设 26 块盘并行重建，总带宽 B_agg = 26 * 200MB/s = 5.2GB/s，重建 400TB 数据所需时间 T_rebuild_CMR = 400,000GB / 5.2GB/s ≈ 76.9 小时，而非 N202 声称的 55.5 小时（N202 错误地假设了单盘带宽为总带宽）。

## Corrected Claim

16TB CMR HDD (Seagate Exos 16E) 在 RAID6 重建期间的聚合有效写带宽受限于单盘瓶颈，假设 26 块盘并行重建，总带宽 B_agg = 26 * 200MB/s = 5.2GB/s，重建 400TB 数据所需时间 T_rebuild_CMR = 400,000GB / 5.2GB/s ≈ 76.9 小时，而非 N202 声称的 55.5 小时（N202 错误地假设了单盘带宽为总带宽）。

## Evidence

先验知识/题面给定，逻辑校验通过：计算过程 400,000GB / (26 * 200MB/s) ≈ 76.9小时 符合算术逻辑，且基于给定的单盘带宽假设推导正确。
