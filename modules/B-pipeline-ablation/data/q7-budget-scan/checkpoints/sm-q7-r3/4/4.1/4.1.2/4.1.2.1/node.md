# N195: NVMe SSD RAID6 重建的实际瓶颈在于 SSD 内部的 Garbage Collection (GC) 和 Wear Leveling，导致持续重写带

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N68

## Claim

NVMe SSD RAID6 重建的实际瓶颈在于 SSD 内部的 Garbage Collection (GC) 和 Wear Leveling，导致持续重写带宽从峰值 3GB/s 下降至 1-2GB/s，具体取决于 SSD 的 DRAM 缓存大小和固件调度算法。

## Corrected Claim

NVMe SSD RAID6 重建的实际瓶颈在于 SSD 内部的 Garbage Collection (GC) 和 Wear Leveling，导致持续重写带宽从峰值 3GB/s 下降至 1-2GB/s，具体取决于 SSD 的 DRAM 缓存大小和固件调度算法。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

NVMe SSD RAID6 rebuild bandwidth limit garbage collection internal overhead
