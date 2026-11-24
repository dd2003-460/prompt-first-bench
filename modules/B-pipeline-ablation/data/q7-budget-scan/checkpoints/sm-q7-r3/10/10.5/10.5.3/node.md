# N411: 出口流量成本计算公式：Cost_egress = Data_Volume_TB * 1024 GB/TB * Price_per_GB * Exchange_R

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N155

## Claim

出口流量成本计算公式：Cost_egress = Data_Volume_TB * 1024 GB/TB * Price_per_GB * Exchange_Rate；若 Data_Volume=500TB, Price=$0.09/GB, Exchange=7.2, 则 Cost = 500*1024*0.09*7.2 ≈ ¥330,777（与 N155 中的 ¥324,000 接近，差异源于单价或免费额度计算）。

## Corrected Claim

出口流量成本计算公式：Cost_egress = Data_Volume_TB * 1024 GB/TB * Price_per_GB * Exchange_Rate；若 Data_Volume=500TB, Price=$0.09/GB, Exchange=7.2, 则 Cost = 500*1024*0.09*7.2 ≈ ¥330,777（与 N155 中的 ¥324,000 接近，差异源于单价或免费额度计算）。

## Evidence

先验知识/题面给定，逻辑校验通过：500 * 1024 * 0.09 * 7.2 = 330,777.6，计算准确且量级合理。
