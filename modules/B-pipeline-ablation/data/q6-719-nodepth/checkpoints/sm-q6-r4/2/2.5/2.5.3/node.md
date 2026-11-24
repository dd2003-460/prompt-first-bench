# N83: 自建 POP 点的回源带宽月度成本 (C_bw_month, ¥/月) 采用阶梯定价模型：C_bw_month = (B_peak * Unit_Price_9

- **status**: pending
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N16

## Claim

自建 POP 点的回源带宽月度成本 (C_bw_month, ¥/月) 采用阶梯定价模型：C_bw_month = (B_peak * Unit_Price_95th) * 1000 + (V_origin_excess * Unit_Price_95th_excess)，其中 Unit_Price_95th 为 95th 百分位带宽单价（¥/Mbps/月），Unit_Price_95th_excess 为超量流量计费单价（¥/GB）。

## Corrected Claim

自建 POP 点的回源带宽月度成本通常包含带宽租赁费（基于95th百分位带宽或峰值带宽）和可能的流量超额费，具体公式取决于运营商合同，常见形式为 C_bw_month = (B_95th * Unit_Price_95th) + (V_excess * Unit_Price_excess)，其中 B_95th 为95th百分位带宽，V_excess 为超出承诺带宽对应的流量或总流量（视合同而定）。

## Evidence

父节点级核验未通过：不完备（子节点之间正交，分别解释了公式中的两个单价参数和一个计算示例，无矛盾。但存在完备性缺陷：父节点公式中明确包含变量 B_peak（峰值带宽）和 V_origin_excess（超量流量），子节点仅提供了单价的市场行情，未提供 B_peak 的估算方法或数据来源，也未提供 V_origin_excess 的定义或估算逻辑，导致无法仅凭子节点独立复现父节点的计算。）

## Search Query

China telecom 95th percentile bandwidth pricing per Mbps per month CDN origin pull cost

## Retrieval Sources

- {'url': 'https://wenku.baidu.com/view/26c304a6950ef12d2af90242a8956bec0975a5cb.html&rut=bd9820eb56f43a40042d01c1bd05b12269ecb67c054f11ec94bc66e632280d72', 'type': 'ddg', 'title': 'CDN机房搭建费用明细解析：自建还是租用？一文看懂2026年成本与选择'}
