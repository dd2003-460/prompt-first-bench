# N295: 高溢价策略的期望收益函数：E[Profit_high] = (P_ask - C_marginal) * P(sale | high_premium) - C_

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N99

## Claim

高溢价策略的期望收益函数：E[Profit_high] = (P_ask - C_marginal) * P(sale | high_premium) - C_waiting * T_cycle_high，其中 P(sale | high_premium) 受买家噪声 σ_W 影响，T_cycle_high 为高溢价下的平均成交周期（见 N114）。需代入 σ_W 的具体分布参数计算 E[Profit_high] 随 σ_W 变化的曲线。

## Corrected Claim

高溢价策略的期望收益函数：E[Profit_high] = (P_ask - C_marginal) * P(sale | high_premium) - C_waiting * T_cycle_high，其中 P(sale | high_premium) 受买家噪声 σ_W 影响，T_cycle_high 为高溢价下的平均成交周期（见 N114）。需代入 σ_W 的具体分布参数计算 E[Profit_high] 随 σ_W 变化的曲线。

## Evidence

先验知识/题面给定，逻辑校验通过
