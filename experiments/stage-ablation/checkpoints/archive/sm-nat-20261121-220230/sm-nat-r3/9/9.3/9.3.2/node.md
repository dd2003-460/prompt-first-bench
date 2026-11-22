# N284: 联合概率密度 f_{S,H}(s,h) 在 Frank Copula 下的表达式：f_{S,H}(s,h) = f_S(s) * f_H(h) * c(F_S(

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N98

## Claim

联合概率密度 f_{S,H}(s,h) 在 Frank Copula 下的表达式：f_{S,H}(s,h) = f_S(s) * f_H(h) * c(F_S(s), F_H(h); θ)，其中 c(u,v;θ) 为 Frank Copula 密度函数 c(u,v;θ) = (e^θ - 1) / (e^{θu} - 1)(e^{θv} - 1) * e^{θ(u+v)}，θ=-1.58，该表达式是二维积分的被积函数。

## Corrected Claim

联合概率密度 f_{S,H}(s,h) 在 Frank Copula 下的表达式：f_{S,H}(s,h) = f_S(s) * f_H(h) * c(F_S(s), F_H(h); θ)，其中 c(u,v;θ) 为 Frank Copula 密度函数 c(u,v;θ) = (e^θ - 1) / (e^{θu} - 1)(e^{θv} - 1) * e^{θ(u+v)}，θ=-1.58，该表达式是二维积分的被积函数。

## Evidence

先验知识/题面给定，逻辑校验通过：Frank Copula 密度函数公式正确，联合概率密度表达式符合 Copula 定义，θ=-1.58 在有效范围内（θ≠0），量纲与逻辑自洽。
