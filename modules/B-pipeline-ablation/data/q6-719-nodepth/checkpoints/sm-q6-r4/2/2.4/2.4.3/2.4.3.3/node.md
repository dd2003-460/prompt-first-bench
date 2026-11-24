# N235: 单 POP 月度带宽成本 Bandwidth_Per_POP = Provisioned_Bandwidth_Mbps × Unit_Price_Mbps_Mo

- **status**: pending
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

父节点级核验未通过：不完备, 有冗余（子节点本质上是同一公式在不同参数（带宽大小、地域/单价）下的三个具体实例，存在严重的参数冗余。虽然它们覆盖了不同场景，但作为‘分解’而言，并未拆解出独立的成本构成要素（如将‘地域’和‘带宽量’作为独立维度分解，而非直接给出三个混合了地域和带宽的固定工作点）。此外，父节点强调‘需区分地域加权计算’，但子节点仅提供了离散的点，未体现加权逻辑或完整的地域覆盖（如缺失二线城市的高带宽场景或一线城市的低带宽场景的独立分析）。）

## Search Query

data center bandwidth leasing price per Mbps per month China tier 1 city tier 2 city
