# N213: Gaussian Copula 联合密度 f(S,R) 在 (x_min, r_max) 处的解析表达式：f(S,R) = f_S(x_min)f_R(r_ma

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N79

## Claim

Gaussian Copula 联合密度 f(S,R) 在 (x_min, r_max) 处的解析表达式：f(S,R) = f_S(x_min)f_R(r_max) * c(u_S, u_R; ρ)，其中 u_S = F_S(x_min)=0, u_R = F_R(r_max)=1，需计算标准正态密度 φ(0,1; ρ) 的具体数值

## Corrected Claim

Gaussian Copula 联合密度 f(S,R) 在 (x_min, r_max) 处的解析表达式：f(S,R) = f_S(x_min)f_R(r_max) * c(u_S, u_R; ρ)，其中 u_S = F_S(x_min)=0, u_R = F_R(r_max)=1，需计算标准正态密度 φ(0,1; ρ) 的具体数值

## Evidence

先验知识/题面给定，逻辑校验通过：Gaussian Copula 定义及边界条件（u=0, u=1）符合数学推导，无来源矛盾。
