# N248: NVMe RAID-6重建速率的理论上限 Rebuild_Rate_max = min(NVMe_Sequential_Write_IOPS * Block_S

- **status**: pending
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N78

## Claim

NVMe RAID-6重建速率的理论上限 Rebuild_Rate_max = min(NVMe_Sequential_Write_IOPS * Block_Size, RAID_Controller_Compute_TBW)；典型企业级NVMe顺序写IOPS=1,000,000，Block_Size=4KB，理论上限=4GB/s；RAID控制器算力通常为2-4GB/s，故Rebuild_Rate_max≈2-4GB/s，N78声称的80-120GB/h（2.2-3.3GB/s）处于合理区间

## Corrected Claim

NVMe RAID-6重建速率的理论上限 Rebuild_Rate_max = min(NVMe_Sequential_Write_IOPS * Block_Size, RAID_Controller_Compute_TBW)；典型企业级NVMe顺序写IOPS=1,000,000，Block_Size=4KB，理论上限=4GB/s；RAID控制器算力通常为2-4GB/s，故Rebuild_Rate_max≈2-4GB/s，N78声称的80-120GB/h（2.2-3.3GB/s）处于合理区间

## Evidence

父节点级核验未通过：非正交（子节点存在严重的数据矛盾和逻辑不一致。父节点基于错误的假设（NVMe IOPS=1M导致4GB/s上限）得出结论，而子节点引入了具体的硬件数据（PM9A3 6.8GB/s），直接否定了父节点的数值基础。此外，子节点3的合成结论（4-6GB/s）与父节点声称的“合理区间”（2.2-3.3GB/s）存在数量级上的冲突，未体现对父节点的修正或解释。）

## Search Query

NVMe sequential write IOPS RAID controller throughput limit rebuild rate
