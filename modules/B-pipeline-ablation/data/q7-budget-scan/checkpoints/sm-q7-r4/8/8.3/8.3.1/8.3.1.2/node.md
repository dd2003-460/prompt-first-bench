# N647: 工作点B（大型阵列/标准冗余）：针对 200-300 块 NVMe SSD，需双控制器（Active-Active）以保证高可用，单控 35W，双控 70W；背

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N270

## Claim

工作点B（大型阵列/标准冗余）：针对 200-300 块 NVMe SSD，需双控制器（Active-Active）以保证高可用，单控 35W，双控 70W；背板因 PCIe Gen4 信号完整性需增加 Retimer 芯片，损耗升至 40W。合计 P_ctrl_backplane ≈ 110W。此为多数企业级存储柜的标准配置。

## Corrected Claim

工作点B（大型阵列/标准冗余）：针对 200-300 块 NVMe SSD，需双控制器（Active-Active）以保证高可用，单控 35W，双控 70W；背板因 PCIe Gen4 信号完整性需增加 Retimer 芯片，损耗升至 40W。合计 P_ctrl_backplane ≈ 110W。此为多数企业级存储柜的标准配置。

## Evidence

先验知识/题面给定，逻辑校验通过：双控功耗（35W*2=70W）与背板Retimer损耗（40W）相加等于110W，数值量级符合企业级存储硬件工程常识。
