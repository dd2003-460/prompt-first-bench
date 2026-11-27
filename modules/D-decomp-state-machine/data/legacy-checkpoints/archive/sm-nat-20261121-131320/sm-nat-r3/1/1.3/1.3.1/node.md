# N25: 热度-大小联合分布的 Copula 函数：采用高斯 Copula 建模 ρ=-0.3 的相关性，联合 CDF F(S,f) = C_Gaussian(F_S(S

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N7

## Claim

热度-大小联合分布的 Copula 函数：采用高斯 Copula 建模 ρ=-0.3 的相关性，联合 CDF F(S,f) = C_Gaussian(F_S(S), F_f(f); ρ=-0.3)，其中 F_S 和 F_f 分别为 Pareto(α=1.1) 和 Pareto(β=0.9) 的边缘 CDF。

## Corrected Claim

热度-大小联合分布的 Copula 函数：采用高斯 Copula 建模 ρ=-0.3 的相关性，联合 CDF F(S,f) = C_Gaussian(F_S(S), F_f(f); ρ=-0.3)，其中 F_S 和 F_f 分别为 Pareto(α=1.1) 和 Pareto(β=0.9) 的边缘 CDF。

## Evidence

先验知识/题面给定，逻辑校验通过：高斯Copula是建模连续变量相关性的标准方法，ρ=-0.3在[-1,1]范围内合理，Pareto分布作为边缘分布符合热度-大小长尾特征，公式结构符合Sklar定理定义。
