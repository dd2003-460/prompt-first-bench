# N410: 工作点B (RAID-5) 的运维隐性成本：RAID-5重建期间（见N137）I/O性能下降约50-70%，若温数据扫描在重建期间发生，扫描时间延长导致的集群等

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N136

## Claim

工作点B (RAID-5) 的运维隐性成本：RAID-5重建期间（见N137）I/O性能下降约50-70%，若温数据扫描在重建期间发生，扫描时间延长导致的集群等待成本 ≈ ΔT_rebuild * ¥5,000/h * P_rebuild_annual，需量化年重建概率。

## Corrected Claim

工作点B (RAID-5) 的运维隐性成本：RAID-5重建期间（见N137）I/O性能下降约50-70%，若温数据扫描在重建期间发生，扫描时间延长导致的集群等待成本 ≈ ΔT_rebuild * ¥5,000/h * P_rebuild_annual，需量化年重建概率。

## Evidence

先验知识/题面给定，逻辑校验通过
