# N260: 电价敏感性分析需引入时间加权因子：若用户仅在白天使用（8h/day），则年运行小时数从 8760h 降至 2920h，电力成本 C_power = P_avg 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N84

## Claim

电价敏感性分析需引入时间加权因子：若用户仅在白天使用（8h/day），则年运行小时数从 8760h 降至 2920h，电力成本 C_power = P_avg * 2920h * 3 * E_price，此修正使 2×4090 与 1×5090 的 TCO 交叉点电价 E_cross 显著上移，改变性价比排序。

## Corrected Claim

电价敏感性分析需引入时间加权因子：若用户仅在白天使用（8h/day），则年运行小时数从 8760h 降至 2920h，电力成本 C_power = P_avg * 2920h * 3 * E_price，此修正使 2×4090 与 1×5090 的 TCO 交叉点电价 E_cross 显著上移，改变性价比排序。

## Evidence

先验知识/题面给定，逻辑校验通过：8h/day * 365 = 2920h 计算正确；电力成本公式量纲正确；由于 2x4090 功耗通常高于 1x5090，运行时间减少会降低高功耗方案的相对成本劣势，从而推高 TCO 交叉点电价，逻辑自洽。
