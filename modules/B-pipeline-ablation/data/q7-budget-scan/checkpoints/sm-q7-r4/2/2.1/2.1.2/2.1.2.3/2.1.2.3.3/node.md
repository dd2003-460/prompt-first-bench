# N492: 服务器主机功耗叠加：N165 仅计算了 SSD 功耗，忽略了服务器主机（CPU/RAM/Fans/PSU）的功耗；一台双路存储服务器在中等负载下功耗约为 400

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N165

## Claim

服务器主机功耗叠加：N165 仅计算了 SSD 功耗，忽略了服务器主机（CPU/RAM/Fans/PSU）的功耗；一台双路存储服务器在中等负载下功耗约为 400-600W；若取 500W，则系统总功耗 = SSD_Power + Host_Power = 0.154kW + 0.5kW = 0.654kW；年电力成本 = 0.654kW * 1.4 (PUE) * 0.8¥/kWh * 8760h ≈ ¥6,410/年。

## Corrected Claim

服务器主机功耗叠加：N165 仅计算了 SSD 功耗，忽略了服务器主机（CPU/RAM/Fans/PSU）的功耗；一台双路存储服务器在中等负载下功耗约为 400-600W；若取 500W，则系统总功耗 = SSD_Power + Host_Power = 0.154kW + 0.5kW = 0.654kW；年电力成本 = 0.654kW * 1.4 (PUE) * 0.8¥/kWh * 8760h ≈ ¥6,410/年。

## Evidence

先验知识/题面给定，逻辑校验通过：双路存储服务器500W功耗及PUE 1.4符合行业常规，算术计算准确（0.654*1.4*0.8*8760≈6410）

## Search Query

dual socket storage server power consumption watts typical load
