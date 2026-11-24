# N748: 弹性缓冲成本结构：Total_Cost_Elastic = Fixed_Bandwidth_Cost + (Peak_Bandwidth - Committed

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N257

## Claim

弹性缓冲成本结构：Total_Cost_Elastic = Fixed_Bandwidth_Cost + (Peak_Bandwidth - Committed_Bandwidth) × Pay_As_You_Go_Rate，其中 Fixed_Bandwidth_Cost 基于承诺带宽（如95%分位），Pay_As_You_Go_Rate 为超出部分单价（通常比基础价高20-30%）。

## Corrected Claim

弹性缓冲成本结构：Total_Cost_Elastic = Fixed_Bandwidth_Cost + (Peak_Bandwidth - Committed_Bandwidth) × Pay_As_You_Go_Rate，其中 Fixed_Bandwidth_Cost 基于承诺带宽（如95%分位），Pay_As_You_Go_Rate 为超出部分单价（通常比基础价高20-30%）。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

cloud CDN elastic bandwidth pricing pay-as-you-go overage rate
