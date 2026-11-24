# N235: 单 POP 月度带宽成本 Bandwidth_Per_POP = Provisioned_Bandwidth_Mbps × Unit_Price_Mbps_Mo

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N70

## Claim

单 POP 月度带宽成本 Bandwidth_Per_POP = Provisioned_Bandwidth_Mbps × Unit_Price_Mbps_Month，其中 Provisioned_Bandwidth_Mbps 为单 POP 预置带宽（需覆盖峰值流量，通常 1-10 Gbps），Unit_Price_Mbps_Month 为机房带宽租赁单价（国内一线城市 ¥100-300/Mbps/月，二线城市 ¥50-150/Mbps/月），需区分地域加权计算。

## Corrected Claim

单 POP 月度带宽成本 Bandwidth_Per_POP = Provisioned_Bandwidth_Mbps × Unit_Price_Mbps_Month，其中 Provisioned_Bandwidth_Mbps 为单 POP 预置带宽（需覆盖峰值流量，通常 1-10 Gbps），Unit_Price_Mbps_Month 为机房带宽租赁单价（国内一线城市 ¥100-300/Mbps/月，二线城市 ¥50-150/Mbps/月），需区分地域加权计算。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

data center bandwidth leasing price per Mbps per month China tier 1 city tier 2 city
