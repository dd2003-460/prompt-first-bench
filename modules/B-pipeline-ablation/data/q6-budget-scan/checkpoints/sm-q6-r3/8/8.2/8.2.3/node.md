# N197: 服务器月度运行时间修正：若服务器并非7x24小时满载，实际耗电量 = P_actual * 24h * 30d * 负载因子(0.7-0.9)；对于CDN节点，

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N61

## Claim

服务器月度运行时间修正：若服务器并非7x24小时满载，实际耗电量 = P_actual * 24h * 30d * 负载因子(0.7-0.9)；对于CDN节点，夜间流量低谷期负载因子降至0.5，月度平均负载因子约为0.85，修正后月耗电量 ≈ 285W * 720h * 0.85 / 1000 = 174.4 kWh

## Corrected Claim

服务器月度运行时间修正：若服务器并非7x24小时满载，实际耗电量 = P_actual * 24h * 30d * 负载因子(0.7-0.9)；对于CDN节点，夜间流量低谷期负载因子降至0.5，月度平均负载因子约为0.85，修正后月耗电量 ≈ 285W * 720h * 0.85 / 1000 = 174.4 kWh

## Evidence

先验知识/题面给定，逻辑校验通过：285W * 720h * 0.85 / 1000 = 174.42 kWh，计算无误，负载因子取值符合CDN业务常识。

## Search Query

CDN server daily traffic load factor average utilization
