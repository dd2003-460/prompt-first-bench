# N71: HDD层重建时间公式修正：T_rebuild_HDD = (有效数据量/重建带宽)，重建带宽=min(读带宽总和, 写带宽总和)，RAID6重建需读N-1块盘写

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N20, N21, N22

## Claim

HDD层重建时间公式修正：T_rebuild_HDD = (有效数据量/重建带宽)，重建带宽=min(读带宽总和, 写带宽总和)，RAID6重建需读N-1块盘写1块盘，实际重建速率受限于最慢盘，400TB/200MB/s≈55.5小时

## Corrected Claim

HDD层重建时间公式修正：T_rebuild_HDD = (有效数据量/重建带宽)，重建带宽=min(读带宽总和, 写带宽总和)，RAID6重建需读N-1块盘写1块盘，实际重建速率受限于最慢盘，400TB/200MB/s≈55.5小时

## Evidence

父节点级核验未通过：非正交, 不完备, 有冗余（子节点本质上是同一公式在不同参数（盘容量、带宽、抑制率）下的三次实例化计算，属于典型的参数化冗余而非正交维度分解；同时，父节点核心强调的“RAID6需读N-1写1”及“受限于最慢盘/读写瓶颈”的机制在子节点中被简化为单一除法，未体现读/写带宽取min的逻辑，导致对父节点关键约束覆盖不全。）

## Search Query

RAID6 rebuild time calculation formula bandwidth limited
