# N182: 下游投影 1（挂价分布宽度）：由 ε_seller 驱动的最终挂价 P_ask = P_ref * (1 + ε_seller) 的方差 Var(P_ask) 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N56

## Claim

下游投影 1（挂价分布宽度）：由 ε_seller 驱动的最终挂价 P_ask = P_ref * (1 + ε_seller) 的方差 Var(P_ask) = σ_seller² * P_ref²，标准差 σ_P_ask = 15% * P_ref，解释了观察到的 15-25% 挂价离散度。

## Corrected Claim

下游投影 1（挂价分布宽度）：由 ε_seller 驱动的最终挂价 P_ask = P_ref * (1 + ε_seller) 的方差 Var(P_ask) = σ_seller² * P_ref²，标准差 σ_P_ask = 15% * P_ref，解释了观察到的 15-25% 挂价离散度。

## Evidence

先验知识/题面给定，逻辑校验通过：方差公式 Var(P_ref*(1+ε)) = P_ref²*Var(ε) 推导正确，标准差 15% 落在 15-25% 离散度区间内，量纲与数值自洽。
