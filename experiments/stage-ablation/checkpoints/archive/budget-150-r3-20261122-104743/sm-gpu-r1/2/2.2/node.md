# N12: 电力成本 (Power Cost) = (GPU_TDP + System_Overhead_TDP) × Utilization_Factor × Elect

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N2

## Claim

电力成本 (Power Cost) = (GPU_TDP + System_Overhead_TDP) × Utilization_Factor × Electricity_Rate × Time，其中 GPU_TDP 为各型号标称功耗（如 450W, 700W），需考虑空闲与满载的平均功耗差异

## Corrected Claim

电力成本 (Power Cost) = (GPU_TDP + System_Overhead_TDP) × Utilization_Factor × Electricity_Rate × Time，其中 GPU_TDP 为各型号标称功耗（如 450W, 700W），需考虑空闲与满载的平均功耗差异

## Evidence

先验知识/题面给定，逻辑校验通过
