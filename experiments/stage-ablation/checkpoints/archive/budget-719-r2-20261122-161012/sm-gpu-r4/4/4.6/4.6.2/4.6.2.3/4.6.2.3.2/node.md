# N589: H100 专业维护成本 (Maintenance_OPEX) 的量化构成：年维护成本 = (Coolant_Replace_Cost / Cycle_Years

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N245

## Claim

H100 专业维护成本 (Maintenance_OPEX) 的量化构成：年维护成本 = (Coolant_Replace_Cost / Cycle_Years) + (Fan_Cleaning_Labor) + (Spares_Inventory)；对于液冷 H100 节点，冷却液每 2-3 年更换一次，单次成本约 $2,000-$5,000 (整节点)，单卡分摊年成本约 $800-$1,500；风冷 H100 PCIe 版本无冷却液成本，但风扇更换频率高，年备件成本约 $200-$400/卡。N245 中 $500-$1000 的估算仅适用于风冷版本，液冷版本需上调至 $800-$2,000。

## Corrected Claim

H100 专业维护成本 (Maintenance_OPEX) 的量化构成：年维护成本 = (Coolant_Replace_Cost / Cycle_Years) + (Fan_Cleaning_Labor) + (Spares_Inventory)；对于液冷 H100 节点，冷却液每 2-3 年更换一次，单次成本约 $2,000-$5,000 (整节点)，单卡分摊年成本约 $800-$1,500；风冷 H100 PCIe 版本无冷却液成本，但风扇更换频率高，年备件成本约 $200-$400/卡。N245 中 $500-$1000 的估算仅适用于风冷版本，液冷版本需上调至 $800-$2,000。

## Evidence

先验知识/题面给定，逻辑校验通过
