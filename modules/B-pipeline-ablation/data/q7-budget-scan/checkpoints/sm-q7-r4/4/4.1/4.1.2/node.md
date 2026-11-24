# N68: NVMe SSD RAID6 重建的持续写入带宽限制（GB/s/drive），受限于 NVMe 队列深度和后台垃圾回收（GC），典型持续重写带宽约为 1-2 G

- **status**: pending
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

父节点级核验未通过：不完备（子节点在主题上正交（一个聚焦底层机制，一个聚焦工程影响），无重复或矛盾。但父节点明确提到了'受限于 NVMe 队列深度'这一关键约束因素，而两个子节点均未提及或解释该因素如何与 GC 共同作用限制带宽，因此覆盖不全。）

## Search Query

nvme raid rebuild sustained write bandwidth gb/s background gc limit
