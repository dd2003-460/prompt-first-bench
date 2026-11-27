# N300: 工作点2（中弹性中偏离）：当需求价格弹性 ε_d = 0.6 且初始偏离度 P_ask_old/P_anchor = 1.20 时，干预后成交周期变化率 ΔT/

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N88, N89, N90

## Claim

工作点2（中弹性中偏离）：当需求价格弹性 ε_d = 0.6 且初始偏离度 P_ask_old/P_anchor = 1.20 时，干预后成交周期变化率 ΔT/T_old = (1.20^(-0.6) - 1) ≈ -0.103，即周期缩短 10.3%。

## Corrected Claim

工作点2（中弹性中偏离）：当需求价格弹性 ε_d = 0.6 且初始偏离度 P_ask_old/P_anchor = 1.20 时，干预后成交周期变化率 ΔT/T_old = (1.20^(-0.6) - 1) ≈ -0.103，即周期缩短 10.3%。

## Evidence

先验知识/题面给定，逻辑校验通过：计算 1.20^(-0.6) ≈ 0.897，0.897 - 1 = -0.103，数值推导准确，符合幂函数性质。

## Search Query

demand price elasticity 0.6 transaction time reduction 20 percent markup
