# N145: 修正后匹配概率 p_match_corrected 的边界条件检验：当 P_ask 超过买家保留价格分布的 95 百分位（U_95）时，Φ((P_max - P

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N41

## Claim

修正后匹配概率 p_match_corrected 的边界条件检验：当 P_ask 超过买家保留价格分布的 95 百分位（U_95）时，Φ((P_max - P_ask)/σ_pref) 趋近于 0，即使 δ_friction 较低，p_match_corrected 仍 < 0.05；此边界用于界定“无效高挂价”区域，避免模型在极端值处失效。

## Corrected Claim

修正后匹配概率 p_match_corrected 的边界条件检验：当 P_ask 超过买家保留价格分布的 95 百分位（U_95）时，Φ((P_max - P_ask)/σ_pref) 趋近于 0，即使 δ_friction 较低，p_match_corrected 仍 < 0.05；此边界用于界定“无效高挂价”区域，避免模型在极端值处失效。

## Evidence

先验知识/题面给定，逻辑校验通过：当 P_ask 远超 P_max 时，正态分布 CDF 项趋近于 0，导致匹配概率极低，符合数学直觉。
