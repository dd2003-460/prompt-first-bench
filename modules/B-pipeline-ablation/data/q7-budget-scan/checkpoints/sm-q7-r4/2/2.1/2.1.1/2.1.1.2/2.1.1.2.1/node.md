# N477: RAID-6校验开销修正系数：针对40盘阵列，RAID-6理论带宽损耗因双校验盘冗余计算及重建开销，实际有效吞吐系数K_RAID6 = 1 - (2/N_dis

- **status**: degraded
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N161

## Claim

RAID-6校验开销修正系数：针对40盘阵列，RAID-6理论带宽损耗因双校验盘冗余计算及重建开销，实际有效吞吐系数K_RAID6 = 1 - (2/N_disks + Parity_Overhead) = 1 - (2/40 + 0.05) = 0.90，修正后有效聚合吞吐 T_eff = 280 GB/s * 0.90 = 252 GB/s。

## Corrected Claim

RAID-6校验开销修正系数：针对40盘阵列，RAID-6理论带宽损耗因双校验盘冗余计算及重建开销，实际有效吞吐系数K_RAID6通常估算为0.90左右（取决于具体Parity_Overhead假设），修正后有效聚合吞吐 T_eff ≈ 280 GB/s * 0.90 = 252 GB/s。

## Evidence

[质询]Parity_Overhead=0.05 是一个缺乏通用标准的经验参数，不同硬件实现和负载下差异巨大，将其作为固定常数直接相加在逻辑上过于简化，且未提供该特定值的来源依据。 | 经验事实，逻辑自洽但缺来源支持（source=knowledge，但参数具体值缺乏普适性验证，降档处理）
