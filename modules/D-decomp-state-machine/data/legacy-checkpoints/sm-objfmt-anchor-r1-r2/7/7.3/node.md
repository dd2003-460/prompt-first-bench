# N107: Total_Cost_of_Ownership_5yr (TCO) 中电力成本项 E_cost = Power_W * Utilization_Hours * 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N30

## Claim

Total_Cost_of_Ownership_5yr (TCO) 中电力成本项 E_cost = Power_W * Utilization_Hours * Rate_kWh * Years；以 RTX 4090 (450W) 为例，若利用率 50% (4380 hours/year over 5 years? No, 0.5*8760*5=21900h)，E_cost = 450W/1000 * 21900h * $0.12/kWh ≈ $1182.6；加上购买成本 $1800，总 TCO ≈ $2982.6。

## Corrected Claim

Total_Cost_of_Ownership_5yr (TCO) 中电力成本项 E_cost = Power_W * Utilization_Hours * Rate_kWh * Years；以 RTX 4090 (450W) 为例，若利用率 50% (4380 hours/year over 5 years? No, 0.5*8760*5=21900h)，E_cost = 450W/1000 * 21900h * $0.12/kWh ≈ $1182.6；加上购买成本 $1800，总 TCO ≈ $2982.6。

## Evidence

先验知识/题面给定，逻辑校验通过：计算过程 0.45kW * 21900h * $0.12/kWh = $1182.6 正确，总成本 $1182.6 + $1800 = $2982.6 正确，量纲与数值量级合理。
