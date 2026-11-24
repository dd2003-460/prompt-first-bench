# N72: SSD层100TB温数据的RAID6重建时间：假设采用1.92TB NVMe SSD，需53块盘，RAID6重建需读51块写1块，NVMe顺序写入带宽约3GB/

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N20, N21, N22

## Claim

SSD层100TB温数据的RAID6重建时间：假设采用1.92TB NVMe SSD，需53块盘，RAID6重建需读51块写1块，NVMe顺序写入带宽约3GB/s/盘，重建速率受控制器和背板限制通常不超过10GB/s，100TB/10GB/s≈2.8小时

## Corrected Claim

SSD层100TB温数据的RAID6重建时间：假设采用1.92TB NVMe SSD，需53块盘，RAID6重建需读51块写1块，NVMe顺序写入带宽约3GB/s/盘，重建速率受控制器和背板限制通常不超过10GB/s，100TB/10GB/s≈2.8小时

## Evidence

父节点级核验通过：正交+完备+无冗余（三个子节点分别对应‘理论最小时间计算’、‘物理硬件瓶颈分析’、‘I/O竞争下的实际耗时推导’，逻辑层次清晰且互不重叠，完整覆盖了从理想模型到物理限制再到业务影响的RAID重建时间估算全过程，无冗余或矛盾。）

## Search Query

NVMe SSD RAID rebuild time GB/s controller bottleneck
