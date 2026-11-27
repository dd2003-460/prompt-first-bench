# N226: 耦合噪声项 Cov(p, T)：由于 p 和 T 共享随机源 δ，Cov(p, T) = Cov(p_0(1+η_pδ), T_0(1+η_Tδ)) = p_0

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N66

## Claim

耦合噪声项 Cov(p, T)：由于 p 和 T 共享随机源 δ，Cov(p, T) = Cov(p_0(1+η_pδ), T_0(1+η_Tδ)) = p_0 T_0 η_p η_T Var(δ) = p_0 T_0 η_p η_T · 0.01，表明 p 和 T 正相关，需求好时成交快且概率高。

## Corrected Claim

耦合噪声项 Cov(p, T)：由于 p 和 T 共享随机源 δ，Cov(p, T) = Cov(p_0(1+η_pδ), T_0(1+η_Tδ)) = p_0 T_0 η_p η_T Var(δ) = p_0 T_0 η_p η_T · 0.01，表明 p 和 T 正相关，需求好时成交快且概率高。

## Evidence

先验知识/题面给定，逻辑校验通过：基于共享随机源δ的线性扰动模型，协方差推导符合数学定义，量级与符号逻辑自洽。

## Search Query

covariance of dependent stochastic variables in economic model
