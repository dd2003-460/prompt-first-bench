# N12: 电力成本 (Power Cost) = (GPU_TDP + System_Overhead_TDP) × Utilization_Factor × Elect

- **status**: pending
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

父节点级核验未通过：不完备, 有冗余（1. 冗余性：前5个子节点均为不同型号GPU的TDP数值，本质上是同一参数（GPU_TDP）的不同取值，属于典型的参数枚举而非独立维度，应压缩为表格或变量列表。2. 不完备性：父节点公式明确包含 'System_Overhead_TDP'、'Utilization_Factor'、'Electricity_Rate' 和 'Time'，但子节点仅覆盖了 GPU_TDP 和 System_Overhead_TDP 的部分硬件功耗，缺失了电价、时间、利用率系数等关键变量，也未涵盖公式中其他必要的计算参数。）
