# N89: Opex_3yr 计算公式：Opex_3yr = (Annual_Electricity_Cost * 3) + (Annual_Cooling_Cost * 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N25

## Claim

Opex_3yr 计算公式：Opex_3yr = (Annual_Electricity_Cost * 3) + (Annual_Cooling_Cost * 3) + (Annual_Labor_Cost * 3)，其中 Annual_Cooling_Cost = Annual_Electricity_Cost * PUE_Coefficient (PUE 通常取 1.2-1.5)

## Corrected Claim

Opex_3yr 计算公式：Opex_3yr = (Annual_Electricity_Cost * 3) + (Annual_Cooling_Cost * 3) + (Annual_Labor_Cost * 3)，其中 Annual_Cooling_Cost = Annual_Electricity_Cost * PUE_Coefficient (PUE 通常取 1.2-1.5)

## Evidence

先验知识/题面给定，逻辑校验通过：Opex_3yr 为三年总运营成本，由电费、冷却费和人工费三年累计构成；冷却成本通常与电力成本通过 PUE 系数关联，PUE 1.2-1.5 为数据中心常见范围，公式结构符合基本经济逻辑。

## Search Query

data center operating cost formula PUE coefficient LLM inference
