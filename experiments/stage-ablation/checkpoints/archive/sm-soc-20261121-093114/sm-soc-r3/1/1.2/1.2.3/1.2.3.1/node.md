# N103: 共享随机源投影：挂价方差分解中的噪声项贡献，Var(ε_seller) = 0.64（基于 σ_ε=0.8），该值直接代入父节点公式 Var(P_ask) = 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N32

## Claim

共享随机源投影：挂价方差分解中的噪声项贡献，Var(ε_seller) = 0.64（基于 σ_ε=0.8），该值直接代入父节点公式 Var(P_ask) = P_market^2 * (0.25^2 * 0.64) = 0.04 * P_market^2。

## Corrected Claim

共享随机源投影：挂价方差分解中的噪声项贡献，Var(ε_seller) = 0.64（基于 σ_ε=0.8），该值直接代入父节点公式 Var(P_ask) = P_market^2 * (0.25^2 * 0.64) = 0.04 * P_market^2。

## Evidence

先验知识/题面给定，逻辑校验通过：0.8^2=0.64，0.25^2=0.0625，0.0625*0.64=0.04，数值推导自洽。
