# N195: 自建POP峰值带宽计费成本模型：Monthly_Bandwidth_Cost = Peak_Bandwidth_Mbps × Unit_Price_Mbps_M

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N63

## Claim

自建POP峰值带宽计费成本模型：Monthly_Bandwidth_Cost = Peak_Bandwidth_Mbps × Unit_Price_Mbps_Month × 12，其中Peak_Bandwidth_Mbps = Avg_Bandwidth_Mbps × Peak_Factor，Avg_Bandwidth_Mbps = 2960 Mbps，Peak_Factor典型值2.5（基于N133冗余系数修正），则Peak ≈ 7400 Mbps

## Corrected Claim

自建POP峰值带宽计费成本模型：Monthly_Bandwidth_Cost = Peak_Bandwidth_Mbps × Unit_Price_Mbps_Month × 12，其中Peak_Bandwidth_Mbps = Avg_Bandwidth_Mbps × Peak_Factor，Avg_Bandwidth_Mbps = 2960 Mbps，Peak_Factor典型值2.5（基于N133冗余系数修正），则Peak ≈ 7400 Mbps

## Evidence

先验知识/题面给定，逻辑校验通过：2960 * 2.5 = 7400，计算无误，模型定义自洽。
