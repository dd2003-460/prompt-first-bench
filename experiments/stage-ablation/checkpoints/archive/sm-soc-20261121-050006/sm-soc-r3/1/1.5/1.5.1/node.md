# N48: 共享随机源：市场出清价格的随机波动项 ε_market，定义为 Var(P_clear | t)，其中 P_clear 为 t 时刻的市场出清价格；该波动源于供

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N9

## Claim

共享随机源：市场出清价格的随机波动项 ε_market，定义为 Var(P_clear | t)，其中 P_clear 为 t 时刻的市场出清价格；该波动源于供需两侧的瞬时冲击（如季节性、突发热点），导致 T_close 和 ΔQ 在计算协方差时存在共同的时间序列噪声成分，需在进行相关性检验前进行去趋势处理。

## Corrected Claim

共享随机源：市场出清价格的随机波动项 ε_market，定义为 Var(P_clear | t)，其中 P_clear 为 t 时刻的市场出清价格；该波动源于供需两侧的瞬时冲击（如季节性、突发热点），导致 T_close 和 ΔQ 在计算协方差时存在共同的时间序列噪声成分，需在进行相关性检验前进行去趋势处理。

## Evidence

先验知识/题面给定，逻辑校验通过：市场出清价格的随机波动确实源于供需冲击，且时间序列数据在计算协方差前进行去趋势处理是标准统计实践，逻辑自洽。
