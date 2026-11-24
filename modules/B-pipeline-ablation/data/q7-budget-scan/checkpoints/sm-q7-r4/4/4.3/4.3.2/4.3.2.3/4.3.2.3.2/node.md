# N727: 随机寻址导致的IOPS瓶颈：在4KB随机读场景，HDD单盘IOPS约100-150，而RAID-6需同时访问多块盘，系统瓶颈IOPS = min(Disk_IO

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N254

## Claim

随机寻址导致的IOPS瓶颈：在4KB随机读场景，HDD单盘IOPS约100-150，而RAID-6需同时访问多块盘，系统瓶颈IOPS = min(Disk_IOPS, Parity_Stripes_IOPS)；若Stripe深度为16，有效IOPS降至单盘水平的1/16，总重建时间 T_random = Total_Ops / Effective_IOPS。

## Corrected Claim

随机寻址导致的IOPS瓶颈：在4KB随机读场景，HDD单盘IOPS约100-150，而RAID-6需同时访问多块盘，系统瓶颈IOPS = min(Disk_IOPS, Parity_Stripes_IOPS)；若Stripe深度为16，有效IOPS降至单盘水平的1/16，总重建时间 T_random = Total_Ops / Effective_IOPS。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

RAID-6 random IOPS bottleneck stripe depth small file
