# N21: 电力运行成本 (C_power) = P_avg_W × T_hours × E_price_per_kWh；其中 P_avg_W 为满载推理平均功耗（如 40

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N4, N5, N6

## Claim

电力运行成本 (C_power) = P_avg_W × T_hours × E_price_per_kWh；其中 P_avg_W 为满载推理平均功耗（如 4090 约 450W, A100 约 400W），E_price 为当地电价（假设 $0.10/kWh），T_hours 为年运行小时数（如 8760h）。

## Corrected Claim

电力运行成本 (C_power) = P_avg_W × T_hours × E_price_per_kWh；其中 P_avg_W 为满载推理平均功耗（如 4090 约 450W, A100 约 400W），E_price 为当地电价（假设 $0.10/kWh），T_hours 为年运行小时数（如 8760h）。

## Evidence

先验知识/题面给定，逻辑校验通过
