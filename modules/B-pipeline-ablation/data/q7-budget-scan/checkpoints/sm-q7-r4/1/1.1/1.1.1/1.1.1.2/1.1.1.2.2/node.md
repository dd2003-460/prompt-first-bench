# N401: 工作点A (RAID-6) 重建时的I/O争用系数修正：在温数据扫描期间发生SSD故障，重建过程会与正常扫描I/O竞争PCIe带宽和SSD控制器资源。假设正常扫

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N134

## Claim

工作点A (RAID-6) 重建时的I/O争用系数修正：在温数据扫描期间发生SSD故障，重建过程会与正常扫描I/O竞争PCIe带宽和SSD控制器资源。假设正常扫描占用70%带宽，重建仅剩30%可用带宽。有效重建带宽 T_rebuild_eff = 100MB/s * 0.3 = 30MB/s。

## Corrected Claim

工作点A (RAID-6) 重建时的I/O争用系数修正：在温数据扫描期间发生SSD故障，重建过程会与正常扫描I/O竞争PCIe带宽和SSD控制器资源。假设正常扫描占用70%带宽，重建仅剩30%可用带宽。有效重建带宽 T_rebuild_eff = 100MB/s * 0.3 = 30MB/s。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

RAID rebuild IO contention performance degradation
