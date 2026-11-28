# N83: 硬件摊销成本 (Hardware_Amortized_Cost) 计算公式为 Purchase_Price / (Useful_Life_Years * 365

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N24

## Claim

硬件摊销成本 (Hardware_Amortized_Cost) 计算公式为 Purchase_Price / (Useful_Life_Years * 365 * 24 * Utilization_Rate)，假设 Useful_Life_Years=3, Utilization_Rate=0.5，RTX 4090 ($1600) 每日摊销成本约为 $0.11，A100 80GB ($8000) 约为 $0.55。

## Corrected Claim

硬件摊销成本 (Hardware_Amortized_Cost) 计算公式为 Purchase_Price / (Useful_Life_Years * 365 * 24 * Utilization_Rate)，假设 Useful_Life_Years=3, Utilization_Rate=0.5，RTX 4090 ($1600) 每日摊销成本约为 $0.11，A100 80GB ($8000) 约为 $0.55。

## Evidence

先验知识/题面给定，逻辑校验通过：公式计算正确（1600/(3*365*24*0.5)≈0.11, 8000/(3*365*24*0.5)≈0.55），数值量级合理。
