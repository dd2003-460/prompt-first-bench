# N178: 工作点 C（低负载高闲置）：P_server_load = 150W（4xV100 空闲+轻量推理），E_price = $0.15/kWh，T_through

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N68

## Claim

工作点 C（低负载高闲置）：P_server_load = 150W（4xV100 空闲+轻量推理），E_price = $0.15/kWh，T_throughput = 20 tok/s（单序列或小 batch），C_local(L) = (150 * 0.15 * L) / (20 * 3600) + C_fixed = 0.000313 * L + C_fixed $/token；适用于调试、小批量验证场景，虽然电力成本低但吞吐率低，单位 token 成本介于 A 和 B 之间

## Corrected Claim

工作点 C（低负载高闲置）：P_server_load = 150W（4xV100 空闲+轻量推理），E_price = $0.15/kWh，T_throughput = 20 tok/s（单序列或小 batch），C_local(L) = (150 * 0.15 * L) / (20 * 3600) + C_fixed = 0.000313 * L + C_fixed $/token；适用于调试、小批量验证场景，虽然电力成本低但吞吐率低，单位 token 成本介于 A 和 B 之间

## Evidence

先验知识/题面给定，逻辑校验通过：计算过程 (150*0.15)/(20*3600) ≈ 0.0003125 与陈述一致，量级合理，符合低负载高闲置场景特征。

## Search Query

GPU server idle power consumption low load inference cost analysis
