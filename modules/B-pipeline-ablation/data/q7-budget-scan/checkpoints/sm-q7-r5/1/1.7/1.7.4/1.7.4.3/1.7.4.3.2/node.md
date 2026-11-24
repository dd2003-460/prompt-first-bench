# N427: 硬件 RAID vs 软件 RAID 的净功耗增量：硬件 RAID 卡额外功耗 ΔP_hw = P_controller_card - P_CPU_overhe

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N187

## Claim

硬件 RAID vs 软件 RAID 的净功耗增量：硬件 RAID 卡额外功耗 ΔP_hw = P_controller_card - P_CPU_overhead_saved。虽然硬件卡消耗 15-25W，但它节省了 CPU 计算 RAID 校验和的能耗。在 x86 服务器中，CPU 执行 RAID 计算的能耗约为 0.5-1.0W（取决于 CPU 频率和指令集优化）。因此，若仅看总系统功耗，硬件 RAID 的净增量约为 14-24W；但若考虑 CPU 释放带来的整体能效提升（PUE 效应），硬件 RAID 在大规模阵列（>100 盘）中更具能效优势。

## Corrected Claim

硬件 RAID vs 软件 RAID 的净功耗增量：硬件 RAID 卡额外功耗 ΔP_hw = P_controller_card - P_CPU_overhead_saved。虽然硬件卡消耗 15-25W，但它节省了 CPU 计算 RAID 校验和的能耗。在 x86 服务器中，CPU 执行 RAID 计算的能耗约为 0.5-1.0W（取决于 CPU 频率和指令集优化）。因此，若仅看总系统功耗，硬件 RAID 的净增量约为 14-24W；但若考虑 CPU 释放带来的整体能效提升（PUE 效应），硬件 RAID 在大规模阵列（>100 盘）中更具能效优势。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

hardware RAID card vs software RAID CPU power overhead comparison
