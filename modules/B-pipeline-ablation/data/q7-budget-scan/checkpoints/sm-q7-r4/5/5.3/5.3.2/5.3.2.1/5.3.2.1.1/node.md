# N551: 3.84TB NVMe SSD RAID6 重建的聚合持续写入带宽 B_agg = min(N_drives_active * W_single_sustain

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N238

## Claim

3.84TB NVMe SSD RAID6 重建的聚合持续写入带宽 B_agg = min(N_drives_active * W_single_sustained, Controller_Bandwidth_Limit)，其中 N_drives_active=236，W_single_sustained 基于 N68 修正值为 1.5 GB/s/drive（取 1-2 GB/s 中值，修正 N72 的 3GB/s 高估），Controller_Bandwidth_Limit 假设为 40 GB/s（PCIe Gen4 x16 理论上限约 15.75GB/s，多控制器聚合可达更高，此处保守取 40GB/s 作为瓶颈上限），故 B_agg ≈ 40 GB/s

## Corrected Claim

3.84TB NVMe SSD RAID6 重建的聚合持续写入带宽 B_agg = min(N_drives_active * W_single_sustained, Controller_Bandwidth_Limit)，其中 N_drives_active=236，W_single_sustained 基于 N68 修正值为 1.5 GB/s/drive（取 1-2 GB/s 中值，修正 N72 的 3GB/s 高估），Controller_Bandwidth_Limit 假设为 40 GB/s（PCIe Gen4 x16 理论上限约 15.75GB/s，多控制器聚合可达更高，此处保守取 40GB/s 作为瓶颈上限），故 B_agg ≈ 40 GB/s

## Evidence

先验知识/题面给定，逻辑校验通过：236*1.5=354 GB/s > 40 GB/s，min函数取值正确，PCIe Gen4 x16单链路~15.75GB/s，多控制器聚合至40GB/s符合工程常识，量纲与计算无误。
