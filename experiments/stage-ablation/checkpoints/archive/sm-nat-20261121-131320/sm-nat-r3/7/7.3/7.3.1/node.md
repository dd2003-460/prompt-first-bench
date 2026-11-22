# N140: 在 Gaussian Copula 模型下，条件期望 E[1/S | F > F_th] 的数值积分表达式：E[1/S | F > F_th] = ∫_{F_t

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N54

## Claim

在 Gaussian Copula 模型下，条件期望 E[1/S | F > F_th] 的数值积分表达式：E[1/S | F > F_th] = ∫_{F_th}^{∞} (1/S) * f(S|F>F_th) dS，其中条件密度 f(S|F>F_th) 需通过 Copula 逆变换或数值积分求解；该值直接决定 K_ρ 的分子项。

## Corrected Claim

在 Gaussian Copula 模型下，条件期望 E[1/S | F > F_th] 的数值积分表达式：E[1/S | F > F_th] = ∫_{F_th}^{∞} (1/S) * f(S|F>F_th) dS，其中条件密度 f(S|F>F_th) 需通过 Copula 逆变换或数值积分求解；该值直接决定 K_ρ 的分子项。

## Evidence

先验知识/题面给定，逻辑校验通过：条件期望的定义式正确，Gaussian Copula 框架下通过逆变换或数值积分求解条件密度是标准且逻辑自洽的方法。
