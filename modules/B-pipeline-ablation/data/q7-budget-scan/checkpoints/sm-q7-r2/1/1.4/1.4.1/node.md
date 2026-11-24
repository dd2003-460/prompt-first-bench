# N46: NVMe SSD阵列裸功耗成本 = (500TB / 1.805) * 5W/TB * 24h * 365d * P_Electricity，其中P_Elect

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N10

## Claim

NVMe SSD阵列裸功耗成本 = (500TB / 1.805) * 5W/TB * 24h * 365d * P_Electricity，其中P_Electricity为当地电价（如$0.10/kWh），计算结果约为$14,900/年

## Corrected Claim

NVMe SSD阵列裸功耗成本 = (500TB / 1.805) * 5W/TB * 24h * 365d * P_Electricity，其中P_Electricity为当地电价（如$0.10/kWh），计算结果约为$1,213/年

## Evidence

先验知识/题面给定，逻辑校验通过：500TB/1.805TB≈277TB有效容量，277*5W≈1385W，1385W*8760h≈12.13MWh，12.13MWh*$0.10/kWh≈$1213/年。等等，这里计算有误。重新计算：500/1.805 = 277.008 TB。277.008 * 5W = 1385.04 W = 1.385 kW。1.385 kW * 24h * 365d = 12,133.8 kWh。12,133.8 kWh * $0.10/kWh = $1,213.38。原陈述称约为$14,900/年，数值量级错误（相差约12倍）。
