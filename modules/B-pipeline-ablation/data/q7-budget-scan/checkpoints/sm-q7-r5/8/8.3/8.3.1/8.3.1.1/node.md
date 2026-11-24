# N646: 工作点A（小型阵列/高能效）：针对 <100 块 NVMe SSD 的中型阵列，采用单颗 Broadcom MegaRAID 或 LSI HBA 控制器，典型 

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N270

## Claim

工作点A（小型阵列/高能效）：针对 <100 块 NVMe SSD 的中型阵列，采用单颗 Broadcom MegaRAID 或 LSI HBA 控制器，典型 TDP 为 25W；背板主要为被动散热+少量信号损耗，估算 20W。合计 P_ctrl_backplane ≈ 45W。此配置下单位 TB 基础设施功耗最低。

## Corrected Claim

工作点A（小型阵列/高能效）：针对 <100 块 NVMe SSD 的中型阵列，采用单颗 Broadcom MegaRAID 或 LSI HBA 控制器，典型 TDP 为 25W；背板主要为被动散热+少量信号损耗，估算 20W。合计 P_ctrl_backplane ≈ 45W。此配置下单位 TB 基础设施功耗最低。

## Evidence

先验知识/题面给定，逻辑校验通过：Broadcom MegaRAID/LSI HBA 控制器 TDP 25W 及背板损耗 20W 符合硬件工程常识，总和计算正确，且对于小规模阵列而言，单控制器方案确实具有最高的单位 TB 能效比。
