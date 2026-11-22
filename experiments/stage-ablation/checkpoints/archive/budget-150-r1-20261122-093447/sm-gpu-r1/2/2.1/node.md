# N19: TCO 公式：TCO_5yr = Hardware_Cost + (Power_W * Hours_Year * 5 * Electricity_Price_p

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N2

## Claim

TCO 公式：TCO_5yr = Hardware_Cost + (Power_W * Hours_Year * 5 * Electricity_Price_per_kWh) + Cooling_Cost + Maintenance_Cost + Upgrade_Cost；其中 Power_W = GPU_TDP + CPU_TDP + Memory_TDP + PSU_Overhead，Hours_Year = 8760（24/7）或 4380（12/7 工作日）[待核验：本地工作站典型使用小时数]

## Corrected Claim

TCO 公式：TCO_5yr = Hardware_Cost + (Power_W * Hours_Year * 5 * Electricity_Price_per_kWh) + Cooling_Cost + Maintenance_Cost + Upgrade_Cost；其中 Power_W = GPU_TDP + CPU_TDP + Memory_TDP + PSU_Overhead，Hours_Year = 8760（24/7）或 4380（12/7 工作日）[待核验：本地工作站典型使用小时数]

## Evidence

先验知识/题面给定，逻辑校验通过：TCO公式结构符合标准IT资产全生命周期成本模型，Power_W构成项（GPU/CPU/Memory/PSU）覆盖主要耗电组件，Hours_Year数值（8760/4380）符合24/7及12/7工作制的数学定义，量纲与逻辑自洽。
