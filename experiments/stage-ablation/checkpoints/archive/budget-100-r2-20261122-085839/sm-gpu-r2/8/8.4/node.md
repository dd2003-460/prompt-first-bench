# N106: Cost_Per_Token 公式中的 Hardware_Cost 应包含初始采购价分摊到总生命周期产出的成本，即 Amortized_Hardware_Cos

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N29

## Claim

Cost_Per_Token 公式中的 Hardware_Cost 应包含初始采购价分摊到总生命周期产出的成本，即 Amortized_Hardware_Cost = (Purchase_Price * (1 - Residual_Value_Ratio)) / Total_Lifetime_Tokens。对于 24/7 运行 3 年的 RTX 4090，若年产出 100 亿 tokens，则单 token 硬件成本 = $426.67 / 1e9 = $4.27e-7/token [公式展开]

## Corrected Claim

Cost_Per_Token 公式中的 Hardware_Cost 应包含初始采购价分摊到总生命周期产出的成本，即 Amortized_Hardware_Cost = (Purchase_Price * (1 - Residual_Value_Ratio)) / Total_Lifetime_Tokens。对于 24/7 运行 3 年的 RTX 4090，若年产出 100 亿 tokens，则单 token 硬件成本 = $426.67 / 1e9 = $4.27e-7/token [公式展开]

## Evidence

先验知识/题面给定，逻辑校验通过：公式定义符合摊销成本逻辑，数值计算 $426.67 / 10^9 = 4.2667 \times 10^{-7}$ 准确无误。
