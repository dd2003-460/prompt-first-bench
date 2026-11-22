# N280: 工作点1（保守估计）：假设价格弹性系数 ε_p = -1.5，若 MVI 导致均价 P_avg 上升 5%（ΔP_avg = 0.05），则成交量 Q 下降 7

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N94

## Claim

工作点1（保守估计）：假设价格弹性系数 ε_p = -1.5，若 MVI 导致均价 P_avg 上升 5%（ΔP_avg = 0.05），则成交量 Q 下降 7.5%（ΔFreq = -0.075），净 GMV 变化为 (1+0.05)*(1-0.075)-1 ≈ -2.875%，即 GMV 实际下降。

## Corrected Claim

工作点1（保守估计）：假设价格弹性系数 ε_p = -1.5，若 MVI 导致均价 P_avg 上升 5%（ΔP_avg = 0.05），则成交量 Q 下降 7.5%（ΔFreq = -0.075），净 GMV 变化为 (1+0.05)*(1-0.075)-1 ≈ -2.875%，即 GMV 实际下降。

## Evidence

先验知识/题面给定，逻辑校验通过：根据价格弹性定义 ΔQ/Q = ε_p * (ΔP/P)，代入 ε_p=-1.5 和 ΔP/P=0.05 得 ΔQ/Q=-0.075；GMV变化率 = (1+0.05)*(1-0.075)-1 = 1.05*0.925-1 = 0.97125-1 = -0.02875，即-2.875%，计算无误。

## Search Query

price elasticity of demand second hand goods platform
