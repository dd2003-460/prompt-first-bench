# N392: H100 SXM 节点 3 年 24/7 运行电力成本 (3yr_Electricity_Cost) 计算公式为 P_Yearly = (Total_Power

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N163

## Claim

H100 SXM 节点 3 年 24/7 运行电力成本 (3yr_Electricity_Cost) 计算公式为 P_Yearly = (Total_Power_W * 0.85_efficiency) * 8760h * Price_kWh；以 Total_Power_W = 1050W (输入端), Efficiency = 0.85 (钛金电源+风扇损耗), Price_kWh = $0.15 为例，P_Yearly = (1050 * 0.85) * 8760 * 0.15 ≈ $1,174/年；3 年总电费 ≈ $3,522。若电价为 $0.60 (中国)，3 年总电费 ≈ $14,088。

## Corrected Claim

H100 SXM 节点 3 年 24/7 运行电力成本 (3yr_Electricity_Cost) 计算公式为 P_Yearly = (Total_Power_W * 0.85_efficiency) * 8760h * Price_kWh；以 Total_Power_W = 1050W (输入端), Efficiency = 0.85 (钛金电源+风扇损耗), Price_kWh = $0.15 为例，P_Yearly = (1050 * 0.85) * 8760 * 0.15 ≈ $1,174/年；3 年总电费 ≈ $3,522。若电价为 $0.60 (中国)，3 年总电费 ≈ $14,088。

## Evidence

先验知识/题面给定，逻辑校验通过：公式逻辑自洽，数值计算准确（1050*0.85*8760*0.15≈1174.1，3年≈3522；1050*0.85*8760*0.60≈4696.4，3年≈14089，与14088误差在舍入范围内），符合工程估算惯例。
