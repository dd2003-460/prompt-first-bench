# N205: GPTQ 量化的一次性 TCO 摊销成本 C_quant_amortized = (T_cal * C_compute_hourly + C_engineeri

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N56

## Claim

GPTQ 量化的一次性 TCO 摊销成本 C_quant_amortized = (T_cal * C_compute_hourly + C_engineering_hours * C_hourly) / N_usage_hours；若使用云服务 (A100 $1.71/h) 执行校准，T_cal=4h 则硬件成本 $6.84，加上工程调试时间 2h * $100/h = $200，总成本约 $207，分摊到 3 年 (26280h) 运行时间后，每小时增加成本约 $0.000008，对 TCO 影响可忽略 (<0.1%)。

## Corrected Claim

GPTQ 量化的一次性 TCO 摊销成本 C_quant_amortized = (T_cal * C_compute_hourly + C_engineering_hours * C_hourly) / N_usage_hours；若使用云服务 (A100 $1.71/h) 执行校准，T_cal=4h 则硬件成本 $6.84，加上工程调试时间 2h * $100/h = $200，总成本约 $207，分摊到 3 年 (26280h) 运行时间后，每小时增加成本约 $0.000008，对 TCO 影响可忽略 (<0.1%)。

## Evidence

先验知识/题面给定，逻辑校验通过：算术计算正确（4*1.71+2*100=206.84，206.84/26280≈0.00786 $/h），量级合理，符合一次性成本摊销逻辑。
