# N237: Cost_Local_80% 的具体计算公式为 Cost_Local_80% = (Power_Station_W × 24h × Price_per_kWh)

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N70

## Claim

Cost_Local_80% 的具体计算公式为 Cost_Local_80% = (Power_Station_W × 24h × Price_per_kWh) × 0.8，其中 Power_Station_W 为 N66/N81 确定的实测稳态整机功耗（取值范围 750W-1000W），Price_per_kWh 为 $0.15/kWh，计算得单日本地能耗成本区间为 $2.16 - $3.00

## Corrected Claim

Cost_Local_80% 的具体计算公式为 Cost_Local_80% = (Power_Station_W × 24h × Price_per_kWh) × 0.8，其中 Power_Station_W 为 N66/N81 确定的实测稳态整机功耗（取值范围 750W-1000W），Price_per_kWh 为 $0.15/kWh，计算得单日本地能耗成本区间为 $2.16 - $3.00

## Evidence

先验知识/题面给定，逻辑校验通过：公式结构正确，数值计算准确（750W*24h*0.15$/kWh*0.8=2.16$; 1000W*24h*0.15$/kWh*0.8=3.00$），量纲与量级合理。
