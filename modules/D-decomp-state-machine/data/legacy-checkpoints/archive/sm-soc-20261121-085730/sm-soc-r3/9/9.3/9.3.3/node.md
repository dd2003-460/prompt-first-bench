# N403: 价格因素干扰的隔离项 P_control：在计算 ΔReturn 时，需减去由价格变动引起的退货率变化 ΔReturn_price = ε_price_retu

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N142

## Claim

价格因素干扰的隔离项 P_control：在计算 ΔReturn 时，需减去由价格变动引起的退货率变化 ΔReturn_price = ε_price_return * (ΔP/P)，其中 ε_price_return 为价格对退货率的弹性（通常为负值，价格越低退货率越低），ΔP/P 为干预前后的相对价格变化，以确保 ΔQ_perception 仅反映标签效应。

## Corrected Claim

价格因素干扰的隔离项 P_control：在计算 ΔReturn 时，需减去由价格变动引起的退货率变化 ΔReturn_price = ε_price_return * (ΔP/P)，其中 ε_price_return 为价格对退货率的弹性（通常为负值，价格越低退货率越低），ΔP/P 为干预前后的相对价格变化，以确保 ΔQ_perception 仅反映标签效应。

## Evidence

先验知识/题面给定，逻辑校验通过：该公式符合经济学中弹性定义及控制变量法的基本逻辑，用于隔离价格效应以提取纯标签效应，量纲与符号逻辑自洽。

## Search Query

price elasticity return rate control variable isolation labeling effect
