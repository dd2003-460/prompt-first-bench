# N52: 采用 Gaussian Copula 模型，对象大小 S 与热度 F 的联合分布密度函数为 f(S,F) = f_S(S) * f_F(F) * C_ρ(F_S

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N16

## Claim

采用 Gaussian Copula 模型，对象大小 S 与热度 F 的联合分布密度函数为 f(S,F) = f_S(S) * f_F(F) * C_ρ(F_S(S), F_F(F))，其中 C_ρ 是相关系数 ρ=-0.3 的 Gaussian Copula 密度，用于计算联合概率。

## Corrected Claim

采用 Gaussian Copula 模型，对象大小 S 与热度 F 的联合分布密度函数为 f(S,F) = f_S(S) * f_F(F) * C_ρ(F_S(S), F_F(F))，其中 C_ρ 是相关系数 ρ=-0.3 的 Gaussian Copula 密度，用于计算联合概率。

## Evidence

先验知识/题面给定，逻辑校验通过：Gaussian Copula 的联合密度公式 f(S,F) = f_S(S) * f_F(F) * C_ρ(F_S(S), F_F(F)) 符合 Sklar 定理及高斯 Copula 的标准定义，相关系数 ρ=-0.3 在有效范围 [-1, 1] 内，量纲与逻辑自洽。
