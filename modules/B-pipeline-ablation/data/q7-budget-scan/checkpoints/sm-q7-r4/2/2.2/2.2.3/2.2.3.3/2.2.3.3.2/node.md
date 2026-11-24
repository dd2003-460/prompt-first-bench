# N543: 工作点C中HDD层扫描性能的瓶颈修正：原假设HDD吞吐0.25GB/s为单盘顺序读极限，但28块HDD并行扫描时，受RAID控制器及背板带宽限制，聚合吞吐可能仅

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N178

## Claim

工作点C中HDD层扫描性能的瓶颈修正：原假设HDD吞吐0.25GB/s为单盘顺序读极限，但28块HDD并行扫描时，受RAID控制器及背板带宽限制，聚合吞吐可能仅提升至2-3GB/s（而非28*0.25=7GB/s），需计算实际聚合吞吐T_agg_hdd。

## Corrected Claim

工作点C中HDD层扫描性能的瓶颈修正：原假设HDD吞吐0.25GB/s为单盘顺序读极限，但28块HDD并行扫描时，受RAID控制器及背板带宽限制，聚合吞吐可能仅提升至2-3GB/s（而非28*0.25=7GB/s），需计算实际聚合吞吐T_agg_hdd。

## Evidence

先验知识/题面给定，逻辑校验通过：RAID控制器及背板带宽确实是多盘并行时的主要瓶颈，2-3GB/s的聚合吞吐估计符合传统SAS/SATA RAID控制器的硬件极限，逻辑自洽。
