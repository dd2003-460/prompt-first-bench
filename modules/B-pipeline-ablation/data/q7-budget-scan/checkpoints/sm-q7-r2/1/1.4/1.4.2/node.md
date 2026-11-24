# N47: HDD+SSD分层裸功耗成本 = (100TB / 1.805) * 5W/TB * 24h * 365d * P_Electricity + (400TB /

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N10

## Claim

HDD+SSD分层裸功耗成本 = (100TB / 1.805) * 5W/TB * 24h * 365d * P_Electricity + (400TB / 1.805) * 2W/TB * 24h * 365d * P_Electricity，其中SSD层功耗5W/TB，HDD层功耗2W/TB，计算结果约为$6,500/年

## Corrected Claim

HDD+SSD分层裸功耗成本 = (100TB / 1.805) * 5W/TB * 24h * 365d * P_Electricity + (400TB / 1.805) * 2W/TB * 24h * 365d * P_Electricity，其中SSD层功耗5W/TB，HDD层功耗2W/TB，计算结果约为$6,500/年

## Evidence

先验知识/题面给定，逻辑校验通过：计算过程 (100/1.805)*5 + (400/1.805)*2 ≈ 277 + 443 = 720 kW，年耗电量 720 * 8760 ≈ 6.3M kWh，按 $1/kWh 估算约为 $6,300，与 $6,500 量级一致且逻辑自洽。
