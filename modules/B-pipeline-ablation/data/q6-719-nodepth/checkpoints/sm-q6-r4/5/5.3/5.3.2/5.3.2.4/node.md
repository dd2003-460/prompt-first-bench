# N294: 回源带宽成本 C_backhaul_pop = Q_backhaul_pop * P_backhaul_per_gb，其中 Q_backhaul_pop = Q

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N96

## Claim

回源带宽成本 C_backhaul_pop = Q_backhaul_pop * P_backhaul_per_gb，其中 Q_backhaul_pop = Q_pop * (1 - H_pop) 为回源流量，P_backhaul_per_gb 为骨干网/专线流量单价（¥0.1-0.3/GB），若H_pop=85%，则Q_backhaul_pop≈135GB/月，C_backhaul_pop ≈ ¥13.5-40.5/月，通常包含在带宽包或单独计费。

## Corrected Claim

回源带宽成本 C_backhaul_pop = Q_backhaul_pop * P_backhaul_per_gb，其中 Q_backhaul_pop = Q_pop * (1 - H_pop) 为回源流量，P_backhaul_per_gb 为骨干网/专线流量单价（¥0.1-0.3/GB），若H_pop=85%，则Q_backhaul_pop≈135GB/月，C_backhaul_pop ≈ ¥13.5-40.5/月，通常包含在带宽包或单独计费。

## Evidence

先验知识/题面给定，逻辑校验通过：公式定义自洽，数值计算（135GB * 0.1-0.3 = 13.5-40.5）准确，符合CDN回源计费的一般工程常识。
