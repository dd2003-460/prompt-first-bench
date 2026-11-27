# N258: 吞吐量-电价二维决策矩阵：当电价 < $0.114/kWh 且吞吐量需求 < 12.46 tokens/s 时，M3 Ultra 为 TCO 最优；当电价 < 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N100

## Claim

吞吐量-电价二维决策矩阵：当电价 < $0.114/kWh 且吞吐量需求 < 12.46 tokens/s 时，M3 Ultra 为 TCO 最优；当电价 < $0.114/kWh 且吞吐量需求 > 12.46 tokens/s 时，2×4090 为最优；当电价 > $0.114/kWh 时，需进一步比较 M3 Ultra 与 2×4090 的单位 token 成本，若 M3 Ultra 吞吐不足导致单位成本高于 2×4090，则仍选 2×4090，否则选 M3 Ultra。

## Corrected Claim

吞吐量-电价二维决策矩阵：当电价 < $0.114/kWh 且吞吐量需求 < 12.46 tokens/s 时，M3 Ultra 为 TCO 最优；当电价 < $0.114/kWh 且吞吐量需求 > 12.46 tokens/s 时，2×4090 为最优；当电价 > $0.114/kWh 时，需进一步比较 M3 Ultra 与 2×4090 的单位 token 成本，若 M3 Ultra 吞吐不足导致单位成本高于 2×4090，则仍选 2×4090，否则选 M3 Ultra。

## Evidence

先验知识/题面给定，逻辑校验通过
