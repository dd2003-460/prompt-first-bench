# N460: NVMe RAID-6的IOPS聚合效率修正：RAID-6在读取时并行度高，但写入时需双盘奇偶校验。对于纯读扫描，IOPS_agg = N_disks * IO

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N154

## Claim

NVMe RAID-6的IOPS聚合效率修正：RAID-6在读取时并行度高，但写入时需双盘奇偶校验。对于纯读扫描，IOPS_agg = N_disks * IOPS_single * Efficiency_Factor。Efficiency_Factor 受控制器队列深度和PCIe通道争用影响。假设 U.2 NVMe 队列深度 QD=1024 时达到峰值 100k IOPS，但在高并发元数据查找（随机小IO）下，由于PCIe事务开销，实际效率降至 60%。IOPS_agg_corrected = 12 * 100k * 0.6 = 720k IOPS。利用率 = 69k / 720k = 9.6%，仍非瓶颈，但需关注PCIe带宽饱和。

## Corrected Claim

NVMe RAID-6的IOPS聚合效率修正：RAID-6在读取时并行度高，但写入时需双盘奇偶校验。对于纯读扫描，IOPS_agg = N_disks * IOPS_single * Efficiency_Factor。Efficiency_Factor 受控制器队列深度和PCIe通道争用影响。假设 U.2 NVMe 队列深度 QD=1024 时达到峰值 100k IOPS，但在高并发元数据查找（随机小IO）下，由于PCIe事务开销，实际效率降至 60%。IOPS_agg_corrected = 12 * 100k * 0.6 = 720k IOPS。利用率 = 69k / 720k = 9.6%，仍非瓶颈，但需关注PCIe带宽饱和。

## Evidence

先验知识/题面给定，逻辑校验通过：算术运算正确（12*100k*0.6=720k, 69k/720k≈9.6%），RAID-6读写特性及PCIe效率衰减符合工程常识

## Search Query

NVMe RAID random read IOPS efficiency PCIe saturation small IO
