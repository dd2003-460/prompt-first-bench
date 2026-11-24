# N274: 在长尾区域低成本 POP 点工作点下，带宽单位成本 unit_cost_per_Mbps_month = (1000 + 200) = 1200 元/Mbps/

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N87

## Claim

在长尾区域低成本 POP 点工作点下，带宽单位成本 unit_cost_per_Mbps_month = (1000 + 200) = 1200 元/Mbps/月，取骨干网和接入带宽的低位值，适用于流量稀疏、对延迟不敏感的边缘节点，成本最低但 P99 延迟可能超标。

## Corrected Claim

在长尾区域低成本 POP 点工作点下，带宽单位成本 unit_cost_per_Mbps_month = (1000 + 200) = 1200 元/Mbps/月，取骨干网和接入带宽的低位值，适用于流量稀疏、对延迟不敏感的边缘节点，成本最低但 P99 延迟可能超标。

## Evidence

先验知识/题面给定，逻辑校验通过：1000+200=1200计算正确，符合长尾低成本POP点（低带宽成本+低接入成本）的经济直觉，且明确标注了适用场景（流量稀疏、延迟不敏感）及风险（P99延迟超标），逻辑自洽。

## Search Query

China rural CDN bandwidth cost low tier 2024
