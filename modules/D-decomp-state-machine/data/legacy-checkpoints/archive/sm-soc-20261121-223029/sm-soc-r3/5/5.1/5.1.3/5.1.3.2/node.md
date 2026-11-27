# N296: 合理定价策略的期望收益函数：E[Profit_rational] = (P_mid - C_marginal) * P(sale | rational) - C

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N99

## Claim

合理定价策略的期望收益函数：E[Profit_rational] = (P_mid - C_marginal) * P(sale | rational) - C_waiting * T_cycle_rational。由于 P_mid 接近市场共识，P(sale | rational) 对 σ_W 不敏感（主要受需求基础影响），T_cycle_rational 较短。需计算 E[Profit_rational] 作为基准线，用于与 E[Profit_high] 比较。

## Corrected Claim

合理定价策略的期望收益函数：E[Profit_rational] = (P_mid - C_marginal) * P(sale | rational) - C_waiting * T_cycle_rational。由于 P_mid 接近市场共识，P(sale | rational) 对 σ_W 不敏感（主要受需求基础影响），T_cycle_rational 较短。需计算 E[Profit_rational] 作为基准线，用于与 E[Profit_high] 比较。

## Evidence

先验知识/题面给定，逻辑校验通过：期望收益公式结构符合经济学基本定义（边际利润*概率-等待成本），且理性定价策略下对噪声不敏感、周期短的定性描述符合市场均衡理论直觉。
