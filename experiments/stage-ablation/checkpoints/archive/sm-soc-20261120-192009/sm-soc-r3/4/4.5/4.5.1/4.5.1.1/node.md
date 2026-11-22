# N261: Heckman 模型逆米尔斯比（IMR）计算公式：IMR_i = φ(λ * Z_i) / Φ(λ * Z_i)，其中 λ 为选择方程残差与结果方程残差的相关系

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N89

## Claim

Heckman 模型逆米尔斯比（IMR）计算公式：IMR_i = φ(λ * Z_i) / Φ(λ * Z_i)，其中 λ 为选择方程残差与结果方程残差的相关系数，Z_i 为选择方程的线性指数；需通过极大似然估计同时获得 λ 和回归系数，若 λ > 0.3 则存在显著正向选择偏差。

## Corrected Claim

Heckman 模型逆米尔斯比（IMR）计算公式：IMR_i = φ(λ * Z_i) / Φ(λ * Z_i)，其中 λ 为选择方程残差与结果方程残差的相关系数，Z_i 为选择方程的线性指数；需通过极大似然估计同时获得 λ 和回归系数，若 λ > 0.3 则存在显著正向选择偏差。

## Evidence

先验知识/题面给定，逻辑校验通过
