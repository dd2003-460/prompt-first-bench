# N19: TCO 公式：TCO_5yr = Hardware_Cost + (Power_W * Hours_Year * 5 * Electricity_Price_p

- **status**: pending
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N2

## Claim

TCO 公式：TCO_5yr = Hardware_Cost + (Power_W * Hours_Year * 5 * Electricity_Price_per_kWh) + Cooling_Cost + Maintenance_Cost + Upgrade_Cost；其中 Power_W = GPU_TDP + CPU_TDP + Memory_TDP + PSU_Overhead，Hours_Year = 8760（24/7）或 4380（12/7 工作日）[待核验：本地工作站典型使用小时数]

## Corrected Claim

TCO 公式：TCO_5yr = Hardware_Cost + (Power_W * Hours_Year * 5 * Electricity_Price_per_kWh) + Cooling_Cost + Maintenance_Cost + Upgrade_Cost；其中 Power_W = GPU_TDP + CPU_TDP + Memory_TDP + PSU_Overhead，Hours_Year = 8760（24/7）或 4380（12/7 工作日）[待核验：本地工作站典型使用小时数]

## Evidence

父节点级核验未通过：不完备（子节点主要聚焦于电力成本敏感性、不同运行场景对比及散热/维护修正，但完全缺失了父节点公式中明确列出的 'Hardware_Cost'（硬件成本）、'Maintenance_Cost'（维护成本，虽在子节点3中提及占比低但未作为独立维度深入）和 'Upgrade_Cost'（升级成本）的具体分解或分析。此外，子节点1和2虽然场景不同，但核心逻辑都是关于电力成本与硬件成本的权衡，存在一定逻辑重叠，但主要问题在于完备性不足。）
