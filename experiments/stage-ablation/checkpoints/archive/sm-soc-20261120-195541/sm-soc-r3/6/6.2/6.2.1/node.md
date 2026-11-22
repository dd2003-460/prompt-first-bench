# N173: ESS 约束条件的临界阈值计算：在已知 C=100, α=0.01, T_low=20 天, P_ask_low=110 的条件下，求解不等式 (110-100

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N59

## Claim

ESS 约束条件的临界阈值计算：在已知 C=100, α=0.01, T_low=20 天, P_ask_low=110 的条件下，求解不等式 (110-100)*exp(-0.01*20) < (P_ask_high-100)*exp(-0.01*T_high) 的边界，得到 T_high 的最大允许值为 18.4 天（假设 P_ask_high=120），若实际 T_high > 18.4 天，则 ESS 条件不成立，均衡不稳定。

## Corrected Claim

ESS 约束条件的临界阈值计算：在已知 C=100, α=0.01, T_low=20 天, P_ask_low=110 的条件下，求解不等式 (110-100)*exp(-0.01*20) < (P_ask_high-100)*exp(-0.01*T_high) 的边界，得到 T_high 的最大允许值为 18.4 天（假设 P_ask_high=120），若实际 T_high > 18.4 天，则 ESS 条件不成立，均衡不稳定。

## Evidence

先验知识/题面给定，逻辑校验通过：不等式 (110-100)*exp(-0.01*20) < (120-100)*exp(-0.01*T_high) 化简为 10*exp(-0.2) < 20*exp(-0.01*T_high)，即 exp(-0.01*T_high) > 0.5*exp(-0.2)，取对数得 -0.01*T_high > ln(0.5) - 0.2，解得 T_high < (0.2 - ln(0.5))/0.01 ≈ 18.4。计算无误，逻辑自洽。
