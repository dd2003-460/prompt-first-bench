# N85: 混合策略下公有云部分出口带宽成本 (C_bw_cloud, ¥/1000 req) 计算为 (V_tail * Unit_Price_cloud) / Q_da

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N17

## Claim

混合策略下公有云部分出口带宽成本 (C_bw_cloud, ¥/1000 req) 计算为 (V_tail * Unit_Price_cloud) / Q_day_total * 1000，其中 V_tail 为长尾区域日均下载流量（GB），Unit_Price_cloud 为公有云 CDN 出口带宽单价（¥/GB）。

## Corrected Claim

混合策略下公有云部分出口带宽成本 (C_bw_cloud, ¥/1000 req) 计算为 (V_tail * Unit_Price_cloud) / Q_day_total * 1000，其中 V_tail 为长尾区域日均下载流量（GB），Unit_Price_cloud 为公有云 CDN 出口带宽单价（¥/GB）。

## Evidence

父节点级核验通过：正交+完备+无冗余（父节点公式由 V_tail 和 Unit_Price_cloud 两个独立变量组成。子节点分别定义了这两个变量的计算逻辑/取值范围，二者在数学上是独立的乘积因子，互不重叠且无矛盾。所有关键输入参数均已覆盖，且每个子节点对应唯一的参数定义，不存在冗余。）
