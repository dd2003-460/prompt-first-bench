# N187: RAID 控制器功耗量化：PCIe Gen4 RAID 控制器（如 Broadcom MegaRAID 或 Marvell）典型功耗 15-25W，分摊到每 T

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N61, N62, N63

## Claim

RAID 控制器功耗量化：PCIe Gen4 RAID 控制器（如 Broadcom MegaRAID 或 Marvell）典型功耗 15-25W，分摊到每 TB 有效容量（假设 1PB 阵列）为 0.015-0.025W/TB；若控制器支持硬件 RAID 而非软件 RAID，功耗更高，需根据具体型号和阵列规模调整。

## Corrected Claim

RAID 控制器功耗量化：PCIe Gen4 RAID 控制器（如 Broadcom MegaRAID 或 Marvell）典型功耗 15-25W，分摊到每 TB 有效容量（假设 1PB 阵列）为 0.015-0.025W/TB；若控制器支持硬件 RAID 而非软件 RAID，功耗更高，需根据具体型号和阵列规模调整。

## Evidence

先验知识/题面给定，逻辑校验通过：PCIe Gen4 RAID控制器典型功耗15-25W符合工程常识，1PB=1000TB，15W/1000TB=0.015W/TB，25W/1000TB=0.025W/TB，数值量级与计算逻辑自洽。

## Search Query

PCIe Gen4 RAID controller power consumption watts per TB effective capacity
