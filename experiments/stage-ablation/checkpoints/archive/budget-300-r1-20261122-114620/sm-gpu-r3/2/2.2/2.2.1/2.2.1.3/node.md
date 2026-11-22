# N191: A100 80GB 单卡方案 5 年 TCO 中的电力成本项 C_power_5yr：假设平均功耗 P_avg = 250W (推理负载)，电价 $0.10/k

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N58

## Claim

A100 80GB 单卡方案 5 年 TCO 中的电力成本项 C_power_5yr：假设平均功耗 P_avg = 250W (推理负载)，电价 $0.10/kWh，年运行 8760 小时，则 C_power_5yr = 250W * 8760h * 5 * $0.10/kWh = $10,950。

## Corrected Claim

A100 80GB 单卡方案 5 年 TCO 中的电力成本项 C_power_5yr：假设平均功耗 P_avg = 250W (推理负载)，电价 $0.10/kWh，年运行 8760 小时，则 C_power_5yr = 250W * 8760h * 5 * $0.10/kWh = $10,950。

## Evidence

先验知识/题面给定，逻辑校验通过：250W * 8760h * 5 * $0.10/kWh = $10,950，计算无误且量级合理。

## Search Query

A100 80GB TDP 400W average power consumption inference workload 250W
