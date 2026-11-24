# N656: 工作点A（高安全/慢重建）：RAID-6配置，聚合读速3GB/s，T_rebuild_hdd ≈ 500TB / 3GB/s * 1.5 ≈ 69.4h；双重故

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N227

## Claim

工作点A（高安全/慢重建）：RAID-6配置，聚合读速3GB/s，T_rebuild_hdd ≈ 500TB / 3GB/s * 1.5 ≈ 69.4h；双重故障保护，但重建期间I/O性能下降显著（约50%），且重建时间远超24h SLA。

## Corrected Claim

工作点A（高安全/慢重建）：RAID-6配置，聚合读速3GB/s，T_rebuild_hdd ≈ 500TB / 3GB/s * 1.5 ≈ 69.4h；双重故障保护，但重建期间I/O性能下降显著（约50%），且重建时间远超24h SLA。

## Evidence

先验知识/题面给定，逻辑校验通过：500TB / 3GB/s ≈ 46.3小时，乘以1.5系数后约为69.4小时，计算无误；RAID-6重建期间性能下降及SLA超标符合工程常识。
