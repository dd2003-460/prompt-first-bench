# N99: Total_Cost_of_Ownership_per_year 的完整展开：TCO_year = (Hardware_Price - Residual_Val

- **status**: pending
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

父节点级核验未通过：有冗余（子节点代表同一公式在不同硬件参数下的具体实例，彼此不重叠且覆盖了父节点提到的主要硬件类型（RTX/H100/MI300X），但在结构上属于‘同构重复’，即它们本质上是同一计算逻辑的三次实例化，而非分解出不同的子成本项（如硬件、电力、维护）。）

## Search Query

GPU total cost of ownership calculation formula depreciation electricity maintenance
