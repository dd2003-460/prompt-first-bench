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

父节点级核验未通过：不完备（子节点1解释技术原因（GC/队列深度导致带宽受限），子节点2阐述工程后果（重建时间延长及可行性评估），两者关注点不同，正交性良好。但父节点明确提到了“受限于 NVMe 队列深度”，而子节点1仅强调了 GC 和 Wear Leveling，遗漏了队列深度这一关键限制因素，导致技术归因不完备。）

## Search Query

nvme raid rebuild sustained write bandwidth gb/s background gc limit
