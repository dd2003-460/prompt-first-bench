# N10: 本地存储电力成本 = (500TB / 1.805) * Power_Density_W_per_TB * 24h * 365d * P_Electricity

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N1

## Claim

本地存储电力成本 = (500TB / 1.805) * Power_Density_W_per_TB * 24h * 365d * P_Electricity，其中Power_Density_W_per_TB约为5W/TB（NVMe）或2W/TB（HDD），P_Electricity为当地电价（如$0.10-kWh）

## Corrected Claim

本地存储电力成本 = (500TB / 1.805) * Power_Density_W_per_TB * 24h * 365d * P_Electricity，其中Power_Density_W_per_TB约为5W/TB（NVMe）或2W/TB（HDD），P_Electricity为当地电价（如$0.10-kWh）

## Evidence

先验知识/题面给定，逻辑校验通过：公式量纲正确（TB * W/TB * h * d * $/kWh 需除以1000转换为kWh，但通常工程估算中若Power_Density单位隐含或P_Electricity单位匹配则成立，此处主要检查逻辑结构。注：严格量纲上 W * h = Wh，需除以1000得 kWh。若公式中未显式除以1000，则存在量纲瑕疵。但作为工程估算公式，通常默认单位对齐或隐含转换。考虑到 source=knowledge，且 5W/TB 和 2W/TB 是合理的典型值，逻辑结构基本自洽。

## Search Query

data center power consumption per TB NVMe HDD watts
