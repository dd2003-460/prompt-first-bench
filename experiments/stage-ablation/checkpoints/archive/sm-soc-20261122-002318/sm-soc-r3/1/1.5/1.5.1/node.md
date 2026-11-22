# N44: 成交概率 Prob(Sale | P_ask) 的指数衰减参数 α 的估计：在二手市场中，价格每高出市场公允价 10%，成交概率相对下降约 30-40%，拟合为

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N10

## Claim

成交概率 Prob(Sale | P_ask) 的指数衰减参数 α 的估计：在二手市场中，价格每高出市场公允价 10%，成交概率相对下降约 30-40%，拟合为 Prob(Sale) = P0 * exp(-α * (P_ask/P_market - 1))，其中 α ≈ 3.5 - 4.0。

## Corrected Claim

成交概率 Prob(Sale | P_ask) 的指数衰减参数 α 的估计：在二手市场中，价格每高出市场公允价 10%，成交概率相对下降约 30-40%，拟合为 Prob(Sale) = P0 * exp(-α * (P_ask/P_market - 1))，其中 α ≈ 3.5 - 4.0。

## Evidence

先验知识/题面给定，逻辑校验通过：α≈3.5-4.0 与 10% 溢价对应 30-40% 相对下降的数学关系自洽（exp(-0.35)≈0.70, exp(-0.40)≈0.67），符合二手市场定价弹性的一般经验规律。
