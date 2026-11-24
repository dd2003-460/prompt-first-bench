# N288: 单POP电力成本 C_power_pop = P_server_avg * 24h * 30d * P_elec，其中 P_server_avg ≈ 500W/

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N95

## Claim

单POP电力成本 C_power_pop = P_server_avg * 24h * 30d * P_elec，其中 P_server_avg ≈ 500W/台 * 10台 = 5kW，P_elec ≈ ¥0.8/kWh，计算得 ¥2,880/月。

## Corrected Claim

单POP电力成本 C_power_pop = P_server_avg * 24h * 30d * P_elec，其中 P_server_avg ≈ 500W/台 * 10台 = 5kW，P_elec ≈ ¥0.8/kWh，计算得 ¥2,880/月。

## Evidence

先验知识/题面给定，逻辑校验通过：5kW * 24h * 30d * 0.8元/kWh = 2880元，计算无误且量级合理。

## Search Query

data center power cost 5kW 24h 30d 0.8 CNY/kWh
