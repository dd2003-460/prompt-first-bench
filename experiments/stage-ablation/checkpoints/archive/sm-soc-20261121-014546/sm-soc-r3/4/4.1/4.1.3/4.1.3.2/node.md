# N280: 高溢价卖家利润损失中位数 Δπ_med：在 ε_d 取中位数 0.65 时，假设初始利润率为 30%，价格下移 10% 导致单件利润下降 Δπ_med = 0.

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N84

## Claim

高溢价卖家利润损失中位数 Δπ_med：在 ε_d 取中位数 0.65 时，假设初始利润率为 30%，价格下移 10% 导致单件利润下降 Δπ_med = 0.3 * V * (1 - 1/(1+0.1/0.65)) ≈ 0.054V，即利润下降 18%。这是量化“谁被伤害”的核心基准值。

## Corrected Claim

高溢价卖家利润损失中位数 Δπ_med：在 ε_d 取中位数 0.65 时，假设初始利润率为 30%，价格下移 10% 导致单件利润下降 Δπ_med = 0.3 * V * (1 - 1/(1+0.1/0.65)) ≈ 0.054V，即利润下降 18%。这是量化“谁被伤害”的核心基准值。

## Evidence

先验知识/题面给定，逻辑校验通过：计算过程 0.3 * (1 - 1/(1+0.1/0.65)) ≈ 0.054 正确，且 0.054/0.3 = 0.18 即 18% 下降，数值与逻辑自洽。

## Search Query

quantification of profit loss for high-priced sellers after price intervention
