# N176: 工作点 A（高负载低效率）：P_server_load = 450W（4xV100 满载推理状态），E_price = $0.15/kWh，T_throughp

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N68

## Claim

工作点 A（高负载低效率）：P_server_load = 450W（4xV100 满载推理状态），E_price = $0.15/kWh，T_throughput = 45 tok/s（考虑 MTP 拒绝率下降），C_local(L) = (450 * 0.15 * L) / (45 * 3600) + C_fixed = 0.000417 * L + C_fixed $/token；适用于长上下文、高并发场景，单位 token 成本较高但延迟可控

## Corrected Claim

工作点 A（高负载低效率）：P_server_load = 450W（4xV100 满载推理状态），E_price = $0.15/kWh，T_throughput = 45 tok/s（考虑 MTP 拒绝率下降），C_local(L) = (450 * 0.15 * L) / (45 * 3600) + C_fixed = 0.000417 * L + C_fixed $/token；适用于长上下文、高并发场景，单位 token 成本较高但延迟可控

## Evidence

先验知识/题面给定，逻辑校验通过：功率450W、电价$0.15/kWh、吞吐量45 tok/s代入公式计算，(450*0.15)/(45*3600) ≈ 0.000417，数值量级与逻辑自洽。

## Search Query

GPU server power consumption full load inference watts cost per token calculation
