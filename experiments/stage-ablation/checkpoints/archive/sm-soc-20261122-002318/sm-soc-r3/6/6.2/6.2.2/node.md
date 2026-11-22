# N251: 自我估值权重 β 的互补性约束：由于 P_fair = α * P_recent_avg + β * P_self_valuation，且通常假设 α + β 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N89

## Claim

自我估值权重 β 的互补性约束：由于 P_fair = α * P_recent_avg + β * P_self_valuation，且通常假设 α + β = 1，则 β = 1 - α。若 α=0.4，则 β=0.6，意味着 60% 的公平锚点来自卖家主观高估。

## Corrected Claim

自我估值权重 β 的互补性约束：由于 P_fair = α * P_recent_avg + β * P_self_valuation，且通常假设 α + β = 1，则 β = 1 - α。若 α=0.4，则 β=0.6，意味着 60% 的公平锚点来自卖家主观高估。

## Evidence

先验知识/题面给定，逻辑校验通过：基于线性组合定义 P_fair = α * P_recent_avg + β * P_self_valuation 及约束 α + β = 1，数学推导 β = 1 - α 成立；代入 α=0.4 得 β=0.6，数值计算无误，量纲一致。

## Search Query

constraint alpha beta sum to one fair price anchor composition
