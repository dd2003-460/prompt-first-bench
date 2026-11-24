# N72: SSD层100TB温数据的RAID6重建时间：假设采用1.92TB NVMe SSD，需53块盘，RAID6重建需读51块写1块，NVMe顺序写入带宽约3GB/

- **status**: pending
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

父节点级核验未通过：非正交（子节点1和子节点2存在逻辑冲突/重叠：子节点1计算出的理论最小时间（3.7h）基于53块盘的总带宽（约79.5GB/s），而子节点2指出物理瓶颈仅为12-15GB/s。若采纳子节点2的物理限制，子节点1的计算结果在工程上是不成立的（因为实际无法达到该并行度）。此外，父节点中的核心假设'重建速率...不超过10GB/s'在子节点中被修正为12-15GB/s，但未明确说明这是针对特定高端控制器的例外情况还是普遍修正，导致上下文一致性略差。）

## Search Query

NVMe SSD RAID rebuild time GB/s controller bottleneck
