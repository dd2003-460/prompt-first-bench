# N75: Gaussian Copula 联合密度函数 C_ρ(u,v) 的具体解析形式：C_ρ(u,v) = Φ_ρ(Φ^{-1}(u), Φ^{-1}(v))，其中 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N25

## Claim

Gaussian Copula 联合密度函数 C_ρ(u,v) 的具体解析形式：C_ρ(u,v) = Φ_ρ(Φ^{-1}(u), Φ^{-1}(v))，其中 Φ_ρ 是相关系数 ρ=-0.3 的二元正态分布 CDF，需通过数值积分或查表计算特定分位点下的联合概率，用于从边缘 Pareto 分布推导联合密度。

## Corrected Claim

Gaussian Copula 联合密度函数 C_ρ(u,v) 的具体解析形式：C_ρ(u,v) = Φ_ρ(Φ^{-1}(u), Φ^{-1}(v))，其中 Φ_ρ 是相关系数 ρ=-0.3 的二元正态分布 CDF，需通过数值积分或查表计算特定分位点下的联合概率，用于从边缘 Pareto 分布推导联合密度。

## Evidence

先验知识/题面给定，逻辑校验通过：Gaussian Copula 的定义即为二元正态分布 CDF 与边缘逆 CDF 的复合，公式形式正确，ρ=-0.3 在合法范围内，数值积分需求符合高维/非标准正态 CDF 计算的实际工程惯例。
