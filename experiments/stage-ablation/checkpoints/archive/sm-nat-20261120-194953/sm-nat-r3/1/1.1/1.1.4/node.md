# N32: 大小与热度负相关（$\rho=-0.3$）的联合分布建模采用高斯-柯皮拉（Gaussian Copula）框架，条件期望 $E[S|R]$ 的函数形式为 $E[

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N6, N7, N8

## Claim

大小与热度负相关（$\rho=-0.3$）的联合分布建模采用高斯-柯皮拉（Gaussian Copula）框架，条件期望 $E[S|R]$ 的函数形式为 $E[S|R=r] = \mu_S + \rho \frac{\sigma_S}{\sigma_R} (Z^{-1}(F_R(r)) - \mu_Z)$，其中 $Z^{-1}$ 为标准正态分布逆函数，$F_R$ 为热度分布 CDF。

## Corrected Claim

大小与热度负相关（$\rho=-0.3$）的联合分布建模采用高斯-柯皮拉（Gaussian Copula）框架，条件期望 $E[S|R]$ 的函数形式为 $E[S|R=r] = \mu_S + \rho \frac{\sigma_S}{\sigma_R} (Z^{-1}(F_R(r)) - \mu_Z)$，其中 $Z^{-1}$ 为标准正态分布逆函数，$F_R$ 为热度分布 CDF。

## Evidence

先验知识/题面给定，逻辑校验通过：该公式符合高斯Copula框架下条件期望的标准推导（基于Sklar定理及正态分布性质），量纲与符号逻辑自洽。
