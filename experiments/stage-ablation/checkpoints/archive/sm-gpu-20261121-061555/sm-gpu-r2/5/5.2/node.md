# N27: 硬件购置成本（CapEx）分解：单卡方案 = GPU_price + PSU_wattage_cost + Chassis_cost + Cooling_cos

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N5

## Claim

硬件购置成本（CapEx）分解：单卡方案 = GPU_price + PSU_wattage_cost + Chassis_cost + Cooling_cost；多卡方案 = N*GPU_price + High_power_PSU_cost + Multi-GPU_Chassis_cost + Interconnect_cost（PCIe riser/NVLink bridge），需对比 2×消费卡 vs 1×数据卡的具体价差

## Corrected Claim

硬件购置成本（CapEx）分解：单卡方案 = GPU_price + PSU_wattage_cost + Chassis_cost + Cooling_cost；多卡方案 = N*GPU_price + High_power_PSU_cost + Multi-GPU_Chassis_cost + Interconnect_cost（PCIe riser/NVLink bridge），需对比 2×消费卡 vs 1×数据卡的具体价差

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

dual consumer GPU vs single datacenter GPU cost comparison LLM inference
