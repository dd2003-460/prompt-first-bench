# N179: 初始利润率 Margin_old 的计算表达式：Margin_old = (P_ask - C_cost) / P_ask，其中 P_ask = P_ref *

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N58

## Claim

初始利润率 Margin_old 的计算表达式：Margin_old = (P_ask - C_cost) / P_ask，其中 P_ask = P_ref * (1 + δ)，代入 δ=20% 和 C_cost = 0.8 * P_ref 作为基准案例，计算得出 Margin_old ≈ 20%。

## Corrected Claim

Margin_old = (P_ask - C_cost) / P_ask，其中 P_ask = P_ref * (1 + δ)，代入 δ=20% 和 C_cost = 0.8 * P_ref 作为基准案例，计算得出 Margin_old ≈ 33.3%。

## Evidence

先验知识/题面给定，逻辑校验通过：代入数值 (1.2 - 0.8) / 1.2 = 0.4 / 1.2 ≈ 33.3%，但题目声称 ≈ 20% 存在计算错误？等等，重新计算：P_ask = 1.2 * P_ref, C_cost = 0.8 * P_ref. Margin = (1.2 - 0.8) / 1.2 = 0.4 / 1.2 = 1/3 ≈ 33.3%。题目说 ≈ 20% 是错误的。

## Search Query

profit margin calculation formula used goods market
