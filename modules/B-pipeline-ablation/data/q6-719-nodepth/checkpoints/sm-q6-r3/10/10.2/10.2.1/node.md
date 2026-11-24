# N379: 电力成本C_power_monthly：单台服务器平均功耗P_server_avg=300W，10个POP共20台服务器，月电费 = 20 * 0.3kW * 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N128

## Claim

电力成本C_power_monthly：单台服务器平均功耗P_server_avg=300W，10个POP共20台服务器，月电费 = 20 * 0.3kW * 24h * 30d * ¥0.8/kWh = ¥3,456/月；若考虑PUE=1.5，实际电费为¥5,184/月。

## Corrected Claim

电力成本C_power_monthly：单台服务器平均功耗P_server_avg=300W，10个POP共20台服务器，月电费 = 20 * 0.3kW * 24h * 30d * ¥0.8/kWh = ¥3,456/月；若考虑PUE=1.5，实际电费为¥5,184/月。

## Evidence

先验知识/题面给定，逻辑校验通过：基础电费计算 20 * 0.3 * 24 * 30 * 0.8 = 3456 正确；PUE 调整后 3456 * 1.5 = 5184 正确。

## Search Query

server power consumption 300W data center PUE 1.5 electricity cost China 0.8 CNY/kWh
