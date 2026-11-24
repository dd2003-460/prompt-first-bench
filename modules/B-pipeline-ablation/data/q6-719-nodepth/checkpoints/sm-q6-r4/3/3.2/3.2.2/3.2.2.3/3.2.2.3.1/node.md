# N730: 100Gbps上行链路满载下的单位流量成本 C_unit_100G = (Monthly_Rent_100G + Power_Cost_100G + Maint

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N251

## Claim

100Gbps上行链路满载下的单位流量成本 C_unit_100G = (Monthly_Rent_100G + Power_Cost_100G + Maintenance_100G) / (100 Gbps × 30 days × 86400s × 1000 / 8) GB，其中 Monthly_Rent_100G ≈ ¥200,000, Power_Cost_100G 需根据满载功耗估算

## Corrected Claim

100Gbps上行链路满载下的单位流量成本 C_unit_100G = (Monthly_Rent_100G + Power_Cost_100G + Maintenance_100G) / (100 Gbps × 30 days × 86400s × 1000 / 8) GB，其中 Monthly_Rent_100G ≈ ¥200,000, Power_Cost_100G 需根据满载功耗估算

## Evidence

先验知识/题面给定，逻辑校验通过：公式量纲正确（成本/流量），100Gbps满载月流量计算逻辑自洽（100*10^9 bps * 30*86400 s / 8 ≈ 3.24*10^15 bits = 4.05*10^14 bytes ≈ 405 PB），¥200,000/月为100G专线合理量级。
