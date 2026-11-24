# N68: NVMe SSD RAID6 重建的持续写入带宽限制（GB/s/drive），受限于 NVMe 队列深度和后台垃圾回收（GC），典型持续重写带宽约为 1-2 G

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N19

## Claim

NVMe SSD RAID6 重建的持续写入带宽限制（GB/s/drive），受限于 NVMe 队列深度和后台垃圾回收（GC），典型持续重写带宽约为 1-2 GB/s per drive，而非峰值顺序写带宽。

## Corrected Claim

NVMe SSD RAID6 重建的持续写入带宽限制（GB/s/drive），受限于 NVMe 队列深度和后台垃圾回收（GC），典型持续重写带宽约为 1-2 GB/s per drive，而非峰值顺序写带宽。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

nvme raid rebuild sustained write bandwidth gb/s background gc limit
