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

父节点级核验通过：正交+完备+无冗余（两个子节点分别聚焦于‘技术成因’（GC/WL导致的带宽衰减机制）和‘工程影响’（对重建时间/成本的具体量化修正），维度不同，无重叠且共同覆盖了父节点中提到的‘限制原因’和‘典型数值范围及其后果’。）

## Search Query

nvme raid rebuild sustained write bandwidth gb/s background gc limit
