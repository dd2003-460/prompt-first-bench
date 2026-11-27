# N99: Total_Cost_of_Ownership_per_year 的完整展开：TCO_year = (Hardware_Price - Residual_Val

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N37

## Claim

Total_Cost_of_Ownership_per_year 的完整展开：TCO_year = (Hardware_Price - Residual_Value_3yr) / 3 + (TDP_kW * 8760h * Electricity_Rate) + (Maintenance_Annual_Cost)。需代入 N39/N40 的折旧数据和 N35 的电力成本公式

## Corrected Claim

Total_Cost_of_Ownership_per_year 的完整展开：TCO_year = (Hardware_Price - Residual_Value_3yr) / 3 + (TDP_kW * 8760h * Electricity_Rate) + (Maintenance_Annual_Cost)。需代入 N39/N40 的折旧数据和 N35 的电力成本公式

## Evidence

先验知识/题面给定，逻辑校验通过：TCO公式结构符合标准财务折旧与运营成本计算逻辑，量纲一致（货币/年），且作为knowledge节点无需外部来源支持。

## Search Query

GPU total cost of ownership calculation formula depreciation electricity maintenance
