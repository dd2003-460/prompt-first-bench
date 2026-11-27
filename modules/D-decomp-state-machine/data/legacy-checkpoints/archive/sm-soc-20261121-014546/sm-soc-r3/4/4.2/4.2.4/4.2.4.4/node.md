# N299: 工作点1（高弹性低偏离）：当需求价格弹性 ε_d = 0.8 且初始偏离度 P_ask_old/P_anchor = 1.15 时，干预后成交周期变化率 ΔT/

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N88, N89, N90

## Claim

工作点1（高弹性低偏离）：当需求价格弹性 ε_d = 0.8 且初始偏离度 P_ask_old/P_anchor = 1.15 时，干预后成交周期变化率 ΔT/T_old = (1.15^(-0.8) - 1) ≈ -0.115，即周期缩短 11.5%。

## Corrected Claim

工作点1（高弹性低偏离）：当需求价格弹性 ε_d = 0.8 且初始偏离度 P_ask_old/P_anchor = 1.15 时，干预后成交周期变化率 ΔT/T_old = (1.15^(-0.8) - 1) ≈ -0.115，即周期缩短 11.5%。

## Evidence

先验知识/题面给定，逻辑校验通过：计算 1.15^(-0.8) ≈ 0.885，变化率 0.885 - 1 = -0.115，即 -11.5%，数值与逻辑均正确。

## Search Query

demand price elasticity 0.8 transaction time reduction 15 percent markup
