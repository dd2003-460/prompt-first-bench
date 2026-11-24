# N82: 自建 POP 点的回源带宽峰值需求 (B_peak, Gbps) 计算为 (V_origin * Peak_Factor) / (Peak_Window_Hou

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N16

## Claim

自建 POP 点的回源带宽峰值需求 (B_peak, Gbps) 计算为 (V_origin * Peak_Factor) / (Peak_Window_Hours * 3600 * 8)，其中 Peak_Factor 为峰值系数（通常 1.5-3.0），Peak_Window_Hours 为高峰时段时长（通常 4-8 小时）。

## Corrected Claim

自建 POP 点的回源带宽峰值需求 (B_peak, Gbps) 计算为 (V_origin * Peak_Factor) / (Peak_Window_Hours * 3600 * 8)，其中 Peak_Factor 为峰值系数（通常 1.5-3.0），Peak_Window_Hours 为高峰时段时长（通常 4-8 小时）。

## Evidence

父节点级核验未通过：不完备（子节点在逻辑上是正交的，分别解释了公式中的三个变量（Peak_Factor, Peak_Window_Hours）以及最终的计算示例。然而，存在明显的完备性缺陷：父节点公式中明确包含变量 V_origin（日均回源流量），但子节点中没有任何一个节点解释 V_origin 的来源、计算方式或定义（例如：V_origin 如何从总流量、缓存命中率、文件平均大小等推导出来）。缺少对 V_origin 的界定使得分解不完整。）
