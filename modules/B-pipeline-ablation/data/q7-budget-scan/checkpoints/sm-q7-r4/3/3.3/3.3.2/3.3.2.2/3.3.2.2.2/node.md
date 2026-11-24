# N626: HDD 层 Overhead 的精确构成：N214 中提到的 '10% RAID overhead' 实际上应细分为 Parity_Overhead + Hot

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N214

## Claim

HDD 层 Overhead 的精确构成：N214 中提到的 '10% RAID overhead' 实际上应细分为 Parity_Overhead + Hot_Spare_Overhead + Filesystem_Journal_Overhead。对于 RAID6，Parity_Overhead ≈ 2/N_disks (N=25 时为 8%)；Hot_Spare 通常预留 1 块盘 (16TB)，占比 16/400 = 4%；Filesystem_Journal (如 XFS) 约占 1-2%。总计 Overhead ≈ 8% + 4% + 1.5% ≈ 13.5%。因此，若逻辑需求为 420TB，物理裸容量需求 V_hdd_phys = 420TB / (1 - 0.135) ≈ 485.7TB。这与 N214 估算的 462TB 存在偏差，N214 低估了 Hot_Spare 和 Journal 的开销。

## Corrected Claim

HDD 层 Overhead 的精确构成：N214 中提到的 '10% RAID overhead' 实际上应细分为 Parity_Overhead + Hot_Spare_Overhead + Filesystem_Journal_Overhead。对于 RAID6，Parity_Overhead ≈ 2/N_disks (N=25 时为 8%)；Hot_Spare 通常预留 1 块盘 (16TB)，占比 16/400 = 4%；Filesystem_Journal (如 XFS) 约占 1-2%。总计 Overhead ≈ 8% + 4% + 1.5% ≈ 13.5%。因此，若逻辑需求为 420TB，物理裸容量需求 V_hdd_phys = 420TB / (1 - 0.135) ≈ 485.7TB。这与 N214 估算的 462TB 存在偏差，N214 低估了 Hot_Spare 和 Journal 的开销。

## Evidence

先验知识/题面给定，逻辑校验通过：RAID6 25盘奇偶校验开销确为2/25=8%，热备1/25=4%，文件系统日志1-2%符合工程常识，总开销13.5%及物理容量换算逻辑自洽。
