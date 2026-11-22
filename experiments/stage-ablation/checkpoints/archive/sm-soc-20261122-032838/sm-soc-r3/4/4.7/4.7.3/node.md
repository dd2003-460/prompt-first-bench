# N86: 量化'卖家短期收入冲击 -10%~-20%'的分解。收入变化 $\Delta Rev = \Delta P \times Q + P \times \Delta

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N24

## Claim

量化'卖家短期收入冲击 -10%~-20%'的分解。收入变化 $\Delta Rev = \Delta P \times Q + P \times \Delta Q$。其中价格效应 $\Delta P \approx -15\%$（溢价压缩），数量效应 $\Delta Q$ 取决于需求弹性 $\epsilon_d$。若 $\epsilon_d = 0.5$（低弹性，刚需品），则 $\Delta Q \approx +7.5\%$，净收入变化为 $-15\% + 7.5\% = -7.5\%$；若 $\epsilon_d = 1.0$，则 $\Delta Q \approx +15\%$，净变化为 0%。因此 -10%~-20% 的区间假设了 $\epsilon_d < 0.5$ 且存在部分卖家退出市场导致的供给收缩。

## Corrected Claim

量化'卖家短期收入冲击 -10%~-20%'的分解。收入变化 $\Delta Rev = \Delta P \times Q + P \times \Delta Q$。其中价格效应 $\Delta P \approx -15\%$（溢价压缩），数量效应 $\Delta Q$ 取决于需求弹性 $\epsilon_d$。若 $\epsilon_d = 0.5$（低弹性，刚需品），则 $\Delta Q \approx +7.5\%$，净收入变化为 $-15\% + 7.5\% = -7.5\%$；若 $\epsilon_d = 1.0$，则 $\Delta Q \approx +15\%$，净变化为 0%。因此 -10%~-20% 的区间假设了 $\epsilon_d < 0.5$ 且存在部分卖家退出市场导致的供给收缩。

## Evidence

先验知识/题面给定，逻辑校验通过：基于收入分解公式 ΔRev ≈ ΔP + ΔQ（忽略二阶项），当 ΔP=-15% 时，若 ε=0.5 则 ΔQ≈+7.5%，净变化 -7.5%；若 ε=1.0 则 ΔQ≈+15%，净变化 0%。推导出的 -10%~-20% 区间确实对应 ε<0.5 且叠加供给收缩（卖家退出）的情形，逻辑自洽且量级合理。

## Search Query

price elasticity of demand second-hand goods revenue impact price transparency
