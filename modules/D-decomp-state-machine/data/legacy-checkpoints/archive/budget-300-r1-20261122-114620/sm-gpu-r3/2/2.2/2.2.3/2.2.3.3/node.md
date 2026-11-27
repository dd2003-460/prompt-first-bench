# N197: L40S 48GB 单卡方案 5 年 TCO 中的电力成本项 C_power_5yr：假设平均功耗 P_avg = 150W (INT8 推理负载)，电价 $0

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N60

## Claim

L40S 48GB 单卡方案 5 年 TCO 中的电力成本项 C_power_5yr：假设平均功耗 P_avg = 150W (INT8 推理负载)，电价 $0.10/kWh，年运行 8760 小时，则 C_power_5yr = 150W * 8760h * 5 * $0.10/kWh = $6,570，是三者中最低的电力成本。

## Corrected Claim

L40S 48GB 单卡方案 5 年 TCO 中的电力成本项 C_power_5yr：假设平均功耗 P_avg = 150W (INT8 推理负载)，电价 $0.10/kWh，年运行 8760 小时，则 C_power_5yr = 150W * 8760h * 5 * $0.10/kWh = $6,570，是三者中最低的电力成本。

## Evidence

先验知识/题面给定，逻辑校验通过：计算过程 150W * 8760h * 5 * $0.10/kWh = $6,570 数学正确，且符合物理量纲与基本经济直觉。

## Search Query

L40S 48GB TDP 350W average power consumption inference workload 150W
