# N141: 混合策略流量切分比例 α 对公有云带宽成本 C_bw_cloud(α) 的边际敏感度为 dC/dα = - V_traffic_total * P_bw_uni

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N40

## Claim

混合策略流量切分比例 α 对公有云带宽成本 C_bw_cloud(α) 的边际敏感度为 dC/dα = - V_traffic_total * P_bw_unit，对于日均2TB下载量，每将1%流量从公有云切回自建，月节省带宽成本 ≈ 2TB*30*0.01 * ¥0.22 ≈ ¥132/月。

## Corrected Claim

混合策略流量切分比例 α 对公有云带宽成本 C_bw_cloud(α) 的边际敏感度为 dC/dα = - V_traffic_total * P_bw_unit，对于日均2TB下载量，每将1%流量从公有云切回自建，月节省带宽成本 ≈ 2TB*30*0.01 * ¥0.22 ≈ ¥132/月。

## Evidence

先验知识/题面给定，逻辑校验通过：数学推导正确（2TB*30*0.01*0.22=132），量纲与数值量级合理，符合成本线性递减的基本经济直觉。
